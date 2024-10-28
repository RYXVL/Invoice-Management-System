import tkinter as tk

class UpdateCompany:

    def __init__(self, root):
        self.root = root
        self.root.title("Update Company Details")

        # Frame for input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Labels and Entries for company details
        labels = [
            "Company ID", "Name", "Street Name", "Street No",
            "City", "State", "Postal Code", "Country",
            "Email", "Phone No"
        ]

        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(self.input_frame, text=label, font=("times new roman", 12)).grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(self.input_frame, font=("times new roman", 12))
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[label] = entry

        # Update button
        self.update_button = tk.Button(self.root, text="Update", font=("times new roman", 14), command=self.update_company)
        self.update_button.pack(pady=10)

    # Function to print entered company details
    def update_company(self):
        details = {label: entry.get() for label, entry in self.entries.items()}
        print("Company Details to Update:")
        for key, value in details.items():
            print(f"{key}: {value}")

if __name__ == '__main__':
    root = tk.Tk()
    app = UpdateCompany(root)
    root.geometry("400x400")
    root.mainloop()
