from mysql.connector import connect

class SQLFileRunner:

    def run_sql_file(self, file_path: str, connection_params: dict) -> None:
        with open(file_path, 'r') as file:
            sql_statement = file.read().strip()

        connection = connect(**connection_params)
        cursor = connection.cursor()
        
        try:
            cursor.execute(sql_statement)
            connection.commit()
        except Exception as e:
            print(f"Error while executing \"{sql_statement}\": {e}")
        finally:
            cursor.close()
            connection.close()