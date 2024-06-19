#!/usr/bin/env python3
"""
Redis
"""
from typing import Union, Optional, Callable
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator
    """
    key = method.__qualname__

    @wraps(method)
    def incr(self, *args, **kwargs):
        """
        Increments key
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return incr


class Cache:
    """
    Redis Cache
    """
    def __init__(self):
        """
        Class cache init
        """
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random string and uses
        it as key to store data to redis
        """
        random_string = str(uuid.uuid4())
        self._redis.set(random_string, data)
        return random_string

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, float, int, bytes]:
        """
        Fetches data from Redis
        """
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        """
        Conversion function
        """
        return str(self._redis.get(key).decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Conversion function
        """
        try:
            return int(self._redis.get(key).decode("utf-8"))
        except Exception:
            return 0
