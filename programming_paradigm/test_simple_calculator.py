import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 7), -3)
        
        # Test zero
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, -3), -3)
        
        # Test floating point numbers
        self.assertEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertEqual(self.calc.add(-1.5, 1.5), 0.0)
        
        # Test large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        
        # Test zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        
        # Test floating point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.3), 3.2)
        self.assertAlmostEqual(self.calc.subtract(1.1, 0.1), 1.0, places=7)
        
        # Test same numbers
        self.assertEqual(self.calc.subtract(7, 7), 0)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(4, 5), 20)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        self.assertEqual(self.calc.multiply(6, -2), -12)
        
        # Test zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test one
        self.assertEqual(self.calc.multiply(1, 8), 8)
        self.assertEqual(self.calc.multiply(9, 1), 9)
        
        # Test floating point numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0)
        
        # Test large numbers
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.divide(6, 2), 3.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 2), -3.0)
        self.assertEqual(self.calc.divide(6, -2), -3.0)
        self.assertEqual(self.calc.divide(-6, -2), 3.0)
        
        # Test division by one
        self.assertEqual(self.calc.divide(5, 1), 5.0)
        self.assertEqual(self.calc.divide(-8, 1), -8.0)
        
        # Test zero dividend
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)
        
        # Test floating point numbers
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333, places=7)
        
        # Test same numbers
        self.assertEqual(self.calc.divide(5, 5), 1.0)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(1.5, 0))
        self.assertIsNone(self.calc.divide(1000000, 0))

    def test_method_return_types(self):
        """Test that methods return expected data types."""
        # Addition should return int or float based on input
        self.assertIsInstance(self.calc.add(2, 3), int)
        self.assertIsInstance(self.calc.add(2.5, 3), float)
        
        # Subtraction should return int or float based on input
        self.assertIsInstance(self.calc.subtract(5, 2), int)
        self.assertIsInstance(self.calc.subtract(5.5, 2), float)
        
        # Multiplication should return int or float based on input
        self.assertIsInstance(self.calc.multiply(3, 4), int)
        self.assertIsInstance(self.calc.multiply(3.0, 4), float)
        
        # Division should always return float (or None for division by zero)
        result = self.calc.divide(6, 2)
        self.assertIsInstance(result, float)
        
        # Division by zero should return None
        result = self.calc.divide(5, 0)
        self.assertIsNone(result)

    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Very large numbers
        large_num = 10**10
        self.assertEqual(self.calc.add(large_num, large_num), 2 * large_num)
        
        # Very small numbers (close to zero)
        small_num = 0.000001
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 2 * small_num, places=7)
        
        # Negative zero (should behave like positive zero)
        self.assertEqual(self.calc.add(-0.0, 5), 5)
        self.assertEqual(self.calc.multiply(-0.0, 100), 0)


if __name__ == '__main__':
    # Run the tests when the script is executed directly
    unittest.main()