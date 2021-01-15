"""
Programmer: Ben Sehnert
Program: test_parser.py
Date: 1/14/2021
Software: classgenerator
RepositoryURL : https://github.com/classgenerator
"""
from parsing.parser import parse
import unittest

class test_parser(unittest.TestCase):
    """
    unit testing for ensuring the proper functioning
    of modules implemented in parser module. This is
    the main module of parsing package which ensures
    validity and conformation with conventions for all
    identifiers passed in as input to the classgenerator

    subclassed:
        unittest ([std lib module]): testing framework
    """
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_parser(self) -> None:
        """[summary]
        """

    ### before moving forward with this one- i feel conflicted
    ### about the placement of functions in parser.
    ### some of these could more practically go in different modules
    ### finalize your decision b4 writing these tests here.

    # def test