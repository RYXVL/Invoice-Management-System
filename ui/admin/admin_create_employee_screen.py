import tkinter as tk
from tkinter import ttk

class AddEmployee:

    def __init__(self, root):
        self.root = root
        self.root.title("Add Employee")

        # Frame for input fields
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Define fields
        fields = [
            "Username", "Password", "Employee ID", "First Name", "Last Name", "Email", 
            "Phone Number", "Hire Date", "Street Name", "Street No", "City", 
            "State", "Postal Code", "Country"
        ]
        
        # Dictionary to store entries
        self.entries = {}

        # Loop to create label and entry for each field
        for idx, field in enumerate(fields):
            tk.Label(self.input_frame, text=field, font=("times new roman", 12)).grid(row=idx, column=0, sticky="w", pady=2)
            
            # If the field is Password, show as asterisks
            show_char = "*" if field == "Password" else None
            entry = tk.Entry(self.input_frame, font=("times new roman", 12), show=show_char)
            entry.grid(row=idx, column=1, pady=2, padx=5)
            
            # Store entry widget in dictionary
            self.entries[field] = entry

        # Add button at the bottom
        self.add_button = tk.Button(self.root, text="Add", font=("times new roman", 14), command=self.submit_data)
        self.add_button.pack(pady=10)

    # Dummy function to print entered data
    def submit_data(self):
        entered_data = {field: entry.get() for field, entry in self.entries.items()}
        print("Entered Employee Data:", entered_data)

if __name__ == '__main__':
    root = tk.Tk()
    app = AddEmployee(root)
    root.geometry("350x600")  # Adjusted window size to fit all fields comfortably
    root.mainloop()
