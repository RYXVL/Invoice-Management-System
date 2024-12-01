from tkinter import Toplevel, Label, Button, ttk, Frame
import tkinter as tk
from dml.employee_dml import EmployeeDML

class UpdateEmployee:

    def __init__(self, root, cursor, go_back_func, selected_company_id, connection):
        self.root = Toplevel(root)
        self.cursor = cursor
        self.connection = connection
        self.prev_screen = root
        self.selected_company_id = selected_company_id
        self.go_back_func = go_back_func
        self.root.title("Update Employee Details")
        self.root.state('zoomed')

        c3 = "#4f8fc0"
        c4 = "#26648e"

        # Frame for input
        self.input_frame = Frame(self.root)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10)

        # Labels and Entries for employee details in two columns
        labels = [
            "Employee ID", "Username", "Password", "First Name",
            "Last Name", "Email", "Phone No", "Hire Date", "Street Name",
            "Street No", "City", "State", "Postal Code", "Country"
        ]

        self.entries = {}
        for i, label in enumerate(labels):
            row, col = divmod(i, 2)  # Calculate row and column for two-column layout
            Label(self.input_frame, text=label, font=("times new roman", 12)).grid(row=row, column=col * 2, sticky="w", pady=5, padx=5)
            entry = tk.Entry(self.input_frame, font=("times new roman", 12))
            if label == "Employee ID":
                entry.config(state="readonly")  # Employee ID should be non-editable
            entry.grid(row=row, column=col * 2 + 1, pady=5, padx=5)
            self.entries[label] = entry

        # Add the "Is Admin" button below the input fields
        Label(self.input_frame, text="Is Admin", font=("times new roman", 12)).grid(row=len(labels), column=0, sticky="w", pady=5, padx=5)
        self.is_admin_button = tk.Button(self.input_frame, text="False", font=("times new roman", 12), command=self.toggle_is_admin, bg=c3)
        self.is_admin_button.grid(row=len(labels), column=1, pady=5, padx=5)

        # Table for displaying employee data
        self.treeview = ttk.Treeview(
            self.root,
            columns=("employee_id", "username", "password", "first_name", "last_name",
                     "email", "phone_no", "hire_date", "street_name", "street_no", "city",
                     "state", "postal_code", "country", "is_admin"),
            show="headings"
        )

        self.treeview.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Define table headers and set column widths
        headers = {
            "employee_id": 80, "username": 100, "password": 100, "first_name": 100,
            "last_name": 100, "email": 120, "phone_no": 100, "hire_date": 100,
            "street_name": 100, "street_no": 80, "city": 100, "state": 100,
            "postal_code": 80, "country": 100, "is_admin": 80
        }

        for col, width in headers.items():
            self.treeview.heading(col, text=col.replace("_", " ").title())
            self.treeview.column(col, width=width, anchor="w")

        self.treeview.bind("<ButtonRelease-1>", self.on_row_select)  # Row selection event

        # Load employee data into the table
        self.load_employees()

        # Update and Back buttons
        Button(self.root, text="Update", font=("times new roman", 14), command=self.update_employee, bg=c3).grid(row=2, column=0, pady=10, sticky="w", padx=10)
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back, bg=c4).grid(row=2, column=0, pady=10, sticky="e", padx=10)

    def toggle_is_admin(self):
        # Toggle between True and False
        current_state = self.is_admin_button.cget("text")
        self.is_admin_button.config(text="True" if current_state == "False" else "False")

    def load_employees(self):
        # Clear existing data in the table
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Fetch employee details from the database
        self.cursor.execute(EmployeeDML.getAllInfoOfAllEmployeesOfACompany(self.selected_company_id))
        rows = self.cursor.fetchall()

        # Insert rows into the table
        for row in rows:
            self.treeview.insert("", "end", values=row)

    def on_row_select(self, event):
        # Get the selected row from the table
        selected_item = self.treeview.selection()[0]
        selected_data = self.treeview.item(selected_item, "values")

        # Populate input fields with selected row's data
        for i, (label, entry) in enumerate(self.entries.items()):
            if label == "Employee ID":
                entry.config(state="normal")
                entry.delete(0, 'end')
                entry.insert(0, selected_data[i])
                entry.config(state="readonly")
            else:
                entry.delete(0, 'end')
                entry.insert(0, selected_data[i])

        # Set the Is Admin button text based on the selected row's value
        is_admin_value = selected_data[-1]  # Last column corresponds to is_admin
        self.is_admin_button.config(text="True" if str(is_admin_value) == "1" else "False")

    def update_employee(self):
        # Collect field values
        details = {label: entry.get() for label, entry in self.entries.items()}
        is_admin = 1 if self.is_admin_button.cget("text") == "True" else 0

        update_query = EmployeeDML.updateAllFieldsOfAnEmployee(
            self.selected_company_id,
            details["Employee ID"],
            details["Username"],
            details["Password"],
            details["First Name"],
            details["Last Name"],
            details["Email"],
            details["Phone No"],
            details["Street Name"],
            details["Street No"],
            details["City"],
            details["State"],
            details["Postal Code"],
            details["Country"],
            is_admin,
            details["Hire Date"]
        )

        self.cursor.execute(update_query)

        self.connection.commit()

        # Refresh the table
        self.load_employees()

        # Clear all fields
        for label, entry in self.entries.items():
            entry.config(state="normal")  # Temporarily make Employee ID editable
            entry.delete(0, tk.END)  # Clear field
            if label == "Employee ID":
                entry.config(state="readonly")  # Set back to readonly

    def go_back(self):
        self.root.destroy()
        self.prev_screen.deiconify()