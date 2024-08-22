NoSQL MongoDB Project
Overview
This project involves working with MongoDB, a NoSQL database, and Python to perform various operations like inserting, updating, and querying documents. Below is a detailed explanation of NoSQL, MongoDB, and the provided scripts.

What is NoSQL?
NoSQL stands for "Not Only SQL" and refers to a class of database management systems that do not follow the traditional relational model. They are designed to handle large volumes of unstructured or semi-structured data, providing scalability and flexibility that traditional SQL databases may not offer.

Types of NoSQL Databases
Document Stores: Store data in JSON-like documents. Example: MongoDB.
Key-Value Stores: Store data as key-value pairs. Example: Redis.
Column-Family Stores: Store data in columns rather than rows. Example: Apache Cassandra.
Graph Databases: Store data as nodes and edges to represent relationships. Example: Neo4j.
Difference Between SQL and NoSQL
Schema: SQL databases require a predefined schema, whereas NoSQL databases allow for dynamic schemas.
Scalability: SQL databases are typically scaled vertically (by increasing hardware), while NoSQL databases are designed for horizontal scaling (by adding more servers).
Data Model: SQL databases use tables and rows, while NoSQL databases use various data models like documents, key-value pairs, columns, or graphs.
ACID Properties
ACID stands for Atomicity, Consistency, Isolation, and Durability. These properties ensure reliable transactions in databases:

Atomicity: Ensures that all parts of a transaction are completed; if not, the transaction is aborted.
Consistency: Ensures that a transaction brings the database from one valid state to another.
Isolation: Ensures that transactions are isolated from each other until they are completed.
Durability: Ensures that once a transaction is committed, it remains so even in the event of a system failure.
What is Document Storage?
Document storage refers to a database model where data is stored in document formats such as JSON or BSON. MongoDB, a popular NoSQL database, uses this model to store data.

Benefits of NoSQL Databases
Scalability: Designed to scale out by distributing data across multiple servers.
Flexibility: Allows for unstructured data and dynamic schema changes.
High Performance: Optimized for high throughput and low latency operations.
Cost-Effective: Can be more cost-effective than traditional relational databases in certain scenarios.
How to Query, Insert, Update, and Delete Information in MongoDB
Query: Use methods like find() to retrieve documents that match specific criteria.
Insert: Use insert_one() or insert_many() to add documents to a collection.
Update: Use update_one() or update_many() to modify existing documents.
Delete: Use delete_one() or delete_many() to remove documents from a collection.
MongoDB Commands and Scripts
MongoDB Command Files
List Databases: 0-list_databases
Insert Document: 1-insert
List All Documents: 3-all
Find All Matches: 4-match
Count Documents: 5-count
Update Document: 6-update
Delete Documents: 7-delete
Python Scripts
List All Documents (8-all.py):

python
Copy code
#!/usr/bin/env python3
from pymongo import MongoClient
from typing import List, Dict

def list_all(mongo_collection) -> List[Dict]:
    """Lists all documents in a MongoDB collection."""
    return list(mongo_collection.find())
Insert a Document (9-insert_school.py):

python
Copy code
#!/usr/bin/env python3
from pymongo import MongoClient
from typing import Dict

def insert_school(mongo_collection, **kwargs) -> str:
    """Inserts a new document into a MongoDB collection."""
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)
Update Topics (10-update_topics.py):

python
Copy code
#!/usr/bin/env python3
from pymongo import MongoClient
from typing import List

def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """Updates the topics of a school document in the MongoDB collection."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
Find Schools by Topic (11-schools_by_topic.py):

python
Copy code
#!/usr/bin/env python3
from pymongo import MongoClient
from typing import List, Dict

def schools_by_topic(mongo_collection, topic: str) -> List[Dict]:
    """Returns a list of schools that have a specific topic."""
    return list(mongo_collection.find({"topics": topic}))
Log Stats (12-log_stats.py):

python
Copy code
#!/usr/bin/env python3
from pymongo import MongoClient

def print_log_stats():
    """Connects to MongoDB and prints log statistics."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    print_log_stats()
Installation and Setup
Install MongoDB: Follow the official MongoDB installation guide for Ubuntu 18.04.
Install Python and PyMongo:
bash
Copy code
sudo apt-get install python3-pip
pip3 install pymongo
Run MongoDB:
bash
Copy code
sudo service mongod start
Usage
Run MongoDB Commands:

bash
Copy code
cat 0-list_databases | mongo
cat 1-insert | mongo my_db
Run Python Scripts:

bash
Copy code
./8-main.py
./9-main.py
./10-main.py
./11-main.py
./12-log_stats.py
Conclusion
This project demonstrates the use of MongoDB with Python for various database operations. It provides hands-on experience with NoSQL databases and MongoDB's query capabilities.
