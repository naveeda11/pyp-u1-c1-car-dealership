class Person(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    def is_employee(self):
        return NotImplementedError()

class Customer(Person):
    def is_employee(self):
        return False

class Employee(Person):
     def is_employee(self):
        return True
