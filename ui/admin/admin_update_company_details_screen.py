import tkinter as tk
from tkinter import Toplevel, Label, Button, messagebox

class UpdateCompany:

    def __init__(self, root, cursor, go_back_func, selected_company_id, connection):
        self.root = Toplevel(root)
        self.cursor = cursor
        self.connection = connection
        self.prev_screen = root
        self.selected_company_id = selected_company_id
        self.go_back_func = go_back_func
        self.root.title("Update Company Details")

        # Frame for input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Labels and Entries for company details
        labels = [
            "Company ID", "Name", "Street Name", "Street No",
            "City", "State", "Postal Code", "Country",
            "Email", "Phone No"
        ]

        self.entries = {}
        for i, label in enumerate(labels):
            Label(self.input_frame, text=label, font=("times new roman", 12)).grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(self.input_frame, font=("times new roman", 12))
            if label == "Company ID":  # Make Company ID uneditable
                entry.insert(0, self.selected_company_id)
                entry.config(state="disabled")
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[label] = entry

        # Pre-fill the fields with existing company data
        self.fetch_company_data()

        # Update button
        Button(self.root, text="Update", font=("times new roman", 14), command=self.update_company).pack(pady=10)
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def fetch_company_data(self):
        query = f"SELECT company_id, company_name, company_street_name, company_street_no, company_city, company_state, company_postal_code, company_country, company_email, company_phone_no FROM Company WHERE company_id = {self.selected_company_id};"
        self.cursor.execute(query)
        company_data = self.cursor.fetchone()

        if company_data:
            # Populate the entries with fetched data
            for i, key in enumerate(self.entries.keys()):
                self.entries[key].insert(0, company_data[i])
        else:
            messagebox.showerror("Error", "Company not found.")
            self.go_back()

    def update_company(self):
        """Collect data from entries and update the company in the database."""
        details = {label: entry.get() for label, entry in self.entries.items()}

        try:
            update_query = f"""
                UPDATE Company 
                SET company_name = '{details["Name"]}', 
                    company_street_name = '{details["Street Name"]}', 
                    company_street_no = '{details["Street No"]}', 
                    company_city = '{details["City"]}', 
                    company_state = '{details["State"]}', 
                    company_postal_code = '{details["Postal Code"]}', 
                    company_country = '{details["Country"]}', 
                    company_email = '{details["Email"]}', 
                    company_phone_no = '{details["Phone No"]}'
                WHERE company_id = {details["Company ID"]}
                """
            self.cursor.execute(update_query)
            self.connection.commit()
            messagebox.showinfo("Success", "Company details updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update company: {e}")

    def go_back(self):
        """Return to the previous screen."""
        self.root.destroy()
        self.prev_screen.deiconify()
