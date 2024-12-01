import tkinter as tk
from tkinter import Toplevel, Label, Button, ttk
from dml.customer_dml import CustomerDML

class UpdateCustomer:

    def __init__(self, root, cursor, go_back_func, selected_company_id, connection):
        self.root = Toplevel(root)
        self.cursor = cursor
        self.connection = connection
        self.prev_screen = root
        self.selected_company_id = selected_company_id
        self.go_back_func = go_back_func
        self.root.title("Update Customer Details")
        self.root.state('zoomed')

        # Frame for input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10)  # Use grid instead of pack for input frame

        # Labels and Entries for customer details
        labels = [
            "Customer ID", "Username", "First Name", "Last Name",
            "Email", "Phone No", "Street Name", "Street No",
            "City", "State", "Postal Code", "Country"
        ]

        self.entries = {}
        for i, label in enumerate(labels):
            Label(self.input_frame, text=label, font=("times new roman", 12)).grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(self.input_frame, font=("times new roman", 12))
            if label == "Customer ID":
                entry.config(state="readonly")  # Make "Customer ID" non-editable
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[label] = entry

        # Table for displaying customer data
        self.treeview = ttk.Treeview(self.root, columns=("customer_id", "username", "first_name", "last_name", "email", "phone_no", "street_name", "street_no", "city", "state", "postal_code", "country"), show="headings")

        # Horizontal scrollbar
        self.scrollbar = tk.Scrollbar(self.root, orient="horizontal", command=self.treeview.xview)
        self.treeview.config(xscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="ew")

        self.treeview.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        # Define the table headers in the desired order and set column widths
        column_widths = {
            "customer_id": 80,
            "username": 100,
            "first_name": 100,
            "last_name": 100,
            "email": 120,
            "phone_no": 100,
            "street_name": 100,
            "street_no": 80,
            "city": 100,
            "state": 100,
            "postal_code": 80,
            "country": 100
        }

        for col, width in column_widths.items():
            self.treeview.heading(col, text=col.replace("_", " ").title())
            self.treeview.column(col, width=width, anchor="w")

        self.treeview.bind("<ButtonRelease-1>", self.on_row_select)  # Bind row selection

        # Load the customer data into the table
        self.load_customers()

        # Update button
        Button(self.root, text="Update", font=("times new roman", 14), command=self.update_customer, bg="#4f8fc0", fg="white").grid(row=3, column=0, pady=10, sticky="w", padx=10)

        # Back button
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back, bg="#26648e", fg="white").grid(row=3, column=1, pady=10, sticky="e", padx=10)

    def load_customers(self):
        # Clear the existing data in the table
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Fetch customers from the database
        self.cursor.execute(CustomerDML.getAllInfoOfAllCustomersOfACompany(self.selected_company_id))
        rows = self.cursor.fetchall()

        # Insert rows into the table in the correct order
        for row in rows:
            self.treeview.insert("", "end", values=row)

    def on_row_select(self, event):
        # Get the selected row from the table
        selected_item = self.treeview.selection()[0]
        selected_data = self.treeview.item(selected_item, "values")

        # Temporarily make "Customer ID" editable to populate it, then set it back to "readonly"
        self.entries["Customer ID"].config(state="normal")
        self.entries["Customer ID"].delete(0, tk.END)
        self.entries["Customer ID"].insert(0, selected_data[0])
        self.entries["Customer ID"].config(state="readonly")

        # Populate the other fields
        self.entries["Username"].delete(0, tk.END)
        self.entries["Username"].insert(0, selected_data[1])
        self.entries["First Name"].delete(0, tk.END)
        self.entries["First Name"].insert(0, selected_data[2])
        self.entries["Last Name"].delete(0, tk.END)
        self.entries["Last Name"].insert(0, selected_data[3])
        self.entries["Email"].delete(0, tk.END)
        self.entries["Email"].insert(0, selected_data[4])
        self.entries["Phone No"].delete(0, tk.END)
        self.entries["Phone No"].insert(0, selected_data[5])
        self.entries["Street Name"].delete(0, tk.END)
        self.entries["Street Name"].insert(0, selected_data[6])
        self.entries["Street No"].delete(0, tk.END)
        self.entries["Street No"].insert(0, selected_data[7])
        self.entries["City"].delete(0, tk.END)
        self.entries["City"].insert(0, selected_data[8])
        self.entries["State"].delete(0, tk.END)
        self.entries["State"].insert(0, selected_data[9])
        self.entries["Postal Code"].delete(0, tk.END)
        self.entries["Postal Code"].insert(0, selected_data[10])
        self.entries["Country"].delete(0, tk.END)
        self.entries["Country"].insert(0, selected_data[11])


    def update_customer(self):
        details = {label: entry.get() for label, entry in self.entries.items()}

        update_query = CustomerDML.updateAllFieldsOfACustomer(
            self.selected_company_id,
            details["Customer ID"],
            details["Username"],
            details["First Name"],
            details["Last Name"],
            details["Email"],
            details["Phone No"],
            details["Street Name"],
            details["Street No"],
            details["City"],
            details["State"],
            details["Postal Code"],
            details["Country"])

        self.cursor.execute(update_query)
        self.connection.commit()

        # Refresh the table to reflect the updated data
        self.load_customers()

        # Clear all the fields after the update
        for label, entry in self.entries.items():
            if label == "Customer ID":
                entry.config(state="normal")  # Temporarily make the "Customer ID" field editable
                entry.delete(0, tk.END)  # Clear the text in the "Customer ID" field
                entry.config(state="readonly")  # Set it back to readonly after clearing
            else:
                entry.delete(0, tk.END)  # Clear text for other fields

    def go_back(self):
        self.root.destroy()
        self.prev_screen.deiconify()