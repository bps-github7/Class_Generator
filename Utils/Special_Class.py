###Programmer: Ben Sehnert
###Program: Special_Class module
###Software: Python Class Generator
###Date: 1/21/2020

"""Defines functions for making abstract base class and other special functions."""
###TODO: Some things to fix here:
### -does not inherit from metaclass = ABC
###-need to reference a good template as per what abc should look like (does anything get implemented like getters, setters, should init take arguments for its instance variables?)
###-should setters take argument? should properties use abstractproperty decorator as per Python 2.7 documentation on ABCs.
###-need answers on these before fully completely implementing ABC generator
def abc_init(file, name, attributes):
    """
Completes the abc init statement by writing attributes to the file
    """
    file.write("    def __init__(self):\n        pass\n\n")
    
def abc_repr(file, attributes):
    '''writes class repr method to a file, given the file object and attribute list'''
    file.write("    def __repr__(self):\n        pass\n\n")
    
def abc_str(file, name, attributes):
    '''Writes class __str__ method to a file, given the file object and attribute list'''
    file.write("    def __str__(self):\n        pass\n\n")

def abc_getter(file, a):
    '''writes the getter for one attribute in pip 3.8 syntax, given the file object and attribute a'''
    file.write("    @abc.abstractmethod\n    @property\n    def {}(self):\n        pass\n\n".format(a))
    
def abc_setter(file, a):
    '''writes the setter for one attribute in the new syntax, given the file object and attribute a'''
    file.write("    @abc.abstractmethod\n    @{}.setter\n    def {}(self):\n        pass\n\n".format(a, a))

def make_abc(name, attributes, methods = None, parent = "metaclass = abc.ABCMeta"):
    with open("{}.py".format(name), "a+") as file:
        file.write("from abc import ABC\n\nclass {}({}):\n".format(name, parent))
        abc_init(file, name, attributes)
        abc_repr(file, attributes)
        abc_str(file, name, attributes)
        for attribute in attributes:
            abc_getter(file, attribute)
        for attribute in attributes:
            abc_setter(file, attribute)
        # for method in methods:
        #     methods(method)

#make_abc("abc_testing", ["balp","kalp","stalp"])