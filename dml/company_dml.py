class CompanyDML:
        
    @staticmethod
    def getBasicInfoAllCompanies():
        return f"SELECT company_id, company_name FROM Company;"
    
    @staticmethod
    def getAllInfoOfACompany(company_id):
        return f"SELECT company_id, company_name, company_street_name, company_street_no, company_city, company_state, company_postal_code, company_country, company_email, company_phone_no FROM Company WHERE company_id = {company_id};"
    
    @staticmethod
    def getCompanyInfoForBilling(company_id):
        return f"SELECT company_name, company_street_name, company_city, company_phone_no FROM company WHERE company_id = {company_id};"
    
    @staticmethod
    def updateAllFieldsOfACompany(company_id, company_name, company_street_name, company_street_no, company_city, company_state, company_postal_code, company_country, company_email, company_phone_no):
        return f"""
            UPDATE Company 
            SET company_name = '{company_name}', 
                company_street_name = '{company_street_name}', 
                company_street_no = '{company_street_no}', 
                company_city = '{company_city}', 
                company_state = '{company_state}', 
                company_postal_code = '{company_postal_code}', 
                company_country = '{company_country}', 
                company_email = '{company_email}', 
                company_phone_no = '{company_phone_no}'
            WHERE company_id = {company_id}
        """