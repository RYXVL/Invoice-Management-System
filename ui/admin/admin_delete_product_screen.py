# import tkinter as tk
import tkinter as tk
from tkinter import ttk
from tkinter import ttk, Toplevel, Label, Button

# class DeleteProduct:

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Delete Product")

#         # Frame for input
#         self.input_frame = tk.Frame(self.root)
#         self.input_frame.pack(padx=10, pady=10)

#         # Label and Entry for product_id
#         tk.Label(self.input_frame, text="Product ID", font=("times new roman", 12)).grid(row=0, column=0, sticky="w", pady=5)
#         self.product_id_entry = tk.Entry(self.input_frame, font=("times new roman", 12))
#         self.product_id_entry.grid(row=0, column=1, pady=5, padx=5)

#         # Delete button
#         self.delete_button = tk.Button(self.root, text="Delete", font=("times new roman", 14), command=self.delete_product)
#         self.delete_button.pack(pady=10)

#     # Dummy function to print entered product_id
#     def delete_product(self):
#         product_id = self.product_id_entry.get()
#         print("Product ID to delete:", product_id)

# if __name__ == '__main__':
#     root = tk.Tk()
#     app = DeleteProduct(root)
#     root.geometry("300x150")
#     root.mainloop()

class DeleteProduct:

    def __init__(self, root, cursor, go_back_func):
        self.prev_screen = root
        self.root = Toplevel(root)
        self.cursor = cursor
        self.go_back_func = go_back_func
        self.root.title("Delete Product")

        # Example UI for deleting a product (input fields, buttons, etc.)
        Label(self.root, text="Product ID").pack(pady=5)
        self.product_id_entry = tk.Entry(self.root)
        self.product_id_entry.pack(pady=5)

        Button(self.root, text="Delete Product", font=("times new roman", 14), command=self.delete_product).pack(pady=10)
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def delete_product(self):
        product_id = self.product_id_entry.get()
        self.cursor.execute("DELETE FROM Product WHERE product_id = ?", (product_id,))
        self.cursor.connection.commit()

    def go_back(self):
        self.root.destroy()
        self.prev_screen.deiconify()