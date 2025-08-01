"""This module defines the RedisCount class.
It imports the redis_connection as redis which is a connection to the redis cache
"""
from typing import Iterable, Any, Union

from collections.abc import MutableSequence
from augur.tasks.init.redis_connection import get_redis_connection
from augur import instance_id
from redis import exceptions
import numbers

class RedisScalar:

    def __init__(self, scalar_name: str, default_value: int = 0, override_existing: bool = False):

        self.redis_scalar_key = f"{instance_id}_{scalar_name}"
        self._scalar_name = scalar_name

        self.__value = default_value
        self.redis = get_redis_connection()

        #Check redis to see if key exists in cache
        if 1 != self.redis.exists(self.redis_scalar_key) or override_existing:
            #Set value
            self.redis.set(self.redis_scalar_key,self.__value)
        else:
            #else get the value 
            self.__value = int(float(self.redis.get(self.redis_scalar_key)))

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, otherVal):
        if isinstance(otherVal, numbers.Number):
            self.__value = otherVal
            self.redis.set(self.redis_scalar_key,self.__value)    
