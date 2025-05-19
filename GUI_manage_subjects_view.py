# gui_manage_subjects_view.py
# 학생이 과목을 추가(신청)하거나 삭제하는 창입니다.
import tkinter as tk
from tkinter import messagebox
from student import Student # Student.MAX_SUBJECTS 등 사용 위함
from subject import Subject # 새 과목 생성을 위함

class ManageSubjectsWindow:
    def __init__(self, root_tk_instance, student_obj, back_to_view_callback_func):
        """
        ManageSubjectsWindow 생성자.
        매개변수:
        root_tk_instance (MainApp): 메인 애플리케이션 tk.Tk 인스턴스.
        student_obj (Student): 현재 로그인한 학생 객체.
        back_to_view_callback_func (function): "완료/뒤로가기" 버튼 클릭 시 호출될 MainApp의 콜백.
        """
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
        """학생의 현재 수강 과목 목록을 리스트박스에 업데이트합니다."""
        self.subjects_listbox.delete(0, tk.END)
        if self.student.subjects:
            for subj in self.student.subjects:
                self.subjects_listbox.insert(tk.END, str(subj))
        else:
            self.subjects_listbox.insert(tk.END, "No subjects enrolled.")

    def enrol_in_new_subject(self):
        """새 과목을 학생의 수강 목록에 추가합니다."""
        if len(self.student.subjects) >= Student.MAX_SUBJECTS:
            messagebox.showwarning("Enrolment Not Allowed", f"You can only enrol in a maximum of {Student.MAX_SUBJECTS} subjects.")
            return
        
        new_subject = Subject()
        self.student.subjects.append(new_subject)
        messagebox.showinfo("Enrolment Successful", f"Subject {new_subject.code} has been enrolled.")
        self.update_enrolled_subjects_display()

    def drop_selected_subject(self):
        """리스트박스에서 선택된 과목을 학생의 수강 목록에서 제거합니다."""
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
# --- [수정 시작] student.py를 수정하지 않기 위한 로직 변경 ---
        # 1. remove_subject 호출 전 현재 과목 수를 기록합니다.
        initial_subject_count = len(self.student.subjects)
        
        # 2. student.py의 remove_subject 메소드를 호출합니다.
        # 이 메소드는 내부적으로 self.student.subjects 리스트를 변경하지만, None을 반환합니다.
        self.student.remove_subject(subject_code_to_drop)
        
        # 3. remove_subject 호출 후 현재 과목 수를 다시 확인합니다.
        final_subject_count = len(self.student.subjects)

        # 4. 과목 수가 줄었다면 삭제가 성공한 것으로 간주합니다.
        if final_subject_count < initial_subject_count:
            messagebox.showinfo("Drop Subject Successful", f"Subject-{subject_code_to_drop} has been dropped.")
            self.update_enrolled_subjects_display() # 성공했으므로 리스트박스 갱신
        else:
            # 과목 수가 그대로라면, 해당 과목을 찾지 못했거나 삭제되지 않은 것입니다.
            messagebox.showerror("Drop Subject Error", f"Could not drop Subject {subject_code_to_drop}. It might not be found in your enrolled list.")