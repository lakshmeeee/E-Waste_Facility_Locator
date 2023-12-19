# import pandas as pd
# import psycopg2
# from psycopg2 import sql

# db_host = "localhost"
# db_name = "e-waste"
# db_user = "postgres"
# db_password = "12345"

# def insert_data():
#     try:
#         connection = psycopg2.connect(
#             host=db_host,
#             database=db_name,
#             user=db_user,
#             password=db_password
#         )
#     except psycopg2.Error as e:
#         print("Error connecting to the database:", e)
#         exit()

#     csv_file_path = 'location_db.csv'

#     try:
#         df = pd.read_csv(csv_file_path)
#     except FileNotFoundError:
#         print(f"CSV file '{csv_file_path}' not found.")
#         exit()


#     cursor = connection.cursor()
#     table_name = 'consumer'

#     # Prepare the INSERT INTO query with placeholders
#     insert_query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
#         sql.Identifier(table_name),
#         sql.SQL(', ').join(map(sql.Identifier, df.columns)),
#         sql.SQL(', ').join(sql.Placeholder() * len(df.columns))
#     )

#     for _, row in df.iterrows():
#         values = [row[column] for column in df.columns]
#         cursor.execute(insert_query, values)

#     # Commit the changes to the database
#     connection.commit()
#     print("Data inserted successfully.")

        
#     cursor.close()
#     connection.close()

# def read_data(sql):
#     try:
#         connection = psycopg2.connect(
#             host=db_host,
#             database=db_name,
#             user=db_user,
#             password=db_password
#         )
#     except psycopg2.Error as e:
#         print("Error connecting to the database:", e)
#         exit()
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     value = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return value


# # import psycopg2
# # import csv

# # conn = psycopg2.connect(database="e-waste_fl", user='postgres', password='ssword', host='localhost', port= '5432')
# # # #Setting auto commit false
# # conn.autocommit = True

# # # #Creating a cursor object using the cursor() method
# # cursor = conn.cursor()

# # csv_file_path = "location_db.csv"
# # table_name = "consumers"


# # with open(csv_file_path, 'r') as csvfile:
# #     csvreader = csv.reader(csvfile)
# #     next(csvreader)  # Skip the header row if it exists
    
# #     for row in csvreader:
# #         # Assuming the CSV columns correspond to the table columns in order
# #         insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))});"
# #         cursor.execute(insert_query, tuple(row))

# # # Commit the changes to the database
# # conn.commit()
# # cursor.close()
# # conn.close()

