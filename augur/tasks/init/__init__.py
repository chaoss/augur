import logging
import sys
from augur.application.db.lib import get_value
from augur.application.db.engine import DatabaseEngine
from augur.application.db.session import DatabaseSession

logger = logging.getLogger(__name__)

def is_bootstrap_mode():
    """Returns True if the current command is a bootstrap command."""
    args = sys.argv
    if "--help" in args:
        return True
    if len(args) > 1 and args[1] == "config":
        return True
    return False

def get_redis_conn_values():
    try:
        with DatabaseEngine() as engine, DatabaseSession(logging.getLogger(__name__), engine) as session:
            redis_db_number = get_value("Redis", "cache_group") * 3
            redis_conn_string = get_value("Redis", "connection_string")
            return redis_db_number, redis_conn_string

    except Exception as e:
        if is_bootstrap_mode():
            return 0, "redis://localhost:6379/0"
        
        logger.critical(f"CRITICAL: Failed to load Redis config. Error: {e}")
        raise e 

def get_rabbitmq_conn_string():
    try:
        with DatabaseEngine() as engine, DatabaseSession(logging.getLogger(__name__), engine) as session:
            return get_value("RabbitMQ", "connection_string")
    except Exception as e:
        if is_bootstrap_mode():
             return "amqp://guest:guest@localhost:5672/"
        
        logger.critical(f"CRITICAL: Failed to load RabbitMQ config. Error: {e}")
        raise e