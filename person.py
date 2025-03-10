class Person:
    def __init__(self, name, age, address, ssn):
        self.name = name
        self.age = age
        self.address = address
        self.__ssn = ssn  # Encapsulated attribute

    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, ssn):
        self.__ssn = ssn

    def role_duties(self):
        return "General responsibilities of a school member."
