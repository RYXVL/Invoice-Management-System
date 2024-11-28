import tkinter as tk
from tkinter import Toplevel, Label, Button, ttk


class GenerateInvoice:
    def __init__(self, employee_menu, cursor, selected_company_id, connection):
        self.employee_menu = employee_menu  # Store the reference to the EmployeeMenu instance
        self.window = Toplevel()
        self.cursor = cursor
        self.connection = connection
        self.selected_company_id = selected_company_id
        print(f"GenerateInvoice: {self.selected_company_id}")
        self.window.title("Generate Invoice")
        self.window.geometry("600x400")
        
        Label(self.window, text="Generate Invoice", font=("times new roman", 24, "bold"), fg="black").pack(pady=10)
        
        # Create a frame for the table
        self.table_frame = tk.Frame(self.window)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create the table (Treeview)
        self.treeview = ttk.Treeview(
            self.table_frame,
            columns=("product_id", "item_name", "brand_name", "product_price", "product_quantity"),
            show="headings",
        )
        self.treeview.pack(fill="both", expand=True)

        # Set up the table headers
        headers = {
            "product_id": "Product ID",
            "item_name": "Item Name",
            "brand_name": "Brand Name",
            "product_price": "Product Price",
            "product_quantity": "Quantity Remaining",
        }
        for col, text in headers.items():
            self.treeview.heading(col, text=text)
            self.treeview.column(col, width=120, anchor="center")

        # Load data into the table
        self.load_products()

        # Add Back button
        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def load_products(self):
        # Clear any existing data in the table
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Fetch data from the database
        query = f"SELECT p.product_id, p.item_name, b.brand_name, p.product_price, p.product_quantity FROM product AS p natural join brand AS b WHERE p.company_id = {self.selected_company_id};"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        # Populate the table with fetched data
        for row in rows:
            self.treeview.insert("", "end", values=row)

    def go_back(self):
        self.window.destroy()  # Close the Generate Invoice window
        self.employee_menu.window.deiconify()  # Show the Employee Menu again
