import unittest

from src.revision.mathematics import sum, factorial, convert_temperature, lcm, hcf


class Test(unittest.TestCase):
    def test_sum_of_int_in_list(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]

        result = sum(data)

        self.assertEqual(result, 6)

    def test_factorial_of_5_is_120(self):
        """
        Test that factorial of 5 is 120
        """

        result = factorial(5)

        self.assertEqual(result, 120)

    def test_factorial_of_0_is_1(self):
        """
        Test that factorial of 0 is 1
        """

        result = factorial(0)

        self.assertEqual(result, 1)

    def test_0_degree_celsius_is_equal_to_32_degree_fahrenheit(self):
        """
        Test that 0 degree celcius is equal to 32 degree fahrenheit
        """

        result = convert_temperature(0, 'C')

        self.assertEqual(result, 32)
    
    def test_24_degree_celsius_is_equal_to_75_point_2_degree_fahrenheit(self):
        """
        Test that 24 degree celcius is equal to 75.2 degree fahrenheit
        """

        result = convert_temperature(24, 'C')

        self.assertEqual(result, 75.2)

    def test_14_degree_fahrenheit_is_equal_to_minus_10_degree_celsius(self):
        """
        Test that 24 degree fahrenheit is equal to 75.2 degree celcius
        """

        result = convert_temperature(14, 'F')

        self.assertEqual(result, -10)

    def test_minus_122_degree_fahrenheit_is_equal_to_minus_85_point_56_degree_celsius(self):
        """
        Test that -122 degree fahrenheit is equal to -85.56 degree celcius
        """

        result = convert_temperature(-122, 'F')

        self.assertEqual(result, -85.56)

    def test_lcm_of_72_and_120_is_360(self):
        """
        Test that LCM of 72 and 120 is 360
        """
        data = [72, 120]

        result = lcm(data)

        self.assertEqual(result, 360)
        
    def test_lcm_of_given_multiple_numbers_is_250(self):
        """
        Test that LCM of 25, 50, 125, 625 is 250
        """
        data = [25, 50, 125, 625]

        result = lcm(data)

        self.assertEqual(result, 250)

    def test_hcf_of_72_and_120_is_24(self):
        """
        Test that HCF of 72 and 120 is 24
        """
        data = [72, 120]

        result = hcf(data)

        self.assertEqual(result, 24)

    def test_hcf_of_given_multiple_numbers_is_8(self):
        """
        Test that HCF of 16, 8, 24 is 8
        """
        data = [16, 8, 24]

        result = hcf(data)

        self.assertEqual(result, 8)

    

if __name__ == '__main__':
    unittest.main()