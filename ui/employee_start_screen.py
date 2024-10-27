import tkinter as tk
from tkinter import Toplevel, Label, Button

class EmployeeScreen:
    
    def __init__(self, root, home_screen):
        self.home_screen = home_screen
        self.window = Toplevel(root)
        self.window.title("Employee Screen")
        self.window.geometry("400x300")
        Label(self.window, text="Employee Screen", font=("times new roman", 24, "bold"), fg="black").pack(expand=True)

        Button(self.window, text="Login", font=("times new roman", 14), command=self.login_action).pack(pady=10)
        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def go_back(self):
        self.window.destroy()
        self.home_screen.show()
    
    def login_action(self):
        pass