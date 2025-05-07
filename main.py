from student import Student
from subject import Subject  
from database import update_student_data, get_student_by_email_password, student_exists
import re
import random

def register_student():
    print("Student Sign Up")
    while True:
        email = input("Email: ")
        password = input("Password: ")
        temp_student = Student("", email, password)

        if not temp_student.is_valid_email() or not temp_student.is_valid_password():
            print("Incorrect email or password format")
        elif student_exists(email):
            print(f"Student {email.split('@')[0].replace('.', ' ').title()} already exists")
            return
        else:
            print("email and password formats acceptable")
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

        if not temp_student.is_valid_email() or not temp_student.is_valid_password():
            print("Incorrect email or password format")
        else:
            student = get_student_by_email_password(email, password)
            if student:
                print("Student Course Menu")
                student_course_menu(student)
                update_student_data(student) 
                return
            else:
                print("Student does not exist")

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
            update_student_data(student)
            student.remove_subject(code)
        elif choice == 's':
            student.show_enrolled_subjects()
        elif choice == 'c':
            print("Updating Password")
            while True:
                new_password = input("New Password: ")
                confirm_password = input("Confirm Password: ")
                if new_password != confirm_password:
                    print("Password does not match - try again")
                else:
                    student.password = new_password  
                    update_student_data(student)  
                    print("Password updated successfully.")
                    break
        else:
            print("Invalid option. Please try again.")

def admin_menu():
    while True:
        choice = input("Admin System (c/g/p/r/s/x) : ").lower()
        if choice == 'x':
            break
        else:
            print("Admin functionality placeholder.")

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