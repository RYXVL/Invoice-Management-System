import tkinter as tk
from tkinter import Toplevel, Label, Frame, Button
from ui.admin.admin_start_screen import AdminScreen
from ui.employee.employee_start_screen import EmployeeScreen
from ui.customer.customer_start_screen import CustomerScreen

class StartScreen:
    def __init__(self, root, cursor, connection):
        self.root = root
        self.cursor = cursor
        self.connection = connection
        self.root.title("Invoice Management System")
        self.root.geometry("750x800")

        self.frame = Frame(self.root, bg="#121212")
        self.frame.place(x=80, y=20, width=600, height=700)

        Label(self.frame, text="Invoice Management System", font=("times new roman", 30, "bold"), bg="#4d4988", fg="white").place(width=600, height=75)

        Button(self.frame, text="Admin", font=("times new roman", 14), fg="white", bg="#B00857", command=self.open_admin_screen).place(x=200, y=200, width=200, height=50)
        Button(self.frame, text="Employee", font=("times new roman", 14), fg="white", bg="#B00857", command=self.open_employee_screen).place(x=200, y=300, width=200, height=50)
        Button(self.frame, text="Customer", font=("times new roman", 14), fg="white", bg="#B00857", command=self.open_customer_screen).place(x=200, y=400, width=200, height=50)

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.deiconify()

    def open_admin_screen(self):
        self.hide()
        AdminScreen(self.root, self, self.cursor, self.connection)

    def open_employee_screen(self):
        self.hide()
        EmployeeScreen(self.root, self, self.cursor, self.connection)

    def open_customer_screen(self):
        self.hide()
        CustomerScreen(self.root, self, self.cursor, self.connection)