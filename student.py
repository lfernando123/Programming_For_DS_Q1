from person import Person
'''Making the Student class by inheriting from the Person class and implementing the role_duties method.'''
class Student(Person):
    def __init__(self, name, age, address, ssn):
        super().__init__(name, age, address, ssn)
        self.grades = {"Mathematics": 0, "Science": 0, "History": 0, "English":
                       0, "Physical Education": 0}

    def assign_grades(self, grades):
        """
        Updates the grades dictionary with new grades and calculates the average grade.
        grades: A dictionary with subjects as keys and grades as values.
        """
        for subject, grade in grades.items():
            if subject in self.grades:  # Ensure the subject exists in the predefined subjects
                self.grades[subject] = grade
            else:
                print(f"Warning: {subject} is not a recognized subject.")

        # Calculate the average grade
        total_grades = sum(self.grades.values())
        num_subjects = len(self.grades)
        average_grade = total_grades / num_subjects if num_subjects > 0 else 0

        return self.grades, average_grade


    def role_duties(self):
        return "Attend classes, complete exams, and participate in activities."
