import tkinter as tk
from tkinter import Toplevel, Label, Button
from ui.admin.admin_add_product_screen import AddProduct
from ui.admin.admin_create_employee_screen import AddEmployee
from ui.admin.admin_delete_customer_screen import DeleteCustomer
from ui.admin.admin_delete_employee_screen import DeleteEmployee
from ui.admin.admin_delete_product_screen import DeleteProduct
from ui.admin.admin_update_company_details_screen import UpdateCompany
from ui.admin.admin_update_customer_screen import UpdateCustomer
from ui.admin.admin_update_employee_screen import UpdateEmployee

class AdminMenu:

    def __init__(self, admin_screen, cursor, selected_company_id, connection):
        self.selected_company_id = selected_company_id
        print(self.selected_company_id)
        self.admin_screen = admin_screen
        self.window = Toplevel()
        self.cursor = cursor
        self.connection = connection
        self.window.title("Admin Menu")
        self.window.geometry("400x500")

        Label(self.window, text="Admin Menu", font=("times new roman", 24, "bold")).pack(pady=10)

        # Add buttons with commands to open corresponding screens
        Button(self.window, text="Add Product", font=("times new roman", 14), bg="#4f8fc0", fg="white", command=self.open_add_product).pack(pady=5)
        Button(self.window, text="Remove Product", font=("times new roman", 14), bg="#4f8fc0", fg="white", command=self.open_delete_product).pack(pady=5)
        Button(self.window, text="Create Employee", font=("times new roman", 14), bg="#4f8fc0", fg="white", command=self.open_add_employee).pack(pady=5)
        Button(self.window, text="Delete Employee", font=("times new roman", 14), bg="#4f8fc0", fg="white", command=self.open_delete_employee).pack(pady=5)
        Button(self.window, text="Delete Customer", font=("times new roman", 14), bg="#4f8fc0", fg="white", command=self.open_delete_customer).pack(pady=5)
        Button(self.window, text="Update Company Details", font=("times new roman", 14), bg="#4f8fc0", fg="white", command=self.open_update_company).pack(pady=5)
        Button(self.window, text="Update Customer", font=("times new roman", 14), bg="#4f8fc0", fg="white", command=self.open_update_customer).pack(pady=5)
        Button(self.window, text="Update Employee", font=("times new roman", 14), bg="#4f8fc0", fg="white", command=self.open_update_employee).pack(pady=5)

        Button(self.window, text="Back", font=("times new roman", 14), bg="#26648e", fg="white", command=self.go_back).pack(pady=10)

    def go_back(self):
        self.window.destroy()
        self.admin_screen.deiconify()

    # Functions to open each screen and pass cursor
    def open_add_product(self):
        self.window.withdraw()
        AddProduct(self.window, self.cursor, self.go_back, self.selected_company_id, self.connection)

    def open_delete_product(self):
        self.window.withdraw()
        DeleteProduct(self.window, self.cursor, self.go_back, self.selected_company_id, self.connection)

    def open_add_employee(self):
        self.window.withdraw()
        AddEmployee(self.window, self.cursor, self.go_back, self.selected_company_id, self.connection)

    def open_delete_employee(self):
        self.window.withdraw()
        DeleteEmployee(self.window, self.cursor, self.go_back, self.selected_company_id, self.connection)

    def open_delete_customer(self):
        self.window.withdraw()
        DeleteCustomer(self.window, self.cursor, self.go_back, self.selected_company_id, self.connection)

    def open_update_company(self):
        self.window.withdraw()
        UpdateCompany(self.window, self.cursor, self.go_back, self.selected_company_id, self.connection)

    def open_update_customer(self):
        self.window.withdraw()
        UpdateCustomer(self.window, self.cursor, self.go_back, self.selected_company_id, self.connection)

    def open_update_employee(self):
        self.window.withdraw()
        UpdateEmployee(self.window, self.cursor, self.go_back, self.selected_company_id, self.connection)
