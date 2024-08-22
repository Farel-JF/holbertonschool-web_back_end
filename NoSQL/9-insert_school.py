#!/usr/bin/env python3
"""a Python function that lists all documents"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection (Collection): The pymongo collection object where
        the document will be inserted.
        **kwargs (Any): Key-value pairs to be included in the new document.
    Returns:
        str: The _id of the newly inserted document."""
    obj = mongo_collection.insert_one(kwargs)
    return obj.inserted_id
