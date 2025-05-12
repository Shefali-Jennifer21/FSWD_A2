import json
from student import Student

FILE_NAME = "students.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Student.from_dict(item) for item in data]
    except FileNotFoundError:
        return []

def get_student_by_email_password(email, password):
    email = email.strip().lower()
    password = password.strip()
    students = load_students()
    for student in students:
        if student.email.strip().lower() == email and student.password == password:
            return student
    return None

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump([s.to_dict() for s in students], file, indent=4)
