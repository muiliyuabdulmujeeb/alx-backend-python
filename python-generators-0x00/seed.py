import csv
import mysql.connector
from mysql.connector.connection import MySQLConnection

#connect to server
def connect_db() -> MySQLConnection:
    conn: MySQLConnection = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "admin",
        port = 3306
    )
    return conn

#check version
def check_version(connection: MySQLConnection) -> str:
    cursor = connection.cursor()
    cursor.execute("SELECT VERSION()")
    version_row = cursor.fetchone()
    return f"Version:{version_row[0]}"

#create database
def create_database(connection: MySQLConnection) -> bool:
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    cursor.close()
    return True

#connect to database
def connect_to_prodev()-> MySQLConnection:
    conn: MySQLConnection = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "admin",
        database = "alx_prodev",
        port = 3306
        )
    return conn

#create table
def create_table(connection: MySQLConnection)-> bool:
    cursor = connection.cursor()
    cursor.execute(
        """ CREATE TABLE user_data(
            user_id VARCHAR(36) PRIMARY KEY DEFAULT(UUID()),
            name VARCHAR(60) NOT NULL,
            email VARCHAR(60) NOT NULL,
            age DECIMAL NOT NULL
            )"""
    )
    cursor.close()
    return True

#insert data
def insert_data(connection: MySQLConnection, data: str) -> bool:
    cursor = connection.cursor()
    try:
        with open(data, mode="r", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)

            rows = []
            for row in reader:
                rows.append((row.get("name"), row.get("email"), row.get("age")))

            sql = "INSERT INTO user_data (name, email, age) VALUES(%s, %s, %s)"
            cursor.executemany(sql, rows)
            connection.commit()
            print(f"{cursor.rowcount} rows inserted")
        return True
    except Exception as e:
        connection.rollback()
        print(f"Error while writing data: {e}")
    finally:    
        cursor.close()

