# gui.py
import tkinter as tk
from tkinter import simpledialog, messagebox
from patient_management import PatientManager
from appointment_management import AppointmentManager
from inventory_management import InventoryManager
from security import hash_password, verify_password

# Dummy user database
user_db = {
    "admin": hash_password("admin123")  # Example username and hashed password
}

class HospitalManagementSystemGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the root window initially
        self.show_login_window()  # Show login window first
        self.root.mainloop()

    def show_login_window(self):
        login_window = tk.Toplevel(self.root)
        login_window.title("Login")
        login_window.geometry("300x200")

        tk.Label(login_window, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(login_window)
        self.username_entry.pack(pady=5)

        tk.Label(login_window, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(login_window, show='*')
        self.password_entry.pack(pady=5)

        tk.Button(login_window, text="Login", command=lambda: self.authenticate(login_window)).pack(pady=20)

    def authenticate(self, login_window):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.check_credentials(username, password):
            login_window.destroy()
            self.show_main_application()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def check_credentials(self, username, password):
        stored_password = user_db.get(username)
        if stored_password:
            return verify_password(stored_password, password)
        return False

    def show_main_application(self):
        self.root.deiconify()  # Show the main application window
        self.root.title("Hospital Management System")
        
        self.patient_manager = PatientManager(self.root, self.create_main_menu)
        self.appointment_manager = AppointmentManager(self.root, self.create_main_menu)
        self.inventory_manager = InventoryManager(self.root, self.create_main_menu)

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()
        tk.Label(self.root, text="Hospital Management System", font=("Helvetica", 16, "bold")).pack(pady=20)
        
        tk.Button(self.root, text="Manage Patients", command=self.manage_patients, bg="lightblue").pack(pady=10)
        tk.Button(self.root, text="Manage Appointments", command=self.manage_appointments, bg="lightgreen").pack(pady=10)
        tk.Button(self.root, text="Manage Inventory", command=self.manage_inventory, bg="lightcoral").pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, bg="lightgrey").pack(pady=10)

    def manage_patients(self):
        self.patient_manager.manage()

    def manage_appointments(self):
        self.appointment_manager.manage()

    def manage_inventory(self):
        self.inventory_manager.manage()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    HospitalManagementSystemGUI()
