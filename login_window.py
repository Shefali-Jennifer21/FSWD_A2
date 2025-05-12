import tkinter as tk
from tkinter import messagebox
from controller import get_student_by_email_password
from enrolment_window import open_enrolment_window

def open_login_window():
    def handle_login():
        email = entry_email.get()
        password = entry_password.get()

        student = get_student_by_email_password(email, password)
        if student:
            messagebox.showinfo("Login Successful", f"Welcome, {student.name}!")
            root.destroy()
            open_enrolment_window(student)
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")


    root = tk.Tk()
    root.title("Student Login")
    root.configure(bg="#d9e6f2")
    window_width = 400
    window_height = 230


    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")


    font_label = ("Helvetica", 11)
    font_entry = ("Helvetica", 11)
    font_button = ("Helvetica", 11, "bold")


    form_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
    form_frame.place(relx=0.5, rely=0.5, anchor="center", width=320, height=160)


    tk.Label(form_frame, text="Email:", font=font_label, bg="white", fg="#333").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_email = tk.Entry(form_frame, font=font_entry, width=25)
    entry_email.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(form_frame, text="Password:", font=font_label, bg="white", fg="#333").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_password = tk.Entry(form_frame, show="*", font=font_entry, width=25)
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    login_btn = tk.Button(form_frame, text="Login", command=handle_login, font=font_button, bg="#4a90e2", fg="black", activebackground="#357ABD")
    login_btn.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    open_login_window()
