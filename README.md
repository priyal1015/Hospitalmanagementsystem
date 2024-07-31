Overview
This project is a Hospital Management System designed to manage patient records, doctor appointments, and medical inventory. It uses various data structures and algorithms to ensure efficient data handling and retrieval.

Features
1.Patient Management: Add, view, delete, update, and list patient records.
2.Appointment Management: Schedule, view, and manage doctor appointments.
3.Inventory Management: Add, view, and manage medical inventory items.

Technologies Used
1.Python: Core programming language.
2.Tkinter: For the graphical user interface (GUI).
3.Data Structures: Binary Search Tree (BST) for patient records and Hash Table for inventory management.
4.Scheduling Algorithms: Used for managing doctor appointments.
5.Security: Password hashing for secure authentication.

Project Structure
1.main.py: Entry point of the application. Initializes the GUI.
2.gui.py: Contains the main GUI components and navigation logic.
3.patient_management.py: Manages patient-related operations and GUI interactions.
4.appointment_management.py: Handles appointment-related operations and GUI interactions.
5.inventory_management.py: Manages inventory-related operations and GUI interactions.
6.data_structures.py: Defines data structures like Binary Search Tree and Hash Table.
7.security.py: Provides password hashing and verification functions.
8.utils.py: Contains utility functions like quicksort for sorting.

Getting Started
-Prerequisites
Python 3.x installed on your system.

-Installation
Install Required Packages:

Ensure you have Tkinter installed (it usually comes with Python).

-Running the Application
1.Run the Application:
python main.py

2.Login:

A login window will appear. Use the following credentials for a test login:

Username: admin
Password: admin123

3.Use the Application:

Once logged in, you can navigate through the main menu to manage patients, appointments, and inventory.

Code Overview
main.py: Starts the application and opens the GUI.
gui.py: Manages the main interface and navigates between different management sections.
patient_management.py: Handles CRUD operations for patient records and displays patient data.
appointment_management.py: Manages appointment scheduling and displays appointment data.
inventory_management.py: Manages inventory records and displays inventory data.
data_structures.py: Implements the BST and Hash Table data structures.
security.py: Provides methods for secure password handling.
utils.py: Contains utility functions for sorting and other operations.
