# import tkinter as tk

# class DeleteCustomer:

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Delete Customer")

#         # Frame for input
#         self.input_frame = tk.Frame(self.root)
#         self.input_frame.pack(padx=10, pady=10)

#         # Label and Entry for customer_id
#         tk.Label(self.input_frame, text="Customer ID", font=("times new roman", 12)).grid(row=0, column=0, sticky="w", pady=5)
#         self.customer_id_entry = tk.Entry(self.input_frame, font=("times new roman", 12))
#         self.customer_id_entry.grid(row=0, column=1, pady=5, padx=5)

#         # Delete button
#         self.delete_button = tk.Button(self.root, text="Delete", font=("times new roman", 14), command=self.delete_customer)
#         self.delete_button.pack(pady=10)

#     # Dummy function to print entered customer_id
#     def delete_customer(self):
#         customer_id = self.customer_id_entry.get()
#         print("Customer ID to delete:", customer_id)

# if __name__ == '__main__':
#     root = tk.Tk()
#     app = DeleteCustomer(root)
#     root.geometry("300x150")
#     root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import ttk, Toplevel, Label, Button

class DeleteCustomer:

    def __init__(self, root, cursor, go_back_func, selected_company_id):
        self.root = Toplevel(root)
        self.prev_screen = root
        self.cursor = cursor
        self.selected_company_id = selected_company_id
        print(self.selected_company_id)
        self.go_back_func = go_back_func
        self.root.title("Delete Customer")

        # Example UI for deleting a customer
        Label(self.root, text="Customer ID").pack(pady=5)
        self.customer_id_entry = tk.Entry(self.root)
        self.customer_id_entry.pack(pady=5)

        Button(self.root, text="Delete Customer", font=("times new roman", 14), command=self.delete_customer).pack(pady=10)
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def delete_customer(self):
        customer_id = self.customer_id_entry.get()
        self.cursor.execute("DELETE FROM Customer WHERE customer_id = ?", (customer_id,))
        self.cursor.connection.commit()

    def go_back(self):
        self.root.destroy()
        self.prev_screen.deiconify()