import tkinter as tk
from tkinter import Toplevel, Label, Button

class EmployeeMenu:
    
    def __init__(self, employee_screen):
        self.employee_screen = employee_screen  # Store the reference to the EmployeeScreen instance
        self.window = Toplevel()
        self.window.title("Employee Menu")
        self.window.geometry("400x300")
        
        Label(self.window, text="Employee Menu", font=("times new roman", 24, "bold"), fg="black").pack(pady=10)

        Button(self.window, text="Generate Invoice", font=("times new roman", 14)).pack(pady=10)
        Button(self.window, text="View Invoice", font=("times new roman", 14)).pack(pady=10)
        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def go_back(self):
        self.window.destroy()  # Close the Employee Menu
        self.employee_screen.window.deiconify()  # Show the Employee Screen again
