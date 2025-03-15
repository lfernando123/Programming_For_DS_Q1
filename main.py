from student import Student
from teacher import Teacher
from staff import Staff

student = Student("Lasitha", 16, "59, Negombo", "067-342-2009")
teacher = Teacher("Mr.Kamal", 40, "Katunayake", "453-123-1985", "Mathematics")
staff = Staff("Ms.Shenika", 35, "789 St", "654-32-1990", "Admin", 5)

print(student.role_duties())
print(teacher.role_duties())
print(staff.role_duties())
