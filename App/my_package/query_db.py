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

# Description: Update new image
def update_image_db(name=None, type=None, image_base64=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Construct the SQL query based on parameters
    query = f'SELECT name, type, image_base64 FROM image_db WHERE name={name}'
    params = []

    try:
        cursor.execute(query, params)
        data = cursor.fetchall()
        conn.close()
    except:
        data =[] # no data
    
    # For check image already in database by name, type
    ## 0: no image have same name, type in DB
    ## 1: have image same name, but not same type
    ## 2: have image same name, type
    check_image = 0
    
    if len(data):
        check_image = 1
        print('This image have same name, let check type')
        for image in range(len(data)):
            if image[1]==type :
                check_image = 2
    
    # Update / Insert  image to image_db
    if check_image ==2: # if image have same name, tpye, just update content
        query_update = f'UPDATE image_db SET image_base64 = {image_base64}'
        params_update  = []

        cursor.execute(query_update, params_update)
        print(f'Updated image {name}.{type}')
        conn.close()
    else:
        query_insert = f'INSERT INTO image_db (name, type, image_base64) VALUES ( {name}, {type}, {image_base64} )'
        params_insert  = []

        cursor.execute(query_insert, params_insert)
        print(f'Inserted image {name}.{type}')
        conn.close()


