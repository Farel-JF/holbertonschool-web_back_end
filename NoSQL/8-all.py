#!/usr/bin/env python3
"""a Python function that lists all documents"""


def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection.
    Args:
        mongo_collection: The pymongo collection object.
    Returns:
        List[Dict]: A list of documents (each document is a dictionary)."""
    liste_docs_de_la_collection = []
    if mongo_collection.find():
        for data in mongo_collection.find():
            liste_docs_de_la_collection.append(data)

    return liste_docs_de_la_collection
