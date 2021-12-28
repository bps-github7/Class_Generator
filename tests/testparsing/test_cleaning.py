"""
Programmer: Ben Sehnert
Program: test_cleaning.py
Date: 12/28/2021
Software: classgenerator
Repository-URL : https://github.com/classgenerator

unit testing for the cleaning module, which santiizes strings
so that the generator creates properly formatted classes and files.
"""

import unittest

import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")


from parsing.cleaning import cleanse, cleanse_methods

class test_inline(unittest.TestCase):
    """[summary]

    Subclassed:
        unittest ([type]): [description]
    """
    def setUp(self):
        """[summary]
        """
    
    def tearDown(self):
        """[summary]
        """

    def test_cleanse(self):
        """can take either comma delimited string or <string []>.
        """
        self.assertEqual(cleanse("attr_a, attr_b, attr_c"), ['attr_a', 'attr_b', 'attr_c'])
        self.assertEqual(cleanse(["ATTR_A", "ATTR_B", "ATTR_C"]), ['attr_a', 'attr_b', 'attr_c'])

        #TODO: there will be more use cases... do these go in a seperate test fn?


    def test_cleanse_methods(self):
        """lowercases and strips whitespace from method names, parses any signitures into object.
        """
        self.assertEqual(cleanse_methods("Example_a, exAMPle_b, example_c",[]),
        ['example_a','example_b','example_c'])

        self.assertEqual(cleanse_methods("example_a, example_b, example_c(a,b,c=80)",[]),
        ['example_a','example_b',{'name' : 'example_c', 'parameters' : 'a,b,c=80'}])

if __name__ == "__main__":
    unittest.main()