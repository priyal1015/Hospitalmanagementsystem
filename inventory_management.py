import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from data_structures import InventoryItem, HashTable

class InventoryManager:
    def __init__(self, root=None, home_callback=None):
        self.root = root
        self.inventory_table = HashTable()
        self.home_callback = home_callback

    def add_inventory_item(self):
        item_id = simpledialog.askstring("Input", "Enter Item ID:", parent=self.root)
        name = simpledialog.askstring("Input", "Enter Item Name:", parent=self.root)
        quantity = simpledialog.askinteger("Input", "Enter Item Quantity:", parent=self.root)
        supplier = simpledialog.askstring("Input", "Enter Supplier:", parent=self.root)
        
        if not all([item_id, name, quantity, supplier]):
            messagebox.showwarning("Warning", "All fields must be filled.", parent=self.root)
            return

        item = InventoryItem(item_id, name, quantity, supplier)
        self.inventory_table.insert(item_id, item)
        messagebox.showinfo("Success", "Inventory item added successfully.", parent=self.root)

    def view_inventory(self):
        self.clear_frame()
        tk.Label(self.root, text="Inventory Records", font=("Helvetica", 14, "bold")).pack(pady=20)

        tree = ttk.Treeview(self.root, columns=("ID", "Name", "Quantity", "Supplier"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Supplier", text="Supplier")
        
        for item_id, item in self.inventory_table.get_all_items():
            tree.insert("", "end", values=(item.item_id, item.name, item.quantity, item.supplier))
        
        tree.pack(pady=10)
        tk.Button(self.root, text="Back to Manage Inventory", command=self.manage, bg="lightgrey").pack(pady=10)
        tk.Button(self.root, text="Home", command=self.home_callback, bg="lightgrey").pack(pady=10)

    def manage(self):
        self.clear_frame()
        tk.Label(self.root, text="Manage Inventory", font=("Helvetica", 16, "bold")).pack(pady=20)
        
        tk.Button(self.root, text="Add Inventory Item", command=self.add_inventory_item, bg="lightcoral").pack(pady=10)
        tk.Button(self.root, text="View Inventory", command=self.view_inventory, bg="lightblue").pack(pady=10)
        tk.Button(self.root, text="Home", command=self.home_callback, bg="lightgrey").pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
