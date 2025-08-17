#Write a simple python script that creates the database alx_book_store in your MySQL server.
import mysql.connector
def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='asmart',
            password='ANOINted@2003',
            database='mysql'
        )
        cursor = connection.cursor()
        # create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully. ")
    except mysql.connector.error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
            if connection:
                connection.close()