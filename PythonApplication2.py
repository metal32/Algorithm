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
        

    """ Inheritance"""
class Developer(Employee):
    raise_amount=1.10
    def __init__(self, first, last, pay, prog_lan):
        Employee.__init__(self, first, last, pay)  
        self.prog_lan=prog_lan
        """As we have already defined first,last and pay in employee class, so instead of defining them again
        we can use super function with init to define them and it will automatically take the value from employee class"""

class Manager(Employee):
    raise_amount=1.15
    def __init__(self,first,last,pay,employees=None):
        Employee.__init__(self,first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print ("-->",emp.fullname())
        

emp1=Employee("Rishab","Garg",30000)
emp2=Employee("Ayush","Mittal",60000)

dev1=Developer("Mayham","livid",50000,"Python")
dev2=Developer("Ayush","Mittal",60000,"Ruby")

mang1=Manager("Ashish","Ranot",100000,[dev1,dev2])

print(mang1.fullname())
print(mang1.pay)
mang1.apply_raise()
print(mang1.pay)
#mang1.print_emp()
mang1.add_emp(emp1)
mang1.print_emp()

print(isinstance(mang1,Manager))
#print(dev1.pay)
#dev1.apply_raise()
#print(dev1.pay)

#print(emp1.pay)
#emp1.apply_raise()
#print(emp1.pay)
#print (emp1.email)
#print (emp1.fullname())
#print (emp1.pay)

#print(dev1.prog_lan)
#print(emp2.raise_amount)
#print(Employee.raise_amount)