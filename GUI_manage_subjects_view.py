import tkinter as tk
from tkinter import messagebox
from student import Student
from subject import Subject 

class ManageSubjectsWindow:
    def __init__(self, root_tk_instance, student_obj, back_to_view_callback_func):
        self.root = root_tk_instance
        self.student = student_obj
        self.back_to_view_callback = back_to_view_callback_func

        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Manage Your Subjects", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.frame, text="Enrolled Subjects (Select to Drop):", font=("Arial", 12, "bold")).pack(pady=(10,0), anchor="w")

        self.subjects_listbox = tk.Listbox(self.frame, height=8, width=70, font=("Arial", 10))
        self.subjects_listbox.pack(pady=5, fill="x")
        self.update_enrolled_subjects_display()

        action_buttons_frame = tk.Frame(self.frame)
        action_buttons_frame.pack(pady=10)

        enrol_button = tk.Button(action_buttons_frame, text="Enrol in New Subject", command=self.enrol_in_new_subject, font=("Arial", 12))
        enrol_button.pack(side="left", padx=5)

        drop_button = tk.Button(action_buttons_frame, text="Drop Selected Subject", command=self.drop_selected_subject, font=("Arial", 12))
        drop_button.pack(side="left", padx=5)

        done_button = tk.Button(self.frame, text="Done (Back to View Subjects)", command=self.back_to_view_callback, font=("Arial", 12))
        done_button.pack(pady=20)

    def update_enrolled_subjects_display(self):
        self.subjects_listbox.delete(0, tk.END)
        if self.student.subjects:
            for subj in self.student.subjects:
                self.subjects_listbox.insert(tk.END, str(subj))
        else:
            self.subjects_listbox.insert(tk.END, "No subjects enrolled.")

    def enrol_in_new_subject(self):
        if len(self.student.subjects) >= Student.MAX_SUBJECTS:
            messagebox.showwarning("Enrolment Not Allowed", f"You can only enrol in a maximum of {Student.MAX_SUBJECTS} subjects.")
            return
        
        new_subject = Subject()
        self.student.subjects.append(new_subject)
        messagebox.showinfo("Enrolment Successful", f"Subject {new_subject.code} has been enrolled.")
        self.update_enrolled_subjects_display()

    def drop_selected_subject(self):
        selected_indices = self.subjects_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Drop Subject Error", "Please select a subject from the list to drop.")
            return
        
        selected_subject_str = self.subjects_listbox.get(selected_indices[0])
        try:
            subject_code_to_drop = selected_subject_str.split(" ")[0]
        except IndexError:
            messagebox.showerror("Drop Subject Error", "Cannot identify subject code from selection.")
            return
        
        initial_subject_count = len(self.student.subjects)
        
        self.student.remove_subject(subject_code_to_drop)
        
        final_subject_count = len(self.student.subjects)

        if final_subject_count < initial_subject_count:
            messagebox.showinfo("Drop Subject Successful", f"Subject-{subject_code_to_drop} has been dropped.")
            self.update_enrolled_subjects_display() 
        else:
            messagebox.showerror("Drop Subject Error", f"Could not drop Subject {subject_code_to_drop}. It might not be found in your enrolled list.")
