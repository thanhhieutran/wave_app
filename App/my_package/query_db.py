import  sqlite3
from    .config import *

# Readme
## This file is function for query database
## Help to check your database
## All config in config file 

# All Config here
DB_PATH = data_path

## For check_db.py
# Description: Get some data for kiln table
def get_kiln_data(id=None, tag=None, start_date=None, end_date=None, limit=None):
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Construct the SQL query based on parameters
    query = 'SELECT id,tag,value,time FROM kiln WHERE 1=1'
    params = []

    if id:
        query += ' AND id = ?'
        params.append(id)

    if tag:
        query += ' AND tag = ?'
        params.append(tag)

    if start_date:
        query += ' AND time >= ?'
        params.append(start_date)       # 2023-10-06 12:30:00

    if end_date:
        query += ' AND time <= ?'
        params.append(end_date)

    order = f' ORDER BY time DESC LIMIT {limit}'
    query += order # limit the number of results

    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()

    return data[::-1]  # Reverse the order to show the latest data first

# Description: Get some data for kiln table
def get_distinct_data(table=None, name_col=None):
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Construct the SQL query based on parameters
    query = f'SELECT DISTINCT {name_col} FROM {table} ORDER BY {name_col} DESC'
    params = []

    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()

    return data[::-1]  # Reverse the order to show the latest data first

# Description: Get all infor of database (table, schema, count all row)
def get_database_info():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Query to get the schema of the tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Query to get the number of rows in each table
    table_info = {}

    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        row_count = cursor.fetchone()[0]
        table_info[table_name] = {'row_count': row_count}

    # Query to get the schema of each table
    schema_info = {}

    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        schema_info[table_name] = {'columns': columns}

    conn.close()

    return {'tables': table_info, 'schemas': schema_info}

