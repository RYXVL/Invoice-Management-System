from utils.sql_file_runner import SQLFileRunner

class Initializer:

    def __init__(self):
        self.sqlFileRunner = SQLFileRunner()

    def initialize_database(self, file_path: str, connection_params: dict) -> None:
        self.sqlFileRunner.run_sql_file(file_path, connection_params)

    def initialize_tables(self, file_path: str, connection_params: dict) -> None:
        self.sqlFileRunner.run_sql_file(file_path, connection_params)
