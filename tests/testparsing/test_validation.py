"""
Programmer: Ben Sehnert
Program: test_diagonalrow.py
Class: SE576-900-ST-18-19
Date: 8/20/2019

module name: test_validation.py
unit test for validation.py in
parsing package of classgenerator
"""
import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")
from parsing.inline import Inline
import unittest
from unittest.mock import patch
from parsing.validation import missing_field,\
continue_prompt, validate_two_piece_inline,\
validate_module_name


class TestValidation(unittest.TestCase):
    """
Class name: test_validation.py

uses unit testing to test the functionality, success and failure of validation.py
most of these functions take a str argument in the format of an inline like so
"ClassName : attr1, attr2 : method : -t -e{send,vsc}". though less sophisticated 
versions of the inline will also pass the test.

A few functions return a validated inline, but most return a [int] code
1 or 0 for success or failure of the validator. Some other functions are
prompts which get approval from a user to proceed with a test, or if they
want to proceed with parsing the inline.
    """
    
    @patch('builtins.input', return_value='y')
    def test_missing_field(self, input):
        """
        This function is the caller function 
        for below function 'continue_prompt'.
        IT defaults to class not being provided
        which fails every time. Providing an argument
        will bring up a prompt asking 
        the user if they want to proceed.

        NOTE: flip return value in the decorator to 'n'
        to see the test fail- will tell prompt not to continue
        because of the missing field. To make the same conditions
        succeed, change the second argument of the first assertEqual
        to 0, representing failure/refusal return value.
        """
        self.assertEqual(missing_field("attributes"), 1)
        self.assertEqual(missing_field(), 0)

    @patch('builtins.input', return_value='y')
    def test_continue_prompt(self, input):
        """passed 'y' it should always returns 1"""
        self.assertEqual(continue_prompt(), 1)
        self.assertEqual(continue_prompt("none"), 1)

    @patch('builtins.input', return_value='y')
    def test_validate_two_piece_inline(self, input):
        """
        possibilities:
            class : attr
            class :     
        """
        self.assertEqual(validate_two_piece_inline("ClassA : attr1, attr2"), Inline("ClassA:attr1,attr2:None:None"))
        self.assertEqual(validate_two_piece_inline("ClassA : "), Inline("ClassA : "))
    
    def test_validate_module_name(self):
        """[summary]
        """
        self.assertEqual(validate_module_name("test_validation"), "test_validation")
        self.assertEqual(validate_module_name("%#$!@.py"), 0)
    
if __name__ == "__main__":
    unittest.main()
    