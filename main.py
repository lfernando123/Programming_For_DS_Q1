from student import Student
from teacher import Teacher
from staff import Staff

# Polymorphic function
def display_info(person):
    """Displays basic information using polymorphism"""
    print(f"Name: {person.name}, Age: {person.age}, Role: {type(person).__name__}")
    print(f"Duties: {person.role_duties()}")
    print("-" * 70)

# Main Execution Block
if __name__ == "__main__":
    student = Student("Lasitha", 16, "59, Negombo", "067-342-2009")
    teacher = Teacher("Mr.Kamal", 40, "Katunayake", "453-123-1985", "Mathematics")
    staff = Staff("Ms.Shenika", 35, "789 St", "654-32-1990", "Admin", 5)

    # Using Polymorphism
    for person in [student, teacher, staff]:
        display_info(person)
