import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()  # get the enviroment varibles


def connect_to_db() -> psycopg2.extensions.connection:
    """Establishes a connection to the PostgreSQL database"""
    db_parms: dict = {
        "host": os.getenv("HOST"),
        "port": os.getenv("DB_PORT"),
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("USER"),
        "password": os.getenv("PASSWORD"),
    }

    try:
        conn: psycopg2.extensions.connection = psycopg2.connect(
            **db_parms
        )  # connect to the data base -> ** stands for kwargs -> key word arguments, basically dict objects(key and value)
        print("Connected to the database!")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
