CREATE TABLE IF NOT EXISTS Invoice (
    invoice_id INT AUTO_INCREMENT,
    invoice_date DATE NOT NULL,
    invoice_total_amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (invoice_id)
);
