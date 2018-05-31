# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class String():
    def _init_(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input('Enter a string: ')

    def print_String(self):
        print(self.str1.upper())

str1 = String()
str1.get_String()
str1.print_String()



import unittest

class TestStringMethods(unittest.TestCase):

    def test_print(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_get_String(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())





  


