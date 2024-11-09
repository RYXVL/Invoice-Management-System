CREATE TABLE IF NOT EXISTS Product_Catalog (
    item_name VARCHAR(64),
    item_description VARCHAR(256) NOT NULL,
    brand_id INT,
    PRIMARY KEY (brand_id, item_name),
    UNIQUE (item_name, brand_id),
    FOREIGN KEY (brand_id) REFERENCES Brand(brand_id) ON UPDATE CASCADE ON DELETE CASCADE
);
