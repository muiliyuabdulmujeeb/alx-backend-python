import time
import sqlite3 
import functools


query_cache = {}
def with_db_connection(func):
    """ your code goes here""" 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with sqlite3.connect('users.db') as conn:
            return func(conn, *args, **kwargs)
    return wrapper

"""your code goes here"""
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        cache_result = query_cache.get(kwargs.get("query"))
        if not cache_result:
            query_result = func(conn, *args, **kwargs)
            query_cache[kwargs.get("query")] = query_result
            return query_result
        return cache_result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")