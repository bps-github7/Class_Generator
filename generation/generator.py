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
    print("doing the generation thing!")
    # makes the clss an abc if name is prepended with ABC    
    # if cls.classes.startswith("ABC"):
    #     cls.classes = cls.classes[3:]
    #     make_abc(cls.classes, cls.attributes)

    # # test_path validates packages/ does the package exist, is it writable etc? 
    # # returns 1 for root, the path to a validated package, or a list of paths to validated packages
    # ##### so we need to test all these cases to write classes appropriately.
    # path = test_path(cls.packages)
    # if path == 1:
    #     # when user doesnt specify a package, use 'root' || './' (cwd where script was invoked)
    #     make_class(cls.classes, cls.attributes,
    #     methods=cls.methods, parents=cls.parents)
    # elif isinstance(path, list):
    #     # makes class in multiple packages if the specs call for that.
    #     for items in path:
    #         make_class(cls.classes, cls.attributes,
    #         cls.methods, parents=cls.parents, packages=items)
    # # being specific prevents class from being generated when package/path was invalid
    # elif path != 0:
    #     make_class(cls.classes, cls.attributes,
    #     methods=cls.methods, parents=cls.parents, packages=path)


# def modified_generator(name, attributes, parents='object', children=None):
#     '''
# Works like the above generator but without possibilities for inheritance.
#     '''
#     if name.startswith("ABC"):
#         name = name[3:]
#         make_abc(name, attributes)
#         # parent also needs to include any parents from up the inheritance hierarchy
#     else:
#         make_class(name, attributes, parents=parents)
