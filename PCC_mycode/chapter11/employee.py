class Employee():

    def __init__(self, first_name, last_name, salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, araise=5000):

        self.salary += araise


emp1 = Employee('john', 'lo', 10000)
print (emp1.first_name, emp1.last_name, emp1.salary)
emp1.give_raise()
print (emp1.first_name, emp1.last_name, emp1.salary)
emp1.give_raise(1000)
print (emp1.first_name, emp1.last_name, emp1.salary)
