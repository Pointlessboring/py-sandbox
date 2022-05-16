import unittest
import random
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):

        self.raises = []
        self.first_name = 'john'
        self.last_name = 'wayne'
        self.employee = Employee(self.first_name, self.last_name, 0)
        
        for n in range (1,11):
            self.raises.append(random.randint(1,10)*1000)
    
    def test_give_default_raise(self):
        base = self.employee.salary
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, base+5000)

    def test_give_custom_raise(self):
        base = self.employee.salary
        new_salary = base
        for amount in self.raises:
            self.employee.give_raise(amount)
            new_salary += amount
        self.assertEqual(self.employee.salary, new_salary)
        print(f"Base: {base}")
        print(f"Raises: {self.raises}")
        print(f"New aalary: {new_salary}")

if __name__ == "__main__":
    unittest.main()