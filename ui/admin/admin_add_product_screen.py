import tkinter as tk
from tkinter import ttk

class AddProduct:

    def __init__(self, root, data):
        self.root = root
        self.root.title("Data Table")

        # Frame for entry and label
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=5)

        # Entry for ID input
        tk.Label(self.input_frame, text="Enter ID:", font=("times new roman", 14)).grid(row=0, column=0, padx=5)
        self.id_entry = tk.Entry(self.input_frame, font=("times new roman", 14))
        self.id_entry.grid(row=0, column=1, padx=5)

        # Define the Treeview widget
        self.tree = ttk.Treeview(self.root, show="headings")

        # Define columns
        columns = tuple(data[0].keys())
        self.tree["columns"] = columns

        # Set column headings and column width
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        # Insert data into the table
        for row in data:
            self.tree.insert("", "end", values=tuple(row.values()))

        # Calculate the required width and height
        num_rows = len(data)
        num_columns = len(columns)
        row_height = 20  # Approximate row height in pixels
        column_width = 100  # Same width as specified in column setup

        table_width = num_columns * column_width
        table_height = min(num_rows * row_height + 30, 300)  # Set a max height

        # Adjust the window size to fit the table
        self.tree.pack(expand=True, fill="both")
        self.root.geometry(f"{table_width}x{table_height + 80}")

        # "Add" button below the table
        self.add_button = tk.Button(self.root, text="Add", font=("times new roman", 14), command=self.add_item)
        self.add_button.pack(pady=10)

    def add_item(self):
        entered_id = self.id_entry.get()
        print(f"ID Entered: {entered_id}")

# Sample data
data = [
    {"ID": 1, "Name": "Alice", "Age": 24},
    {"ID": 2, "Name": "Bob", "Age": 30},
    {"ID": 3, "Name": "Charlie", "Age": 22},
]

if __name__  == '__main__':

    root = tk.Tk()
    app = AddProduct(root, data)
    root.geometry("400x300")
    root.mainloop()