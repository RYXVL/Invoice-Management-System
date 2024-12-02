import tkinter as tk
from tkinter import Toplevel, Label, Button, messagebox
from dml.company_dml import CompanyDML

class UpdateCompany:

    def __init__(self, root, cursor, go_back_func, selected_company_id, connection):
        self.root = Toplevel(root)
        self.cursor = cursor
        self.connection = connection
        self.prev_screen = root
        self.selected_company_id = selected_company_id
        self.go_back_func = go_back_func
        self.root.title("Update Company Details")
        self.root.state('zoomed')

        # Frame for input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Labels and Entries for company details
        labels = [
            "Company ID", "Name", "Street Name", "Street No",
            "City", "State", "Postal Code", "Country",
            "Email", "Phone No"
        ]

        # Generate the labels and corresponding input fields on the screen
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

        # Update button with color (c3)
        update_button = Button(self.root, text="Update", font=("times new roman", 14), command=self.update_company, bg="#4f8fc0", fg="white")
        update_button.pack(pady=10)

        # Back button with color (c4)
        back_button = Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back, bg="#26648e", fg="white")
        back_button.pack(pady=10)

    def fetch_company_data(self):
        self.cursor.execute(CompanyDML.getAllInfoOfACompany(self.selected_company_id))
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

        missing_fields = [field for field, value in details.items() if not value]
        if missing_fields:
            missing_fields_str = ', '.join(missing_fields)
            tk.messagebox.showerror("Error", f"The following fields must be filled: {missing_fields_str}")
            return
        
        if not details["Street No"].isdigit():
            messagebox.showerror("Error", "Street No should be a valid number!")
            return
        
        if not details["Postal Code"].isdigit() or len(details["Postal Code"]) > 5:
            messagebox.showerror("Error", "Postal Code should be a number with a maximum length of 5!")
            return
        
        if not details["Phone No"].isdigit() or len(details["Phone No"]) > 10:
            messagebox.showerror("Error", "Phone No should be a number with a maximum length of 10!")
            return

        try:
            self.cursor.callproc(
                'UpdateAllFieldsOfACompany', 
                [
                    details["Company ID"], 
                    details["Name"], 
                    details["Street Name"], 
                    details["Street No"], 
                    details["City"], 
                    details["State"], 
                    details["Postal Code"], 
                    details["Country"], 
                    details["Email"], 
                    details["Phone No"]
                ]
            )
            self.connection.commit()
            messagebox.showinfo("Success", "Company details updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update company: {e}")

    def go_back(self):
        """Return to the previous screen."""
        self.root.destroy()
        self.prev_screen.deiconify()