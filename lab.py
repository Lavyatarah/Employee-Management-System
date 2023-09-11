import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="#0C9295")  # Set the background color of the main window

        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("ID", "Name", "Role", "Gender", "Status")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("ID", anchor=tk.CENTER, width=100)
        self.tree.column("Name", anchor=tk.CENTER, width=200)
        self.tree.column("Role", anchor=tk.CENTER, width=100)
        self.tree.column("Gender", anchor=tk.CENTER, width=100)
        self.tree.column("Status", anchor=tk.CENTER, width=100)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Role", text="Role")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Status", text="Status")
        self.tree.place(x=10, y=10)
        # Create a style for buttons
        button_style = ttk.Style()
        button_style.configure("TButton", padding=6, font=("Arial", 12), background="#007ACC", foreground="white")
        
        self.add_button = ttk.Button(root, text="Add", command=self.add_employee, style="TButton")
        self.add_button.place(x=10, y=360)
        self.update_button = ttk.Button(root, text="Update", command=self.update_employee, style="TButton")
        self.update_button.place(x=100, y=360)
        self.delete_button = ttk.Button(root, text="Delete", command=self.delete_employee, style="TButton")
        self.delete_button.place(x=190, y=360)

        self.id_entry = tk.Entry(root, font=("Arial", 12))
        self.id_entry.place(x=10, y=300)
        self.name_entry = tk.Entry(root, font=("Arial", 12))
        self.name_entry.place(x=120, y=300)
        self.role_entry = tk.Entry(root, font=("Arial", 12))
        self.role_entry.place(x=230, y=300)
        self.gender_entry = tk.Entry(root, font=("Arial", 12))
        self.gender_entry.place(x=340, y=300)
        self.status_entry = tk.Entry(root, font=("Arial", 12))
        self.status_entry.place(x=450, y=300)

        self.employee_data = []
        self.load_data()

    def load_data(self):
        # In this simplified example, we manually populate the employee_data list.
        self.employee_data = [
            {"ID": "1", "Name": "John", "Role": "Manager", "Gender": "Male", "Status": "Active"},
            {"ID": "2", "Name": "Alice", "Role": "Developer", "Gender": "Female", "Status": "Inactive"},
        ]
        self.display_data()

    def display_data(self):
        self.tree.delete(*self.tree.get_children())
        for employee in self.employee_data:
            self.tree.insert("", tk.END, values=(
                employee["ID"],
                employee["Name"],
                employee["Role"],
                employee["Gender"],
                employee["Status"]
            ))

    def clear_entries(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.role_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)

    def add_employee(self):
        id = self.id_entry.get()
        name = self.name_entry.get()
        role = self.role_entry.get()
        gender = self.gender_entry.get()
        status = self.status_entry.get()

        if id and name and role and gender and status:
            new_employee = {"ID": id, "Name": name, "Role": role, "Gender": gender, "Status": status}
            self.employee_data.append(new_employee)
            self.display_data()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def update_employee(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_item = selected_item[0]
            id = self.id_entry.get()
            name = self.name_entry.get()
            role = self.role_entry.get()
            gender = self.gender_entry.get()
            status = self.status_entry.get()

            if id and name and role and gender and status:
                for employee in self.employee_data:
                    if employee["ID"] == self.tree.item(selected_item, "values")[0]:
                        employee["ID"] = id
                        employee["Name"] = name
                        employee["Role"] = role
                        employee["Gender"] = gender
                        employee["Status"] = status
                self.display_data()
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Error", "Please select an employee to update.")

    def delete_employee(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_item = selected_item[0]
            id_to_delete = self.tree.item(selected_item, "values")[0]
            for employee in self.employee_data:
                if employee["ID"] == id_to_delete:
                    self.employee_data.remove(employee)
            self.display_data()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please select an employee to delete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()
