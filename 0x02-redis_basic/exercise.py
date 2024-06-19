#!/usr/bin/env python3
"""
Redis
"""
from typing import Union, Callable, Optional
import redis


class Cache():
    """
    Redis
    """
    def __init__(self):
        """
        class cache init
        """
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random string and uses
        it as key to store data to redis
        """
        import uuid

        random_string = str(uuid.uuid4())
        self._redis.set(random_string, data)
        return random_string
