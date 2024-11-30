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