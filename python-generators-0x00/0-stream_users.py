from itertools import islice
from seed import connect_to_prodev


connection = connect_to_prodev()

def stream_users():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    users = cursor.fetchall()
    for user in users:
        yield user
    cursor.close()


connection.close()