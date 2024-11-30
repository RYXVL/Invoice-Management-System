class InvoiceDML:

    @staticmethod
    def getMaxInvoiceID():
        return f"SELECT MAX(invoice_id) FROM Invoice;"

    @staticmethod
    def insertNewInvoice(todays_date, invoice_total):
        return f"INSERT INTO Invoice (invoice_date, invoice_total_amount) VALUES (\"{todays_date}\", {invoice_total});"