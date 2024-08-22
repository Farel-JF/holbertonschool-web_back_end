#!/usr/bin/env python3
"""A Python function to find schools with a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Finds all schools that have the specified topic.
    Args:
        mongo_collection (Collection): The pymongo collection object where the
        documents are stored.
        topic (str): The topic to search for.
    Returns:
        List[Dict]: A list of dictionaries representing schools with the
        specified topic."""
    return list(mongo_collection.find({"topics": topic}))
