"""
Improved bulk database operations with better error handling and performance.
"""
import logging
from typing import List, Optional, Union, Dict, Any
from sqlalchemy import text
from sqlalchemy.exc import OperationalError, DataError, IntegrityError
from psycopg2.errors import DeadlockDetected
import time
import random


class BulkOperationError(Exception):
    """Custom exception for bulk operation errors."""
    pass


class BulkOperationHandler:
    """Handles bulk database operations with improved error handling and
    performance."""

    def __init__(
        self,
        logger: logging.Logger,
        max_retries: int = 10,
        initial_backoff: float = 1.0,
        max_backoff: float = 30.0
    ):
        self.logger = logger
        self.max_retries = max_retries
        self.initial_backoff = initial_backoff
        self.max_backoff = max_backoff

    def _calculate_backoff(self, attempt: int) -> float:
        """Calculate exponential backoff with jitter."""
        backoff = min(self.initial_backoff * (2 ** attempt), self.max_backoff)
        jitter = random.uniform(0, 0.1 * backoff)
        return backoff + jitter

    def _handle_deadlock(
        self,
        attempt: int,
        operation: str,
        data_size: int
    ) -> None:
        """Handle deadlock with exponential backoff."""
        backoff = self._calculate_backoff(attempt)
        self.logger.debug(
            f"Deadlock detected during {operation}. "
            f"Attempt {attempt + 1}/{self.max_retries}. "
            f"Data size: {data_size}. "
            f"Retrying in {round(backoff)} seconds."
        )
        time.sleep(backoff)

    def _handle_data_error(
        self,
        error: DataError,
        data: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Handle data errors by cleaning and validating data."""
        cleaned_data = []
        for item in data:
            try:
                # Add data cleaning logic here
                cleaned_data.append(item)
            except Exception:
                self.logger.warning("Failed to clean data item")
                continue
        return cleaned_data

    def bulk_insert(
        self,
        data: Union[List[dict], dict],
        table,
        natural_keys: List[str],
        return_columns: Optional[List[str]] = None,
        string_fields: Optional[List[str]] = None,
        on_conflict_update: bool = True,
        session = None
    ) -> Optional[List[dict]]:
        """
        Bulk insert data into a table with handling for duplicates.
        
        Args:
            data (list or dict): Data to insert. Can be a list of dictionaries or a single dictionary.
            table (Table): SQLAlchemy table object
            natural_keys (list): List of column names that form the natural key
            return_columns (list, optional): List of column names to return after insert
            string_fields (list, optional): List of column names that should be treated as strings
            on_conflict_update (bool, optional): Whether to update existing records on conflict
            session (Session, optional): SQLAlchemy session to use
        
        Returns:
            ResultProxy: Result of the insert operation
        """
        if not data:
            return None

        # Convert single dict to list for uniform handling
        if isinstance(data, dict):
            data = [data]

        # Get column names from the table
        columns = [c.name for c in table.__table__.columns if not c.primary_key]
        
        # Build column list for insert
        column_list = ', '.join(columns)
        
        # Build values placeholders
        value_list = ', '.join([':' + col for col in columns])
        
        # Build base insert statement
        sql = f"INSERT INTO {table.__tablename__} ({column_list}) VALUES ({value_list})"
        
        # Add ON CONFLICT clause if natural keys are provided
        if natural_keys and on_conflict_update:
            # Build the conflict target
            conflict_target = ', '.join(natural_keys)
            
            # Build the update set clause
            update_columns = [c for c in columns if c not in natural_keys]
            if update_columns:
                update_set = ', '.join(f"{c} = excluded.{c}" for c in update_columns)
                sql += f" ON CONFLICT ({conflict_target}) DO UPDATE SET {update_set}"
            else:
                sql += f" ON CONFLICT ({conflict_target}) DO NOTHING"
        
        # Add RETURNING clause if specified
        if return_columns:
            sql += f" RETURNING {', '.join(return_columns)}"

        # Create the SQLAlchemy text object
        stmt = text(sql)

        # Create a set to track processed natural keys
        processed_keys = set()
        results = []

        try:
            # Execute each insert individually
            for item in data:
                # Create key tuple for duplicate checking
                key_tuple = tuple(item[k] for k in natural_keys)
                
                # Skip if we've already processed this key
                if key_tuple in processed_keys:
                    continue
                
                processed_keys.add(key_tuple)

                try:
                    # Validate data types
                    for col_name, col in table.__table__.columns.items():
                        if col_name in item:
                            try:
                                # Try to convert the value to the column's type
                                col.type.python_type(item[col_name])
                            except (ValueError, TypeError):
                                raise DataError(
                                    f"Invalid data type for column {col_name}",
                                    params=item,
                                    orig=None
                                )

                    result = session.execute(stmt, item)
                    if return_columns:
                        row = result.fetchone()
                        if row:
                            results.append(dict(zip(return_columns, row)))
                except Exception as e:
                    session.rollback()
                    if isinstance(e, (IntegrityError, DataError)):
                        raise
                    raise BulkOperationError(f"Error during bulk insert: {str(e)}") from e

            # Commit the transaction
            session.commit()

            return results if return_columns else None
        except Exception as e:
            # Rollback on any error
            session.rollback()
            raise

    def _prepare_insert_statement(
        self,
        table,
        natural_keys: List[str],
        return_columns: Optional[List[str]] = None,
        string_fields: Optional[List[str]] = None,
        on_conflict_update: bool = True
    ):
        """
        Prepare an insert statement with ON CONFLICT handling.

        Args:
            table: SQLAlchemy table object
            natural_keys (list): List of column names that form the natural key
            return_columns (list, optional): List of column names to return after insert
            string_fields (list, optional): List of column names that should be treated as strings
            on_conflict_update (bool): Whether to update existing records on conflict

        Returns:
            str: The prepared insert statement
        """
        # Get column names from the table
        columns = [c.name for c in table.__table__.columns if not c.primary_key]
        
        # Build column list for insert
        column_list = ', '.join(columns)
        
        # Build values placeholders
        value_list = ', '.join(['?' for _ in columns])
        
        # Build base insert statement
        sql = f"INSERT INTO {table.__tablename__} ({column_list}) VALUES ({value_list})"
        
        # Add ON CONFLICT clause if natural keys are provided
        if natural_keys and on_conflict_update:
            # Build the conflict target
            conflict_target = ', '.join(natural_keys)
            
            # Build the update set clause
            update_columns = [c for c in columns if c not in natural_keys]
            if update_columns:
                update_set = ', '.join(f"{c} = excluded.{c}" for c in update_columns)
                sql += f" ON CONFLICT ({conflict_target}) DO UPDATE SET {update_set}"
            else:
                sql += f" ON CONFLICT ({conflict_target}) DO NOTHING"
        
        # Add RETURNING clause if specified
        if return_columns:
            sql += f" RETURNING {', '.join(return_columns)}"
        
        return text(sql)

    def bulk_config_update(
        self,
        settings: List[dict],
        table,
        natural_keys: List[str] = ["section_name", "setting_name"],
        return_columns: Optional[List[str]] = None,
        on_conflict_update: bool = True,
        session = None
    ) -> Optional[List[dict]]:
        """
        Bulk update configuration settings with handling for duplicates.
        
        Args:
            settings (list): List of configuration settings to update
            table (Table): SQLAlchemy table object (Config)
            natural_keys (list): List of column names that form the natural key
            return_columns (list, optional): List of column names to return after update
            on_conflict_update (bool, optional): Whether to update existing records on conflict
            session (Session, optional): SQLAlchemy session to use
        
        Returns:
            Optional[List[dict]]: Returned data if return_columns specified
        """
        if not settings:
            return None

        # Process settings to ensure type information
        processed_settings = []
        for setting in settings:
            if "type" not in setting:
                setting["type"] = setting["value"].__class__.__name__
            if setting["type"] == "NoneType":
                setting["type"] = None
            processed_settings.append(setting)

        # Use bulk_insert with ON CONFLICT DO UPDATE
        return self.bulk_insert(
            processed_settings,
            table,
            natural_keys,
            return_columns,
            None,  # string_fields
            on_conflict_update,
            session
        )
