# import tkinter as tk

# class DeleteEmployee:

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Delete Employee")

#         # Frame for input
#         self.input_frame = tk.Frame(self.root)
#         self.input_frame.pack(padx=10, pady=10)

#         # Label and Entry for employee_id
#         tk.Label(self.input_frame, text="Employee ID", font=("times new roman", 12)).grid(row=0, column=0, sticky="w", pady=5)
#         self.employee_id_entry = tk.Entry(self.input_frame, font=("times new roman", 12))
#         self.employee_id_entry.grid(row=0, column=1, pady=5, padx=5)

#         # Delete button
#         self.delete_button = tk.Button(self.root, text="Delete", font=("times new roman", 14), command=self.delete_employee)
#         self.delete_button.pack(pady=10)

#     # Dummy function to print entered employee_id
#     def delete_employee(self):
#         employee_id = self.employee_id_entry.get()
#         print("Employee ID to delete:", employee_id)

# if __name__ == '__main__':
#     root = tk.Tk()
#     app = DeleteEmployee(root)
#     root.geometry("300x150")
#     root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import ttk, Toplevel, Label, Button

class DeleteEmployee:

    def __init__(self, root, cursor, go_back_func):
        self.root = Toplevel(root)
        self.cursor = cursor
        self.prev_screen = root
        self.go_back_func = go_back_func
        self.root.title("Delete Employee")

        # Example UI for deleting an employee
        Label(self.root, text="Employee ID").pack(pady=5)
        self.employee_id_entry = tk.Entry(self.root)
        self.employee_id_entry.pack(pady=5)

        Button(self.root, text="Delete Employee", font=("times new roman", 14), command=self.delete_employee).pack(pady=10)
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def delete_employee(self):
        employee_id = self.employee_id_entry.get()
        self.cursor.execute("DELETE FROM Employee WHERE employee_id = ?", (employee_id,))
        self.cursor.connection.commit()

    def go_back(self):
        self.root.destroy()
        self.prev_screen.deiconify()