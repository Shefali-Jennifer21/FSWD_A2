
# views/login_view.py
import tkinter as tk
from tkinter import messagebox
import database # get_student_by_email_password 사용
from student import Student # is_valid_email을 사용하려면 필요 (임시 Student 객체 생성)

class LoginWindow:
    def __init__(self, root, show_enrolment_callback):
        self.root = root # MainApp의 인스턴스
        self.show_enrolment_callback = show_enrolment_callback # 콜백 함수 저장

        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(expand=True)

        self.root.title("GUIUniApp - Login")
        self.root.geometry("400x300") # 로그인 창 크기

        tk.Label(self.frame, text="Email:", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="w")
        self.email_entry = tk.Entry(self.frame, width=30, font=("Arial", 12))
        self.email_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.frame, text="Passworld:", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="w")
        self.password_entry = tk.Entry(self.frame, show="*", width=30, font=("Arial", 12))
        self.password_entry.grid(row=1, column=1, pady=5)

        login_button = tk.Button(self.frame, text="Login", command=self.attempt_login, font=("Arial", 12), width=10)
        login_button.grid(row=2, column=0, columnspan=2, pady=20)

    def attempt_login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get()

        # 1. 빈 필드 예외 처리
        if not email or not password:
            messagebox.showerror("Login Error", "Please enter both email and password.")
            return

        # 2. 이메일 형식 예외 처리 (Student 클래스의 is_valid_email 사용)
        # 임시 Student 객체를 만들어 유효성 검사를 할 수도 있지만,
        # 여기서는 data_manager에 해당 기능이 있다면 사용하는 것이 더 적절할 수 있습니다.
        # 만약 Student 클래스의 정적 메소드나 별도 유틸리티 함수가 있다면 더 좋음.
        # 현재 Student 클래스에는 인스턴스 메소드로 있으므로, 여기서는 정규식 직접 사용 또는
        # Student 객체 생성 후 검증 필요. 일단 로그인 시도 후 결과로 판단하는 방식도 가능.
        # 과제 요구사항: "incorrect email format should be handled"
        # student.py 의 EMAIL_REGEX 를 직접 사용할 수도 있습니다.
        from student import EMAIL_REGEX, Student # (Student는 임시 객체 생성용)
        temp_student_for_validation = Student("test", email, "testpass") # name, password는 임시값
        if not temp_student_for_validation.is_valid_email():
             messagebox.showerror("Login Error", "Invalid email format.")
             return

        # 3. 자격 증명 확인
        student = database.get_student_by_email_password(email, password)

        if student:
            messagebox.showinfo("Login Successful", f"Welcome, {student.name}!")
            self.show_enrolment_callback(student) # 성공 시, 학생 객체와 함께 콜백 호출
        else:
            # 로그인 실패 시, 이메일 존재 여부 및 형식 오류를 한 번에 묶어서 처리할 수도 있음
            # (세분화된 오류 메시지를 원한다면 data_manager.student_exists(email) 등을 추가 활용)
            messagebox.showerror("Incorrect email or password, or user not registered.\n(Please check the email format.)")