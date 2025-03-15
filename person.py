'''Making base class Person and its methods abstract to prevent instantiation of the 
class and to enforce the implementation of the role_duties method in the derived classes.'''
class Person:
    def __init__(self, name, age, address, ssn):
        self.name = name
        self.age = age
        self.address = address
        self.__ssn = ssn  # Encapsulated attribute

    # Get method for the ssn attribute
    def get_ssn(self):
        return self.__ssn

    # Set method for the ssn attribute
    def set_ssn(self, ssn):
        self.__ssn = ssn

    # Abstract method
    def role_duties(self):
        return "General responsibilities of a school member."
