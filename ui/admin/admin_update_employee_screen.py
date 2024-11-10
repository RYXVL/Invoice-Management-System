import tkinter as tk
from tkinter import Toplevel, Label, Button

class UpdateEmployee:

    def __init__(self, root, cursor, go_back_func, selected_company_id):
        self.root = Toplevel(root)
        self.cursor = cursor
        self.prev_screen = root
        self.selected_company_id = selected_company_id
        print(self.selected_company_id)
        self.go_back_func = go_back_func
        self.root.title("Update Employee Details")

        # Frame for input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Labels and Entries for employee details
        labels = [
            "Username", "Password", "Employee ID", "First Name",
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
        Button(self.root, text="Update", font=("times new roman", 14), command=self.update_employee).pack(pady=10)
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def update_employee(self):
        details = {label: entry.get() for label, entry in self.entries.items()}
        print("Employee Details to Update:")
        for key, value in details.items():
            print(f"{key}: {value}")

        # Update the employee details in the database
        self.cursor.execute(
            "UPDATE Employee SET employee_name = ?, email = ?, phone_no = ?, street_name = ?, street_no = ?, city = ?, state = ?, postal_code = ?, country = ? WHERE employee_id = ?",
            (
                details["First Name"] + " " + details["Last Name"], details["Email"], details["Phone No"],
                details["Street Name"], details["Street No"], details["City"], details["State"],
                details["Postal Code"], details["Country"], details["Employee ID"]
            )
        )
        self.cursor.connection.commit()

    def go_back(self):
        self.root.destroy()
        self.prev_screen.deiconify()