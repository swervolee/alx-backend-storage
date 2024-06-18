#!/usr/bin/env python3
"""
Inserting into a document
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    inserts kwargs into mongo_collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
