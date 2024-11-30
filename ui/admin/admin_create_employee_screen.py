import tkinter as tk
from tkinter import ttk, Toplevel, Label, Button

class AddEmployee:

    def __init__(self, root, cursor, go_back_func, selected_company_id, connection):
        self.root = Toplevel(root)
        self.prev_screen = root
        self.cursor = cursor
        self.connection = connection
        self.selected_company_id = selected_company_id
        self.go_back_func = go_back_func
        self.root.title("Add Employee")
        self.root.state("zoomed")  # Set window to open in full screen

        # Create a frame for grid layout
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Define the labels and keys for fields
        fields = [
            "Employee Username", "Employee Password", "Employee First Name", "Employee Last Name", 
            "Employee Email", "Employee Phone No", "Employee Hire Date", "Employee Street Name", 
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
        self.cursor.execute(f"SELECT MAX(employee_id) FROM employee WHERE company_id = {self.selected_company_id}")
        max_id_result = self.cursor.fetchone()[0]
        newEmployeeID = (max_id_result + 1) if max_id_result else 1
        employee_data = {field: entry.get() for field, entry in self.entries.items()}
        employee_data["Is Admin"] = self.is_admin_value.get()
        insertEmployeeQuery = f"INSERT INTO Employee (employee_user_name, employee_password, employee_id, employee_first_name, employee_last_name, employee_email, employee_phone_no, employee_hire_date, employee_street_name, employee_street_no, employee_city, employee_state, employee_postal_code, employee_country, company_id, is_admin) VALUES (\"{employee_data['Employee Username']}\", \"{employee_data['Employee Password']}\", {newEmployeeID}, \"{employee_data['Employee First Name']}\", \"{employee_data['Employee Last Name']}\", \"{employee_data['Employee Email']}\", \"{employee_data['Employee Phone No']}\", \"{employee_data['Employee Hire Date']}\", \"{employee_data['Employee Street Name']}\", {employee_data['Employee Street No']}, \"{employee_data['Employee City']}\", \"{employee_data['Employee State']}\", \"{employee_data['Employee Postal Code']}\", \"{employee_data['Employee Country']}\", {self.selected_company_id}, {employee_data['Is Admin']});"
        self.cursor.execute(insertEmployeeQuery)
        self.connection.commit()

    def go_back(self):
        """Go back to the previous screen."""
        self.root.destroy()
        self.prev_screen.deiconify()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AddEmployee(root, cursor=None, go_back_func=None, selected_company_id=1, connection=None)
#     root.mainloop()
