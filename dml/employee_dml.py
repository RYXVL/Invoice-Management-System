class EmployeeDML:

    @staticmethod
    def getMaxEmployeeIdOfCompany(selected_company_id):
        return f"SELECT MAX(employee_id) FROM employee WHERE company_id = {selected_company_id};"
    
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