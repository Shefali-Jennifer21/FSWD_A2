import json
import os
from student import Student

FILE_NAME = "students.json"

def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
        return [Student.from_dict(item) for item in data]

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump([s.to_dict() for s in students], file, indent=4)

def update_student_data(updated_student):
    students = load_students()
    for i, student in enumerate(students):
        if student.email == updated_student.email:
            students[i] = updated_student
            break
    else:
        students.append(updated_student)
    save_students(students)

def get_student_by_email_password(email, password):
    for student in load_students():
        if student.email == email and student.password == password:
            return student
    return None

def student_exists(email):
    for student in load_students():
        if student.email == email.strip():  
            return True
    return False