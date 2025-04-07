"""
Tests for improved bulk database operations.
"""
import pytest
import logging
from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import DataError
from sqlalchemy.orm import sessionmaker

from augur.application.db.bulk_operations import BulkOperationHandler

Base = declarative_base()

class TestTable(Base):
    __tablename__ = 'test_table'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    value = Column(Integer)

@pytest.fixture
def engine():
    """Create a test database engine."""
    return create_engine('sqlite:///:memory:', echo=False)

@pytest.fixture
def session(engine):
    """Create a new database session for a test."""
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

@pytest.fixture
def handler():
    """Create a BulkOperationHandler instance."""
    logger = logging.getLogger('test_bulk_operations')
    logger.setLevel(logging.INFO)
    return BulkOperationHandler(logger)

def test_bulk_insert_success(handler, session):
    data = [
        {'name': 'test1', 'value': 1},
        {'name': 'test2', 'value': 2}
    ]
    
    result = handler.bulk_insert(
        data, TestTable, ['name'],
        return_columns=['id', 'name'],
        session=session
    )
    
    # Verify the results
    rows = list(result)
    assert len(rows) == 2
    assert rows[0]['name'] == 'test1'
    assert rows[1]['name'] == 'test2'

def test_bulk_insert_empty_data(handler, session):
    result = handler.bulk_insert([], TestTable, ['name'], session=session)
    assert result is None

def test_bulk_insert_single_item(handler, session):
    data = {'name': 'test1', 'value': 1}
    
    result = handler.bulk_insert(
        data, TestTable, ['name'],
        return_columns=['id', 'name'],
        session=session
    )
    
    # Verify the result
    rows = list(result)
    assert len(rows) == 1
    assert rows[0]['name'] == 'test1'

def test_bulk_insert_duplicate_handling(handler, session):
    data = [
        {'name': 'test1', 'value': 1},
        {'name': 'test1', 'value': 2}  # Same name, different value
    ]
    
    result = handler.bulk_insert(
        data, TestTable, ['name'],
        return_columns=['id', 'name'],
        session=session
    )
    
    # Verify that only one row exists with the updated value
    rows = list(result)
    assert len(rows) == 1
    assert rows[0]['name'] == 'test1'

def test_bulk_insert_data_error(handler, session):
    data = [
        {'name': 'test1', 'value': 'invalid'}  # value should be integer
    ]
    
    with pytest.raises(DataError):
        handler.bulk_insert(data, TestTable, ['name'], session=session)
        session.flush()  # Force the error to be raised

def test_prepare_insert_statement_basic(handler):
    stmt = handler._prepare_insert_statement(TestTable, ['name'], None)
    assert stmt is not None

def test_prepare_insert_statement_no_conflict(handler):
    stmt = handler._prepare_insert_statement(TestTable, ['name'], None, on_conflict_update=False)
    assert stmt is not None

def test_prepare_insert_statement_return_columns(handler):
    stmt = handler._prepare_insert_statement(TestTable, ['name'], ['id', 'name'])
    assert stmt is not None

def test_prepare_insert_statement_string_fields(handler):
    stmt = handler._prepare_insert_statement(TestTable, ['name'], None, string_fields=['name'])
    assert stmt is not None

def test_bulk_config_update(handler, session):
    """Test the bulk_config_update method."""
    # Create a test table that mimics the Config table
    class ConfigTable(Base):
        __tablename__ = 'config_table'
        
        id = Column(Integer, primary_key=True)
        section_name = Column(String)
        setting_name = Column(String)
        value = Column(String)
        type = Column(String)
        
        __table_args__ = (
            UniqueConstraint('section_name', 'setting_name', name='uix_config_section_setting'),
        )
    
    # Create the table
    ConfigTable.__table__.create(session.get_bind())
    
    # Test data
    settings = [
        {
            "section_name": "test_section",
            "setting_name": "test_setting1",
            "value": "value1",
            "type": "str"
        },
        {
            "section_name": "test_section",
            "setting_name": "test_setting2",
            "value": "value2",
            "type": "str"
        }
    ]
    
    # Test bulk insert
    result = handler.bulk_config_update(
        settings, ConfigTable, 
        return_columns=['section_name', 'setting_name', 'value'],
        session=session
    )
    
    # Verify the results
    assert result is not None
    assert len(result) == 2
    assert result[0]['section_name'] == 'test_section'
    assert result[0]['setting_name'] == 'test_setting1'
    assert result[0]['value'] == 'value1'
    assert result[1]['section_name'] == 'test_section'
    assert result[1]['setting_name'] == 'test_setting2'
    assert result[1]['value'] == 'value2'
    
    # Test update existing
    settings[0]['value'] = 'updated_value1'
    result = handler.bulk_config_update(
        settings, ConfigTable, 
        return_columns=['section_name', 'setting_name', 'value'],
        session=session
    )
    
    # Verify the update
    assert result is not None
    assert len(result) == 2
    assert result[0]['value'] == 'updated_value1'
    
    # Clean up
    ConfigTable.__table__.drop(session.get_bind()) 