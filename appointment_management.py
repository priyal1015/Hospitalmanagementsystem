import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from data_structures import Appointment
import heapq

class AppointmentManager:
    def __init__(self, root=None, home_callback=None):
        self.root = root
        self.appointments = []
        self.home_callback = home_callback

    def add_appointment(self):
        appointment_id = simpledialog.askstring("Input", "Enter Appointment ID:", parent=self.root)
        patient_id = simpledialog.askstring("Input", "Enter Patient ID:", parent=self.root)
        doctor_id = simpledialog.askstring("Input", "Enter Doctor ID:", parent=self.root)
        date = simpledialog.askstring("Input", "Enter Date (YYYY-MM-DD):", parent=self.root)
        time = simpledialog.askstring("Input", "Enter Time (HH:MM):", parent=self.root)
        
        if not all([appointment_id, patient_id, doctor_id, date, time]):
            messagebox.showwarning("Warning", "All fields must be filled.", parent=self.root)
            return
        
        appointment = Appointment(appointment_id, patient_id, doctor_id, date, time)
        heapq.heappush(self.appointments, (date, time, appointment))
        messagebox.showinfo("Success", "Appointment added successfully.", parent=self.root)

    def view_appointments(self):
        self.clear_frame()
        tk.Label(self.root, text="Appointment Records", font=("Helvetica", 14, "bold")).pack(pady=20)

        tree = ttk.Treeview(self.root, columns=("ID", "Patient ID", "Doctor ID", "Date", "Time"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Patient ID", text="Patient ID")
        tree.heading("Doctor ID", text="Doctor ID")
        tree.heading("Date", text="Date")
        tree.heading("Time", text="Time")
        
        for date, time, appointment in self.appointments:
            tree.insert("", "end", values=(appointment.appointment_id, appointment.patient_id, appointment.doctor_id, date, time))
        
        tree.pack(pady=10)
        tk.Button(self.root, text="Back to Manage Appointments", command=self.manage, bg="lightgrey").pack(pady=10)
        tk.Button(self.root, text="Home", command=self.home_callback, bg="lightgrey").pack(pady=10)

    def manage(self):
        self.clear_frame()
        tk.Label(self.root, text="Manage Appointments", font=("Helvetica", 16, "bold")).pack(pady=20)
        
        tk.Button(self.root, text="Add Appointment", command=self.add_appointment, bg="lightgreen").pack(pady=10)
        tk.Button(self.root, text="View Appointments", command=self.view_appointments, bg="lightblue").pack(pady=10)
        tk.Button(self.root, text="Home", command=self.home_callback, bg="lightgrey").pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
