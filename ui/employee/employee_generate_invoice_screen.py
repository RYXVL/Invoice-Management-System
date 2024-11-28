import tkinter as tk
from tkinter import Toplevel, Label, Button, ttk, Entry


class GenerateInvoice:
    def __init__(self, employee_menu, cursor, selected_company_id, connection):
        self.employee_menu = employee_menu
        self.window = Toplevel()
        self.cursor = cursor
        self.connection = connection
        self.selected_company_id = selected_company_id
        print(f"GenerateInvoice: {self.selected_company_id}")
        self.window.title("Generate Invoice")
        self.window.geometry("600x500")
        
        Label(self.window, text="Generate Invoice", font=("times new roman", 24, "bold"), fg="black").pack(pady=10)

        # Frame for input fields and Add button
        self.input_frame = tk.Frame(self.window)
        self.input_frame.pack(pady=10)

        # Product ID field
        Label(self.input_frame, text="Product ID:", font=("times new roman", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.product_id_entry = Entry(self.input_frame, font=("times new roman", 12), state="readonly")
        self.product_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Quantity field
        Label(self.input_frame, text="Quantity:", font=("times new roman", 12)).grid(row=0, column=2, padx=5, pady=5)
        self.quantity_entry = Entry(self.input_frame, font=("times new roman", 12))
        self.quantity_entry.grid(row=0, column=3, padx=5, pady=5)

        # Add button
        self.add_button = Button(self.input_frame, text="Add", font=("times new roman", 12), command=self.add_item)
        self.add_button.grid(row=0, column=4, padx=10, pady=5)

        # Frame for the table
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

        # Bind the row selection event
        self.treeview.bind("<ButtonRelease-1>", self.on_row_select)

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

    def on_row_select(self, event):
        # Get the selected row
        selected_item = self.treeview.selection()
        if selected_item:
            selected_data = self.treeview.item(selected_item[0], "values")
            # Populate the Product ID field
            self.product_id_entry.config(state="normal")
            self.product_id_entry.delete(0, tk.END)
            self.product_id_entry.insert(0, selected_data[0])  # Product ID
            self.product_id_entry.config(state="readonly")

    def add_item(self):
        # Get the entered data
        product_id = self.product_id_entry.get()
        quantity_text = self.quantity_entry.get()

        if not product_id or not quantity_text:
            print("Error: Both fields must be filled.")
            return

        try:
            quantity = int(quantity_text)
        except ValueError:
            print("Error: Quantity must be a number.")
            return

        # Get the remaining quantity of the selected product
        selected_item = self.treeview.selection()
        if not selected_item:
            print("Error: No row selected.")
            return

        selected_data = self.treeview.item(selected_item[0], "values")
        remaining_quantity = int(selected_data[4])  # Quantity Remaining

        if quantity > remaining_quantity:
            print("Error: Entered quantity exceeds remaining quantity.")
        else:
            print(f"Product ID: {product_id}, Quantity: {quantity}")
            # Clear the fields
            self.product_id_entry.config(state="normal")
            self.product_id_entry.delete(0, tk.END)
            self.product_id_entry.config(state="readonly")
            self.quantity_entry.delete(0, tk.END)

    def go_back(self):
        self.window.destroy()  # Close the Generate Invoice window
        self.employee_menu.window.deiconify()  # Show the Employee Menu again
