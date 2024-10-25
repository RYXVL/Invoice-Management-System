import os
from initializer import Initializer

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

def getFilesInDirectory(directory):
    lst = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            absolute_path = os.path.join(root, file)
            lst.append(absolute_path)
            # print(absolute_path)
    return lst

initializer = Initializer()

current_path = os.getcwd()

new_path = os.path.join(current_path, "database_initializer")
files = getFilesInDirectory(new_path)
for file in files:
    initializer.initialize_database(file, connection_params_dbs)

new_path = os.path.join(current_path, "table_initializer")
files = getFilesInDirectory(new_path)
for file in files:
    initializer.initialize_tables(file, connection_params_tables)