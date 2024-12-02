class ProcessDML:

    @staticmethod
    def getCustomerIdOfAnInvoice(invoice_id):
        return f"select customer_id from processes where invoice_id = {invoice_id};"