import mysql.connector
 
def create_database():
    try:
        
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="0000"
        )
        if connection.is_connected():
            cursor=connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("The database has been created successfully")
        
    except mysql.connector.Error as err:
        print(f"Error found:{err}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
            print("The database has been closed succcessfully")
            
create_database()