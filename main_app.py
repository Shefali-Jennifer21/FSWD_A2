# main_app.py
import tkinter as tk
from login_view import LoginWindow
from enrolment_view import EnrolmentWindow
from student import Student # Student 객체 타입을 확인하기 위함 (선택적)
import database # 학생 데이터 저장을 위해 추가

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUIUniApp")
        self.geometry("400x300") # 초기 창 크기 (조정 가능)

        self.current_student = None # 현재 로그인한 학생 객체 저장

        # 초기 화면으로 로그인 창 표시
        self.show_login_window()

    def show_login_window(self):
        # 이전 창이 있다면 파괴
        for widget in self.winfo_children():
            widget.destroy()
        LoginWindow(self, self.switch_to_enrolment_window) #login_view

    def switch_to_enrolment_window(self, student_obj):
        self.current_student = student_obj
        # 이전 창이 있다면 파괴
        for widget in self.winfo_children():
            widget.destroy()
        EnrolmentWindow(self, self.current_student, self.switch_to_login_window) #enrolment_view

    def switch_to_login_window(self):
        # 수강 신청 창에서 로그아웃하거나, 변경사항 저장 후 돌아올 때
        if self.current_student:
            # 변경된 학생 정보를 파일에 저장
            database.update_student_data(self.current_student)
            self.current_student = None

        # 이전 창이 있다면 파괴
        for widget in self.winfo_children():
            widget.destroy()
        self.show_login_window()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
