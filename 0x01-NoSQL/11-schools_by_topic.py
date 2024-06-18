#!/usr/bin/env python3
"""
Document query
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Document query
    """
    return list(mongo_collection.find({"topics": topic})
