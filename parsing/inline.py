'''
Programmer: Ben Sehnert
Program: inline class for ClassGen program
Date: 10/28/2020
Module level docstring: implements the Inline class
'''


import sys
import re
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")
from utils.misc_functions import clean_list, cleanse
from parsing.extension import Extension

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

        ### lets do essential validation
        self.inline = inline.split(":")
        # gives progress tracking output text when set to True. 
        self.verbose = verbose
        ### Initializing these in advance to avoid not defined errors
        self.attributes = None
        self.methods = None
        self.options = {"testing" : False, "exporting" : False, "module" : False, "abc" : False}
        if self.inline[0] is None:
            print("Inline cannot be parsed if no class identifier is provided")
            return None
        else:
            # get an extension out of class name, 
            # if none is provided then sets to defaults
            self.extension = Extension(self.inline[0].strip())
            self.class_name = self.extension.class_name
            self.parents = self.extension.parents
            self.packages = self.extension.packages
            if self.verbose:
                print(f"creating inline (human readable representation) for class {self.class_name}")
        # defensive prograamming to avoid IndexError
        # in cases where no colons are provided or attr was skipped.
        if len(self.inline) > 1:
            if len(self.inline) >= 2 and self.inline[1] in ('', ' ', None):
                pass
            else:
                # trying to get rid of whitespace between commas
                self.attributes = cleanse(self.inline[1].strip())
        if len(self.inline) > 2:
            if len(self.inline) >= 3 and self.inline[2] in ('',' ',None):
                pass
            else:
                self.methods = cleanse(self.inline[2].strip())
        if len(self.inline) > 3:
            if len(self.inline) == 4:
                self.parse_options(self.inline[3].strip())

    ### getters / setters because accessing options kind of wierd with a dict
    @property
    def testing(self):
        return self.options["testing"]

    @property
    def exporting(self):
        return self.options["exporting"]

    @property
    def module(self):
        return self.options["module"]

    @property
    def abc(self):
        return self.options["abc"]


    def parse_options(self, arg):
        """[summary]

        Args:
            arg ([type]): [description]
        """
        options = arg.split("-")
        for items in options:
            if len(items) > 1:
                # for collapsable args
                for i in items:
                    self.switch_flipper(i)
            # for traditional args
            else:
                self.switch_flipper(items)
        if self.module and self.abc:
            print("Error: You cannot make an abstract base class a module.")
            return 0


    def switch_flipper(self, arg):
        """Tests the options one at a time
        to flip any switch to True if provided.

        Args:
            arg (str - technically its a chr): single character flag/switch

        Returns:
            [int]: will return 0 for errors, 1 for success
        """
        if arg in (" ",""):
            return 1
        if arg == "t":
            self.options["testing"] = True
        elif arg == "e":
            self.options["exporting"] = True
        elif arg == "m":
            self.options["module"] = True
        elif arg == "a":
            self.options["abc"] = True
        else:
            print(f"Error: {arg} option provided is not recognized (See README)")
            return 0


    ## facilitate adding parents/ packages
    ## by making the nested objects' interface more public
    def add_parents(self, new_parents):
        self.extension.add_parents(new_parents)
        self.parents = cleanse(self.extension.parents)

    def add_packages(self, new_packages):
        self.extension.add_packages(new_packages)
        self.packages = cleanse(self.extension.packages)



    def __eq__(self, other):
        if isinstance(other, self.__class__) and \
        self.class_name == other.class_name and \
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
        return repr({"classname" : self.class_name, "attributes" : self.attributes , "methods" :  self.methods, "options" : self.options})

    def __str__(self, single_line=True, show_extension=False, show_defaults=False):
        if single_line:
            if show_extension:
                if show_defaults:
                    return "{} : {} : {} : {}".format(self.extension.__str__(show_defaults-True), self.attributes, self.methods, self.options)    
                return "{} : {} : {} : {}".format(self.extension, self.attributes, self.methods, self.options)    
            return "{} : {} : {} : {}".format(self.class_name, self.attributes, self.methods, self.options)
        else:
            return \
f"Class name: {self.class_name}\n\
Attributes: {self.attributes}\n\
Methods: {self.methods}\n\
Options: {self.options}\n\
Parents: {self.parents}\n\
Packages: {self.packages}\n"


    @classmethod
    def from_details(cls, classname, attr, method, parents, packages, opts):
        return Inline(f"{classname}({parents}) ({packages}) : {attr} : {method} : {opts}")

    @classmethod
    def from_individual_arguments(cls, *args, verbose=False, ignore_extensions=False):
        """
        Builds an inline object from the component parts.
        Returns:
            [Inline] : the Inline created out of the args provided
        
        I'd like to get rid of this method at some point.
        berry bulky and easily relied upon, rather than
        a more rigerous method of validation
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
    first = Inline("ClassA(barn,house) (pillow) : attr1, attr2, attr3, attr4\
: method1, method2, method3 : -tem")

    # print(first.exporting)

    # Default arg setting seems to be working nicely
    second = Inline("ClassB")
    # print(second.exporting)

    new = [first, second]
    for items in new:
        print(items.packages)