import unittest

def is_valid_number(number_string: str):
    if number_string.lstrip("-").isdigit():
        return True
    else:
        return False


print(is_valid_number("12aaa"))

class TestIsValidNumber(unittest.TestCase):

    def test_valid_number(self):
        #self.assertEqual('foo'.upper(), 'FOO') #sprawdz czy cos jest rownowazne
        #inaczej
        expected = True
        actual = is_valid_number("12")
        self.assertEqual(actual, expected)


    def test_negative_number(self):
        expected = True
        actual = is_valid_number("-2137")
        self.assertEqual(actual, expected)

    def test_all_letters(self):
        expected = False
        actual = is_valid_number("absjskdf")
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        expected = False
        actual = is_valid_number("")
        self.assertEqual(actual, expected)

    def test_number_with_dashes(self):
        expected = False
        actual = is_valid_number("123-213")
        self.assertEqual(actual, expected)