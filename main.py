from student import Student
from teacher import Teacher
from staff import Staff

# Polymorphic function
def display_info(person):
    """Displays basic information using polymorphism"""
    print(f"Name: {person.name}, Age: {person.age}, Role: {type(person).__name__}")
    print(f"Duties: {person.role_duties()}")
    print(person.display_schedule()) if type(person).__name__ == "Teacher" else None
    print(person.display_attendance()) if type(person).__name__ == "Student" else None
    print(person.display_grades()) if type(person).__name__ == "Student" else None
    print(f"Salary: ${person.calculate_salary()}") if type(person).__name__ == "Staff" else None
    print("-" * 70)
    

# Main Execution Block
if __name__ == "__main__":
    student = Student("Lasitha", 16, "59, Negombo", "0167-3412-2009")
    teacher = Teacher("Mr.Kamal", 40, "Katunayake", "0453-1123-1985", "Mathematics")
    staff = Staff("Ms.Shenika", 35, "789 St", "0654-3232-1990", "Admin", 5)

    # Using Polymorphism
    for person in [student, teacher, staff]:

        if person == student:
            # Assign grades
            grades = {"Mathematics": 90, "Science": 85, "History": 88, "English": 92, "Physical Education": 95}
            student.assign_grades(grades)

            # Mark attendance
            student.attendance("2021-09-01", "Present")
            student.attendance("2021-09-03", "Absent")

            # # Modify SSN using setter
            # student.set_ssn("111-22-3333")
            # print(student.get_ssn())

            # Invalid SSN update attempt
            student.set_ssn("12345")

        elif person == teacher:
            # Schedule classes
            teacher.schedule_classes("Monday", "10:00 AM - 11:30 AM")
            teacher.schedule_classes("Wednesday", "12:00 PM - 1:30 PM") 

        display_info(person)
            
