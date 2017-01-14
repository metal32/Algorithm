"""CREATING A NEW CLASS"""
class Employee:
    raise_amount=1.04
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+"@gmail.com"
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
        """ Class METHOD """
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount=amount
        """ Class method are used to create multiple objects"""
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, pay)
    """ Class will split the string and create multiple objects when it is called"""
emp1=Employee("Mayham","livid",50000)
emp2=Employee("Ayush","Mittal",60000)

print (emp1.email)
print (emp1.fullname())
print (emp1.pay)

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

"""THERE are total 3 type of method in python a) Regular method as seen earlier b)Class Method c) Static Method"""
emp1.set_raise_amount(1.05) 
"""IT will set the raise amount of the whole class irrespective whether what is the stance as the function is inside a
 class method and the variable is defined inside a class Employee"""

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

"""Example for class method in which we have the details of the employee in the form of a string"""

emp1_string="John-Doe-45000"

new_emp1=Employee.from_string(emp1_string)

print(new_emp1.pay)