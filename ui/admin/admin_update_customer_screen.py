import tkinter as tk
from tkinter import Toplevel, Label, Button

class UpdateCustomer:

    def __init__(self, root, cursor, go_back_func, selected_company_id):
        self.root = Toplevel(root)
        self.cursor = cursor
        self.prev_screen = root
        self.selected_company_id = selected_company_id
        print(self.selected_company_id)
        self.go_back_func = go_back_func
        self.root.title("Update Customer Details")

        # Frame for input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Labels and Entries for customer details
        labels = [
            "Username", "Password", "Customer ID", "First Name",
            "Last Name", "Email", "Phone No", "Street Name",
            "Street No", "City", "State", "Postal Code", "Country"
        ]

        self.entries = {}
        for i, label in enumerate(labels):
            Label(self.input_frame, text=label, font=("times new roman", 12)).grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(self.input_frame, font=("times new roman", 12))
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[label] = entry

        # Update button
        Button(self.root, text="Update", font=("times new roman", 14), command=self.update_customer).pack(pady=10)
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def update_customer(self):
        details = {label: entry.get() for label, entry in self.entries.items()}
        print("Customer Details to Update:")
        for key, value in details.items():
            print(f"{key}: {value}")

        # Update the customer details in the database
        self.cursor.execute(
            "UPDATE Customer SET customer_name = ?, email = ?, phone_no = ?, street_name = ?, street_no = ?, city = ?, state = ?, postal_code = ?, country = ? WHERE customer_id = ?",
            (
                details["First Name"] + " " + details["Last Name"], details["Email"], details["Phone No"],
                details["Street Name"], details["Street No"], details["City"], details["State"],
                details["Postal Code"], details["Country"], details["Customer ID"]
            )
        )
        self.cursor.connection.commit()

    def go_back(self):
        self.root.destroy()
        self.prev_screen.deiconify()