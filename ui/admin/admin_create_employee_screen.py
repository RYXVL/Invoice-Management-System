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
        Button(self.root, text="Create Employee", font=("times new roman", 14), command=self.create_employee).pack(pady=10)
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def toggle_is_admin(self):
        """Toggle the is_admin value between True and False."""
        current_value = self.is_admin_value.get()
        new_value = not current_value
        self.is_admin_value.set(new_value)
        self.is_admin_button.config(text=str(new_value), bg="green" if new_value else "red", fg="white")

    def create_employee(self):
        """Collect input data and print it."""
        employee_data = {field: entry.get() for field, entry in self.entries.items()}
        employee_data["Is Admin"] = self.is_admin_value.get()
        print("Employee Data:")
        for key, value in employee_data.items():
            print(f"{key}: {value}")

    def go_back(self):
        """Go back to the previous screen."""
        self.root.destroy()
        self.prev_screen.deiconify()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AddEmployee(root, cursor=None, go_back_func=None, selected_company_id=1, connection=None)
#     root.geometry("600x400")
#     root.mainloop()
