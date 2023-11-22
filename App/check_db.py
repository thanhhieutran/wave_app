import  sqlite3
from    my_package.config import *
from    my_package.query_db import *
import base64
from PIL import Image

# Read me
# This file for check all infor all your database is using in this Application
## Check all infor table and row


print ("""Here is your infor
--------------------------------------------
       """)
if __name__ == '__main__':
    
    #1 Get DB infor
    if show_db_info:
        
        database_info = get_database_info()

        # Print the obtained information
        print("Tables and Row Counts:")
        for table, info in database_info['tables'].items():
            print(f"{table}: {info['row_count']} rows")

        print("\nTable Schemas:")
        for table, info in database_info['schemas'].items():
            print(f"{table} Schema:")
            for column in info['columns']:
                print(f"  {column[1]} - {column[2]}")
    else:
        print("""show db info is disable , check config.py
--------------------------------------------
              """)
    
    #2 Get kiln data 
    if show_kiln_data:
        #ex: (tag='Pyrometer', start_date='2023-10-20', end_date='2023-10-29')
        kiln_data = get_kiln_data(limit=10, end_date='2023-10-29')

        ## Print header
        print("{:<8} {:<15} {:<10} {:<10}".format('id', 'tag', 'value', 'time'))

        ## Print data
        for data in kiln_data:
            id, tag, value, time = data
            print("{:<8} {:<15} {:<10} {:<10}".format(id, tag, value, time))
    else:
        print("""Get kiln data is disable , check config.py
--------------------------------------------              
              """)
    
    #3 Check distinct data from table
    if check_distinct_data:
        data = get_distinct_data(table='kiln', name_col='tag')
        # print(data)
        print(f'There have {len(data)} instance:')
        for i in range(len(data)):
            k = data[i]
            i +=1
            print("{:<2} {:<8}".format(i, k[0]))
    else:
        print("""check_distinct_data is disable , check config.py
--------------------------------------------              
              """)
    
    #4 Update image to Database
    image_path = '/home/hieutran/Documents/wave_app/App/media/photo.jpg'
    with open(image_path, 'rb') as image_file:
        # Read the image file as bytes
        image_data = image_file.read()
    base64_encoded_image = base64.b64encode(image_data).decode('utf-8')   
    name_image = 'photo'
    type_image = 'jpg'
    image_base64 = base64_encoded_image
    update_image_db(name_image, type_image, image_base64) 

