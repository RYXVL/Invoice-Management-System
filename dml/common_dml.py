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
