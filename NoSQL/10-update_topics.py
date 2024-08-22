#!/usr/bin/env python3
"""A Python function that updates topics in a MongoDB collection"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a school document in the MongoDB collection based
    on the school's name.
    Args:
        mongo_collection (Collection): The pymongo collection object where the
        document will be updated.
        name (str): The name of the school to update.
        topics (List[str]): A list of topics to set for the school.
    Returns:
        None"""

    mongo_collection.update_many({"name": name},{"$set": {"topics": topics}})
