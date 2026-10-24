import unittest
from validation import is_valid_quantity, calculate_discount

class TestQuantityValidation(unittest.TestCase):
    def test_quantity_boundaries(self):
        cases = [(0, False), (1, True), (2, True), (99, True), (100, True), (101, False)]
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(is_valid_quantity(value), expected)

    def test_invalid_types(self):
        for value in (10.5, "abc", None):
            with self.subTest(value=value):
                self.assertFalse(is_valid_quantity(value))

class TestDiscountCalculation(unittest.TestCase):
    def test_student_gets_discount(self):
        self.assertEqual(calculate_discount(1000, "student"), 900)
        
    def test_teacher_gets_discount(self):
        self.assertEqual(calculate_discount(1000, "teacher"), 900)
        
    def test_guest_has_no_discount(self):
        self.assertEqual(calculate_discount(1000, "guest"), 1000)

if __name__ == "__main__":
    unittest.main()