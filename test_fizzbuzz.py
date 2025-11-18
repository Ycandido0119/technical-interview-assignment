import unittest
from io import StringIO
import sys
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        """Capture stdout for testing print statements"""
        self.held_output = StringIO()
        sys.stdout = self.held_output
    
    def tearDown(self):
        """Reset stdout after each test"""
        sys.stdout = sys.__stdout__
    
    def get_output(self):
        """Helper method to get captured output"""
        return self.held_output.getvalue().strip()

    # Test cases for fizz/buzz logic
    def test_number_divisible_by_3_prints_fizz(self):
        fizzbuzz(3, 3)
        output = self.get_output()
        self.assertIn("Fizz", output)
        self.assertIn("3", output)

    def test_number_divisible_by_5_prints_buzz(self):
        fizzbuzz(5, 5)
        output = self.get_output()
        self.assertIn("Buzz", output)
        self.assertIn("5", output)
    
    def test_number_divisible_by_3_and_5_prints_fizzbuzz(self):
        fizzbuzz(15, 15)
        output = self.get_output()
        self.assertIn("Fizz", output)
        self.assertIn("Buzz", output)
        self.assertIn("15", output)

    def test_number_not_divisible_by_3_or_5_prints_number(self):
        fizzbuzz(7, 7)
        output = self.get_output()
        self.assertEqual(output, "7")
        self.assertNotIn("Fizz", output)
        self.assertNotIn("Buzz", output)

    # Test cases for error handling
    def test_first_number_too_small(self):
        with self.assertRaises(ValueError) as context:
            fizzbuzz(0, 10)
        self.assertIn("between 1 and 100", str(context.exception))

    def test_second_number_too_large(self):
        with self.assertRaises(ValueError) as context:
            fizzbuzz(10, 101)
        self.assertIn("between 1 and 100", str(context.exception))
    
    def test_first_number_greater_than_second(self):
        with self.assertRaises(ValueError) as context:
            fizzbuzz(20, 10)
        self.assertIn("The first number must be less than or equal to the second number", str(context.exception))
    
    def test_both_numbers_out_of_range(self):
        with self.assertRaises(ValueError) as context:
            fizzbuzz(-5, 150)
        self.assertIn("between 1 and 100", str(context.exception))

    def test_first_number_equal_to_second(self):
        fizzbuzz(10, 10)
        output = self.get_output()
        self.assertIn("Buzz", output)
        self.assertIn("10", output)

if __name__ == '__main__':
    unittest.main()
