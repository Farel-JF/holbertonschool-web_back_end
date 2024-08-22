#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient

def print_log_stats():
    """Connects to MongoDB and prints log statistics."""

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method})
    for method in methods}

    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    print_log_stats()
