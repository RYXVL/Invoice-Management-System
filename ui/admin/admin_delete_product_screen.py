import tkinter as tk

class DeleteProduct:

    def __init__(self, root):
        self.root = root
        self.root.title("Delete Product")

        # Frame for input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Label and Entry for product_id
        tk.Label(self.input_frame, text="Product ID", font=("times new roman", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.product_id_entry = tk.Entry(self.input_frame, font=("times new roman", 12))
        self.product_id_entry.grid(row=0, column=1, pady=5, padx=5)

        # Delete button
        self.delete_button = tk.Button(self.root, text="Delete", font=("times new roman", 14), command=self.delete_product)
        self.delete_button.pack(pady=10)

    # Dummy function to print entered product_id
    def delete_product(self):
        product_id = self.product_id_entry.get()
        print("Product ID to delete:", product_id)

if __name__ == '__main__':
    root = tk.Tk()
    app = DeleteProduct(root)
    root.geometry("300x150")
    root.mainloop()
