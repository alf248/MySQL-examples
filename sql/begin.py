import sql.tables as create_table
import sql.insert as insert
import sql.select as select
from mysql.connector import connect, Error


def begin_sql(username, password, database):
    initialize_database(username, password, database)
    connect_to_database_and_query(username, password, database)


def create_database(connection, database):
    with connection.cursor() as cursor:
        cursor.execute("DROP DATABASE IF EXISTS "+database)
        cursor.execute("CREATE DATABASE "+database)


def create_tables_and_insert_records(connection):
    with connection.cursor() as cursor:
        
        cursor.execute(create_table.brands)
        cursor.execute(create_table.models)
        cursor.execute(create_table.customers)
        cursor.execute(create_table.orders)
        
        cursor.execute(insert.brands)
        cursor.execute(insert.models)
        cursor.execute(insert.customers)
        cursor.execute(insert.orders)

        connection.commit()


def select_queries(connection):
    with connection.cursor() as cursor:

        cursor.execute(select.select_brands)
        print("German brands:")
        for row in cursor.fetchall():
            print("\t",row[0])

        cursor.execute(select.count_all_models_for_each_brand)
        print("Models per brand:")
        for row in cursor.fetchall():
            print("\t",row[0], row[1])

        cursor.execute(select.count_fast_models_for_each_brand)
        print("Fast models per brand:")
        for row in cursor.fetchall():
            print("\t",row[0]+":", row[1])

        cursor.execute(select.total_sum_payed_per_model)
        print("Total sum payed per model:")
        for row in cursor.fetchall():
            print("\t",row[0]+":", row[1])



def initialize_database(username, password, database):
    try:
        with connect(
            host="localhost",
            user=username,
            password=password,
        ) as connection:
            create_database(connection, database)
            
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
            create_tables_and_insert_records(connection)
            select_queries(connection)
            
    except Error as e:
        print("error")
        print(e)