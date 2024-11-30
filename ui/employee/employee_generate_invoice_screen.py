import tkinter as tk
from tkinter import Toplevel, Label, Button, ttk, Entry
from reportlab.pdfgen import canvas
from datetime import date
from dml.common_dml import CommonDML
from dml.product_dml import ProductDML
from dml.invoice_dml import InvoiceDML
from dml.invoice_line_items_dml import InvoiceLineItemsDML
from dml.processes_dml import ProcessDML
from dml.company_dml import CompanyDML
from dml.customer_dml import CustomerDML


class GenerateInvoice:
    def __init__(self,employee_menu, root, cursor, selected_company_id, connection, employee_id):
        self.employee_menu = employee_menu
        self.window = Toplevel()
        self.prev_screen = root
        self.cursor = cursor
        self.connection = connection
        self.selected_company_id = selected_company_id
        self.employee_id = employee_id
        print(f"GenerateInvoice: {self.selected_company_id}")
        self.window.title("Generate Invoice")
        # self.window.geometry("600x800")
        self.window.state("zoomed")
        
        Label(self.window, text="Generate Invoice", font=("times new roman", 24, "bold"), fg="black").pack(pady=10)

        # Frame for input fields and Add button
        self.input_frame = tk.Frame(self.window)
        self.input_frame.pack(pady=10)

        Label(self.input_frame, text="Customer ID:", font=("times new roman", 12)).grid(row=0, column=5, padx=5, pady=5)
        self.customer_id_entry = Entry(self.input_frame, font=("times new roman", 12))
        self.customer_id_entry.grid(row=0, column=6, padx=5, pady=5)

        # Product ID field
        Label(self.input_frame, text="Product ID:", font=("times new roman", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.product_id_entry = Entry(self.input_frame, font=("times new roman", 12), state="readonly")
        self.product_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Quantity field
        Label(self.input_frame, text="Quantity:", font=("times new roman", 12)).grid(row=0, column=2, padx=5, pady=5)
        self.quantity_entry = Entry(self.input_frame, font=("times new roman", 12))
        self.quantity_entry.grid(row=0, column=3, padx=5, pady=5)

        # Add button
        self.add_button = Button(self.input_frame, text="Add", font=("times new roman", 12), command=self.add_item, bg="#53d2dc", fg="white")
        self.add_button.grid(row=0, column=4, padx=10, pady=5)

        # Frame for the product table
        self.table_frame = tk.Frame(self.window)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create the product table (Treeview)
        self.treeview = ttk.Treeview(
            self.table_frame,
            columns=("product_id", "item_name", "brand_name", "product_price", "product_quantity"),
            show="headings",
        )
        self.treeview.pack(fill="both", expand=True)

        # Set up the product table headers
        headers = {
            "product_id": "Product ID",
            "item_name": "Item Name",
            "brand_name": "Brand Name",
            "product_price": "Product Price",
            "product_quantity": "Quantity Remaining",
        }
        for col, text in headers.items():
            self.treeview.heading(col, text=text)
            self.treeview.column(col, width=120, anchor="center")

        # Bind the row selection event
        self.treeview.bind("<ButtonRelease-1>", self.on_row_select)

        # Load data into the product table
        self.load_products()

        # Frame for the billed items table
        self.billed_table_frame = tk.Frame(self.window)
        self.billed_table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create the billed items table
        self.billed_treeview = ttk.Treeview(
            self.billed_table_frame,
            columns=("serial", "item_name", "unit_price", "quantity_bought", "price"),
            show="headings",
        )
        self.billed_treeview.pack(fill="both", expand=True)

        # Set up the billed items table headers
        billed_headers = {
            "serial": "Serial Number",
            "item_name": "Item Name",
            "unit_price": "Unit Price",
            "quantity_bought": "Quantity Bought",
            "price": "Price",
        }
        for col, text in billed_headers.items():
            self.billed_treeview.heading(col, text=text)
            self.billed_treeview.column(col, width=120, anchor="center")

        # Add Delete Added Item button
        Button(self.window, text="Delete Added Item", font=("times new roman", 12), command=self.delete_item, bg="#53d2dc", fg="white").pack(pady=10)

        Button(self.window, text="Generate Invoice", font=("times new roman", 14), command=self.generate_invoice, bg="#4f8fc0", fg="white").pack(pady=10)

        # Add Back button
        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back, bg="#26648e", fg="white").pack(pady=10)

        # Serial number for billed items
        self.serial_number = 1

    def load_products(self):
        # Clear any existing data in the table
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Fetch data from the database
        # query = f"SELECT p.product_id, p.item_name, b.brand_name, p.product_price, p.product_quantity FROM product AS p NATURAL JOIN brand AS b WHERE p.company_id = {self.selected_company_id} and p.product_quantity != 0;"
        query = CommonDML.getProductsOfACompany(self.selected_company_id)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        # Populate the table with fetched data
        for row in rows:
            self.treeview.insert("", "end", values=row)

    def on_row_select(self, event):
        # Get the selected row
        selected_item = self.treeview.selection()
        if selected_item:
            selected_data = self.treeview.item(selected_item[0], "values")
            # Populate the Product ID field
            self.product_id_entry.config(state="normal")
            self.product_id_entry.delete(0, tk.END)
            self.product_id_entry.insert(0, selected_data[0])  # Product ID
            self.product_id_entry.config(state="readonly")

    def add_item(self):
        product_id = self.product_id_entry.get()
        quantity_text = self.quantity_entry.get()

        if not product_id or not quantity_text:
            print("Error: Both fields must be filled.")
            return

        try:
            quantity = int(quantity_text)
        except ValueError:
            print("Error: Quantity must be a number.")
            return

        selected_item = self.treeview.selection()
        if not selected_item:
            print("Error: No row selected.")
            return

        selected_data = self.treeview.item(selected_item[0], "values")
        remaining_quantity = int(selected_data[4])  # Quantity Remaining
        item_name = selected_data[1]  # Item Name
        unit_price = float(selected_data[3])  # Unit Price

        if quantity > remaining_quantity:
            print("Error: Entered quantity exceeds remaining quantity.")
        else:
            # total_price = unit_price * quantity
            total_price = round(unit_price * quantity, 2)


            # Insert into the billed items table
            self.billed_treeview.insert(
                "", "end",
                values=(self.serial_number, item_name, unit_price, quantity, total_price),
            )
            self.serial_number += 1

            # Update the product quantity in the database and the product table
            new_quantity = remaining_quantity - quantity
            self.cursor.execute(ProductDML.updateProductQuantityOfACompany(self.selected_company_id, product_id, new_quantity))
            self.connection.commit()
            self.load_products()

            # Clear the fields
            self.product_id_entry.config(state="normal")
            self.product_id_entry.delete(0, tk.END)
            self.product_id_entry.config(state="readonly")
            self.quantity_entry.delete(0, tk.END)

    def delete_item(self):
        selected_item = self.billed_treeview.selection()
        if not selected_item:
            print("Error: No row selected in billed items table.")
            return

        selected_data = self.billed_treeview.item(selected_item[0], "values")
        serial, item_name, unit_price, quantity_bought, price = selected_data

        # Update the product quantity in the database and product table
        product_id = self.get_product_id(item_name)
        if product_id:
            self.cursor.execute(ProductDML.getQuantityOfAProductOfACompany(self.selected_company_id, product_id))
            old_qty = self.cursor.fetchone()[0]
            self.cursor.execute(ProductDML.updateProductQuantityOfACompany(self.selected_company_id, product_id, old_qty + quantity_bought))
            # self.cursor.execute(f"UPDATE product SET product_quantity = product_quantity + {quantity_bought} WHERE product_id = {product_id} AND company_id = {self.selected_company_id};")
            self.connection.commit()
            self.load_products()

        # Delete the item from the billed items table
        self.billed_treeview.delete(selected_item[0])

    def get_product_id(self, item_name):
        self.cursor.execute(ProductDML.getProductIDOfACompanyProduct(self.selected_company_id, item_name))
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def getNewInvoiceID(self):
        self.cursor.execute(InvoiceDML.getMaxInvoiceID())
        max_id_result = self.cursor.fetchone()[0]
        # newInvoiceID = (max_id_result + 1) if max_id_result else 1
        return max_id_result
    
    def insertInvoiceItems(self, customer_id, billed_items):
        invoice_total = 0
        for item in billed_items:
            invoice_total += int(float(item[4]))
        todaysDate = date.today().strftime("%Y-%m-%d")
        # queryInsertIntoInvoice = f"INSERT INTO Invoice (invoice_date, invoice_total_amount) VALUES (\"{todaysDate}\", {invoice_total});"
        queryInsertIntoInvoice = InvoiceDML.insertNewInvoice(todaysDate, invoice_total)
        self.cursor.execute(queryInsertIntoInvoice)
        self.connection.commit()
        
        newInvoiceID = self.getNewInvoiceID()
        for item in billed_items:
            # queryGetProductID = f"SELECT product_id FROM Product WHERE company_id = {self.selected_company_id} AND item_name = \"{item[1]}\";"
            queryGetProductID = ProductDML.getProductIDOfACompanyProduct(self.selected_company_id, item[1])
            self.cursor.execute(queryGetProductID)
            product_id = self.cursor.fetchone()[0]
            print(f"INVOICE ID: {newInvoiceID}")
            # queryInsertIntoInvoiceLineItems = f"INSERT INTO Invoice_line_items (invoice_item_id, invoice_item_quantity, company_id, invoice_id, product_id) VALUES ({item[0]}, {item[3]}, {self.selected_company_id}, {newInvoiceID}, {product_id});"
            queryInsertIntoInvoiceLineItems = InvoiceLineItemsDML.insertNewInvoiceLineItem(item[0], item[3], self.selected_company_id, newInvoiceID, product_id)
            self.cursor.execute(queryInsertIntoInvoiceLineItems)
            self.connection.commit()

        # queryInsertIntoProcesses = f"INSERT INTO Processes (company_id, customer_id, employee_id, invoice_id) VALUES ({self.selected_company_id}, {customer_id}, {self.employee_id}, {newInvoiceID});"
        queryInsertIntoProcesses = ProcessDML.insertNewProcess(self.selected_company_id, customer_id, self.employee_id, newInvoiceID)
        self.cursor.execute(queryInsertIntoProcesses)
        self.connection.commit()

 
    
    def generate_invoice(self):
        customer_id = self.customer_id_entry.get()
        if not customer_id:
            print("Error: Customer ID is required.")
            return

        # Prepare the list of items for the invoice
        billed_items = []
        for item in self.billed_treeview.get_children():
            row = self.billed_treeview.item(item, "values")
            serial, item_name, unit_price, quantity_bought, price = row
            billed_items.append([serial, item_name, unit_price, quantity_bought, price])

        self.insertInvoiceItems(customer_id, billed_items)

        # Fetch necessary company details from the database
        # query = f"SELECT company_name, company_street_name, company_city, company_phone_no FROM company WHERE company_id = {self.selected_company_id};"
        query = CompanyDML.getCompanyInfoForBilling(self.selected_company_id)
        self.cursor.execute(query)
        company_details = self.cursor.fetchone()

        company_name, address, city, contact_number = company_details
        print(f"Customer ID: {customer_id}")
        print(billed_items)

        # Generate and open the invoice PDF
        self.generate_invoice_pdf(billed_items, company_name, address, city, contact_number, customer_id)


    def generate_invoice_pdf(self, billed_items, company_name, address, city, contact_number, customer_id):
        # Generate a random invoice number within the specified range
        generated_invoice_no = self.getNewInvoiceID()
        # generated_invoice_no = random.randint(1000000, 9999999)

        # Insert company and customer values into their corresponding tables and commit changes
        # mycursor.execute(f'INSERT INTO company VALUES({generated_invoice_no}, "{self.company_name}", "{self.address}", "{self.city}", {self.compno}, "{self.file_name}");')
        # db.commit()

        # Format the date
        # tempDate = self.date
        # dateList = tempDate.split("/")
        # tempDate = dateList[2] + "-" + dateList[1] + "-" + dateList[0]

        # mycursor.execute(f'INSERT INTO customer VALUES({generated_invoice_no}, "{self.c_name}", {self.contact}, "{tempDate}");')
        # db.commit()

        # Define positions for the table
        HEIGHT = 130
        WIDTH = [25, 75, 125, 148, 173]

        # Create a canvas with a custom name and custom size
        c = canvas.Canvas(f'{self.selected_company_id}_{customer_id}_invoice{generated_invoice_no}.pdf', pagesize=(200, 250), bottomup=0)

        # Set font color for the entire PDF
        c.setFillColorRGB(0, 0, 0)

        # Draw horizontal lines
        c.line(5, 45, 195, 45)
        c.line(15, 120, 185, 120)

        # Set font style and size
        c.setFont("Times-Bold", 5)

        # Iterate over the main list and put item details at their respective positions
        for i in range(len(billed_items)):
            for j in range(len(billed_items[0])):
                c.drawCentredString(WIDTH[j], HEIGHT, str(billed_items[i][j]))
            # mycursor.execute(f'INSERT INTO purchase VALUES({generated_invoice_no}, "{self.lst[i][1]}", {self.lst[i][2]}, {self.lst[i][3]});')
            # db.commit()
            HEIGHT = HEIGHT + 10

        # Draw vertical lines for the bill layout
        c.line(35, 108, 35, 210)
        c.line(110, 108, 110, 210)
        c.line(140, 108, 140, 210)
        c.line(160, 108, 160, 210)

        # Draw horizontal lines
        c.line(15, 220, 185, 220)
        c.line(15, 210, 185, 210)

        # Calculate subtotal
        subtotal = sum(float(x[4]) for x in billed_items)
        c.drawCentredString(148, 218, "Subtotal: ")
        c.drawCentredString(173, 218, str(round(subtotal, 2)))

        # Draw company logo and details
        # c.translate(10, 40)
        # c.scale(1, -1)
        # c.drawImage(f'{self.file_name}', 0, 0, width=50, height=30)
        # c.scale(1, -1)
        # c.translate(-10, -40)

        # Draw company name, address, and contact info
        c.setFont("Times-Bold", 10)
        c.drawRightString(180, 20, company_name)

        c.setFont("Times-Bold", 5)
        c.drawRightString(180, 25, address)

        c.drawRightString(180, 30, city)

        c.setFont("Times-Bold", 6)
        c.drawRightString(180, 35, f"Ph: {contact_number}")

        # Add invoice title
        c.setFont("Times-Bold", 8)
        c.drawCentredString(100, 55, "INVOICE")

        # queryGetCustomerInfo = f"SELECT customer_first_name, customer_last_name FROM Customer WHERE customer_id = {customer_id} AND company_id = {self.selected_company_id};"
        queryGetCustomerInfo = CustomerDML.getCustomerInfoForBilling(self.selected_company_id, customer_id)
        self.cursor.execute(queryGetCustomerInfo)
        customer_info = self.cursor.fetchone()
        customer_first_name, customer_last_name = customer_info

        # Add invoice details
        c.setFont("Times-Bold", 5)
        c.drawRightString(70, 70, "Invoice No. :")
        c.drawRightString(100, 70, f"{generated_invoice_no}")
        c.drawRightString(70, 80, "Date :")
        c.drawRightString(100, 80, date.today().strftime("%Y-%m-%d"))
        c.drawRightString(70, 90, "Customer ID :")
        c.drawRightString(100, 90, customer_id)
        c.drawRightString(70, 100, "Customer Name :")
        c.drawRightString(100, 100, f"{customer_first_name} {customer_last_name}")

        # Draw item table header
        c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)
        c.drawCentredString(25, 118, "S.No.")
        c.drawCentredString(75, 118, "Item")
        c.drawCentredString(125, 118, "Unit Price")
        c.drawCentredString(148, 118, "Qty.")
        c.drawCentredString(173, 118, "Total")

        # Footer message
        c.drawString(30, 230, "This is a system-generated invoice and does not require a signature.")

        # Save the generated PDF
        c.showPage()
        c.save()

        # Open the generated invoice PDF
        import os
        os.startfile(f'{self.selected_company_id}_{customer_id}_invoice{generated_invoice_no}.pdf')

    def go_back(self):
        self.window.destroy()
        self.prev_screen.deiconify()
