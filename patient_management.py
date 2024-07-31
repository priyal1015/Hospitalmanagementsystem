import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from data_structures import Patient, BinarySearchTree

class PatientManager:
    def __init__(self, root=None, home_callback=None):
        self.root = root
        self.patients_tree = BinarySearchTree()
        self.home_callback = home_callback

    def add_patient(self):
        patient_id = simpledialog.askstring("Input", "Enter Patient ID:", parent=self.root)
        name = simpledialog.askstring("Input", "Enter Patient Name:", parent=self.root)
        age = simpledialog.askinteger("Input", "Enter Patient Age:", parent=self.root)
        gender = simpledialog.askstring("Input", "Enter Patient Gender:", parent=self.root)
        contact = simpledialog.askstring("Input", "Enter Patient Contact:", parent=self.root)
        
        if not all([patient_id, name, age, gender, contact]):
            messagebox.showwarning("Warning", "All fields must be filled.", parent=self.root)
            return
        
        patient = Patient(patient_id, name, age, gender, contact)
        self.patients_tree.insert(patient_id, patient)
        messagebox.showinfo("Success", "Patient added successfully.", parent=self.root)

    def view_patient(self):
        patient_id = simpledialog.askstring("Input", "Enter Patient ID to search:", parent=self.root)
        patient = self.patients_tree.search(patient_id)
        if patient:
            patient_info = (f"ID: {patient.patient_id}, Name: {patient.name}, "
                            f"Age: {patient.age}, Gender: {patient.gender}, Contact: {patient.contact}")
            messagebox.showinfo("Patient Information", patient_info, parent=self.root)
        else:
            messagebox.showerror("Error", "Patient not found.", parent=self.root)

    def delete_patient(self):
        patient_id = simpledialog.askstring("Input", "Enter Patient ID to delete:", parent=self.root)
        self.patients_tree.delete(patient_id)
        messagebox.showinfo("Success", "Patient deleted successfully.", parent=self.root)

    def update_patient(self):
        patient_id = simpledialog.askstring("Input", "Enter Patient ID to update:", parent=self.root)
        patient = self.patients_tree.search(patient_id)
        if patient:
            name = simpledialog.askstring("Input", "Enter new Patient Name:", initialvalue=patient.name, parent=self.root)
            age = simpledialog.askinteger("Input", "Enter new Patient Age:", initialvalue=patient.age, parent=self.root)
            gender = simpledialog.askstring("Input", "Enter new Patient Gender:", initialvalue=patient.gender, parent=self.root)
            contact = simpledialog.askstring("Input", "Enter new Patient Contact:", initialvalue=patient.contact, parent=self.root)
            
            if not all([name, age, gender, contact]):
                messagebox.showwarning("Warning", "All fields must be filled.", parent=self.root)
                return
            
            updated_patient = Patient(patient_id, name, age, gender, contact)
            self.patients_tree.insert(patient_id, updated_patient)  # Update patient in BST
            messagebox.showinfo("Success", "Patient updated successfully.", parent=self.root)
        else:
            messagebox.showerror("Error", "Patient not found.", parent=self.root)

    def display_patients_table(self):
        self.clear_frame()
        tk.Label(self.root, text="Patient Records", font=("Helvetica", 14, "bold")).pack(pady=20)

        tree = ttk.Treeview(self.root, columns=("ID", "Name", "Age", "Gender", "Contact"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Age", text="Age")
        tree.heading("Gender", text="Gender")
        tree.heading("Contact", text="Contact")
        
        for key, patient in self.patients_tree.get_all_items():
            tree.insert("", "end", values=(patient.patient_id, patient.name, patient.age, patient.gender, patient.contact))
        
        tree.pack(pady=10)
        tk.Button(self.root, text="Back to Manage Patients", command=self.manage, bg="lightgrey").pack(pady=10)
        tk.Button(self.root, text="Home", command=self.home_callback, bg="lightgrey").pack(pady=10)

    def manage(self):
        self.clear_frame()
        tk.Label(self.root, text="Manage Patients", font=("Helvetica", 16, "bold")).pack(pady=20)
        
        tk.Button(self.root, text="Add Patient", command=self.add_patient, bg="lightgreen").pack(pady=10)
        tk.Button(self.root, text="View Patient", command=self.view_patient, bg="lightblue").pack(pady=10)
        tk.Button(self.root, text="Delete Patient", command=self.delete_patient, bg="lightcoral").pack(pady=10)
        tk.Button(self.root, text="Update Patient", command=self.update_patient, bg="lightyellow").pack(pady=10)
        tk.Button(self.root, text="Display All Patients", command=self.display_patients_table, bg="lightpink").pack(pady=10)
        tk.Button(self.root, text="Home", command=self.home_callback, bg="lightgrey").pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
