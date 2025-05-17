import re
import random
from subject import Subject

EMAIL_REGEX = r"^[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+@university\.com$"
PASSWORD_REGEX = r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$" 

class Student:
    MAX_SUBJECTS = 4

    def __init__(self, name, email, password): 
        self.id = f"{random.randint(1, 999999):06}"  
        self.name = name
        self.email = email.lower()
        self.password = password
        self.subjects = []

    def is_valid_email(self):
        return re.fullmatch(EMAIL_REGEX, self.email, re.IGNORECASE)

    def is_valid_password(self):
        return re.fullmatch(PASSWORD_REGEX, self.password)

    def enrol_subject(self):
        if len(self.subjects) >= self.MAX_SUBJECTS:
            print("Students are allowed to enrol in 4 subjects only.")
            return

        subject = Subject()  
        self.subjects.append(subject)
        print(f"Enrolling in {subject.code}")
        print(f"You are now enrolled in {len(self.subjects)} out of {self.MAX_SUBJECTS} subjects")

    def remove_subject(self, code):
        for subj in self.subjects:
            if subj.code == code:
                self.subjects.remove(subj)
                print(f"Dropping Subject-{code}")
                print(f"You are now enrolled in {len(self.subjects)} out of {self.MAX_SUBJECTS} subjects")
                return
        print(f"Subject-{code} not found.")

    def calculate_average(self):
        if not self.subjects:
            return 0
        return sum(subj.mark for subj in self.subjects) / len(self.subjects)

    def has_passed(self):
        return self.calculate_average() >= 50 and len(self.subjects) == self.MAX_SUBJECTS

    def show_enrolled_subjects(self):
        print(f"Showing {len(self.subjects)} subjects")
        for subj in self.subjects:
            print(subj)

    def __str__(self):
        return f"{self.name} ({self.email})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subjects": [subject.to_dict() for subject in self.subjects]
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data["name"], data["email"], data["password"])
        student.id = data.get("id", f"{random.randint(1, 999999):06}")  
        student.subjects = [Subject.from_dict(subj) for subj in data.get("subjects", [])]
        return student
