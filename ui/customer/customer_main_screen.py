import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry
from tkinter import ttk
import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry
from reportlab.pdfgen import canvas
from datetime import date
from dml.common_dml import CommonDML
from dml.company_dml import CompanyDML
from dml.customer_dml import CustomerDML
from dml.processes_dml import ProcessDML

class CustomerMainScreen:

    def __init__(self, root, login_screen, customer_id, cursor,selected_company):
        self.login_screen = login_screen
        self.customer_id = customer_id
        self.selected_company = selected_company
        self.cursor = cursor
        self.window = Toplevel(root)
        self.window.title("Customer Main Screen")
        self.window.geometry("600x400")

        Label(self.window, text="Customer Main Screen", font=("times new roman", 24, "bold")).pack(pady=10)
        
        Label(self.window, text="Enter Invoice ID:", font=("times new roman", 14)).pack(pady=5)
        self.invoice_entry = Entry(self.window, font=("times new roman", 14), state="readonly")
        self.invoice_entry.pack(pady=5)

        Button(self.window, text="Submit", font=("times new roman", 14), command=self.print_invoice_id, bg="#4f8fc0", fg="white").pack(pady=10)

        # Back button
        Button(self.window, text="Back", font=("times new roman", 14), command=self.go_back, bg="#26648e", fg="white").pack(pady=10)

        # Table for displaying invoice data
        self.invoice_table = ttk.Treeview(self.window, columns=("invoice_id", "invoice_date"), show="headings")
        self.invoice_table.heading("invoice_id", text="Invoice ID")
        self.invoice_table.heading("invoice_date", text="Invoice Date")
        self.invoice_table.pack(pady=10)

        self.populate_table()

        # Bind the row selection event
        self.invoice_table.bind("<<TreeviewSelect>>", self.on_row_select)

    def populate_table(self):
        self.cursor.callproc('GetInvoicesOfACustomerOfACompany', (self.selected_company, self.customer_id))
        for results in self.cursor.stored_results():
            rows = results.fetchall()
        # Insert data into the table
            for row in rows:
                self.invoice_table.insert("", "end", values=row)

    def on_row_select(self, event):
        selected_item = self.invoice_table.selection()
        if selected_item:
            invoice_data = self.invoice_table.item(selected_item[0], "values")
            invoice_id = invoice_data[0]  # Get the invoice ID from the selected row
            self.invoice_entry.config(state="normal")
            self.invoice_entry.delete(0, tk.END)
            self.invoice_entry.insert(0, invoice_id)
            self.invoice_entry.config(state="readonly")

    def print_invoice_id(self):
        invoice_id = self.invoice_entry.get()
        
        if not invoice_id:
            tk.messagebox.showerror("Error", "No invoice id selected!")
            return

        self.invoice_entry.config(state="normal")
        self.invoice_entry.delete(0, tk.END)
        self.invoice_entry.config(state="readonly")
        self.generate_invoice(invoice_id)

    def generate_invoice(self, invoice_id):
        queryGetInvoiceItems = CommonDML.getInvoiceItems(invoice_id)
        self.cursor.execute(queryGetInvoiceItems)
        result = self.cursor.fetchall()

        billed_items = []
        for item in result:
            serial, item_name, unit_price, quantity_bought, price = item
            billed_items.append([serial, item_name, unit_price, quantity_bought, price])

        query = CompanyDML.getCompanyInfoForBilling(self.selected_company)
        self.cursor.execute(query)
        company_details = self.cursor.fetchone()
        company_name, address, city, contact_number = company_details
        queryGetCustomerID = ProcessDML.getCustomerIdOfAnInvoice(invoice_id)
        self.cursor.execute(queryGetCustomerID)
        customer_id = self.cursor.fetchone()[0]
        customer_id = str(customer_id)

        # Generate and open the invoice PDF
        self.generate_invoice_pdf(billed_items, company_name, address, city, contact_number, customer_id, invoice_id)

    def generate_invoice_pdf(self, billed_items, company_name, address, city, contact_number, customer_id, invoice_id):
        generated_invoice_no = invoice_id

        # Define positions for the table
        HEIGHT = 130
        WIDTH = [25, 75, 125, 148, 173]

        # Create a canvas with a custom name and custom size
        c = canvas.Canvas(f'{self.selected_company}_{customer_id}_invoice{generated_invoice_no}.pdf', pagesize=(200, 250), bottomup=0)

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

        queryGetCustomerInfo = CustomerDML.getCustomerInfoForBilling(self.selected_company, customer_id)
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
        os.startfile(f'{self.selected_company}_{customer_id}_invoice{generated_invoice_no}.pdf')

    def go_back(self):
        self.window.destroy()
        self.login_screen.window.deiconify()