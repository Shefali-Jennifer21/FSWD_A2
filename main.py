from student import Student
from subject import Subject  
from database import update_student_data, get_student_by_email_password, student_exists
from admin import Admin
import re
import random

PASSWORD_REGEX = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$&!%*])[A-Za-z0-9@#$&!%*]{8,}$"

def register_student():
    print("Student Sign Up")
    while True:
        email = input("Email: ")
        password = input("Password: ")
        
        temp_student = Student("", email, password)

        if not temp_student.is_valid_email():
            print("Invalid email format. Must be firstname.lastname@university.com")
            continue

        password_errors = temp_student.validate_password()
        if password_errors:
            print("Invalid password format:")
            for err in password_errors:
                print(f"- {err}")
            continue

        if student_exists(email):
            print(f"Student {email.split('@')[0].replace('.', ' ').title()} already exists")
            return

        print("Email and password formats are acceptable.")
        name = input("Name: ")
        student = Student(name, email, password)
        update_student_data(student)  
        print(f"Enrolling Student {name}")
        return


def login_student():
    print("Student Sign In")
    while True:
        email = input("Email: ")
        password = input("Password: ")
        temp_student = Student("", email, password)

        valid_email = temp_student.is_valid_email()
        password_errors = temp_student.validate_password()
        valid_password = len(password_errors) == 0

        if not valid_email:
            print("Invalid email format. Must be firstname.lastname@university.com")
        if not valid_password:
            print("Invalid password format:")
            for err in password_errors:
                print(f"- {err}")

        if valid_email and valid_password:
            email = email.lower()
            student = get_student_by_email_password(email, password)
            if student:
                print("Student Course Menu")
                student_course_menu(student)
                update_student_data(student)
                return
            else:
                print("Student does not exist")
                return
            
def student_course_menu(student):
    while True:
        choice = input("Student Course Menu (c/e/r/s/x): ").lower()
        if choice == 'x':
            break
        elif choice == 'e':
            if len(student.subjects) < Student.MAX_SUBJECTS:
                student.enrol_subject()
                update_student_data(student) 
            else:
                print("Students are allowed to enrol in 4 subjects only.")
        elif choice == 'r':
            code = input("Remove Subject by ID: ")
            student.remove_subject(code)
            update_student_data(student)
        elif choice == 's':
            student.show_enrolled_subjects()
        elif choice == 'c':
            print("Updating Password")
        while True:
            new_password = input("New Password: ")
            confirm_password = input("Confirm Password: ")

            if new_password != confirm_password:
                print("Passwords do not match - try again")
                continue

            temp_student = Student(student.name, student.email, new_password)
            password_errors = temp_student.validate_password()

            if password_errors:
                print("Invalid password format:")
                for err in password_errors:
                    print(f"- {err}")
            else:
                student.password = new_password
                update_student_data(student)
                print("Password updated successfully.")
                break

def student_menu():
    while True:
        choice = input("Student System (l/r/x): ").lower()
        if choice == 'x':
            break
        elif choice == 'l':
            login_student()
        elif choice == 'r':
            register_student()
        else:
            print("Invalid student option. Please try again.")

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("Admin System (c/g/p/r/s/x)")
        choice = input("Choose an option: ").lower()
        if choice == 'x':
            break
        elif choice == 'c':
            Admin.clear_database()
        elif choice == 'g':
            Admin.group_students_by_grade()
        elif choice == 'p':
            Admin.partition_students_pass_fail()
        elif choice == 'r':
            sid = input("Enter Student ID to remove: ")
            Admin.remove_student_by_id(sid)
        elif choice == 's':
            Admin.show_all_students()
        else:
            print("Invalid option. Please try again.")

def main():
    while True:
        choice = input("University System: (A)dmin, (S)tudent, or X : ").lower()
        if choice == 'x':
            print("Thank you !")
            break 
        elif choice == 'a':
            admin_menu()
        elif choice == 's':
            student_menu()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

