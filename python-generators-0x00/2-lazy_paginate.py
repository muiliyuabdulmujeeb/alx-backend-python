from seed import connect_to_prodev




def paginate_users(page_size, offset):
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data ORDER BY user_id LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size: int):
    #for the first time, the offset would be 0, then it would be page_size + offset, the next one would be new_page_size + offset
    offset = 0
    while True:
        rows = paginate_users(page_size, offset)
        if not rows:
            break
        offset += page_size
        yield rows

