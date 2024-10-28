import tkinter as tk
from tkinter import Toplevel, Label, Button

class CustomerSignupScreen:
    def __init__(self, customer_screen):
        self.customer_screen = customer_screen
        self.window = Toplevel()
        self.window.title("Customer Signup")
        self.window.geometry("400x300")
        
        Label(self.window, text="Signup", font=("times new roman", 24, "bold")).pack(pady=10)
        
        Label(self.window, text="Username:", font=("times new roman", 14)).pack(pady=5)
        self.username_entry = tk.Entry(self.window, font=("times new roman", 14))
        self.username_entry.pack(pady=5)

        Label(self.window, text="Password:", font=("times new roman", 14)).pack(pady=5)
        self.password_entry = tk.Entry(self.window, font=("times new roman", 14), show="*")
        self.password_entry.pack(pady=5)

        Button(self.window, text="Signup", font=("times new roman", 14), command=self.signup_action).pack(pady=10)
        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def signup_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Signup Username: {username}")
        print(f"Signup Password: {password}")

    def go_back(self):
        self.window.destroy()
        self.customer_screen.deiconify()