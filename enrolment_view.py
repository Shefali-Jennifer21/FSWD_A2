# views/enrolment_view.py
import tkinter as tk
from tkinter import messagebox, simpledialog
import database # 학생 정보 저장을 위해 MainApp에서 처리하도록 변경
from student import Student

class EnrolmentWindow:
    def __init__(self, root, student, show_login_callback):
        self.root = root # MainApp의 인스턴스
        self.student = student
        self.show_login_callback = show_login_callback

        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(expand=True)

        self.root.title(f"GUIUniApp - Enrolment ({self.student.name})")
        self.root.geometry("600x450") # 수강 신청 창 크기

        tk.Label(self.frame, text=f"{self.student.name}, this is the subject enrolment page.", font=("Arial", 14)).pack(pady=10)

        # 현재 수강 과목 표시
        tk.Label(self.frame, text="Currently Enrolled Subjects:", font=("Arial", 12, "bold")).pack(pady=(10,0), anchor="w")
        self.enrolled_subjects_listbox = tk.Listbox(self.frame, height=6, width=60, font=("Arial", 10))
        self.enrolled_subjects_listbox.pack(pady=5)
        self.update_enrolled_subjects_display()


        button_frame = tk.Frame(self.frame)
        button_frame.pack(pady=10)
        # "새 과목 수강 신청" 버튼
        # 현재 Subject 생성 방식(랜덤)에 따라 버튼 텍스트 및 기능이 이렇습니다.
        # 만약 특정 과목을 '선택'하는 방식이라면 UI가 변경되어야 합니다.


        enrol_button = tk.Button(button_frame, text="Enrol in New Subject", command=self.enrol_in_new_subject, font=("Arial", 12))
        enrol_button.pack(side="left", padx=5) # side="left"로 가로 배치

        # "선택 과목 삭제" 버튼 - action_buttons_frame 에 추가
        # 이 버튼이 동작하려면 self.drop_selected_subject 메소드의 주석을 해제하고 내용을 완성해야 합니다.
        drop_button = tk.Button(button_frame, text="Drop Selected Subject", command=self.drop_selected_subject, font=("Arial", 12))
        drop_button.pack(side="left", padx=5) # side="left"로 가로 배치

        # "로그아웃 및 저장" 버튼 - self.frame 에 직접 추가 (버튼들 아래에 위치)
        logout_button = tk.Button(self.frame, text="Logout and Save", command=self.logout, font=("Arial", 12))
        logout_button.pack(pady=20)

    def update_enrolled_subjects_display(self):
        self.enrolled_subjects_listbox.delete(0, tk.END) # 기존 목록 삭제
        if self.student.subjects:
            for subj in self.student.subjects:
                # Subject 객체의 __str__ 메소드가 호출되어 문자열로 표시됨
                self.enrolled_subjects_listbox.insert(tk.END, str(subj))
        else:
            self.enrolled_subjects_listbox.insert(tk.END, "No subjects enrolled.")
        
        # 수강 과목 수 업데이트 (예: 창 제목이나 별도 라벨)
        self.root.title(f"GUIUniApp - Enrolment({self.student.name}) - {len(self.student.subjects)}/{Student.MAX_SUBJECTS} subjects.")


    def enrol_in_new_subject(self):
        if len(self.student.subjects) >= self.student.MAX_SUBJECTS:
            messagebox.showwarning("Enrolment Not Allowed", f"You can only enrol in a maximum of {self.student.MAX_SUBJECTS} subjects.")
            return

        # student.py의 enrol_subject는 print문으로 결과를 알리므로, GUI에서는 다르게 처리
        # 현재 student.enrol_subject()는 Subject()를 내부적으로 생성함
        # 성공 여부나 메시지를 반환하도록 student.py를 수정하거나, 여기서 직접 Subject 추가
        
        # Student.enrol_subject()를 직접 호출하는 대신, 로직을 가져오거나 수정된 메소드 사용
        # self.student.enrol_subject() # 이 메소드는 print를 사용하고, GUI 피드백이 없음
        
        # GUI에 맞게 수정된 로직 (Student 클래스 수정 또는 여기서 직접 처리)
        from subject import Subject # 새 과목 생성
        new_subject = Subject() # 랜덤 과목 생성
        self.student.subjects.append(new_subject)
        
        messagebox.showinfo("Enrolment Successful", f"Subject {new_subject.code} has been enrolled.")
        self.update_enrolled_subjects_display()
        # data_manager.update_student_data(self.student) # 로그아웃 시 한 번에 저장

    def drop_selected_subject(self): # 선택적 기능
         selected_indices = self.enrolled_subjects_listbox.curselection()
         if not selected_indices:
             messagebox.showwarning("Drop Subject Error", "Please select a subject from the list to drop.")
             return
        
         selected_subject_str = self.enrolled_subjects_listbox.get(selected_indices[0])
         subject_code_to_drop = selected_subject_str.split(" ")[0] # "CODE - Mark: XX..." 에서 CODE 추출

    #     # Student 클래스에 remove_subject_by_code(code) 메소드가 있으면 좋음
    #     # 현재 remove_subject(code)는 print를 사용함
         original_subject_count = len(self.student.subjects)
         self.student.remove_subject(subject_code_to_drop) # 이 메소드도 GUI 피드백 수정 필요

         if len(self.student.subjects) < original_subject_count:
             messagebox.showinfo("과목 삭제 완료", f"Subject-{subject_code_to_drop} has been dropped.")
             self.update_enrolled_subjects_display()
             # data_manager.update_student_data(self.student) # 로그아웃 시 한 번에 저장
         else: # 삭제 실패 (코드가 없거나 할 때)
             messagebox.showerror("과목 삭제 오류", f"Subject-{subject_code_to_drop} could not be found or an error occurred while dropping.")


    def logout(self):
        # MainApp의 콜백을 호출하여 로그인 창으로 돌아가면서 현재 학생 정보 저장
        self.show_login_callback()