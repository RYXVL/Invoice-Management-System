CREATE TABLE IF NOT EXISTS Brand (
    brand_id INT AUTO_INCREMENT,
    brand_name VARCHAR(64) UNIQUE NOT NULL,
    PRIMARY KEY (brand_id)
);
