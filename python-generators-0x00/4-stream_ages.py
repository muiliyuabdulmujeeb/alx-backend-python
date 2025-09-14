from seed import connect_to_prodev

connection = connect_to_prodev()

def stream_user_ages():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    ages = cursor.fetchall()
    for age_dict in ages:
        age = int(age_dict.get("age"))
        yield int(age)

def average_age():
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
        average = total_age/count
    
    print("Average age of users: ", average)

average_age()