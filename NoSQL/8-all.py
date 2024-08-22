#!/usr/bin/env python3
"""a Python function that lists all documents"""


def list_all(mongo_collection) -> List[Dict]:
    """Lists all documents in a MongoDB collection.
    Args:
        mongo_collection: The pymongo collection object.
    Returns:
        List[Dict]: A list of documents (each document is a dictionary)."""
    return list(mongo_collection.find())
