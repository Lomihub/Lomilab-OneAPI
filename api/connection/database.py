import mysql.connector
from dotenv import load_dotenv, dotenv_values
import os

class Database():
    def __init__(self):
        self.database = connect_database()
    
    def __str__(self) -> str:
        return self.database
        
    def __del__(self):
        close_database(self.database)
        
    def get_database(self) -> mysql.connector.connection.MySQLConnection:
        return self.database

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
        """
        CREATE TABLE IF NOT EXISTS User
        (
            Id             INT PRIMARY KEY AUTO_INCREMENT,
            BindId         VARCHAR(32)  NOT NULL,
            Username       VARCHAR(255) NOT NULL,
            Password       VARCHAR(255) NOT NULL,
            DisplayName    VARCHAR(255) NOT NULL,
            Role           ENUM ('admin', 'user') DEFAULT 'user',
            Status         BOOLEAN                DEFAULT TRUE,
            Email          VARCHAR(255),
            GoogleId       VARCHAR(255),
            FacebookId     VARCHAR(255),
            GithubId       VARCHAR(255),
            CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
            UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
            ProfilePicture VARCHAR(255),
            Blacklist      BOOLEAN                DEFAULT FALSE
        )
        """
    )
    database.commit()

def create_token_table(database: mysql.connector.connection.MySQLConnection):
    cursor = database.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Token (
            Id INT PRIMARY KEY AUTO_INCREMENT,
            UserId INT NOT NULL,
            NameToken VARCHAR(255) NOT NULL,
            Status BOOLEAN DEFAULT TRUE,
            TokenKey VARCHAR(32) NOT NULL,
            TokenType ENUM('admin', 'user') DEFAULT 'user',
            CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
            AccessedTime DATETIME,
            ExpiredTime DATETIME,
            RemainQuota INT,
            LimitedQuota INT DEFAULT 10,
            QuotaResetTime DATETIME,
            Models TEXT,
            Subnet VARCHAR(255),
            FOREIGN KEY (UserId) REFERENCES User(Id)
        )
        """
    )
    database.commit()
    
def create_api_key_table(database: mysql.connector.connection.MySQLConnection):
    cursor = database.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Token (
            Id INT PRIMARY KEY AUTO_INCREMENT,
            UserId INT NOT NULL,
            NameToken VARCHAR(255) NOT NULL,
            Status BOOLEAN DEFAULT TRUE,
            TokenKey VARCHAR(32) NOT NULL,
            TokenType ENUM('admin', 'user') DEFAULT 'user',
            CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
            AccessedTime DATETIME,
            ExpiredTime DATETIME,
        )
        """
    )
    database.commit()