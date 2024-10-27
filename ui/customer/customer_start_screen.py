import tkinter as tk
from tkinter import Toplevel, Label, Button
from ui.customer.customer_signup_screen import CustomerSignupScreen
from ui.customer.customer_login_screen import CustomerLoginScreen

class CustomerScreen:
    
    def __init__(self, root, home_screen):
        self.home_screen = home_screen
        self.window = Toplevel(root)
        self.window.title("Customer Screen")
        self.window.geometry("400x300")
        
        Label(self.window, text="Customer Screen", font=("times new roman", 24, "bold"), fg="black").pack(pady=10)

        Button(self.window, text="Signup", font=("times new roman", 14), command=self.open_signup).pack(pady=10)
        Button(self.window, text="Login", font=("times new roman", 14), command=self.open_login).pack(pady=10)
        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def go_back(self):
        self.window.destroy()
        self.home_screen.show()
    
    def open_signup(self):
        self.window.withdraw()
        CustomerSignupScreen(self.window)

    def open_login(self):
        self.window.withdraw()
        CustomerLoginScreen(self.window)