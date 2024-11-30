class CommonDML:

    @staticmethod
    def fetchNotSoldProductsByACompany(company_id: str) -> str:
        selectQuery = (
            f"SELECT pc.*, b.brand_name "
            f"FROM product_catalog pc "
            f"LEFT JOIN product p "
            f"ON pc.item_name = p.item_name AND pc.brand_id = p.brand_id AND p.company_id = {company_id} "
            f"JOIN brand b "
            f"ON pc.brand_id = b.brand_id "
            f"WHERE p.company_id IS NULL;"
        )
        return selectQuery
    
    @staticmethod
    def getInvoiceItems(invoice_id):
        return f"select invoice_item_id, item_name, product_price, invoice_item_quantity, product_price * invoice_item_quantity as price from invoice natural join invoice_line_items natural join product where invoice_id = {invoice_id};"
    
    @staticmethod
    def getProductsOfACompany(company_id):
        return f"SELECT p.product_id, p.item_name, b.brand_name, p.product_price, p.product_quantity FROM product AS p NATURAL JOIN brand AS b WHERE p.company_id = {company_id} and p.product_quantity != 0;"
    
    @staticmethod
    def getInvoicesOfACustomerOfACompany(company_id, customer_id):
        return f"""
            SELECT DISTINCT invoice.invoice_id, invoice_date 
            FROM invoice 
            JOIN processes 
            ON invoice.invoice_id = processes.invoice_id 
            WHERE customer_id = {customer_id} and company_id = {company_id};
        """