import os
import tkinter as tk
from initializer import Initializer
from utils.constants import database_initialize_order, table_initialize_order
from ui.start_screen import StartScreen
from mysql.connector import connect

# connection_params_dbs = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'omegaroot',
# }

connection_params_tables = {
    'host': 'localhost',
    'user': 'root',
    'password': 'omegaroot',
    'database': 'ims'
}

# initializer = Initializer()

# current_path = os.getcwd()
# initializer_path = os.path.join(current_path, "initializer")

# for database_initializer_path in database_initialize_order:
#     database_initializer_file_path = os.path.join(initializer_path, database_initializer_path)
#     initializer.initialize_database(database_initializer_file_path, connection_params_dbs)

# for table_initializer_path in table_initialize_order:
#     table_initializer_file_path = os.path.join(initializer_path, table_initializer_path)
#     initializer.initialize_tables(table_initializer_file_path, connection_params_tables)

# metadata_initializer_file_path = os.path.join(initializer_path, "data_initializer.sql")
# initializer.initialize_metadata(metadata_initializer_file_path, connection_params_tables)


connection = connect(**connection_params_tables)
cursor = connection.cursor()    

root = tk.Tk()
app = StartScreen(root, cursor)
root.mainloop()

cursor.close()
connection.close()