#!/usr/bin/env python3
"""
Manipulate doc
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Manipulate document"""
    return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
