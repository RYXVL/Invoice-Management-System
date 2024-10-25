CREATE TABLE IF NOT EXISTS Product_Catalog (
    item_id INT,
    item_name VARCHAR(64),
    item_description VARCHAR(256) NOT NULL,
    PRIMARY KEY (item_id, item_name)
);
