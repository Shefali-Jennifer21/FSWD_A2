from database import load_students, save_students
from student import Student

class Admin:

    @staticmethod
    def show_all_students():
        students = load_students()
        if not students:
            print("No students found.")
            return
        print("\n--- All Students ---")
        for s in students:
            print(f"  {s.name} : : {s.id} -->  Email: {s.email}")

    @staticmethod
    def clear_database():
        confirm = input("Are you sure you want to clear the Database? (Y)ES / (N)O: ").strip().lower()
        if confirm == 'y':
            save_students([])
            print("All student data has been cleared.")
        else:
            print("Operation cancelled. Student data remains unchanged.")

    @staticmethod
    def remove_student_by_id(student_id):
        students = load_students()
        new_students = [s for s in students if s.id != student_id]
        if len(new_students) == len(students):
            print(f"No student with ID {student_id} found.")
        else:
            print(f"Student with ID {student_id} has been removed.")
        save_students(new_students)

    @staticmethod
 
    def group_students_by_grade():
        students = load_students()
        grade_groups = {}

        for student in students:
            for subject in student.subjects:
                grade_groups.setdefault(subject.grade, []).append((student, subject))

        if not grade_groups:
            print("No subject data found for grouping.")
            return

        print("\n--- Grouped by Grade ---")
        for grade, entries in grade_groups.items():
            print(f"\nGRADE: {grade}")
            for student, subject in entries:
                print(f"  {student.name} : : {student.id} -->  Subject Code: {subject.code} - MARK: {subject.mark:.2f}")


    @staticmethod
    def partition_students_pass_fail():
        students = load_students()

        print("\n--- Passed Students ---")
        

        any_passed = False
        for s in students:
            for subject in s.subjects:
                if subject.grade != "F":
                    print(f"{s.name} : : {s.id} --> Subject Code: {subject.code} - GRADE: {subject.grade} - MARK: {subject.mark:.2f}")
                    any_passed = True
        if not any_passed:
            print("No passed students.")
        
        
        print("\n--- Failed Students ---")
        any_failed = False
        for s in students:
            for subject in s.subjects:
                if subject.grade == "F":
                    print(f"{s.name} : : {s.id} --> Subject Code: {subject.code} - GRADE: F - MARK: {subject.mark:.2f}")
                    any_failed = True
        if not any_failed:
            print("No failed subjects.")
