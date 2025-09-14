from seed import connect_to_prodev

connection = connect_to_prodev()

def stream_users_in_batches(batch_size: int):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data ORDER BY user_id")
    rows = cursor.fetchmany(batch_size)

    for row in rows:
        yield row

def batch_processing(batch_size: int):
    for user in stream_users_in_batches(batch_size):
        if user.get("age") > 25:
            yield user

for user in batch_processing(50):
    print(user)
connection.close()