import tkinter as tk
import tkinter as tk
from tkinter import Toplevel, Label, Button, StringVar, OptionMenu, Entry
from tkinter import Toplevel, Label, Button, StringVar, OptionMenu
from tkinter import Toplevel, Label, Button, StringVar, OptionMenu, Entry, Canvas, Frame, Scrollbar
from ui.customer.customer_main_screen import CustomerMainScreen
from dml.customer_dml import CustomerDML

# class CustomerSignupScreen:
#     def __init__(self, customer_screen, cursor):
#         self.customer_screen = customer_screen
#         self.window = Toplevel()
#         self.cursor = cursor
#         self.window.title("Customer Signup")
#         self.window.geometry("400x400")
        
#         Label(self.window, text="Signup", font=("times new roman", 24, "bold")).pack(pady=10)
        
#         Label(self.window, text="Username:", font=("times new roman", 14)).pack(pady=5)
#         self.username_entry = tk.Entry(self.window, font=("times new roman", 14))
#         self.username_entry.pack(pady=5)

#         Label(self.window, text="Password:", font=("times new roman", 14)).pack(pady=5)
#         self.password_entry = tk.Entry(self.window, font=("times new roman", 14), show="*")
#         self.password_entry.pack(pady=5)

#         Label(self.window, text="Select Company:", font=("times new roman", 14)).pack(pady=5)
#         self.company_var = StringVar()
#         self.company_dropdown = OptionMenu(self.window, self.company_var, *self.fetch_company_names())
#         self.company_dropdown.config(font=("times new roman", 12))
#         self.company_dropdown.pack(pady=5)

#         Button(self.window, text="Signup", font=("times new roman", 14), command=self.signup_action).pack(pady=10)
#         Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

#     def fetch_company_names(self):
#         self.cursor.execute("SELECT company_id, company_name FROM Company")
#         queryResult = self.cursor.fetchall()
#         print(queryResult)
#         companyToID = {}
#         for row in queryResult:
#             companyToID[row[1]] = row[0]
#         companies = [row[1] for row in queryResult]
#         self.companyToID = companyToID
#         if companies:
#             self.company_var.set(companies[0])  # Set default selection
#         return companies

#     def signup_action(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#         selected_company = self.company_var.get()
#         print(f"Signup Username: {username}")
#         print(f"Signup Password: {password}")
#         print(f"Selected Company: {selected_company}")

#     def go_back(self):
#         self.window.destroy()
#         self.customer_screen.deiconify()

class CustomerSignupScreen:
    def __init__(self, customer_screen, cursor, connection):
        self.customer_screen = customer_screen
        self.cursor = cursor
        self.connection = connection
        self.window = Toplevel()
        self.window.title("Customer Signup")
        self.window.geometry("400x600")

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

        Label(scrollable_frame, text="Enter Username:", font=("times new roman", 14)).pack(pady=5)
        self.username_entry = Entry(scrollable_frame, font=("times new roman", 14))
        self.username_entry.pack(pady=5)

        Label(scrollable_frame, text="Enter Password:", font=("times new roman", 14)).pack(pady=5)
        self.password_entry = Entry(scrollable_frame, font=("times new roman", 14), show="*")
        self.password_entry.pack(pady=5)

        # Additional fields
        self.create_field(scrollable_frame, "First Name:", "first_name")
        self.create_field(scrollable_frame, "Last Name:", "last_name")
        self.create_field(scrollable_frame, "Email:", "email")
        self.create_field(scrollable_frame, "Phone No:", "phone_no")
        self.create_field(scrollable_frame, "Street Name:", "street_name")
        self.create_field(scrollable_frame, "Street No:", "street_no", is_numeric=True)
        self.create_field(scrollable_frame, "City:", "city")
        self.create_field(scrollable_frame, "State:", "state")
        self.create_field(scrollable_frame, "Postal Code:", "postal_code", is_numeric=True)
        self.create_field(scrollable_frame, "Country:", "country")

        Label(scrollable_frame, text="Select Company:", font=("times new roman", 14)).pack(pady=5)
        self.company_var = StringVar()
        self.company_dropdown = OptionMenu(scrollable_frame, self.company_var, *self.fetch_company_names())
        self.company_dropdown.config(font=("times new roman", 12))
        self.company_dropdown.pack(pady=5)

        Button(scrollable_frame, text="Signup", font=("times new roman", 14), command=self.signup_action).pack(pady=10)
        Button(scrollable_frame, text="Back", font=("times new roman", 14), command=self.go_back).pack(pady=10)

    def create_field(self, frame, label_text, attribute, is_numeric=False):
        Label(frame, text=label_text, font=("times new roman", 14)).pack(pady=5)
        entry = Entry(frame, font=("times new roman", 14))
        entry.pack(pady=5)
        setattr(self, f"{attribute}_entry", entry)  # Store entry widget in an attribute

    def fetch_company_names(self):
        self.cursor.execute("SELECT company_id, company_name FROM Company")
        queryResult = self.cursor.fetchall()
        print(queryResult)
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
        self.cursor.execute(f"SELECT MAX(customer_id) FROM Customer WHERE company_id = {company_id}")
        max_id_result = self.cursor.fetchone()[0]
        customer_id = (max_id_result + 1) if max_id_result else 1

        # Print values for debugging
        # print(f"Username: {username}, Password: {password}, First Name: {first_name}, Last Name: {last_name}, "
        #       f"Email: {email}, Phone No: {phone_no}, Street Name: {street_name}, Street No: {street_no}, "
        #       f"City: {city}, State: {state}, Postal Code: {postal_code}, Country: {country}, "
        #       f"Company ID: {company_id}, Customer ID: {customer_id}")


        queryToExecute = CustomerDML.insertCustomer(username, password, customer_id, first_name, last_name, email, phone_no, street_name,
             street_no, city, state, postal_code, country, company_id)
        
        print(queryToExecute)
        # Insert into database
        self.cursor.execute(queryToExecute)
        self.connection.commit()
        # self.cursor.connection.commit()

        self.window.withdraw()
        CustomerMainScreen(self.window, self,customer_id,self.cursor,self.companyToID[company_name])

    def get_company_id(self, company_name):
        return self.companyToID[self.company_var.get()]

    def go_back(self):
        self.window.destroy()
        self.customer_screen.deiconify()