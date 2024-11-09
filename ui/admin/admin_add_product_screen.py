import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk, Toplevel, Label, Button

class AddProduct:

    def __init__(self, root, cursor, go_back_func):
        self.root = Toplevel(root)
        self.cursor = cursor
        self.go_back_func = go_back_func
        self.root.title("Add Product")

        # Frame for entry and label
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=5)

        # Entry for Product Name
        tk.Label(self.input_frame, text="Enter Product Name:", font=("times new roman", 14)).grid(row=0, column=0, padx=5)
        self.product_name_entry = tk.Entry(self.input_frame, font=("times new roman", 14))
        self.product_name_entry.grid(row=0, column=1, padx=5)

        # Entry for Product Price
        tk.Label(self.input_frame, text="Enter Product Price:", font=("times new roman", 14)).grid(row=1, column=0, padx=5)
        self.product_price_entry = tk.Entry(self.input_frame, font=("times new roman", 14))
        self.product_price_entry.grid(row=1, column=1, padx=5)

        # Define the Treeview widget
        self.tree = ttk.Treeview(self.root, show="headings")

        # Define columns for the table (based on the data structure)
        self.tree["columns"] = ("Product ID", "Product Name", "Product Price")

        # Set column headings and column width
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        # Insert data into the table (if there's existing data, can be fetched from database)
        self.load_data()

        # Calculate the required width and height
        num_rows = len(self.tree.get_children())
        row_height = 20  # Approximate row height in pixels
        column_width = 100  # Same width as specified in column setup

        table_width = len(self.tree["columns"]) * column_width
        table_height = min(num_rows * row_height + 30, 300)  # Set a max height

        # Adjust the window size to fit the table
        self.tree.pack(expand=True, fill="both")
        self.root.geometry(f"{table_width}x{table_height + 80}")

        # "Add" button below the table
        self.add_button = tk.Button(self.root, text="Add Product", font=("times new roman", 14), command=self.add_item)
        self.add_button.pack(pady=10)

        # "Back" button
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def load_data(self):
        # Query the database to load the current products into the treeview
        self.cursor.execute("SELECT item_name, item_description, brand_id FROM Product_Catalog")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)

    def add_item(self):
        # Get values from the entry fields
        product_name = self.product_name_entry.get()
        product_price = self.product_price_entry.get()

        # Insert new product into the database
        self.cursor.execute("INSERT INTO Product (product_name, product_price) VALUES (?, ?)", 
                            (product_name, product_price))
        self.cursor.connection.commit()

        # Add the new product to the treeview
        self.tree.insert("", "end", values=("New ID", product_name, product_price))  # Replace with actual ID if needed

        # Optionally, clear the entry fields after adding
        self.product_name_entry.delete(0, tk.END)
        self.product_price_entry.delete(0, tk.END)

    def go_back(self):
        self.root.destroy()
        self.go_back_func()


# Sample data
data = [
    {"ID": 1, "Name": "Alice", "Age": 24},
    {"ID": 2, "Name": "Bob", "Age": 30},
    {"ID": 3, "Name": "Charlie", "Age": 22},
]

# if __name__  == '__main__':

#     root = tk.Tk()
#     app = AddProduct(root, data)
#     root.geometry("400x300")
#     root.mainloop()