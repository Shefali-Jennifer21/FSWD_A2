
# views/login_view.py
import tkinter as tk
from tkinter import messagebox
import database # get_student_by_email_password 사용
from student import EMAIL_REGEX, Student # is_valid_email을 사용하려면 필요 (임시 Student 객체 생성)-유효성 검사

class LoginWindow:
  # 로그인 화면을 생성하고 사용자 입력을 처리하는 클래스 """
        #root_tk_instance (MainApp): 이 로그인 창의 위젯들이 그려질 부모 Tkinter 인스턴스.
        #login_success_callback_func (function): 로그인 성공 시 호출될 MainApp의 콜백 함수. 학생 객체를 인자로 받습니다.
    def __init__(self, root, login_success_callback_func):
        self.root = root # MainApp의 인스턴스
        self.login_success_callback = login_success_callback_func # 콜백 함수 저장

        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(expand=True)

        self.root.title("GUIUniApp - Login")
        self.root.geometry("400x300") # 로그인 창 크기

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

        # 1. 빈 필드 예외 처리
        if not email or not password:
            messagebox.showerror("Login Error", "Please enter both email and password.")
            return

        # 2. 이메일 형식 예외 처리 (Student 클래스의 is_valid_email 사용)
        temp_student_for_validation = Student("t_name", email, "t_pw") # name, password는 임시값
        if not temp_student_for_validation.is_valid_email():
             messagebox.showerror("Login Error", "Invalid email format.")
             return

        # 3. 자격 증명 확인
        student = database.get_student_by_email_password(email, password)

        if student:
            messagebox.showinfo("Login Successful", f"Welcome, {student.name}!")
            self.login_success_callback(student) # 성공 시, 학생 객체와 함께 콜백 호출
        else:
            # (세분화된 오류 메시지를 원한다면 data_manager.student_exists(email) 등을 추가 활용)
            messagebox.showerror("Incorrect email or password, or user not registered.\n(Please check the email format.)")