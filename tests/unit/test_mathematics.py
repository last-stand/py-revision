import unittest

from src.revision.mathematics import sum, factorial


class Test(unittest.TestCase):
    def test_sum_of_int_in_list(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]

        result = sum(data)

        self.assertEqual(result, 6)

    def test_factorial_of_given_number(self):

        result = factorial(5)

        self.assertEqual(result, 120)
    

if __name__ == '__main__':
    unittest.main()