import logging

from augur.application.db.lib import get_value

def get_redis_conn_values():

    redis_db_number = get_value("Redis", "cache_group") * 3
    redis_conn_string = get_value("Redis", "connection_string")

    if redis_conn_string[-1] != "/":
        redis_conn_string += "/"

    return redis_db_number, redis_conn_string

def get_rabbitmq_conn_string():

    rabbbitmq_conn_string = get_value("RabbitMQ", "connection_string")

    return rabbbitmq_conn_string
