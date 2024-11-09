CREATE TABLE IF NOT EXISTS Customer (
    customer_user_name VARCHAR(16) NOT NULL,
    customer_password VARCHAR(32) NOT NULL,
    customer_id INT,
    customer_first_name VARCHAR(32) NOT NULL,
    customer_last_name VARCHAR(32),
    customer_email VARCHAR(64) UNIQUE NOT NULL,
    customer_phone_no CHAR(10) UNIQUE NOT NULL,
    customer_street_name VARCHAR(128),
    customer_street_no INT,
    customer_city VARCHAR(32),
    customer_state VARCHAR(16) NOT NULL,
    customer_postal_code CHAR(5) NOT NULL,
    customer_country VARCHAR(16) NOT NULL,
    company_id INT,
    PRIMARY KEY (company_id, customer_id),
    UNIQUE (company_id, customer_user_name),
    FOREIGN KEY (company_id) REFERENCES Company(company_id) ON UPDATE CASCADE ON DELETE CASCADE
);
