
import tkinter as tk
from tkinter import messagebox
import database # get_student_by_email_password
from student import EMAIL_REGEX, Student # is_valid_email

class LoginWindow:
    def __init__(self, root, login_success_callback_func):
        self.root = root 
        self.login_success_callback = login_success_callback_func 

        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(expand=True)

        self.root.title("GUIUniApp - Login")
        self.root.geometry("400x300") 

        tk.Label(self.frame, text="Email:", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="w")
        self.email_entry = tk.Entry(self.frame, width=30, font=("Arial", 12))
        self.email_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.frame, text="Password:", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="w")
        self.password_entry = tk.Entry(self.frame, show="*", width=30, font=("Arial", 12))
        self.password_entry.grid(row=1, column=1, pady=5)

        login_button = tk.Button(self.frame, text="Login", command=self.attempt_login, font=("Arial", 12), width=10)
        login_button.grid(row=2, column=0, columnspan=2, pady=20)

    def attempt_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Login Error", "Please enter both email and password.")
            return

        # email form exception
        temp_student_for_validation = Student("t_name", email, "t_pw")
        if not temp_student_for_validation.is_valid_email():
             messagebox.showerror("Login Error", "Invalid email format.")
             return

        # validation 
        student = database.get_student_by_email_password(email, password)

        if student:
            messagebox.showinfo("Login Successful", f"Welcome, {student.name}!")
            self.login_success_callback(student) 
        else:
            messagebox.showerror("Incorrect email or password, or user not registered.\n(Please check the email format.)")
