import tkinter as tk

def open_enrolment_window(student):
    window = tk.Tk()
    window.title("Subject Enrolment")

    welcome = f"Welcome {student.name}!"
    tk.Label(window, text=welcome, font=("Arial", 14)).pack(pady=20)


    window.mainloop()
