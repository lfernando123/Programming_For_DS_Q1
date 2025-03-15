from person import Person

class Teacher(Person):
    def __init__(self, name, age, address, ssn, subject):
        super().__init__(name, age, address, ssn)
        self.subject = subject
        self.class_schedule = {}

    def schedule_classes(self, schedule):
        self.class_schedule = schedule

    def role_duties(self):
        return "Teach classes, assign grades, and prepare lessons."
