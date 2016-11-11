import unittest

import manipulatron


class Test1(unittest.TestCase):
    def test_string_converted_to_upper_case(self):
        self.assertEqual("HELLO", manipulatron.upper("hello"))

    def test_string_converted_to_lower_case(self):
        self.assertEqual("hello", manipulatron.lower("HELLO"))

    def test_string_stripped(self):
        self.assertEqual("hello", manipulatron.strip("   hello    "))

    def test_knights_say_ni(self):
        self.assertEqual("Ni!", manipulatron.knights_say_ni())
