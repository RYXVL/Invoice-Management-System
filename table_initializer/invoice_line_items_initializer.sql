CREATE TABLE IF NOT EXISTS Invoice_Line_Items (
    invoice_item_id INT,
    invoice_item_quantity INT NOT NULL,
    invoice_id INT,
    product_id INT NOT NULL,
    PRIMARY KEY (invoice_id, invoice_item_id),
    FOREIGN KEY (invoice_id) REFERENCES Invoice(invoice_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);
