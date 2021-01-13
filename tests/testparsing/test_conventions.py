"""
Programmer: Ben Sehnert
Program: Unit tests for conventions.py module
Software: classgenerator
Date: 1/13/2021

unittesting for the conventions.py file which
contains functions that correct and or validate
identifiers provided through a users inline specification.
"""
version = 1.0

import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")
import unittest
from unittest.mock import patch
from unittest.mock import Mock
# maybe conventions belongs in parsing instead ? >>>
from utils.conventions import is_identifier, ask_case, case_check,\
coerce_case, case_prompt, class_correct_convention, field_correct_convention,\
package_correct_convention, module_correct_convention


# for testing prompts w/ multiple possible answers
# m = Mock()
# m.side_effects = ['y', 'n']
##### See commented out line in case_prompt- this isnt working as expected.

class TestConventions(unittest.TestCase):
    """Provides comprehensive testing for all functions in conventions.py.

    Subclassed:
        unittest (std library module): provides testing framework.
    """
    def set_up(self):
        """[summary]
        """

    def tear_down(self):
        """[summary]
        """
    
    def test_is_identifier(self):
        """[summary]
        """
        self.assertEqual(is_identifier("Example"), True)
        self.assertEqual(is_identifier("%$#@!"), False)

    @patch('builtins.input', return_value='y')
    def test_ask_case(self, input):
        """Because 'banana' is lowercase and no item_type is provided
        ask_case will ask if the class name should be titlecased, input
        of 'y' is provided and the case corrected identifier is returned.
        """
        self.assertEqual(ask_case("banana"), "Banana")
        self.assertEqual(ask_case("HORSE_GUM", item_type="field"), "horse_gum")

    @patch('builtins.input', return_value='y')
    def test_case_check(self, input):
        """case_check(item, item_type="class", preferences="ask")
        """
        # case 1- leave preference as 'ask'- will take y from builtins.input
        # and return a case corrected class identifier
        self.assertEqual(case_check("example"), "Example")

        # change item_type to field and preferences to corece-
        # automatically convert the item to lowercase and add underscrores.
        self.assertEqual(case_check("GOAT BISCUIT", item_type="field", preferences="coerce"), "goat_biscuit")
        
        # preference is none so the item is returned with no side-effects
        self.assertEqual(case_check("butter", preferences="none"), "butter")


    
    def test_coerce_case(self):
        """How can we deal with the cases where 
        there is no whitespace between ident words?

        this function is pretty limited (for now) if this can be achieved.
        """
        self.assertEqual(coerce_case("banana_sundae"), "BananaSundae")
        self.assertEqual(coerce_case("BATTLESHIP_NO", item_type="field"), "battleship_no")
        self.assertEqual(coerce_case("Bagel Machinery", item_type="package"), "bagelmachinery")
        self.assertEqual(coerce_case("Fast_Mongoose", item_type="module"), "fast_mongoose")


    @patch('builtins.input', return_value='y')
    def test_case_prompt(self, input):
        """Signiture:
            case_prompt(item, item_type="class)
        """
        self.assertEqual(case_prompt("banana"), 1)

        # how do i pass multiple return values to unittest.mock.patch
        # self.assertEqual(case_prompt("Banana", item_type="n"), 0)



    def test_class_correct_convention(self):
        """[summary]
        """
        self.assertEqual(class_correct_convention("Corrected Biscuit"), "CorrectedBiscuit")
        self.assertEqual(class_correct_convention("muffin_hustler"), "MuffinHustler")
    
    def test_field_correct_convention(self):
        """[summary]
        """
        self.assertEqual(field_correct_convention("BISCUIT BRIGADE"), "biscuit_brigade")

        # this isnt 100% desirable outcome- see comments about handling lack of whitespace above.
        self.assertEqual(field_correct_convention("TrouserPolitician"), "trouserpolitician")
    
    def test_package_correct_convention(self):
        """[summary]
        """
        self.assertEqual(package_correct_convention("s_T_un_T"), "stunt")
        self.assertEqual(package_correct_convention("WAFFLE_copter"), "wafflecopter")
    

    def test_module_correct_convention(self):
        """[summary]
        """
        self.assertEqual(module_correct_convention("Bacon Hound"), "bacon_hound")
        self.assertEqual(module_correct_convention("Fresh_PIZZA"), "fresh_pizza")
    


if __name__ == "__main__":
    unittest.main()