CREATE TABLE IF NOT EXISTS Product (
    product_id INT,
    product_price DECIMAL(10, 2) NOT NULL,
    product_quantity INT NOT NULL,
    company_id INT,
    item_name VARCHAR(64),
    brand_id INT,
    PRIMARY KEY (company_id, product_id),
    UNIQUE (company_id, item_name, brand_id),
    FOREIGN KEY (company_id) REFERENCES Company(company_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (item_name, brand_id) REFERENCES Product_Catalog(item_name, brand_id) ON UPDATE CASCADE ON DELETE CASCADE
);
