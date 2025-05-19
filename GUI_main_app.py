# main_app.py
import tkinter as tk
from GUI_login_view import LoginWindow
from GUI_view_subjects_view import ViewSubjectsWindow     # <<< [새로운 뷰] 과목 조회 창 임포트 >>>
from GUI_manage_subjects_view import ManageSubjectsWindow 
import database # 학생 데이터 저장을 위해 추가

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUIUniApp")
        self.geometry("400x300")

        self.current_student = None # make variable for current_stu

        self.show_login_window()    # Display login window as initial screen


    def clear_all_widgets(self):
        """All child widgets are removed. """
        for widget in self.winfo_children(): # winfo_children()은 현재 위젯의 모든 자식 위젯 리스트를 반환
            widget.destroy()

    def show_login_window(self):
        self.clear_all_widgets() # 메소드 호출 확인
        LoginWindow(self, self.callback_login_success) # <<< [콜백 함수 변경] >>>
        self.title("GUIUniApp - Login")
        self.geometry("400x300")

    def callback_login_success(self, student_obj):
        """로그인 성공 시 호출: 과목 조회 창으로 전환합니다."""
        self.current_student = student_obj #현재 로그인한 학생을 인자로 가짐
        self.show_view_subjects_window()

    def show_view_subjects_window(self):
        """과목 조회 창을 표시합니다."""
        self.clear_all_widgets()
        ViewSubjectsWindow(
            self,                           # 부모 윈도우 (MainApp)
            self.current_student,           # 현재 로그인한 학생 객체
            self.callback_go_to_manage_subjects, # "과목 관리" 버튼 클릭 시 호출될 함수
            self.callback_logout            # "로그아웃" 버튼 클릭 시 호출될 함수
        )
        self.title(f"GUIUniApp - View Enrolments ({self.current_student.name})")
        self.geometry("600x450")

    def callback_go_to_manage_subjects(self):
        """과목 조회 창에서 호출: 과목 관리 창으로 전환합니다."""
        self.show_manage_subjects_window()

    def show_manage_subjects_window(self):
        """과목 관리 창을 표시합니다."""
        self.clear_all_widgets()
        ManageSubjectsWindow(
            self,                           # 부모 윈도우 (MainApp)
            self.current_student,           # 현재 로그인한 학생 객체
            self.callback_back_to_view_subjects # "완료/뒤로가기" 버튼 클릭 시 호출될 함수
        )   
        self.title(f"GUIUniApp - Manage Enrolments ({self.current_student.name})")
        self.geometry("600x500") # 과목 관리 창 크기

    def callback_back_to_view_subjects(self):
        """과목 관리 창에서 호출: 과목 조회 창으로 돌아갑니다."""
        # current_student 객체는 ManageSubjectsWindow에서 변경되었을 수 있으므로,
        # ViewSubjectsWindow는 이 객체의 최신 상태를 반영하여 다시 그려집니다.
        self.show_view_subjects_window()

    def callback_logout(self):
        """로그아웃 처리: 학생 데이터를 저장하고 로그인 창으로 돌아갑니다."""
        if self.current_student:
            print(f"Logging out and saving data for {self.current_student.name}...") # 디버깅용
            database.update_student_data(self.current_student) # 데이터 저장
            self.current_student = None # 현재 학생 정보 초기화
        self.show_login_window() # 로그인 창 표시


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
