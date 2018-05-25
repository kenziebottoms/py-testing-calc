import unittest
from calculator import Calculator


def setUpModule():
    print('Setting up module...')


def tearDownModule():
    print('Tearing down module...')


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Setting up class...')
        self.calc = Calculator()

    @classmethod
    def tearDownClass(self):
        print('Tearing down class...')

    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(7, 2), 5)

    # Write test methods for subtract, multiply, and divide


if __name__ == '__main__':
    unittest.main()
