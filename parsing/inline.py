'''
Programmer: Ben Sehnert
Program: inline class for ClassGen program
Date: 10/28/2020
Module level docstring: implements the Inline class
'''


import sys

sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")
from utils.path_testing import NoFileNameError
from parsing.extension import Extension
from parsing.cleaning import cleanse, cleanse_methods
from parsing.validation import attributes_main, methods_main, validate_class_name, validate_field, validate_members, validate_signiture

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

    version = 4.1

    def __init__(self, inline : str, verbose = False):

        ### lets do essential validation
        self.inline = inline.split(":")
        # gives progress tracking output text when set to True. 
        self.verbose = verbose
        ### Initializing these in advance to avoid not defined errors
        self.attributes = None
        self.methods = None
        self.options = {"testing" : False, "exporting" : False,
        "module" : False, "abc" : False,
        "parents" : object, "packages" : 'root'}
        if self.inline[0] is None:
            print("Inline cannot be parsed if no class identifier is provided")
        else:
            try:
                self.extension = Extension(self.inline[0].strip())
                self.class_name = self.extension.class_name
                self.options['parents'] = self.extension.parents
                self.options['packages'] = self.extension.packages
            except NoFileNameError:
                # TODO: can define your own exception for when extension parsing goes bad.
                print("error while parsing your extension")
        if len(self.inline) > 1:
            self.attributes = attributes_main(cleanse(self.inline[1].strip()))
        if len(self.inline) > 2:
            self.methods = cleanse_methods(self.inline[2].strip(),[])
        if len(self.inline) > 3:
            if len(self.inline) == 4:
                self.parse_options(self.inline[3].strip())

    ### getters / setters - accessing options is kind of weird with a dictionary
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
                for arg in items:
                    self.switch_flipper(arg)
            # for traditional args - does this actually get used? we can yeet switch_flipper if not.
            else:
                self.switch_flipper(items)
        # raise an error if ABC and module option are provided.


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

    def add_parents(self, new_parents):
        """Facilitates adding parents
        by making nested object interface more public

        Args:
            new_parents (str): a string of new parent(s) to add.
        """
        self.extension.add_parents(new_parents)
        self.options['parents'] = cleanse(self.extension.parents)

    def add_packages(self, new_packages):
        """Facilitates adding packages
        by making nested object interface more public

        Args:
            new_packages (str): a string of new package(s) to add.
        """
        self.extension.add_packages(new_packages)
        self.options['packages'] = cleanse(self.extension.packages)

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
        return repr({"classname" : self.class_name,
            "attributes" : self.attributes,
            "methods" :  self.methods,
            "options" : self.options})

    def __str__(self):
        return "{} : {} : {} : {}".format(
            self.class_name,
            self.attributes,
            self.methods,
            self.options)

if __name__ == "__main__":
    print(Inline("classA(rodent) (rodent-well) : attr_a, attr_b :\
        method_a, method_b, method_c(a,b) : -te").__str__())
    