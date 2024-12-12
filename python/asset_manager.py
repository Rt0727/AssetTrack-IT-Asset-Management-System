# asset_manager.py

import psycopg2
from db_connector import get_db_connection

def add_asset(asset_name, asset_type, purchase_date, value):
    """Add a new asset to the database."""
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = """
    INSERT INTO assets (asset_name, asset_type, purchase_date, value)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (asset_name, asset_type, purchase_date, value))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Asset {asset_name} added successfully.")

def update_asset(asset_id, asset_name, asset_type, purchase_date, value):
    """Update asset details in the database."""
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = """
    UPDATE assets
    SET asset_name = %s, asset_type = %s, purchase_date = %s, value = %s
    WHERE asset_id = %s
    """
    cursor.execute(query, (asset_name, asset_type, purchase_date, value, asset_id))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Asset {asset_id} updated successfully.")

def delete_asset(asset_id):
    """Delete an asset from the database."""
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = "DELETE FROM assets WHERE asset_id = %s"
    cursor.execute(query, (asset_id,))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Asset {asset_id} deleted successfully.")

def get_all_assets():
    """Fetch all assets from the database."""
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = "SELECT * FROM assets"
    cursor.execute(query)
    
    assets = cursor.fetchall()
    cursor.close()
    connection.close()
    return assets