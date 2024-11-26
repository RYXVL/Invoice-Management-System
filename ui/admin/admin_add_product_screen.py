import tkinter as tk
from tkinter import ttk, Toplevel, Button
from dml.common_dml import CommonDML

class AddProduct:

    def __init__(self, root, cursor, go_back_func, selected_company_id, connection):
        self.root = Toplevel(root)
        self.cursor = cursor
        self.connection = connection
        self.selected_company_id = selected_company_id
        print(self.selected_company_id)
        self.prev_screen = root
        self.go_back_func = go_back_func
        self.root.title("Add Product")

        # Frame for entry and label
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=5)

        # Entry for Item Name
        tk.Label(self.input_frame, text="Item Name:", font=("times new roman", 14)).grid(row=0, column=0, padx=5)
        self.item_name_entry = tk.Entry(self.input_frame, font=("times new roman", 14))
        self.item_name_entry.grid(row=0, column=1, padx=5)

        # Entry for Brand ID
        tk.Label(self.input_frame, text="Brand ID:", font=("times new roman", 14)).grid(row=0, column=2, padx=5)
        self.brand_id_entry = tk.Entry(self.input_frame, font=("times new roman", 14))
        self.brand_id_entry.grid(row=0, column=3, padx=5)

        # Entry for Product Price
        tk.Label(self.input_frame, text="Price:", font=("times new roman", 14)).grid(row=1, column=0, padx=5)
        self.product_price_entry = tk.Entry(self.input_frame, font=("times new roman", 14))
        self.product_price_entry.grid(row=1, column=1, padx=5)

        # Entry for Quantity
        tk.Label(self.input_frame, text="Quantity:", font=("times new roman", 14)).grid(row=1, column=2, padx=5)
        self.quantity_entry = tk.Entry(self.input_frame, font=("times new roman", 14))
        self.quantity_entry.grid(row=1, column=3, padx=5)

        # Define the Treeview widget
        self.tree = ttk.Treeview(self.root, show="headings")

        # Define columns for the table (based on the data structure)
        self.tree["columns"] = ("Item Name", "Item Description", "Brand ID", "Brand Name")

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
        self.root.geometry(f"{table_width}x{table_height + 120}")

        # "Add" button below the table
        self.add_button = tk.Button(self.root, text="Add Product", font=("times new roman", 14), command=self.add_item)
        self.add_button.pack(pady=10)

        # "Back" button
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def load_data(self):
        # Query the database to load the current products into the treeview
        selectQuery = CommonDML().fetchNotSoldProductsByACompany(self.selected_company_id)
        self.cursor.execute(selectQuery)
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)

    def add_item(self):
        # Get values from the entry fields
        item_name = self.item_name_entry.get()
        brand_id = self.brand_id_entry.get()
        product_price = self.product_price_entry.get()
        quantity = self.quantity_entry.get()

        # Validate inputs (optional)
        if not item_name or not brand_id or not product_price or not quantity:
            tk.messagebox.showerror("Error", "All fields must be filled!")
            return

        # Insert new product into the database
        try:
            self.cursor.execute(f"SELECT MAX(product_id) FROM product WHERE company_id = {self.selected_company_id}")
            max_id_result = self.cursor.fetchone()[0]
            newProductID = (max_id_result + 1) if max_id_result else 1

            self.cursor.execute(f"""
                INSERT INTO Product (product_id, product_price, product_quantity, company_id, item_name, brand_id)
                VALUES ({newProductID}, {product_price}, {quantity}, {self.selected_company_id}, "{item_name}", {brand_id});
            """)
            self.connection.commit()

            # Refresh the table after successful insertion
            self.refresh_table()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to add product: {e}")

        # Clear the entry fields
        self.item_name_entry.delete(0, tk.END)
        self.brand_id_entry.delete(0, tk.END)
        self.product_price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def go_back(self):
        self.root.destroy()
        self.prev_screen.deiconify()

    def refresh_table(self):
        # Clear the current contents of the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Re-fetch data and update the Treeview
        self.load_data()



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