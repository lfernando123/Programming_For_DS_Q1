from person import Person

class Staff(Person):
    def __init__(self, name, age, address, ssn, role, years_of_service, base_salary=30000):
        super().__init__(name, age, address, ssn)
        self.role = role
        self.years_of_service = years_of_service
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary + (self.years_of_service * 1000)

    def role_duties(self):
        return "Manage logistics, administrative tasks, and school operations."
