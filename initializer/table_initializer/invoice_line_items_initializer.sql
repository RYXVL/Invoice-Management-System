CREATE TABLE IF NOT EXISTS Invoice_Line_Items (
    invoice_item_id INT,
    invoice_item_quantity INT NOT NULL,
    company_id INT,
    invoice_id INT,
    product_id INT NOT NULL,
    PRIMARY KEY (invoice_id, invoice_item_id),
    FOREIGN KEY (invoice_id) REFERENCES Invoice(invoice_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (company_id, product_id) REFERENCES Product(company_id, product_id) ON UPDATE CASCADE ON DELETE CASCADE
);
