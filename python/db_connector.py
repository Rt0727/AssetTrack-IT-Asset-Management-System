# db_connector.py

import psycopg2
import os

def get_db_connection():
    """Establish and return a connection to the PostgreSQL database."""
    connection = psycopg2.connect(
        dbname=os.getenv('DB_NAME', 'asset_db'),
        user=os.getenv('DB_USER', 'admin'),
        password=os.getenv('DB_PASSWORD', 'securepassword'),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432')
    )
    return connection