import mysql.connector
# from mysql.connector import Error
import getpass
def connect_to_server():
    try:
        host = input("Enter host name eg localhost: ")
        user = input("Enter MySQL username: ")
        password = getpass.getpass("Enter MySQL password: ")

        myconnection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
        )

        if myconnection.is_connected():
            print("Connection is successful") 
            return myconnection, host, user, password
        
    except mysql.connector.Error as e:
        print(e)
        return None


def createDB(myconnection):
    mycursor = myconnection.cursor()
    db_name = "alx_book_store"

    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print(f"Database '{db_name}' created successfully!")
        return db_name
    
    except mysql.connector.Error as e:
        if "database exists" in str(e).lower():
            print(f"Failure in creation of the database: {db_name} already exists")
        print(f"Failure in creation of the database: {e}")
    finally:
        mycursor.close()

def connectToDB(host, user, password, db_name):
    try:
        myconnection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )

        if myconnection.is_connected():
            print(f"Connection to the database '{db_name}' successful") 
            return myconnection  
    
    except mysql.connector.Error as e:
        print(f"Connection to the database '{db_name}' unsuccessful: {e}")
        return None
    

myconnection, host, user, password=connect_to_server()
db_name = createDB(myconnection)
db_connection = connectToDB(host, user, password, db_name)

myconnection.close()