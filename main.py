import sql_setup
import os


mySQL_username = os.getenv('USERNAME')
mySQL_password = os.getenv('PASSWORD')
mySQL_database = "sql_examples"

if (not mySQL_username or not mySQL_password):
    print("--ENV vars not found")
    print("--need USERNAME and PASSWORD for database")
    print("--you can put them in an .env file:")
    print("\tUSERNAME=<my_name>")
    print("\tPASSWORD=<my_password>")
    quit()

sql_setup.start(mySQL_username, mySQL_password, mySQL_database)