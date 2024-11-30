class ProductDML:

    @staticmethod
    def getMaxProductIdOfCompany(selected_company_id):
        return f"SELECT MAX(product_id) FROM product WHERE company_id = {selected_company_id}"
    
    @staticmethod
    def insertNewProduct(newProductID, product_price, quantity, selected_company_id, item_name, brand_id):
        return f"""
            INSERT INTO Product (product_id, product_price, product_quantity, company_id, item_name, brand_id)
            VALUES ({newProductID}, {product_price}, {quantity}, {selected_company_id}, "{item_name}", {brand_id});
            """
    
    @staticmethod
    def getBasicInfoAllProducts(company_id):
        return f"SELECT p.product_id, p.product_price, p.product_quantity, p.item_name, b.brand_name FROM product AS p NATURAL JOIN brand AS b WHERE p.company_id = {company_id};"

    @staticmethod
    def deleteProduct(product_id, company_id):
        return f"DELETE FROM Product WHERE product_id = {product_id} AND company_id = {company_id}"
    
    @staticmethod
    def getQuantityOfAProductOfACompany(company_id, product_id):
        return f"SELECT product_quantity FROM Product WHERE product_id = {product_id} AND company_id = {company_id};"

    @staticmethod
    def updateProductQuantityOfACompany(company_id, product_id, new_quantity):
        return f"UPDATE product SET product_quantity = {new_quantity} WHERE product_id = {product_id} AND company_id = {company_id};"
    
    @staticmethod
    def getProductIDOfACompanyProduct(company_id, item_name):
        return f"SELECT product_id FROM product WHERE item_name = '{item_name}' AND company_id = {company_id};"