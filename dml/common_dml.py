class CommonDML:
    
    @staticmethod
    def getInvoiceItems(invoice_id):
        return f"select invoice_item_id, item_name, product_price, invoice_item_quantity, product_price * invoice_item_quantity as price from invoice natural join invoice_line_items natural join product where invoice_id = {invoice_id};"
    
    @staticmethod
    def getProductsOfACompany(company_id):
        return f"SELECT p.product_id, p.item_name, b.brand_name, p.product_price, p.product_quantity FROM product AS p NATURAL JOIN brand AS b WHERE p.company_id = {company_id} and p.product_quantity != 0;"