"""
Programmer: Ben Sehnert
Program: classgenerator.main
Software: classgenerator
Date: 1/5/2021

facilitates generation of classes, given a single classdict 
"""

from utils.regular_class import make_class
from utils.special_class import make_abc

def class_generator(cls):
    '''
Decides what function to run to build the specified class list.
NOTE: assumes that the current working dir is the project folder and it is writable.
for inheritance, invoked inside a loop to create correct parents, children etc
    '''
    # # test for inheritance
    # if name.count(">") > 0:
    #     inheritance(name, attributes, parent)
    # elif name.startswith("ABC"):
    #     name = name[3:]
    #     make_abc(name, attributes)
    #     # parent also needs to include any parents from up the inheritance hierarchy
    # else:
    #     make_class(name, attributes, parent=parent)
    make_class(cls.classes, cls.attributes,
    methods=cls.methods, parent=cls.parents, packages="testing")
    # make_class(class.classes, class.attributes, methods=class.methods, parent=class.parents,
    # packages=class.packages, testing=class.testing, exporting=class.exporting)


def modified_generator(name, attributes, parent='object', children=None):
    '''
Works like the above generator but without possibilities for inheritance.
    '''
    if name.startswith("ABC"):
        name = name[3:]
        make_abc(name, attributes)
        # parent also needs to include any parents from up the inheritance hierarchy
    else:
        make_class(name, attributes, parent=parent)
