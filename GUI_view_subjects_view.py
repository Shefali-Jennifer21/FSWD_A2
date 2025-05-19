import tkinter as tk
from student import Student

class ViewSubjectsWindow:
    def __init__(self, root_tk_instance, student_obj, manage_subjects_callback_func, logout_callback_func):
        self.root = root_tk_instance
        self.student = student_obj
        self.manage_subjects_callback = manage_subjects_callback_func
        self.logout_callback = logout_callback_func

        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text=f"Welcome, {self.student.name}!", font=("Arial", 16)).pack(pady=10)
        
        tk.Label(self.frame, text=f"Student ID: {self.student.id}", font=("Arial", 12)).pack(pady=(5,1), anchor='w')
        tk.Label(self.frame, text=f"Student name: {self.student.name}", font=("Arial", 12)).pack(pady=(1,1), anchor='w')
        tk.Label(self.frame, text=f"Student Email: {self.student.email}", font=("Arial", 12)).pack(pady=(1,5), anchor='w')

        tk.Label(self.frame, text="Your Enrolled Subjects:", font=("Arial", 12, "bold")).pack(pady=(10,0), anchor="w")

        self.subjects_listbox = tk.Listbox(self.frame, height=10, width=70, font=("Arial", 10))
        self.subjects_listbox.pack(pady=5, fill="x")

        self.update_enrolled_subjects_display()

        action_button_frame = tk.Frame(self.frame)
        action_button_frame.pack(pady=20)

        manage_btn = tk.Button(action_button_frame, text="Manage Subjects", command=self.manage_subjects_callback, font=("Arial", 12))
        manage_btn.pack(side="left", padx=10)

        logout_btn = tk.Button(action_button_frame, text="Logout", command=self.logout_callback, font=("Arial", 12))
        logout_btn.pack(side="left", padx=10)

    def update_enrolled_subjects_display(self):
        self.subjects_listbox.delete(0, tk.END)
        if self.student.subjects:
            for subj in self.student.subjects:
                self.subjects_listbox.insert(tk.END, str(subj))
        else:
            self.subjects_listbox.insert(tk.END, "No subjects enrolled yet.")
