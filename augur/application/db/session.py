import os
import re
import time
import sys
import random
import logging
import json
import httpx
import sqlalchemy as s

from typing import Optional, List, Union
from psycopg2.errors import DeadlockDetected

# from augur.tasks.util.random_key_auth import RandomKeyAuth
from augur.application.db.engine import create_database_engine
from augur.application.config import AugurConfig
from augur.application.db.models import Platform
from augur.tasks.util.worker_util import remove_duplicate_dicts, remove_duplicate_naturals


def remove_null_characters_from_string(string):

    if string:
        return string.replace("\x00", "\uFFFD")

    return string

def remove_null_characters_from_strings_in_dict(data, fields):

    for field in fields:

        # ensure the field exits in the dict
        try:
            data[field] = remove_null_characters_from_string(data[field])
        except KeyError:
            print(
                f"Error tried to remove null characters from the field: {field}, but it wasn't present in the dict")
            continue

        except AttributeError:
            continue

    return data

def remove_null_characters_from_list_of_dicts(data_list, fields):

    for value in data_list:
        value = remove_null_characters_from_strings_in_dict(value, fields)

    return data_list


class DatabaseSession(s.orm.Session):

    def __init__(self, logger, engine=None):
    
        self.logger = logger
        self.config = AugurConfig(logger=logger, session=self)

        self.engine = engine
        if self.engine is None:
            self.engine = create_database_engine()

        super().__init__(self.engine)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.close()
    
    def execute_sql(self, sql_text):

        with self.engine.connect():
            connection = self.engine.connect()

            return connection.execute(sql_text)

    def fetchall_data_from_sql_text(self,sql_text):
        result = self.execute_sql(sql_text).fetchall()
        return [dict(zip(row.keys(), row)) for row in result]

    def insert_data(self, data: Union[List[dict], dict], table, natural_keys: List[str], return_columns: Optional[List[str]] = None, string_fields: Optional[List[str]] = None, on_conflict_update:bool = True) -> Optional[List[dict]]:

        if isinstance(data, list) is False:
            
            # if a dict is passed to data then 
            # convert it to a list with one value
            if isinstance(data, dict) is True:
                data = [data]
            
            else:
                self.logger.info("Data must be a list or a dict")
                return None

        if len(data) == 0:
            # self.logger.info("Gave no data to insert, returning...")
            return None

        if isinstance(data[0], dict) is False: 
            self.logger.info("Must be list of dicts")
            return None

        # remove any duplicate data 
        # this only counts something as a duplicate if every field is the same
        data = remove_duplicate_dicts(data)
        data = remove_duplicate_naturals(data,natural_keys)

        # remove null data from string fields
        if string_fields and isinstance(string_fields, list):
            data = remove_null_characters_from_list_of_dicts(data, string_fields)

        # creates list of arguments to tell sqlalchemy what columns to return after the data is inserted
        returning_args = []
        if return_columns:
            for column in return_columns:
                argument = getattr(table, column)
                returning_args.append(argument)

        # creates insert on table
        # that returns cols specificed in returning_args
        # and inserts the data specified in data
        # NOTE: if return_columns does not have an values this still works
        stmnt = s.dialects.postgresql.insert(table).returning(*returning_args).values(data)


        if on_conflict_update:

            # create a dict that the on_conflict_do_update method requires to be able to map updates whenever there is a conflict. See sqlalchemy docs for more explanation and examples: https://docs.sqlalchemy.org/en/14/dialects/postgresql.html#updating-using-the-excluded-insert-values
            setDict = {}
            for key in data[0].keys():
                    setDict[key] = getattr(stmnt.excluded, key)
                
            stmnt = stmnt.on_conflict_do_update(
                #This might need to change
                index_elements=natural_keys,
                
                #Columns to be updated
                set_ = setDict
            )

        else:
            stmnt = stmnt.on_conflict_do_nothing(
                index_elements=natural_keys
            )


        # print(str(stmnt.compile(dialect=s.dialects.postgresql.dialect())))
        attempts = 0
        # creates list from 1 to 10
        sleep_time_list = list(range(1,11))
        deadlock_detected = False

        # if there is no data to return then it executes the insert then returns nothing
        if not return_columns:

            while attempts < 10:
                try:
                    with self.engine.connect() as connection:
                        connection.execute(stmnt)
                        break
                except s.exc.OperationalError as e:
                    # print(str(e).split("Process")[1].split(";")[0])
                    if isinstance(e.orig, DeadlockDetected):
                        deadlock_detected = True
                        sleep_time = random.choice(sleep_time_list)
                        self.logger.debug(f"Deadlock detected on {table.__table__} table...trying again in {round(sleep_time)} seconds: transaction size: {len(data)}")
                        time.sleep(sleep_time)

                        attempts += 1
                        continue
                    
                    raise e

            else:
                self.logger.error("Unable to insert data in 10 attempts")
                return None

            if deadlock_detected is True:
                self.logger.error("Made it through even though Deadlock was detected")
                    
            return None
        

        # othewise it gets the requested return columns and returns them as a list of dicts
        while attempts < 10:
            try:
                with self.engine.connect() as connection:
                    return_data_tuples = connection.execute(stmnt).fetchall()
                    break
            except s.exc.OperationalError as e:
                if isinstance(e.orig, DeadlockDetected):
                    sleep_time = random.choice(sleep_time_list)
                    self.logger.debug(f"Deadlock detected on {table.__table__} table...trying again in {round(sleep_time)} seconds: transaction size: {len(data)}")
                    time.sleep(sleep_time)

                    attempts += 1
                    continue   

                raise e

        else:
            self.logger.error("Unable to insert and return data in 10 attempts")
            return None

        if deadlock_detected is True:
            self.logger.error("Made it through even though Deadlock was detected")

        return_data = []
        for data_tuple in return_data_tuples:
            return_data.append(dict(data_tuple))

        # using on confilict do nothing does not return the 
        # present values so this does gets the return values
        if not on_conflict_update:

            conditions = []
            for column in natural_keys:

                column_values = [value[column] for value in data]

                column = getattr(table, column)

                conditions.append(column.in_(tuple(column_values)))

            result = (
                self.query(table).filter(*conditions).all()
            )

            for row in result:

                return_dict = {}
                for field in return_columns:

                    return_dict[field] = getattr(row, field)

                return_data.append(return_dict)


        return return_data