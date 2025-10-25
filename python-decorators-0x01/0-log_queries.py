import sqlite3
import functools
from datetime import datetime, timezone

#### decorator to lof SQL queries
""" YOUR CODE GOES HERE"""
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args:
            print(f"{datetime.now(timezone.utc)}: query{args} executed by function {func.__name__}")
        if kwargs:
            print(f"{datetime.now(timezone.utc)}: query{kwargs} executed by function {func.__name__}")
        func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")