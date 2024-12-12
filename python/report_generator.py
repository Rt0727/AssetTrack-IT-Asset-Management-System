# report_generator.py

import pandas as pd
from db_connector import get_db_connection

def generate_asset_report():
    """Generate a report for all assets."""
    connection = get_db_connection()
    query = "SELECT asset_name, asset_type, purchase_date, value FROM assets"
    df = pd.read_sql(query, connection)
    connection.close()
    
    # Generate a summary report
    report = df.groupby('asset_type').agg({'value': 'sum'}).reset_index()
    print(report)
    report.to_csv('asset_report.csv', index=False)
    print("Asset report generated as asset_report.csv.")