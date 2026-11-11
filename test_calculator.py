import unittest
from main import Calculator


class TestCalculator(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(Calculator.decimal_to_binary(10), [0, 1, 0, 1])

    def test_binary_to_decimal(self):
        self.assertEqual(Calculator.binary_to_decimal([0, 1, 0, 1]), 10)

    def test_and_gate(self):
        self.assertEqual(Calculator._AND(1, 1), 1)
        self.assertEqual(Calculator._AND(1, 0), 0)

    def test_or_gate(self):
        self.assertEqual(Calculator._OR(1, 0), 1)
        self.assertEqual(Calculator._OR(0, 0), 0)

    def test_xor_gate(self):
        self.assertEqual(Calculator._XOR(1, 0), 1)
        self.assertEqual(Calculator._XOR(1, 1), 0)

    def test_half_adder(self):
        self.assertEqual(Calculator._half_adder(1, 1), (0, 1))

    def test_full_adder(self):
        self.assertEqual(Calculator._full_adder(1, 1, 1), (1, 1))

    def test_add_fixed(self):
        result = Calculator.add_fixed(10, 20, 8)

        self.assertEqual(result["result"], 30)
        self.assertFalse(result["overflow"])

    def test_overflow(self):
        result = Calculator.add_fixed(255, 1, 8)

        self.assertEqual(result["result"], 0)
        self.assertTrue(result["overflow"])


if __name__ == "__main__":
    unittest.main()
