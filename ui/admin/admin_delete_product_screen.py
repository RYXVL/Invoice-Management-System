import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label, Button

class DeleteProduct:

    def __init__(self, root, cursor, go_back_func, selected_company_id, connection):
        self.prev_screen = root
        self.root = Toplevel(root)
        self.cursor = cursor
        self.connection = connection
        self.selected_company_id = selected_company_id
        self.go_back_func = go_back_func
        self.root.title("Delete Product")

        # # Fetch the products for the selected company
        # self.fetch_products()

        # Frame for product ID and table
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Label and Entry for product_id (non-editable)
        tk.Label(self.input_frame, text="Product ID", font=("times new roman", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.product_id_entry = tk.Entry(self.input_frame, font=("times new roman", 12), state='readonly')  # Non-editable field
        self.product_id_entry.grid(row=0, column=1, pady=5, padx=5)

        # Table to display products
        self.tree = ttk.Treeview(self.root, columns=("product_id", "product_price", "product_quantity",  "item_name", "brand_name"), show="headings")
        self.tree.pack(pady=10, padx=10)
        self.tree.heading("product_id", text="Product ID")
        self.tree.heading("item_name", text="Item Name")
        self.tree.heading("product_price", text="Price")
        self.tree.heading("product_quantity", text="Quantity")
        self.tree.heading("brand_name", text="Brand Name")
        self.tree.bind("<ButtonRelease-1>", self.on_select)

        # Fetch the products for the selected company
        self.fetch_products()

        # Delete and Back buttons
        Button(self.root, text="Delete Product", font=("times new roman", 14), command=self.delete_product).pack(pady=10)
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def fetch_products(self):
        """Fetch products based on the selected company_id and populate the table."""
        self.cursor.execute(f"SELECT p.product_id, p.product_price, p.product_quantity, p.item_name, b.brand_name FROM product AS p natural join brand AS b where p.company_id = {self.selected_company_id};")
        products = self.cursor.fetchall()

        # Clear the table before populating new data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert rows into the table
        for product in products:
            self.tree.insert("", "end", values=product)

    def on_select(self, event):
        """When a row is selected, display the product ID in the Entry field."""
        selected_item = self.tree.focus()
        product_id = self.tree.item(selected_item)["values"][0]  # Get the product_id from the selected row
        self.product_id_entry.config(state='normal')  # Make it editable temporarily
        self.product_id_entry.delete(0, tk.END)  # Clear the entry
        self.product_id_entry.insert(0, product_id)  # Insert the selected product_id
        self.product_id_entry.config(state='readonly')  # Make it non-editable again

    def delete_product(self):
        """Delete the selected product from the database."""
        product_id = self.product_id_entry.get()
        if product_id:
            self.cursor.execute(f"DELETE FROM Product WHERE product_id = {product_id} AND company_id = {self.selected_company_id}")
            self.connection.commit()
            self.fetch_products()  # Refresh the product table
            self.product_id_entry.delete(0, tk.END)  # Clear the product ID entry

    def go_back(self):
        """Go back to the previous screen."""
        self.root.destroy()
        self.prev_screen.deiconify()

# if __name__ == "__main__":
#     root = tk.Tk()
#     # Assuming cursor and connection are already established
#     app = DeleteProduct(root, cursor=None, go_back_func=None, selected_company_id=1, connection=None)
#     root.geometry("600x400")
#     root.mainloop()
