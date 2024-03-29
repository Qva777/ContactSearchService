import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    """ Connect to PgSQL """
    return psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
