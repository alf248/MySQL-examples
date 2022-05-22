from sql_queries import *
from getpass import getpass
from mysql.connector import connect, Error


def start(username, password, database):
    initialize_database(username, password, database)
    connect_to_database_and_query(username, password, database)

def setup_database_queries(connection, database_name):
    with connection.cursor() as cursor:
        cursor.execute("DROP DATABASE IF EXISTS "+database_name)
        cursor.execute("CREATE DATABASE "+database_name)

def insertion_queries(connection):
    with connection.cursor() as cursor:
        cursor.execute(create_car_brand_table)
        cursor.execute(create_car_models_table)
        cursor.execute(insert_car_brands)
        cursor.execute(insert_car_models)
        connection.commit()

def selection_queries(connection):
    with connection.cursor() as cursor:
        cursor.execute(select_brands)
        print("German brands:")
        for row in cursor.fetchall():
            print("\t",row[0])

    with connection.cursor() as cursor:
        cursor.execute(count_all_models_for_each_brand)
        print("Models per brand:")
        for row in cursor.fetchall():
            print("\t",row[0], row[1])

    with connection.cursor() as cursor:
        cursor.execute(count_fast_models_for_each_brand)
        print("Fast models per brand:")
        for row in cursor.fetchall():
            print("\t",row[0], row[1])

def initialize_database(username, password, database):
    try:
        with connect(
            host="localhost",
            user=username,
            password=password,
        ) as connection:
            setup_database_queries(connection, database)
            
    except Error as e:
        print("error")
        print(e)

def connect_to_database_and_query(username, password, database):
    try:
        with connect(
            host="localhost",
            user=username,
            password=password,
            database=database
        ) as connection:
            insertion_queries(connection)
            selection_queries(connection)
            
    except Error as e:
        print("error")
        print(e)