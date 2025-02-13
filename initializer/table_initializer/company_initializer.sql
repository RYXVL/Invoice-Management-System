CREATE TABLE IF NOT EXISTS Company (
    company_id INT AUTO_INCREMENT,
    company_name VARCHAR(64) UNIQUE NOT NULL,
    company_street_name VARCHAR(128),
    company_street_no INT,
    company_city VARCHAR(32),
    company_state VARCHAR(16) NOT NULL,
    company_postal_code CHAR(5) NOT NULL,
    company_country VARCHAR(16) NOT NULL,
    company_email VARCHAR(64) UNIQUE NOT NULL,
    company_phone_no CHAR(10) UNIQUE NOT NULL,
    PRIMARY KEY (company_id)
);
