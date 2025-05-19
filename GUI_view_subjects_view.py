# gui_view_subjects_view.py
# 학생이 신청한 과목 목록을 보여주는 창입니다.
import tkinter as tk
# from tkinter import messagebox # 현재 직접 사용 X
from student import Student # Student.MAX_SUBJECTS 등 사용 위함

class ViewSubjectsWindow:
    def __init__(self, root_tk_instance, student_obj, manage_subjects_callback_func, logout_callback_func):
        """
        ViewSubjectsWindow 생성자.
        매개변수:
        root_tk_instance (MainApp): 메인 애플리케이션 tk.Tk 인스턴스.
        student_obj (Student): 현재 로그인한 학생 객체.
        manage_subjects_callback_func (function): "과목 관리" 버튼 클릭 시 호출될 MainApp의 콜백.
        logout_callback_func (function): "로그아웃" 버튼 클릭 시 호출될 MainApp의 콜백.
        """
        self.root = root_tk_instance
        self.student = student_obj
        self.manage_subjects_callback = manage_subjects_callback_func
        self.logout_callback = logout_callback_func

        # 이 뷰의 모든 위젯을 담을 메인 프레임
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text=f"Welcome, {self.student.name}!", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.frame, text=f"Student ID: {self.student.id}", font=("Arial", 12)).pack(pady=10)
        tk.Label(self.frame, text=f"Student Email: {self.student.email}", font=("Arial", 12)).pack(pady=10)

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
        """학생의 현재 수강 과목 목록을 리스트박스에 업데이트합니다."""
        self.subjects_listbox.delete(0, tk.END)
        if self.student.subjects:
            for subj in self.student.subjects:
                self.subjects_listbox.insert(tk.END, str(subj))
        else:
            self.subjects_listbox.insert(tk.END, "No subjects enrolled yet.")