"""
Improved bulk database operations with better error handling and performance.
"""
import logging
from typing import List, Optional, Union, Dict, Any
from sqlalchemy import text
from sqlalchemy.exc import OperationalError, DataError
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
        on_conflict_update: bool = True
    ) -> Optional[List[dict]]:
        """
        Improved bulk insert operation with better error handling.

        Args:
            data: Data to insert
            table: SQLAlchemy table
            natural_keys: List of natural key columns
            return_columns: Columns to return after insert
            string_fields: String fields that need special handling
            on_conflict_update: Whether to update on conflict

        Returns:
            Optional[List[dict]]: Returned data if return_columns specified
        """
        if not isinstance(data, list):
            data = [data]

        if not data:
            return [] if return_columns else None

        attempt = 0
        while attempt < self.max_retries:
            try:
                # Prepare the insert statement
                stmnt = self._prepare_insert_statement(
                    table,
                    data,
                    natural_keys,
                    return_columns,
                    string_fields,
                    on_conflict_update
                )

                # Execute the statement
                with table.metadata.bind.begin() as connection:
                    if return_columns:
                        result = connection.execute(stmnt)
                        return [
                            dict(row) for row in result.mappings()
                        ]
                    connection.execute(stmnt)
                    return None

            except OperationalError as e:
                if isinstance(e.orig, DeadlockDetected):
                    self._handle_deadlock(
                        attempt,
                        "bulk insert",
                        len(data)
                    )
                    attempt += 1
                    continue
                raise

            except DataError as e:
                cleaned_data = self._handle_data_error(e, data)
                if not cleaned_data:
                    raise BulkOperationError(
                        "All data items failed validation"
                    )
                data = cleaned_data
                continue

            except Exception:
                if len(data) == 1:
                    raise

                # Split data and retry with smaller batches
                mid = len(data) // 2
                first_half = self.bulk_insert(
                    data[:mid],
                    table,
                    natural_keys,
                    return_columns,
                    string_fields,
                    on_conflict_update
                )
                second_half = self.bulk_insert(
                    data[mid:],
                    table,
                    natural_keys,
                    return_columns,
                    string_fields,
                    on_conflict_update
                )

                if return_columns:
                    return (
                        (first_half or []) +
                        (second_half or [])
                    )
                return None

        raise BulkOperationError(
            "Failed to complete bulk insert after "
            f"{self.max_retries} attempts"
        )

    def _prepare_insert_statement(
        self,
        table,
        data: List[dict],
        natural_keys: List[str],
        return_columns: Optional[List[str]],
        string_fields: Optional[List[str]],
        on_conflict_update: bool
    ) -> text:
        """Prepare the SQL insert statement."""
        # Implementation of statement preparation
        # This would include the actual SQL generation logic
        pass
