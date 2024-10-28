import tkinter as tk

class DeleteCustomer:

    def __init__(self, root):
        self.root = root
        self.root.title("Delete Customer")

        # Frame for input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Label and Entry for customer_id
        tk.Label(self.input_frame, text="Customer ID", font=("times new roman", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.customer_id_entry = tk.Entry(self.input_frame, font=("times new roman", 12))
        self.customer_id_entry.grid(row=0, column=1, pady=5, padx=5)

        # Delete button
        self.delete_button = tk.Button(self.root, text="Delete", font=("times new roman", 14), command=self.delete_customer)
        self.delete_button.pack(pady=10)

    # Dummy function to print entered customer_id
    def delete_customer(self):
        customer_id = self.customer_id_entry.get()
        print("Customer ID to delete:", customer_id)

if __name__ == '__main__':
    root = tk.Tk()
    app = DeleteCustomer(root)
    root.geometry("300x150")
    root.mainloop()
