CREATE TABLE IF NOT EXISTS Product (
    product_id INT,
    product_price DECIMAL(10, 2) NOT NULL,
    product_quantity INT NOT NULL,
    company_id INT,
    item_id INT NOT NULL,
    PRIMARY KEY (company_id, product_id),
    UNIQUE (company_id, item_id),
    FOREIGN KEY (company_id) REFERENCES Company(company_id),
    FOREIGN KEY (item_id) REFERENCES Product_Catalog(item_id)
);
