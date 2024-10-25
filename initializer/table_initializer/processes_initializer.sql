CREATE TABLE IF NOT EXISTS Processes (
    company_id INT,
    customer_id INT,
    employee_id INT,
    invoice_id INT,
    PRIMARY KEY (company_id, customer_id, employee_id, invoice_id),
    FOREIGN KEY (company_id, customer_id) REFERENCES Customer(company_id, customer_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (company_id, employee_id) REFERENCES Employee(company_id, employee_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (invoice_id) REFERENCES Invoice(invoice_id) ON UPDATE CASCADE ON DELETE CASCADE
);
