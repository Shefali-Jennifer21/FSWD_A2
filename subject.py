import random

class Subject:
    def __init__(self, code=None, mark=None):
        self.code = code or self.generate_code()
        self.mark = mark if mark is not None else random.randint(25, 100)
        self.grade = self.calculate_grade()

    def generate_code(self):
        try:
            return f"{random.randint(1, 999):03}" 
        except Exception as e:
            print(f"Error generating subject code: {e}")
            return "000"

    def calculate_grade(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "F"

    def __str__(self):
        return f"{self.code} - Mark: {self.mark} - Grade: {self.grade}"

    def to_dict(self):
        return {
            "code": self.code,
            "mark": self.mark,
            "grade": self.grade
        }

    @classmethod
    try:
            code = data.get("code")
            mark = data.get("mark")
            if code is None or mark is None:
                raise ValueError("Missing required subject fields: 'code' and 'mark'")
            return cls(code=code, mark=mark)
        except Exception as e:
            print(f"Error creating Subject from data: {e}")
            return cls()
