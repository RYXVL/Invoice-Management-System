CREATE TABLE IF NOT EXISTS Processes (
    company_id INT,
    customer_id INT,
    employee_id INT,
    invoice_id INT,
    PRIMARY KEY (company_id, customer_id, employee_id, invoice_id),
    FOREIGN KEY (company_id) REFERENCES Company(company_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id),
    FOREIGN KEY (invoice_id) REFERENCES Invoice(invoice_id)
);
