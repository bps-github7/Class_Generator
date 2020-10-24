###Programmer: Ben Sehnert
###Program: Misc_Functions Module
###Software: Python class Generator
###Date: 1/21/2020

from Regular_Class import make_class 
from Special_Class import make_abc

"""Module defines miscellaneous functions used for the class generator"""

def class_generator(name, attributes, methods = None, parent = 'object', children = None ):
    '''
Decides what function to run to build the specified class list.
NOTE: assumes that the current working dir is the project folder and it is writable.
for inheritance, invoked inside a loop to create correct parents, children etc
    '''
    ###test for inheritance
    if name.count(">") > 0:
        inheritance(name, attributes, parent)
    elif name.startswith("ABC"):
        name = name[3:]
        make_abc(name, attributes)
        #parent also needs to include any parents from up the inheritance hierarchy
    else:
        make_class(name, attributes, parent = parent)

def modified_generator(name, attributes, parent = 'object', children = None ):
    '''
Works like the above generator but without possibilities for inheritance.
    '''
    if name.startswith("ABC"):
        name = name[3:]
        make_abc(name, attributes)
        #parent also needs to include any parents from up the inheritance hierarchy
    else:
        make_class(name, attributes, parent = parent)


def list_to_str(a, delimiter = ","):
    """
Takes a list and returns a string.
    """
    return '{}'.format(delimiter).join(map(str, a))

def custom_strip(string):
    """
Dumb I know, but strip is a method, not a callable function
    """
    return string.strip()

def str_to_list(a, delimiter = ","):
    """
Takes a string and returns  a list
    """
    #have u tried switching custom_strip with a.strip
    ## try on REPL cuz dont know why a object method isnt a callable
    return list(map(custom_strip, a.split(delimiter)))    


def inheritance(name, attributes, methods = None, parent = 'object', runs = 0):
    """
<Abstract: >
    Handles inheritance. Breaks up passed in string argument, that tells us
    the names and attribute lists for a class.
<Dev notes: >
    last updated Thursday 2/20/2020 9:27pm EST
    everything is working as hoped/expected.
    would be wise to modularize and test drive develop this some more.
    im sure there are unexpected issues lurking.
   """
    # methods = list_to_str(methods)
    family = name.split(">")
    family_attributes = attributes.split(">")
    #family_methods = methods.split(">")
    if len(family) != len(family_attributes):
        print("Error: mismatch in number of classes and attributes\n\
        Make sure that occurences of /'>/' are consistent on \n\
        both sides of : in -c option's dictionary")
        return 0
    #we now have a family of class names and class attributes,
    #belonging to the first family in the list
    parents = family[0]
    parent_attr = family_attributes[0]
    #we will enumerate the current members, delimited by a
    #comma, or backslash for attribute listings
    inheriter(parents, parent_attr, parent = parent.strip(), runs = runs)
    del family[0]
    del family_attributes[0]
    name = " > ".join(family)
    attr = " > ".join(family_attributes)
    #calling it with runs = 1 so that function knows it's been called before.
    if len(family) > 0:
        inheritance(name, attr, parent = parents.strip(), runs = 1)
    else:
        #finished succesfully!
        return 0

def inheriter(parents, parent_attr, parent = 'object', runs = 0):
    for x,y in zip(parents.split(","), parent_attr.split("/")):
        if runs == 0:
            modified_generator(x.strip(), str_to_list(y))
        #case where the inheritance function has already been invoked once.
        else:
            modified_generator(x.strip(), str_to_list(y), parent = parent)

#additional command line options.
def make_unittest(name, attr):
    with open("Test_{}.py".format(name), "a+") as file:
        file.write("import unittest \n\nfrom {} import {}".format(name,name))
        file.write("\n\n'''Module Level Docstring goes here'''\nclass Test_{}\
(unittest.TestCase):\n    '''Class Level DocString goes here'''\n    Version = 0.1\n")
        file.write("    def setUp(self):\n        self.m = {}('need to enter test values here before your unittest can be run')\n\n")

def export():
    '''Implements options for exporting the finished class file via email, ssh, tgz and etc'''
    pass

#make_methods("walp,chalp,skone,SMmode,CMnode")
#inheritance("skone, chalp, bisk > apricot, fritter", "skn1, skn2, skn3 / chalp1,chalp2,chalp3,chalp4 / bisk1,bisk2,bisk3 > apc1,apc2,apc3 / frit1,frit2,frit3,frit4,frit5,frit6")
