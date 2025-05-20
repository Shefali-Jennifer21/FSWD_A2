import tkinter as tk
from GUI_login_view import LoginWindow
from GUI_view_subjects_view import ViewSubjectsWindow   
from GUI_manage_subjects_view import ManageSubjectsWindow 
import database

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUIUniApp")
        self.geometry("400x300")

        self.current_student = None
        
        self.show_login_window()    


    def clear_all_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_login_window(self):
        self.clear_all_widgets()
        LoginWindow(self, self.callback_login_success)
        self.title("GUIUniApp - Login")
        self.geometry("400x300")

    def callback_login_success(self, student_obj):
        self.current_student = student_obj
        self.show_view_subjects_window()

    def show_view_subjects_window(self):
        self.clear_all_widgets()
        ViewSubjectsWindow(
            self,                          
            self.current_student,          
            self.callback_go_to_manage_subjects,
            self.callback_logout           
        )
        self.title(f"GUIUniApp - View Enrolments ({self.current_student.name})")
        self.geometry("600x450")

    def callback_go_to_manage_subjects(self):
        self.show_manage_subjects_window()

    def show_manage_subjects_window(self):
        self.clear_all_widgets()
        ManageSubjectsWindow(
            self,                           
            self.current_student,          
            self.callback_back_to_view_subjects 
        )   
        self.title(f"GUIUniApp - Manage Enrolments ({self.current_student.name})")
        self.geometry("600x500") 

    def callback_back_to_view_subjects(self):
        self.show_view_subjects_window()

    def callback_logout(self):
        if self.current_student:
            print(f"Logging out and saving data for {self.current_student.name}...") 
            database.update_student_data(self.current_student)
            self.current_student = None 
        self.show_login_window() 


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
