from student import Student
from teacher import Teacher
from staff import Staff

student = Student("Alice", 14, "123 St", "123-45-6789")
teacher = Teacher("Mr. Smith", 40, "456 St", "987-65-4321", "Mathematics")
staff = Staff("Ms. Johnson", 35, "789 St", "654-32-1987", "Admin", 5)

print(student.role_duties())
print(teacher.role_duties())
print(staff.role_duties())
