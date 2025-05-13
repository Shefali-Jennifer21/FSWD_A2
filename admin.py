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
            print(s)

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
                grade_groups.setdefault(subject.grade, []).append(student)

        if not grade_groups:
            print("No subject data found for grouping.")
            return

        print("\n--- Grouped by Grade ---")
        seen_ids = set()
        for grade, group in grade_groups.items():
            print(f"Grade {grade}:")
            for student in group:
                if student.id not in seen_ids:
                    print(f"  {student}")
                    seen_ids.add(student.id)

    @staticmethod
    def partition_students_pass_fail():
        students = load_students()
        passed = [
            s for s in students
            if s.calculate_average() >= 50 and len(s.subjects) == Student.MAX_SUBJECTS
        ]
        failed = [
            s for s in students
            if s.calculate_average() < 50 or len(s.subjects) < Student.MAX_SUBJECTS
        ]

        print("\n--- Passed Students ---")
        if passed:
            for s in passed:
                print(s)
        else:
            print("No passed students.")

        print("\n--- Failed Students ---")
        if failed:
            for s in failed:
                print(s)
        else:
            print("No failed students.")
