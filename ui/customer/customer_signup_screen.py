import tkinter as tk
import tkinter as tk
from tkinter import Toplevel, Label, Button, StringVar, OptionMenu, Entry
from tkinter import Toplevel, Label, Button, StringVar, OptionMenu
from tkinter import Toplevel, Label, Button, StringVar, OptionMenu, Entry, Canvas, Frame, Scrollbar
from ui.customer.customer_main_screen import CustomerMainScreen
from dml.customer_dml import CustomerDML
from dml.company_dml import CompanyDML

class CustomerSignupScreen:
    def __init__(self, customer_screen, cursor, connection):
        self.customer_screen = customer_screen
        self.cursor = cursor
        self.connection = connection
        self.window = Toplevel()
        self.window.title("Customer Signup")
        # self.window.geometry("400x600")
        self.window.state("zoomed")

        # Create a canvas with a scrollbar
        canvas = Canvas(self.window)
        scrollbar = Scrollbar(self.window, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Add widgets to scrollable frame
        Label(scrollable_frame, text="Signup", font=("times new roman", 24, "bold")).pack(pady=10)

        # Add input fields with labels in rows
        self.create_field_row(scrollable_frame, "Enter Username:", "username")
        self.create_field_row(scrollable_frame, "Enter Password:", "password", show="*")
        self.create_field_row(scrollable_frame, "First Name:", "first_name")
        self.create_field_row(scrollable_frame, "Last Name:", "last_name")
        self.create_field_row(scrollable_frame, "Email:", "email")
        self.create_field_row(scrollable_frame, "Phone No:", "phone_no")
        self.create_field_row(scrollable_frame, "Street Name:", "street_name")
        self.create_field_row(scrollable_frame, "Street No:", "street_no", is_numeric=True)
        self.create_field_row(scrollable_frame, "City:", "city")
        self.create_field_row(scrollable_frame, "State:", "state")
        self.create_field_row(scrollable_frame, "Postal Code:", "postal_code", is_numeric=True)
        self.create_field_row(scrollable_frame, "Country:", "country")

        Label(scrollable_frame, text="Select Company:", font=("times new roman", 14)).pack(pady=5)
        self.company_var = StringVar()
        self.company_dropdown = OptionMenu(scrollable_frame, self.company_var, *self.fetch_company_names())
        self.company_dropdown.config(font=("times new roman", 12), bg="#ffe3b3")  # Set color to c1
        self.company_dropdown.pack(pady=5)

        Button(scrollable_frame, text="Signup", font=("times new roman", 14), command=self.signup_action, bg="#4f8fc0", fg="white").pack(pady=10)
        Button(scrollable_frame, text="Back", font=("times new roman", 14), command=self.go_back, bg="#26648e", fg="white").pack(pady=10)

    def create_field_row(self, frame, label_text, attribute, show=None, is_numeric=False):
        row_frame = Frame(frame)
        row_frame.pack(pady=5, fill="x")

        label = Label(row_frame, text=label_text, font=("times new roman", 14))
        label.pack(side="left", padx=5)

        entry = Entry(row_frame, font=("times new roman", 14), show=show)
        entry.pack(side="left", padx=5, fill="x", expand=True)
        
        # Store entry widget in an attribute
        setattr(self, f"{attribute}_entry", entry)

    def fetch_company_names(self):
        self.cursor.execute(CompanyDML.getBasicInfoAllCompanies())
        queryResult = self.cursor.fetchall()
        companyToID = {}
        for row in queryResult:
            companyToID[row[1]] = row[0]
        companies = [row[1] for row in queryResult]
        self.companyToID = companyToID
        if companies:
            self.company_var.set(companies[0])  # Set default selection
        return companies

    def signup_action(self):
        # Fetch values from entries
        username = self.username_entry.get()
        password = self.password_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        phone_no = self.phone_no_entry.get()
        street_name = self.street_name_entry.get()
        street_no = self.street_no_entry.get() or None
        city = self.city_entry.get()
        state = self.state_entry.get()
        postal_code = self.postal_code_entry.get()
        country = self.country_entry.get()
        company_name = self.company_var.get()

        # Get company_id from selected company name
        company_id = self.get_company_id(company_name)

        # Generate new customer_id
        self.cursor.execute(CustomerDML.getMaxCustomerIDOfACompany(company_id))
        max_id_result = self.cursor.fetchone()[0]
        customer_id = (max_id_result + 1) if max_id_result else 1

        # Insert into database
        queryToExecute = CustomerDML.insertCustomer(username, password, customer_id, first_name, last_name, email, phone_no, street_name,
             street_no, city, state, postal_code, country, company_id)
        
        print(queryToExecute)
        self.cursor.execute(queryToExecute)
        self.connection.commit()

        self.window.withdraw()
        CustomerMainScreen(self.window, self, customer_id, self.cursor, self.companyToID[company_name])

    def get_company_id(self, company_name):
        return self.companyToID[self.company_var.get()]

    def go_back(self):
        self.window.destroy()
        self.customer_screen.deiconify()
