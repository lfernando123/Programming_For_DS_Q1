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
        # Validation of the SSN format
        if isinstance(ssn, str) and len(ssn) == 14:
            self.__ssn = ssn
        else:
            print("Invalid SSN format! Please provide a valid SSN (e.g., XXXX-XXXX-XXXX).")

    # Abstract method
    def role_duties(self):
        return "General responsibilities of a school member."
