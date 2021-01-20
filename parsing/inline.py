'''
Programmer: Ben Sehnert
Program: inline class for ClassGen program
Date: 10/28/2020
Module level docstring: implements the Inline class
'''

import sys
import re
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")
from utils.misc_functions import clean_list

class Inline:
    '''
Class Level Docstring: this is a class that repersents inline class
specifications.

Return values: Inline object

Side-effects: creates an Inline object in the scope of the
invokation/call to the constructor. Memory is consumed while
the object is in use.

Exceptions: Unknown at this point.
    '''

    version = 4.0

    def __init__(self, inline : str, verbose = False):
        self.inline = inline.split(":")
        # gives progress tracking output text when set to True. 
        self.verbose = verbose
        ### Initializing these in advance to avoid not defined errors
        self.attributes = None
        self.methods = None
        self.options = None
        self.defensive_initialize()

    def defensive_initialize(self):
        """Keeps the Inline from being
        Initialized with incorrect or badly
        formated values.

        Returns:
            [type]: [description]
        """
        #### cant make class with no name
        if self.inline[0] is None:
            print("Inline cannot be parsed if no class identifier is provided")
            return None
        else:
            self.classes = self.inline[0].strip()
            self.get_extension()
            if self.verbose:
                print(f"creating inline (human readable representation) for class {self.classes}")
        # defensive prograamming to avoid IndexError
        # in cases where no colons are provided or attr was skipped.
        if len(self.inline) > 1:
            if len(self.inline) >= 2 and self.inline[1] in ('', ' ', None):
                pass
            else:
                self.attributes = self.inline[1].strip()
        if len(self.inline) > 2:
            if len(self.inline) >= 3 and self.inline[2] in ('',' ',None):
                pass
            else:
                self.methods = self.inline[2].strip()
        if len(self.inline) > 3:
            if len(self.inline) == 4:
                self.options = self.inline[3].strip()

    def get_extension(self):
        """Handles any case where class meta data
        is passed in when Inline is initialized.
        """
        ### example(parents) (packages)
        if self.classes.count(") ("):
            classes = self.classes.split(") (")
            self.classes = classes[0].split("(")[0].strip()
            self.parents = classes[0].split("(")[1].strip()
            self.packages = classes[1].strip(")")
        ### Only the packaging - example (packages)
        elif self.classes.count(" ("):
            classes = self.classes.split(" (")
            self.classes = classes[0].strip()
            self.parents = object
            self.packages = classes[1].strip(")").strip()
        ### only the parent - example(parents)
        elif re.match(r"(\w)*[()]", self.classes):
            # the python equivalent of above expression
            # will snag on undesired tokens, resulting in wrong values.
            classes = self.classes.split("(")
            self.classes = classes[0].strip()
            self.parents = classes[1].strip(")").strip()
            self.packages = "root"
        else:
            self.classes = self.classes.strip()
            self.parents = object
            self.packages = "root"

    def __eq__(self, other):
        if isinstance(other, self.__class__) and \
        self.classes == other.classes and \
        self.attributes == other.attributes and \
        self.methods == other.methods and \
        self.options == other.options:
            return True
        print("Not the same Inline")
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        # not safe but what can we do?
        return self.__str__()

    def __str__(self, single_line=True, simple_print=False):
        if single_line:
            if simple_print:
                return "{} : {} : {} : {}".format(self.classes, self.attributes, self.methods, self.options)
            classes = f"{self.classes}({self.parents}) ({self.packages})"
            return "{} : {} : {} : {}".format(classes, self.attributes, self.methods, self.options)
        else:
            return "class(es): {}\n\
attributes: {}\n\
methods: {}\n\
options: {}".format(self.classes, self.attributes,
                      self.methods, self.options)

    @classmethod
    def from_details(cls, classname, attr, method, parents, packages, opts):
        return Inline(f"{classname}({parents}) ({packages}) : {attr} : {method} : {opts}")

    @classmethod
    def from_individual_arguments(cls, *args, verbose=False, ignore_extensions=False):
        """
        Builds an inline object from the component parts.
        Returns:
            [type]: [description]
        """
        items = clean_list(args)
        if ignore_extensions:
            class_names = []
            if items[0].count("),"):
                classes = items[0].split("),")
                for item in classes:
                    if item.count("("):
                        class_names.append(item.split("(")[0])
        items[0] = ",".join(class_names)
        if len(items) == 1:
            return Inline(items[0], verbose=verbose)
        elif len(items) == 2:
            return Inline(f"{items[0]}:{items[1]}", verbose=verbose)
        elif len(items) == 3:
            return Inline(f"{items[0]}:{items[1]}:{items[2]}", verbose=verbose)
        elif len(items) == 4:
            return Inline(f"{items[0]}:{items[1]}:{items[2]}:{items[3]}", verbose=verbose)
        else:
            print("cannot generate inline with more than 4 (: delimited)\
arguments\nRefer to the README file for instructions on proper inline format")
            return 0

if __name__ == "__main__":
    first = Inline.from_individual_arguments("ClassA(aloha, doorknob-grenade) (biscuits, chalpskone, arf), ClassB(A1,A2) (PA,PB)", ['attr1', 'attr2'], ['method1', 'method2'], "-t -e", ignore_extensions=True)
    # second = Inline.from_details("ClassA", ['attr1', 'attr2'], ['method1', 'method2'], "funky, bisk, capitler", "Hi Moofa, Chalpskone", "-t -e")
    print(first.classes)
    # new = [first, second]

    # print(new)
    # for i in new:
    #     print(i.classes)
    #     print(i.attributes)
    #     print(i.methods)
    #     print(i.parents)
    #     print(i.packages)
    #     print(i.options)
    #     print("\n\n")