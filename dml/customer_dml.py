class CustomerDML:

    @staticmethod
    def getUsernameAndPassword(company_id: int, username: str, password: str) -> str:
        selectQuery = f'SELECT customer_user_name, customer_password
                        FROM Customer
                        WHERE company_id = {company_id} AND customer_user_name = "{username}";'