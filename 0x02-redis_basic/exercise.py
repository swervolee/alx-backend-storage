#!/usr/bin/env python3
"""
Redis
"""

import redis


class Cache():
    """
    Redis
    """
    __redis = None

    def __init__(self):
        """
        class cache init
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: any) -> str:
        """
        Generates a random string and uses
        it as key to store data to redis
        """
        import uuid

        random_string = str(uuid.uuid4())
        self.__redis.set(random_string, data)
        return random_string
