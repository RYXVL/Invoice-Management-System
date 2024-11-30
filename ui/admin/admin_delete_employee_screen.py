import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label, Button
from dml.employee_dml import EmployeeDML

class DeleteEmployee:

    def __init__(self, root, cursor, go_back_func, selected_company_id, connection):
        self.root = Toplevel(root)
        self.cursor = cursor
        self.connection = connection
        self.prev_screen = root
        self.selected_company_id = selected_company_id
        self.go_back_func = go_back_func
        self.root.title("Delete Employee")
        self.root.state("zoomed")  # Set window to open in full screen

        # Employee Table with updated columns
        self.employee_table = ttk.Treeview(
            self.root,
            columns=("ID", "Username", "First Name", "Last Name", "Email", "Phone", "Hire Date", "Is Admin"),
            show="headings",
        )
        self.employee_table.heading("ID", text="Employee ID")
        self.employee_table.heading("Username", text="Employee Username")
        self.employee_table.heading("First Name", text="First Name")
        self.employee_table.heading("Last Name", text="Last Name")
        self.employee_table.heading("Email", text="Email")
        self.employee_table.heading("Phone", text="Phone")
        self.employee_table.heading("Hire Date", text="Hire Date")
        self.employee_table.heading("Is Admin", text="Is Admin")
        self.employee_table.pack(pady=10, fill=tk.BOTH, expand=True)

        # Populate the table
        self.fetch_employees()

        # Non-editable Employee ID field
        Label(self.root, text="Selected Employee ID").pack(pady=5)
        self.employee_id_entry = tk.Entry(self.root, state="readonly")
        self.employee_id_entry.pack(pady=5)

        # Buttons
        Button(self.root, text="Delete Employee", font=("times new roman", 14), bg="#4f8fc0", fg="white", command=self.delete_employee).pack(pady=10)
        Button(self.root, text="Back", font=("times new roman", 14), bg="#26648e", fg="white", command=self.go_back).pack(pady=10)

        # Bind row selection event
        self.employee_table.bind("<<TreeviewSelect>>", self.on_row_select)

    def fetch_employees(self):
        """Fetch and display employees in the table."""
        for row in self.employee_table.get_children():
            self.employee_table.delete(row)  # Clear existing rows

        # query = f"SELECT employee_id, employee_user_name, employee_first_name, employee_last_name, employee_email, employee_phone_no, employee_hire_date, is_admin FROM Employee WHERE company_id = {self.selected_company_id};"
        self.cursor.execute(EmployeeDML.getBasicInfoAllEmployees(self.selected_company_id))
        employees = self.cursor.fetchall()
        for employee in employees:
            self.employee_table.insert("", "end", values=employee)

    def on_row_select(self, event):
        """Handle row selection and display employee_id."""
        selected_item = self.employee_table.selection()
        if selected_item:
            employee_id = self.employee_table.item(selected_item[0])["values"][0]
            self.employee_id_entry.config(state="normal")
            self.employee_id_entry.delete(0, tk.END)
            self.employee_id_entry.insert(0, employee_id)
            self.employee_id_entry.config(state="readonly")

    def delete_employee(self):
        """Delete selected employee and refresh the table."""
        employee_id = self.employee_id_entry.get()
        if employee_id:
            self.cursor.execute(EmployeeDML.deleteEmployee(employee_id, self.selected_company_id))
            self.connection.commit()
            self.fetch_employees()
            self.employee_id_entry.config(state="normal")
            self.employee_id_entry.delete(0, tk.END)
            self.employee_id_entry.config(state="readonly")

    def go_back(self):
        """Return to the previous screen."""
        self.root.destroy()
        self.prev_screen.deiconify()