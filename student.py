from person import Person

class Student(Person):
    def __init__(self, name, age, address, ssn):
        super().__init__(name, age, address, ssn)
        self.grades = {}

    def assign_grades(self, grades):
        self.grades = grades
        return sum(grades.values()) / len(grades)

    def role_duties(self):
        return "Attend classes, complete assignments, and participate in activities."
