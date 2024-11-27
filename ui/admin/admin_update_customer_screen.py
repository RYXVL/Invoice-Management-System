import tkinter as tk
from tkinter import Toplevel, Label, Button, ttk

class UpdateCustomer:

    def __init__(self, root, cursor, go_back_func, selected_company_id, connection):
        self.root = Toplevel(root)
        self.cursor = cursor
        self.connection = connection
        self.prev_screen = root
        self.selected_company_id = selected_company_id
        self.go_back_func = go_back_func
        self.root.title("Update Customer Details")

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
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[label] = entry

        # Table for displaying customer data
        self.treeview = ttk.Treeview(self.root, columns=("customer_id", "username", "first_name", "last_name", "email", "phone_no", "street_name", "street_no", "city", "state", "postal_code", "country"), show="headings")
        self.treeview.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        
        # Define the table headers in the desired order
        self.treeview.heading("customer_id", text="Customer ID")
        self.treeview.heading("username", text="Username")
        self.treeview.heading("first_name", text="First Name")
        self.treeview.heading("last_name", text="Last Name")
        self.treeview.heading("email", text="Email")
        self.treeview.heading("phone_no", text="Phone No")
        self.treeview.heading("street_name", text="Street Name")
        self.treeview.heading("street_no", text="Street No")
        self.treeview.heading("city", text="City")
        self.treeview.heading("state", text="State")
        self.treeview.heading("postal_code", text="Postal Code")
        self.treeview.heading("country", text="Country")
        self.treeview.bind("<ButtonRelease-1>", self.on_row_select)  # Bind row selection

        # Load the customer data into the table
        self.load_customers()

        # Update button
        Button(self.root, text="Update", font=("times new roman", 14), command=self.update_customer).grid(row=2, column=0, pady=10, sticky="w", padx=10)
        
        # Back button
        Button(self.root, text="Back", font=("times new roman", 14), command=self.go_back).grid(row=2, column=1, pady=10, sticky="e", padx=10)

    def load_customers(self):
        # Clear the existing data in the table
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Fetch customers from the database
        self.cursor.execute(f"SELECT customer_id, customer_user_name, customer_first_name, customer_last_name, customer_email, customer_phone_no, customer_street_name, customer_street_no, customer_city, customer_state, customer_postal_code, customer_country FROM Customer WHERE company_id = {self.selected_company_id};")
        rows = self.cursor.fetchall()

        # Insert rows into the table in the correct order
        for row in rows:
            self.treeview.insert("", "end", values=row)

    def on_row_select(self, event):
        # Get the selected row from the table
        selected_item = self.treeview.selection()[0]
        selected_data = self.treeview.item(selected_item, "values")

        # Populate the input fields with the selected row's data
        self.entries["Customer ID"].delete(0, tk.END)
        self.entries["Customer ID"].insert(0, selected_data[0])
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
        print("Customer Details to Update:")
        for key, value in details.items():
            print(f"{key}: {value}")

        # Update the customer details in the database
        update_query = f"""
        UPDATE Customer 
        SET customer_user_name = '{details["Username"]}', 
            customer_first_name = '{details["First Name"]}', 
            customer_last_name = '{details["Last Name"]}', 
            customer_email = '{details["Email"]}', 
            customer_phone_no = '{details["Phone No"]}', 
            customer_street_name = '{details["Street Name"]}', 
            customer_street_no = '{details["Street No"]}', 
            customer_city = '{details["City"]}', 
            customer_state = '{details["State"]}', 
            customer_postal_code = '{details["Postal Code"]}', 
            customer_country = '{details["Country"]}' 
        WHERE customer_id = {details["Customer ID"]}
        AND company_id = {self.selected_company_id};
        """
        self.cursor.execute(update_query)
        self.connection.commit()

        # Refresh the table to reflect the updated data
        self.load_customers()

    def go_back(self):
        self.root.destroy()
        self.prev_screen.deiconify()
