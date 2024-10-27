class CompanyDML:

    @staticmethod
    def insert(company_name: str, company_street_name: str, company_street_no: int,
               company_city: str, company_state: str, company_postal_code: str,
               company_country: str, company_email: str, company_phone_no: str) -> None:
        insertQuery = f'INSERT INTO Company (company_name, company_street_name, company_street_no,
                        company_city, company_state, company_postal_code, company_country,
                        company_email, company_phone_no) VALUES ("{company_name}", 
                        "{company_street_name}", {company_street_no}, "{company_city}", 
                        "{company_state}", "{company_postal_code}", "{company_country}", 
                        "{company_email}", "{company_phone_no}");'