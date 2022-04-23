import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        self.employee = Employee("John", "Doe", 100_000)
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(105_000, self.employee.annual_salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(10_000)
        self.assertEqual(110_000, self.employee.annual_salary)


if __name__ == "__main__":
    unittest.main()