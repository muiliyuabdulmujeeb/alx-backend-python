import time
import sqlite3 
import functools

#### paste your with_db_decorator here
def with_db_connection(func):
    """ your code goes here""" 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with sqlite3.connect('users.db') as conn:
            return func(conn, *args, **kwargs)
    return wrapper
""" your code goes here"""

def retry_on_failure(retries, delay):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(conn, *args, **kwargs):
            try:
                result = func(conn, *args, **kwargs)
                return result
            except Exception:
                for i in range(retries):
                    try:
                        result = func(conn, *args, **kwargs)
                        return result
                    except Exception as e:
                        if i + 1 == retries:
                            raise Exception(e)
                    time.sleep(delay)
        return wrapper
    return decorator
@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)