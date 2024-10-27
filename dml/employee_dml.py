class CustomerDML:

    @staticmethod
    def getUsernameAndPasswordEmployee(company_id: int, username: str, password: str, is_admin: bool) -> str:
        selectQuery = f'SELECT customer_user_name, customer_password
                        FROM Customer
                        WHERE company_id = {company_id} AND customer_user_name = "{username}" AND is_admin = '
        if is_admin:
            selectQuery += 'TRUE;'
        else:
            selectQuery += 'FALSE;'