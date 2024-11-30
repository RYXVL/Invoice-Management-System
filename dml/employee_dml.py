class EmployeeDML:

    # @staticmethod
    # def getUsernameAndPasswordEmployee(company_id: int, username: str, password: str, is_admin: bool) -> str:
    #     selectQuery = f'SELECT customer_user_name, customer_password
    #                     FROM Customer
    #                     WHERE company_id = {company_id} AND customer_user_name = "{username}" AND is_admin = '
    #     if is_admin:
    #         selectQuery += 'TRUE;'
    #     else:
    #         selectQuery += 'FALSE;'

    @staticmethod
    def getMaxEmployeeIdOfCompany(selected_company_id):
        return f"SELECT MAX(employee_id) FROM employee WHERE company_id = {selected_company_id};"
    
    @staticmethod
    def insertNewEmployee(employee_username, employee_password, employee_id, 
                          employee_first_name, employee_last_name, 
                          employee_email, employee_phone_no, 
                          employee_hire_date, employee_street_name, 
                          employee_street_no, employee_city, employee_state, 
                          employee_postal_code, employee_country, company_id, 
                          is_admin):
        return f"""INSERT INTO Employee 
            (employee_user_name, employee_password, employee_id, 
            employee_first_name, employee_last_name, employee_email, 
            employee_phone_no, employee_hire_date, employee_street_name, 
            employee_street_no, employee_city, employee_state, 
            employee_postal_code, employee_country, company_id, is_admin) 
            VALUES (\"{employee_username}\", \"{employee_password}\", 
            {employee_id}, \"{employee_first_name}\", 
            \"{employee_last_name}\", \"{employee_email}\", 
            \"{employee_phone_no}\", \"{employee_hire_date}\", 
            \"{employee_street_name}\", {employee_street_no}, 
            \"{employee_city}\", \"{employee_state}\", 
            \"{employee_postal_code}\", \"{employee_country}\", 
            {company_id}, {is_admin});"""
    
    @staticmethod
    def getBasicInfoAllEmployees(company_id):
        return f"SELECT employee_id, employee_user_name, employee_first_name, employee_last_name, employee_email, employee_phone_no, employee_hire_date, is_admin FROM Employee WHERE company_id = {company_id};"
    
    @staticmethod
    def deleteEmployee(employee_id, company_id):
        return f"DELETE FROM Employee WHERE employee_id = {employee_id} AND company_id = {company_id};"
    
    @staticmethod
    def getAdminPassword(admin_username, company_id):
        return f"SELECT employee_password FROM employee WHERE company_id = {company_id} AND employee_user_name = '{admin_username}' AND is_admin = 1;"
    
    @staticmethod
    def getEmployeeIdAndPassword(company_id, username):
        return f"SELECT employee_password, employee_id FROM employee WHERE company_id = {company_id} AND employee_user_name =  '{username}' AND is_admin = 0;"
    
    @staticmethod
    def getAllInfoOfAllEmployeesOfACompany(company_id):
        return f"SELECT employee_id, employee_user_name, employee_password, employee_first_name, employee_last_name, employee_email, employee_phone_no, employee_hire_date, employee_street_name, employee_street_no, employee_city, employee_state, employee_postal_code, employee_country, is_admin FROM Employee WHERE company_id = {company_id};"
    
    @staticmethod
    def updateAllFieldsOfAnEmployee(company_id, employee_id, employee_user_name, employee_password, employee_first_name, employee_last_name, employee_email, employee_phone_no, employee_street_name, employee_street_no, employee_city, employee_state, employee_postal_code, employee_country, is_admin, employee_hire_date):
        return f"""
            UPDATE Employee 
            SET employee_user_name = '{employee_user_name}', 
                employee_password = '{employee_password}', 
                employee_first_name = '{employee_first_name}', 
                employee_last_name = '{employee_last_name}', 
                employee_email = '{employee_email}', 
                employee_phone_no = '{employee_phone_no}', 
                employee_street_name = '{employee_street_name}', 
                employee_street_no = '{employee_street_no}', 
                employee_city = '{employee_city}', 
                employee_state = '{employee_state}', 
                employee_postal_code = '{employee_postal_code}', 
                employee_country = '{employee_country}', 
                is_admin = {is_admin}, 
                employee_hire_date = '{employee_hire_date}'
            WHERE employee_id = '{employee_id}' 
            AND company_id = '{company_id}'
        """