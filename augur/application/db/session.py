import time
import random
from sqlalchemy.orm import Session
from sqlalchemy.dialects import postgresql
from sqlalchemy.exc import OperationalError
from sqlalchemy import func, or_

from typing import Optional, List, Union
from psycopg2.errors import DeadlockDetected

from augur.tasks.util.worker_util import remove_duplicates_by_uniques


def remove_null_characters_from_string(string):
    if string:
        return string.replace("\x00", "\uFFFD")
    return string


def remove_null_characters_from_strings_in_dict(data, fields):
    for field in fields:
        try:
            data[field] = remove_null_characters_from_string(data[field])
        except KeyError:
            print(f"Error: tried to remove null characters from field '{field}', but it wasn't present in dict")
            continue
        except AttributeError:
            continue
    return data


def remove_null_characters_from_list_of_dicts(data_list, fields):
    for value in data_list:
        value = remove_null_characters_from_strings_in_dict(value, fields)
    return data_list


class DatabaseSession(Session):

    def __init__(self, logger, engine=None, from_msg=None, **kwargs):
        self.logger = logger
        self.engine = engine
        self.engine_created = False

        if self.engine is None:
            self.logger.debug("Passing engine will be required soon")
            from augur.application.db.engine import DatabaseEngine
            self.engine_created = True
            self.engine = DatabaseEngine().engine
            if from_msg:
                logger.debug(f"ENGINE CREATE: {from_msg}")
            else:
                logger.debug("ENGINE CREATE")

        super().__init__(bind=self.engine, **kwargs)   

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        
        self.close()

    def __del__(self):
        self.close()

    def execute_sql(self, sql_text):
        with self.engine.begin() as connection:
            return_data = connection.execute(sql_text)
        return return_data

    def fetchall_data_from_sql_text(self, sql_text):
        with self.engine.begin() as connection:
            result = connection.execute(sql_text)
        return [dict(row) for row in result.mappings()]

    def insert_data(
        self,
        data_input: Union[List[dict], dict],
        table,
        natural_keys: List[str],
        return_columns: Optional[List[str]] = None,
        string_fields: Optional[List[str]] = None,
        on_conflict_update: bool = True
    ) -> Optional[List[dict]]:

       
        if not isinstance(data_input, list):
            if isinstance(data_input, dict):
                data = [data_input]
            else:
                self.logger.info("Data must be a list or a dict")
                return None
        else:
            data = list(data_input)

        if not data:
            return None

        if not isinstance(data[0], dict):
            self.logger.info("Must be list of dicts")
            return None

      
        data = remove_duplicates_by_uniques(data, natural_keys)

       
        if string_fields and isinstance(string_fields, list):
            data = remove_null_characters_from_list_of_dicts(data, string_fields)

        returning_args = []
        if return_columns:
            for column in return_columns:
                argument = getattr(table, column)
                returning_args.append(argument)

        stmnt = postgresql.insert(table).returning(*returning_args).values(data)

        if on_conflict_update:
            setDict = {}
            base_table = getattr(table, "__table__", table)
            for key in data[0].keys():
                existing_col = getattr(base_table.c, key)
                setDict[key] = func.coalesce(getattr(stmnt.excluded, key), existing_col)

            stmnt = stmnt.on_conflict_do_update(
                index_elements=natural_keys,
                set_=setDict
            )
        else:
            stmnt = stmnt.on_conflict_do_nothing(index_elements=natural_keys)

        attempts = 0
        sleep_time_list = list(range(10, 66))
        deadlock_detected = False

        
        def run_insert(statement):
            nonlocal attempts, deadlock_detected
            while attempts < 10:
                try:
                    with self.engine.begin() as connection:
                        return connection.execute(statement)
                except OperationalError as e:
                    if isinstance(e.orig, DeadlockDetected):
                        deadlock_detected = True
                        sleep_time = random.choice(sleep_time_list)
                        self.logger.debug(
                            f"Deadlock detected on {getattr(table, '__table__', table)} table... "
                            f"retrying in {sleep_time} seconds (transaction size: {len(data)})"
                        )
                        time.sleep(sleep_time)
                        attempts += 1
                        continue
                    raise e
                except Exception as e:
                    if len(data) == 1:
                        raise e
                    time.sleep(3)
                    first_half = data[:len(data)//2]
                    second_half = data[len(data)//2:]
                    res1 = self.insert_data(first_half, table, natural_keys, return_columns, string_fields, on_conflict_update)
                    res2 = self.insert_data(second_half, table, natural_keys, return_columns, string_fields, on_conflict_update)
                    return (res1 or []) + (res2 or [])
            else:
                self.logger.error("Unable to insert data in 10 attempts")
                return None

        if not return_columns:
            run_insert(stmnt)
            if deadlock_detected:
                self.logger.error("Made it through even though Deadlock was detected")
            return None

        return_data_tuples = run_insert(stmnt)
        if return_data_tuples is None:
            return None

        return_data = [dict(row) for row in return_data_tuples.mappings()]

        if not on_conflict_update:
            conditions = []
            for column in natural_keys:
                column_values = [value[column] for value in data]
                column_obj = getattr(table, column)
               
                conditions.append(column_obj.in_(tuple(column_values)))

            result = self.query(table).filter(or_(*conditions)).all()
            for row in result:
                return_dict = {field: getattr(row, field) for field in return_columns}
                return_data.append(return_dict)

        if deadlock_detected:
            self.logger.error("Made it through even though Deadlock was detected")

        return return_data