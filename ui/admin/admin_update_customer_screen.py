import tkinter as tk

class UpdateCustomer:

    def __init__(self, root):
        self.root = root
        self.root.title("Update Customer Details")

        # Frame for input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Labels and Entries for customer details
        labels = [
            "Username", "Password", "Customer ID", "First Name",
            "Last Name", "Email", "Phone No", "Street Name",
            "Street No", "City", "State", "Postal Code", "Country"
        ]

        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(self.input_frame, text=label, font=("times new roman", 12)).grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(self.input_frame, font=("times new roman", 12))
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[label] = entry

        # Update button
        self.update_button = tk.Button(self.root, text="Update", font=("times new roman", 14), command=self.update_customer)
        self.update_button.pack(pady=10)

    # Function to print entered customer details
    def update_customer(self):
        details = {label: entry.get() for label, entry in self.entries.items()}
        print("Customer Details to Update:")
        for key, value in details.items():
            print(f"{key}: {value}")

if __name__ == '__main__':
    root = tk.Tk()
    app = UpdateCustomer(root)
    root.geometry("400x500")
    root.mainloop()
