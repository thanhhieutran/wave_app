import  sqlite3
from    my_package.config import *
from    my_package.query_db import *
import base64
from PIL import Image
import os
from io import BytesIO
import matplotlib.pyplot as plt
from my_package.synthetic_data import *

# Read me
# This file for check all infor all your database is using in this Application
## Check all infor table and row


print ("""Here is your infor""")
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
        print("""#1---show db info is disable , check config.py
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
        print("""#2---Get kiln data is disable , check config.py""")
    
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
        print("""#3---check_distinct_data is disable , check config.py""")
    
    #4 Update image to Database
    # Update all image in media folder then save it in to database
    if update_image :
        # Clear all image before sync
        clear_image_db()

        # List all file in media folder
        all_files = os.listdir(image_folder_path)

        # Filter image files by extension
        image_files = [file for file in all_files if file.lower().endswith(('.png', '.jpg', '.webp', '.gif'))]

        for image in image_files:
            image_path = os.path.join(image_folder_path, image)

            # Get image name and type
            image_name, image_extension = os.path.splitext(image)
            image_type = image_extension[1:].lower()

            # Convert image to base64
            try:
                with open(image_path, 'rb') as image_content:
                    image_data = base64.b64encode(image_content.read()).decode("utf-8")
            except Exception as e:
                print(f"Error converting image {image_content} to base64: {e}")
                continue

            # Update the database
            update_image_db(name= image_name, type=image_type, image_base64=image_data)
    else:
        print("""#4---Update image function is disable - Please enable it if you want to use""")

    #5 Get image base64 in database
    if get_image_string :
        image_path = 'App/media/cement_factory.jpg'
        image_content = get_image_from_path(image_path)
        print(image_content)
    else:
        print("""#5---Get image function is disable - Please enable it if you want to use""")


    # audience_days1 = generate_time_series(1)
    # # audience_hits1 = generate_random_walk(10000, 20000, 0.2)
    # print([('A', next(audience_days1), next(env_value('nghien_than'))) for i in range(9)])

    # test_data = get_kiln_data(limit=4, tag='Pyrometer')
    # print(test_data)
    # # for test in test_data:
    # #     print(test)
    pyrometer_data = get_kiln_data (tag="Pyrometer", limit=10)  
    print(pyrometer_data)