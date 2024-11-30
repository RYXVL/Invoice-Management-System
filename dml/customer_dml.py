class CustomerDML:

    # @staticmethod
    # def getUsernameAndPassword(company_id: int, username: str, password: str) -> str:
    #     selectQuery = f'SELECT customer_user_name, customer_password
    #                     FROM Customer
    #                     WHERE company_id = {company_id} AND customer_user_name = "{username}";'
        
    @staticmethod
    def insertCustomer(customer_user_name: str, customer_password: str, customer_id: int, customer_first_name: str,
               customer_last_name: str, customer_email: str, customer_phone_no: str, customer_street_name: str,
               customer_street_no: int, customer_city: str, customer_state: str, customer_postal_code: str,
               customer_country: str, company_id: int) -> None:
        insertQuery = f'''INSERT INTO Customer (customer_user_name, customer_password, customer_id, 
                      customer_first_name, customer_last_name, customer_email, customer_phone_no, 
                      customer_street_name, customer_street_no, customer_city, customer_state, 
                      customer_postal_code, customer_country, company_id) VALUES ("{customer_user_name}", 
                      "{customer_password}", {customer_id}, "{customer_first_name}", "{customer_last_name}", 
                      "{customer_email}", "{customer_phone_no}", "{customer_street_name}", {customer_street_no}, 
                      "{customer_city}", "{customer_state}", "{customer_postal_code}", "{customer_country}", {company_id});'''
        return insertQuery
    
    @staticmethod
    def getBasicInfoAllCustomers(company_id):
        return f"SELECT customer_id, customer_user_name, customer_first_name, customer_last_name, customer_email, customer_phone_no FROM Customer WHERE company_id = {company_id};"
    
    @staticmethod
    def deleteCustomer(customer_id, company_id):
        return f"DELETE FROM Customer WHERE customer_id = {customer_id} AND company_id = {company_id};"
    
    @staticmethod
    def getAllInfoOfAllCustomersOfACompany(company_id):
        return f"SELECT customer_id, customer_user_name, customer_first_name, customer_last_name, customer_email, customer_phone_no, customer_street_name, customer_street_no, customer_city, customer_state, customer_postal_code, customer_country FROM Customer WHERE company_id = {company_id};"
    
    @staticmethod
    def getCustomerInfoForBilling(company_id, customer_id):
        return f"SELECT customer_first_name, customer_last_name FROM Customer WHERE customer_id = {customer_id} AND company_id = {company_id};"

    @staticmethod
    def updateAllFieldsOfACustomer(company_id, customer_id, customer_user_name, customer_first_name, customer_last_name, customer_email, customer_phone_no, customer_street_name, customer_street_no, customer_city, customer_state, customer_postal_code, customer_country):
        return f"""
            UPDATE Customer 
            SET customer_user_name = '{customer_user_name}', 
                customer_first_name = '{customer_first_name}', 
                customer_last_name = '{customer_last_name}', 
                customer_email = '{customer_email}', 
                customer_phone_no = '{customer_phone_no}', 
                customer_street_name = '{customer_street_name}', 
                customer_street_no = '{customer_street_no}', 
                customer_city = '{customer_city}', 
                customer_state = '{customer_state}', 
                customer_postal_code = '{customer_postal_code}', 
                customer_country = '{customer_country}' 
            WHERE customer_id = {customer_id} 
            AND company_id = {company_id}
        """
    
    @staticmethod
    def getMaxCustomerIDOfACompany(company_id):
        return f"SELECT MAX(customer_id) FROM Customer WHERE company_id = {company_id};"
    
    @staticmethod
    def getCustomerPasswordOfACompany(company_id, username):
        return f"SELECT customer_password FROM customer WHERE company_id = {company_id} AND customer_user_name =  '{username}';"
    
    @staticmethod
    def getCustomerIDOfACompany(company_id, username):
        return f"SELECT customer_id FROM customer WHERE company_id = {company_id} AND customer_user_name =  '{username}';"