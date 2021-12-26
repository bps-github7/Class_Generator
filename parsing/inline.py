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
from parsing.cleaning import cleanse
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
            return None
        else:
            try:
                self.extension = Extension(self.inline[0].strip())
                self.class_name = self.extension.class_name
                self.options['parents'] = self.extension.parents
                self.options['packages'] = self.extension.packages
            except NoFileNameError:
                # in reality, we
                #  1. will catch a nameless or invalid identifier before this point
                #  2. if we didn't, we should catch this exception futher up the call stack
                #  - think options or main
                print("error while parsing your extension")
        # defensive prograamming to avoid IndexError
        # in cases where no colons are provided or attr was skipped.
        if len(self.inline) > 1:
            self.attributes = attributes_main(cleanse(self.inline[1].strip()))
        if len(self.inline) > 2:
            self.methods = cleanse(self.inline[2].strip())
            # regular_methods = methods_main(cleanse_regular_methods(self.inline[2].strip()))
            # signitures = None
            # if self.inline[2].count("("):
            #     signitures = cleanse_with_signitures(self.inline[2].strip())
            # self.methods = self.parse_methods(regular_methods, signitures)
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

    def parse_methods(self, names : list[str], signitures = None):
        """Determines the type of each method/function passed in

        Args:
            methods ([list]): list of methods to be parsed.

        Returns:
            all_methods ([{names} {signitures}])
        """
        all_methods = {"names" :
                {"static" : [], "class" : [], "instance" : [], "functions" : []},
                "signitures" :
                {"static" : [], "class" : [], "instance" : [], "functions" : []}}
        for items in names:
            if items.startswith("sm"):
                all_methods["names"]["static"].append(items[2:])
            elif items.startswith("cm"):
                all_methods["names"]["class"].append(items[2:])
            elif items.startswith("fn"):
                all_methods["names"]["functions"].append(items[2:])
            else:
                all_methods["names"]["instance"].append(items)
        if signitures:
            for items in signitures:
                if items.startswith("sm"):
                    all_methods["signitures"]["static"].append(items[2:])
                elif items.startswith("cm"):
                    all_methods["signitures"]["class"].append(items[2:])
                elif items.startswith("fn"):
                    all_methods["signitures"]["functions"].append(items[2:])
                else:
                    all_methods["signitures"]["instance"].append(items)
        return all_methods


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
            ",".join(self.attributes),
            ",".join(self.methods),
            self.options)


    @classmethod
    def from_details(cls, classname, attr, method, parents, packages, opts):
        return Inline(f"{classname}({parents}) ({packages}) : {attr} : {method} : {opts}")

  
if __name__ == "__main__":
#     first = Inline("ClassA(barn,house) (pillow) : attr1, attr2, attr3, attr4\
# : method1, method2, method3 : -tem")

#     # print(first.exporting)

#     # Default arg setting seems to be working nicely
#     second = Inline("ClassB")
#     # print(second.exporting)

#     new = [first, second]
#     for items in new:
#         print(items.packages)

    print(Inline("Hello(Hi,Bisk,Chalp) (reindeer,dolphin):\
        attr1, sandman, CVattr2 :\
        SMname, CM*&**cone, arffff, FNnoodle, FNbasket(p, ending='cones'), CMshitbasket(x) shitcone(x,y,z), SMmotherfuck(y) :\
        -tem").__repr__())
