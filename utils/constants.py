import os
database_initialize_order = [os.path.join("database_initializer", "ims_initializer.sql")]


table_initialize_order = [
    os.path.join("table_initializer", "company_initializer.sql"),
    os.path.join("table_initializer", "customer_initializer.sql"),
    os.path.join("table_initializer", "employee_initializer.sql"),
    os.path.join("table_initializer", "brand_initializer.sql"),
    os.path.join("table_initializer", "product_catalog_initializer.sql"),
    os.path.join("table_initializer", "invoice_initializer.sql"),
    os.path.join("table_initializer", "product_initializer.sql"),
    os.path.join("table_initializer", "invoice_line_items_initializer.sql"),
    os.path.join("table_initializer", "processes_initializer.sql"),
]
