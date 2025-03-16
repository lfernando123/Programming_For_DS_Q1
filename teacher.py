from person import Person

class Teacher(Person):
    def __init__(self, name, age, address, ssn, subject):
        super().__init__(name, age, address, ssn)
        self.subject = subject
        self.class_schedule = {}


    def schedule_classes(self, day, time):
        """Assigns a class schedule for the teacher."""
        self.class_schedule[day] = time


    def display_schedule(self):
        """Displays the teacher's class schedule."""
        if not self.class_schedule:
            return f"{self.name} has no scheduled classes."
        schedule = "\n".join([f"{day}: {time}" for day, time in self.class_schedule.items()])
        return f"Class Schedule for {self.name}:\n{schedule}"
    

    def role_duties(self):
        return "Teach classes, assign grades, and prepare lessons."
