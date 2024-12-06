import mysql.connector
from dotenv import load_dotenv, dotenv_values
import os
from auth import User

def connect_database() -> mysql.connector.connection.MySQLConnection:
    try :
        load_dotenv()
        database = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE_NAME"),
            port=os.getenv("MYSQL_PORT")
        )
        return database
    except:
        raise ValueError("Can't connect to database")
    
def close_database(database: mysql.connector.connection.MySQLConnection):
    database.close()
    
def create_user_table(database: mysql.connector.connection.MySQLConnection):
    cursor = database.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS User (\n" +
        "Id INT PRIMARY KEY AUTO_INCREMENT,\n" +
        "Username VARCHAR(255) NOT NULL UNIQUE,\n" +
        "Password VARCHAR(64) NOT NULL,\n" +
        "DisplayName VARCHAR(255),\n" +
        "Token VARCHAR(255)\n" +
        ")"
    )
    database.commit()

def import_user_to_table(user: User) -> None:
    database = connect_database()
    cursor = database.cursor()

    create_user_table(database)
    cursor.execute(
        "INSERT INTO User (Id, Username, Password, DisplayName, Token) VALUES (%s, %s, %s, %s, %s)",
        (user.Id, user.Username, user.Password, user.DisplayName, user.Token)
    )
    database.commit()
    close_database(database)
