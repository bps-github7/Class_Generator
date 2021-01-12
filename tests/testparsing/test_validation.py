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
from parsing.validation import validate_four_piece_inline

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
    -basic_validate_members
    -basic_validate
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

    # def test_missing_field(self):
    #     """[summary]
    #     """

    # def test_continue_prompt(self):
    #     """[summary]
    #     """

    # def test_validate_options(self):
    #     """[summary]
    #     """

    # def test_validate_two_piece_inline(self):
    #     """
    #     possibilities:
    #         class : attr
    #         class :     
    #     """

    # def test_validate_three_piece_inline(self):
    #     """
    #     possiblities:
    #         class : attr : method
    #         class :      : method
    #         class : attr :
    #         class :      :      
    #     """

    def test_validate_four_piece_inline(self):
        """
        possiblities:
            class : attributes : methods : options
            class : attributes : methods : 
            class : attributes :         : options
            class : attributes :         :          
            class :            : methods : options      
            class :            : methods : 
            class :            :         :         
            class :            :         : options
        """
        # full inline- works w no problems
        self.assertEqual(validate_four_piece_inline(
        "ClassA : attr1, attr2 : method1 : -t"),
        Inline("ClassA : attr1, attr2 : method1 : -t"))

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
