"""
Tests for improved bulk database operations.
"""
import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError, DataError
from psycopg2.errors import DeadlockDetected

from augur.application.db.bulk_operations import BulkOperationHandler, BulkOperationError

Base = declarative_base()

class TestTable(Base):
    __tablename__ = 'test_table'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)

@pytest.fixture
def engine():
    return create_engine('postgresql://postgres:postgres@localhost:5432/augur_test')

@pytest.fixture
def handler():
    import logging
    logger = logging.getLogger('test_bulk_operations')
    return BulkOperationHandler(logger)

@pytest.fixture
def session(engine):
    Base.metadata.create_all(engine)
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_bulk_insert_success(handler, session):
    data = [
        {'name': 'test1', 'value': 1},
        {'name': 'test2', 'value': 2}
    ]
    
    result = handler.bulk_insert(
        data, TestTable, ['name'],
        return_columns=['id', 'name']
    )
    
    assert len(result) == 2
    assert all('id' in item for item in result)
    assert all('name' in item for item in result)

def test_bulk_insert_empty_data(handler, session):
    result = handler.bulk_insert([], TestTable, ['name'])
    assert result is None

def test_bulk_insert_single_item(handler, session):
    data = {'name': 'test1', 'value': 1}
    
    result = handler.bulk_insert(
        data, TestTable, ['name'],
        return_columns=['id', 'name']
    )
    
    assert len(result) == 1
    assert result[0]['name'] == 'test1'

def test_bulk_insert_duplicate_handling(handler, session):
    data = [
        {'name': 'test1', 'value': 1},
        {'name': 'test1', 'value': 2}
    ]
    
    result = handler.bulk_insert(
        data, TestTable, ['name'],
        return_columns=['id', 'name']
    )
    
    assert len(result) == 1
    assert result[0]['name'] == 'test1'

def test_bulk_insert_data_error(handler, session):
    data = [
        {'name': 'test1', 'value': 'invalid'}  # value should be integer
    ]
    
    with pytest.raises(DataError):
        handler.bulk_insert(data, TestTable, ['name']) 