class DataVisualizer:

    @staticmethod
    def getTopSellingProductsOfACompany(cursor, company_id, max_returned_records_count):
        query = f"""SELECT p.item_name AS product_name, p.product_price AS unit_price, 
                  SUM(ili.invoice_item_quantity) AS total_quantity_sold, 
                  SUM(ili.invoice_item_quantity * p.product_price) AS total_revenue
                  FROM Product p
                  JOIN Invoice_Line_Items ili 
                  ON p.company_id = ili.company_id AND p.product_id = ili.product_id
                  WHERE p.company_id = {company_id}
                  GROUP BY p.item_name, p.product_price
                  ORDER BY total_revenue DESC
                  LIMIT {max_returned_records_count};"""
        cursor.execute(query)
        return cursor.fetchall()
    
    @staticmethod
    def getLowStockProductsInformation(cursor, company_id, bottom_threshold):
        query = f"""SELECT p.item_name AS product_name, b.brand_name AS brand,
                    p.product_quantity AS current_stock, p.product_price AS unit_price
                    FROM Product p
                    JOIN Brand b 
                    ON p.brand_id = b.brand_id
                    WHERE p.product_quantity < {bottom_threshold} AND p.company_id = {company_id}
                    ORDER BY p.product_quantity ASC;"""
        cursor.execute(query)
        return cursor.fetchall()
    
    @staticmethod
    def getProductCatalogPerformanceAcrossCompanies(cursor):
        query = f"""SELECT 
    b.brand_name AS brand,
    p.item_name AS product_name,
    comp.company_name AS company,
    SUM(ili.invoice_item_quantity) AS total_units_sold,
    SUM(ili.invoice_item_quantity * p.product_price) AS total_revenue
FROM 
    Brand b
JOIN 
    Product_Catalog pc ON b.brand_id = pc.brand_id
JOIN 
    Product p ON pc.item_name = p.item_name AND pc.brand_id = p.brand_id
JOIN 
    Company comp ON p.company_id = comp.company_id
JOIN 
    Invoice_Line_Items ili ON p.company_id = ili.company_id AND p.product_id = ili.product_id
GROUP BY 
    b.brand_name, p.item_name, comp.company_name
ORDER BY 
    total_revenue DESC;"""
        
        @staticmethod
        def getBrandRevenueOfCompanies(cursor, company_id):
            query = f"""SELECT 
    comp.company_name AS company,
    b.brand_name AS brand,
    SUM(ili.invoice_item_quantity * p.product_price) AS brand_revenue
FROM 
    Company comp
JOIN 
    Product p ON comp.company_id = p.company_id
JOIN 
    Product_Catalog pc ON p.item_name = pc.item_name AND p.brand_id = pc.brand_id
JOIN 
    Brand b ON pc.brand_id = b.brand_id
JOIN 
    Invoice_Line_Items ili ON p.company_id = ili.company_id AND p.product_id = ili.product_id
WHERE p.company_id = 1
GROUP BY 
    comp.company_name, b.brand_name
ORDER BY 
    brand_revenue DESC;"""