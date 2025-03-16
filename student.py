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
    
    def display_grades(self):
        """Displays the student's grades."""
        if not self.grades:
            return f"{self.name} has no grades yet."
        grades = "\n".join([f"{subject}: {grade}" for subject, grade in self.grades.items()])
        return f"Grades for {self.name}:\n{grades}"
    
    def attendance(self, date, status):
        """Marks the student's attendance as 'Present' or 'Absent' for a given date."""
        if status not in ["Present", "Absent"]:
            print("Invalid status! Use 'Present' or 'Absent'.")
            return
        self.attendance_record[date] = status
        print(f"Attendance marked for {self.name} on {date}: {status}")

    def display_attendance(self):
        """Displays the student's overall attendance record."""
        if not self.attendance_record:
            return f"{self.name} has no attendance records."
        attendance_list = "\n".join([f"{date}: {status}" for date, status in self.attendance_record.items()])
        return f"Attendance Record for {self.name}:\n{attendance_list}"


    def role_duties(self):
        return "Attend classes, complete exams, and participate in activities."
