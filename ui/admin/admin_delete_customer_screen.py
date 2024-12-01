import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label, Button
from dml.customer_dml import CustomerDML

class DeleteCustomer:

    def __init__(self, root, cursor, go_back_func, selected_company_id, connection):
        self.root = Toplevel(root)
        self.prev_screen = root
        self.cursor = cursor
        self.connection = connection
        self.selected_company_id = selected_company_id
        self.go_back_func = go_back_func
        self.root.title("Delete Customer")
        self.root.state("zoomed")

        # Setup the table on screen that shows existing customers
        self.customer_table = ttk.Treeview(
            self.root,
            columns=("ID", "Username", "First Name", "Last Name", "Email", "Phone"),
            show="headings",
        )
        self.customer_table.heading("ID", text="Customer ID")
        self.customer_table.heading("Username", text="Username")
        self.customer_table.heading("First Name", text="First Name")
        self.customer_table.heading("Last Name", text="Last Name")
        self.customer_table.heading("Email", text="Email")
        self.customer_table.heading("Phone", text="Phone")
        self.customer_table.pack(pady=10, fill=tk.BOTH, expand=True)

        # Populate the table with data fetched from the database
        self.fetch_customers()

        # Non-editable Customer ID field
        Label(self.root, text="Selected Customer ID").pack(pady=5)
        self.customer_id_entry = tk.Entry(self.root, state="readonly")
        self.customer_id_entry.pack(pady=5)

        # Buttons
        Button(self.root, text="Delete Customer", font=("times new roman", 14), bg="#4f8fc0", fg="white", command=self.delete_customer).pack(pady=10)
        Button(self.root, text="Back", font=("times new roman", 14), bg="#26648e", fg="white", command=self.go_back).pack(pady=10)

        # Bind row selection event
        self.customer_table.bind("<<TreeviewSelect>>", self.on_row_select)

    def fetch_customers(self):
        """Fetch and display customers in the table."""
        for row in self.customer_table.get_children():
            self.customer_table.delete(row)  # Clear existing rows

        # Fetch data of existing customers and populate it on the screen inside the table displayed
        self.cursor.execute(CustomerDML.getBasicInfoAllCustomers(self.selected_company_id))
        customers = self.cursor.fetchall()
        for customer in customers:
            self.customer_table.insert("", "end", values=customer)

    def on_row_select(self, event):
        """Handle row selection and display customer_id."""
        selected_item = self.customer_table.selection()
        if selected_item:
            customer_id = self.customer_table.item(selected_item[0])["values"][0]
            self.customer_id_entry.config(state="normal")
            self.customer_id_entry.delete(0, tk.END)
            self.customer_id_entry.insert(0, customer_id)
            self.customer_id_entry.config(state="readonly")

    def delete_customer(self):
        """Delete selected customer and refresh the table."""
        customer_id = self.customer_id_entry.get()
        if customer_id:
            self.cursor.execute(CustomerDML.deleteCustomer(customer_id, self.selected_company_id))
            self.connection.commit()
            self.fetch_customers()
            self.customer_id_entry.config(state="normal")
            self.customer_id_entry.delete(0, tk.END)
            self.customer_id_entry.config(state="readonly")
        else:
            tk.messagebox.showerror("Error", "Please select a customer to be deleted first!")
            return

    def go_back(self):
        """Return to the previous screen."""
        self.root.destroy()
        self.prev_screen.deiconify()