import os
from initializer import Initializer
from utils.constants import database_initialize_order, table_initialize_order

connection_params_dbs = {
    'host': 'localhost',
    'user': 'root',
    'password': 'omegaroot',
}

connection_params_tables = {
    'host': 'localhost',
    'user': 'root',
    'password': 'omegaroot',
    'database': 'ims'
}

initializer = Initializer()

current_path = os.getcwd()
initializer_path = os.path.join(current_path, "initializer")

for database_initializer_path in database_initialize_order:
    database_initializer_file_path = os.path.join(initializer_path, database_initializer_path)
    initializer.initialize_database(database_initializer_file_path, connection_params_dbs)

for table_initializer_path in table_initialize_order:
    table_initializer_file_path = os.path.join(initializer_path, table_initializer_path)
    initializer.initialize_tables(table_initializer_file_path, connection_params_tables)