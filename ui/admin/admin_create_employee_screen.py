import tkinter as tk
from tkinter import ttk, Toplevel, Label, Button
from dml.employee_dml import EmployeeDML
import re

class AddEmployee:

    def __init__(self, root, cursor, go_back_func, selected_company_id, connection):
        self.root = Toplevel(root)
        self.prev_screen = root
        self.cursor = cursor
        self.connection = connection
        self.selected_company_id = selected_company_id
        self.go_back_func = go_back_func
        self.root.title("Add Employee")
        self.root.state("zoomed")

        # Create a frame for grid layout
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Define the labels and keys for fields
        fields = [
            "Employee Username", "Employee Password", "Employee First Name", "Employee Last Name", 
            "Employee Email", "Employee Phone No", "Employee Hire Date (YYYY-MM-DD)", "Employee Street Name", 
            "Employee Street No", "Employee City", "Employee State", "Employee Postal Code", 
            "Employee Country"
        ]

        self.entries = {}  # Dictionary to hold entry widgets

        # Arrange inputs in rows with 2 per row
        for idx, field in enumerate(fields):
            row, col = divmod(idx, 2)
            Label(self.input_frame, text=field).grid(row=row, column=col*2, padx=5, pady=5, sticky="e")
            entry = tk.Entry(self.input_frame)
            entry.grid(row=row, column=col*2+1, padx=5, pady=5, sticky="w")
            self.entries[field] = entry

        # Add toggle button for Is Admin
        row = (len(fields) + 1) // 2  # Place it in the next available row
        Label(self.input_frame, text="Is Admin").grid(row=row, column=0, padx=5, pady=5, sticky="e")
        self.is_admin_value = tk.BooleanVar(value=False)
        self.is_admin_button = Button(
            self.input_frame, text="False", font=("times new roman", 14),
            command=self.toggle_is_admin, bg="red", fg="white"
        )
        self.is_admin_button.grid(row=row, column=1, padx=5, pady=5, sticky="w")

        # Buttons for actions
        Button(self.root, text="Create Employee", font=("times new roman", 14), bg="#4f8fc0", fg="white", command=self.create_employee).pack(pady=10)
        Button(self.root, text="Back", font=("times new roman", 14), bg="#26648e", fg="white", command=self.go_back).pack(pady=10)

    def toggle_is_admin(self):
        """Toggle the is_admin value between True and False."""
        current_value = self.is_admin_value.get()
        new_value = not current_value
        self.is_admin_value.set(new_value)
        self.is_admin_button.config(text=str(new_value), bg="green" if new_value else "red", fg="white")

    def create_employee(self):
        # Find the employee id of the new employee to be created
        self.cursor.execute(EmployeeDML.getMaxEmployeeIdOfCompany(self.selected_company_id))
        max_id_result = self.cursor.fetchone()[0]
        newEmployeeID = (max_id_result + 1) if max_id_result else 1

        # Get data of the new employee and push it to the database corresponding to its new employee id
        employee_data = {field: entry.get() for field, entry in self.entries.items()}
        employee_data["Is Admin"] = self.is_admin_value.get()

        # Sanity check: Ensure no fields are empty
        missing_fields = [field for field, value in employee_data.items() if not value and field != "Is Admin"]
        if missing_fields:
            missing_fields_str = ', '.join(missing_fields)
            tk.messagebox.showerror("Error", f"The following fields must be filled: {missing_fields_str}")
            return
        
        if not employee_data['Employee Phone No'].isdigit() or len(employee_data['Employee Phone No']) > 10:
            tk.messagebox.showerror("Error", "Phone number must be all numbers and maximum 10 characters.")
            return

        if not re.match(r"^\d{4}-\d{2}-\d{2}$", employee_data['Employee Hire Date (YYYY-MM-DD)']):
            tk.messagebox.showerror("Error", "Hire date must be in the format yyyy-mm-dd.")
            return

        if not employee_data['Employee Street No'].isdigit():
            tk.messagebox.showerror("Error", "Street number must be an integer.")
            return

        if not employee_data['Employee Postal Code'].isdigit() or len(employee_data['Employee Postal Code']) > 5:
            tk.messagebox.showerror("Error", "Postal code must be all numbers and maximum 5 characters.")
            return
        
        self.cursor.callproc(
            'InsertNewEmployee',
            [
                employee_data['Employee Username'],
                employee_data['Employee Password'],
                newEmployeeID,
                employee_data['Employee First Name'],
                employee_data['Employee Last Name'],
                employee_data['Employee Email'],
                employee_data['Employee Phone No'],
                employee_data['Employee Hire Date (YYYY-MM-DD)'],
                employee_data['Employee Street Name'],
                employee_data['Employee Street No'],
                employee_data['Employee City'],
                employee_data['Employee State'],
                employee_data['Employee Postal Code'],
                employee_data['Employee Country'],
                self.selected_company_id,
                employee_data['Is Admin']
            ]
        )
        self.connection.commit()
        # Clear all input fields after commit
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        tk.messagebox.showinfo("Success", "New employee has been created successfully!")

    def go_back(self):
        """Go back to the previous screen."""
        self.root.destroy()
        self.prev_screen.deiconify()