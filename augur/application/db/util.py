import time
import logging
from typing import Callable, TypedDict, Any, List, Dict, Optional, Union
from sqlalchemy.exc import OperationalError
from augur.application.db.models.base import Base


def catch_operational_error(func: Callable[[], Any]) -> Any:
    """
    Executes a function and retries up to 4 times if OperationalError occurs.
    Implements exponential backoff starting with 240 seconds.
    """
    attempts = 0
    error: Optional[str] = None
    timeout = 240

    while attempts < 4:
        if attempts > 0:
            #Do a 30% exponential backoff
            time.sleep(timeout)
            timeout = int(timeout * 1.3)
        try:
            return func()
        except OperationalError as e:
            print(f"ERROR: {e}")
            error = str(e)

        attempts += 1

    raise Exception(error)


def execute_session_query(query: Any, query_type: str = "all") -> Any:
    """
    Executes an SQLAlchemy ORM query with retries on OperationalError.
    
    Args:
        query: SQLAlchemy ORM query object.
        query_type: One of 'all', 'one', 'first'.
    
    Returns:
        Query result according to query_type.
    """
    func: Optional[Callable[[], Any]] = None

    if query_type == "all":
        func = query.all
    elif query_type == "one":
        func = query.one
    elif query_type == "first":
        func = query.first
    else:
        raise Exception(f"ERROR: Unsupported query type '{query_type}'")

    return catch_operational_error(func)

def convert_orm_list_to_dict_list(result: List["Base"]) -> List[Dict[str, Any]]:
    """
    Converts a list of ORM model instances to a list of dictionaries.
    """
    new_list: List[Dict[str, Any]] = []

    for row in result:
        row_dict = dict(row.__dict__)  # Copy to avoid mutating the ORM instance
        row_dict.pop("_sa_instance_state", None)  # Remove SQLAlchemy internal state
        new_list.append(row_dict)

    return new_list

class ConfigDict(TypedDict, total=False):
    type: Optional[str]
    value: Union[str, int, float, bool]

def convert_type_of_value(
    config_dict: ConfigDict, logger: Optional[logging.Logger] = None
) -> ConfigDict:
    """
    Converts the 'value' field in config_dict to the type specified in 'type'.
    Supported types: str, int, bool, float.
    """
    data_type: Optional[str] = config_dict.get("type")

    if data_type == "str" or data_type is None:
        return config_dict

    elif data_type == "int":
        config_dict["value"] = int(config_dict["value"])

    elif data_type == "bool":
        value = str(config_dict["value"]).lower()
        config_dict["value"] = value != "false"

    elif data_type == "float":
        config_dict["value"] = float(config_dict["value"])

    else:
        msg = f"Need to add support for {data_type} types to config"
        if logger:
            logger.error(msg)
        else:
            print(msg)

    return config_dict