import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(-2, 5), 3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 0), 0)

    # --- Subtraction Tests ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtract_resulting_in_negative(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- Multiplication Tests ---
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    # --- Division Tests ---
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_negative_result(self):
        self.assertEqual(self.calc.divide(10, -2), -5.0)

    def test_divide_by_one(self):
        self.assertEqual(self.calc.divide(7, 1), 7.0)

    def test_divide_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0.0)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()
