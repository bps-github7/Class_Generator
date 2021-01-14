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
from parsing.validation import validate_four_piece_inline, missing_field,\
continue_prompt, validate_multiple_packaging_inline, validate_file,\
validate_inline, validate_options, validate_two_piece_inline,\
validate_three_piece_inline, validate_multiple, validate_inheritance,\
validate_module_name, validate_package_name, validate_single_packaging_inline,\
validate_members, validate_packaging


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

the following functions are tested:
    -missing_fields
    -continue_prompt
    -validate_options
    -validate_two_piece_inline
    -validate_three_piece_inline
    -validate_four_piece_inline
    -validate_members
    -validate_inline
    -validate_multiple
    -validate_inheritance
    -validate_packaging
    -validate_single_packaging_inline
    -validate_multiple_packaging_inline
    -validate_package_name
    -validate_module_name
    """
    # def set_up(self):
    #     """[summary]
    #     """
    #     self.valid_inline = ""

    # def tear_down(self):
    #     """[summary]
    #     """

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

    # TODO this should handle the whitespaces as expected
    # def test_validate_options(self):
    #     """
    #     validate_options should coerce an option set
    #     to a desired format and thus remove whitespace
    #     between flag args to a reasonable amount ie.
    #     no more than one space between flags,
    #     """
    #     self.assertEqual(validate_options(" -t"), "-t")
    #     self.assertEqual(validate_options("-e "), "-e")
    #     self.assertEqual(validate_options("-t{ut,cc}    "), "-t{ut,cc}")
    #     self.assertEqual(validate_options("    -e{vsc}"), "-e{vsc}")
    #     self.assertEqual(validate_options("-e{vsc}    -t"), "-e{vsc} -t")

    # NOTE there are 3 other methods for testing w/ unittest
    # assertTrue, assertFalse and assertException
    # use them son
    def test_validate_two_piece_inline(self):
        """
        possibilities:
            class : attr
            class :     
        """
        # have to prevent the sub functions from coercing ClassA -> Classa
        self.assertEqual(validate_two_piece_inline("ClassA : attr1, attr2"), Inline("ClassA:attr1,attr2:None:None"))

    # def test_validate_three_piece_inline(self):
    #     """
    #     possiblities:
    #         class : attr : method
    #         class :      : method
    #         class : attr :
    #         class :      :      
    #     """

    # TODO very irritatingly broken
    # def test_validate_four_piece_inline(self):
    #     """
    #     possiblities:
    #         class : attributes : methods : options
    #         class : attributes : methods : 
    #         class : attributes :         : options
    #         class : attributes :         :          
    #         class :            : methods : options      
    #         class :            : methods : 
    #         class :            :         :         
    #         class :            :         : options
    #     """
    #     # full inline- works w no problems
    #     self.assertEqual(validate_four_piece_inline(
    #     "ClassA : attr1, attr2 : method1 : -t"),
    #     Inline("ClassA : attr1, attr2 : method1 : -t"))

        # # full inline minus options
        # self.assertEqual(validate_four_piece_inline(
        # "ClassA : attr1, attr2 : method1 : "),
        # Inline("ClassA : attr1, attr2 : method1 : "))

        # # full inline minus methods
        # self.assertEqual(validate_four_piece_inline(
        # "ClassA : attr1, attr2 : : -t "),
        # Inline("ClassA : attr1, attr2 : : -t "))

        # # methods and options missing
        # self.assertEqual(validate_four_piece_inline(
        # "ClassA : attr, batter :  : "),
        # Inline("ClassA : attr, batter :  : "))

        # # attributes missing
        # self.assertEqual(validate_four_piece_inline(
        # "ClassA : : method :-t"),
        # Inline("ClassA : : method :-t"))

        # # attributes and options missing
        # self.assertEqual(validate_four_piece_inline(
        # "ClassA : : method :"),
        # Inline("ClassA : : method :"))

        # # attributes and methods missing
        # self.assertEqual(validate_four_piece_inline(
        # "ClassA : : :-e -t"),
        # Inline("ClassA : : :-e -t"))

        # # attributes methods and options missing
        # self.assertEqual(validate_four_piece_inline(
        # "ClassA : : :"),
        # Inline("ClassA : : :"))

    # def test_validate_members(self):
    #     """[summary]
    #     """

    # def test_validate_inline(self):
    #     """[summary]
    #     """

    # def test_validate_multiple(self):
    #     """[summary]
    #     """

    # def test_validate_inheritance(self):
    #     """[summary]
    #     """

    # def test_validate_packaging(self):
    #     """[summary]
    #     """

    # def test_validate_multiple_packaging_inline(self):
    #     """[summary]
    #     """

    # def test_validate_single_packaging_inline(self):
    #     """[summary]
    #     """

    # def test_validate_package_name(self):
    #     """[summary]
    #     """
    
    # def test_validate_module_name(self):
    #     """[summary]
    #     """
    
if __name__ == "__main__":
    unittest.main()
