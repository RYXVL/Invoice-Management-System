class InvoiceLineItemsDML:

    @staticmethod
    def insertNewInvoiceLineItem(invoice_item_id, invoice_item_quantity, company_id, invoice_id, product_id):
        return f"INSERT INTO Invoice_line_items (invoice_item_id, invoice_item_quantity, company_id, invoice_id, product_id) VALUES ({invoice_item_id}, {invoice_item_quantity}, {company_id}, {invoice_id}, {product_id});"