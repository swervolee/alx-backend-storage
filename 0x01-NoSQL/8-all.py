#!/usr/bin/env python3
"""
python mongo
"""
import pymongo


def list_all(mongo_collection):
    """
    list collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
