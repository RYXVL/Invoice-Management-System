class ProcessDML:

    @staticmethod
    def getCustomerIdOfAnInvoice(invoice_id):
        return f"select customer_id from processes where invoice_id = {invoice_id};"
    
    @staticmethod
    def insertNewProcess(company_id, customer_id, employee_id, invoice_id):
        return f"INSERT INTO Processes (company_id, customer_id, employee_id, invoice_id) VALUES ({company_id}, {customer_id}, {employee_id}, {invoice_id});"