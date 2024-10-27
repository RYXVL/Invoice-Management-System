CREATE TABLE IF NOT EXISTS Product_Catalog (
    item_id INT AUTO_INCREMENT,
    item_name VARCHAR(64),
    item_description VARCHAR(256) NOT NULL,
    PRIMARY KEY (item_id, item_name)
);
