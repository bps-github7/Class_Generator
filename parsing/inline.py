'''
Programmer: Ben Sehnert
Program: inline class for ClassGen program
Date: 10/28/2020
Module level docstring: implements the Inline class
'''
import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")

class Inline:
    '''
Class Level Docstring: this is a class that repersents inline class
specifications.

constructor: creates an instance of the Inline class. performs cleansing to
strip white space from fields, which is noise in the classGen mini language.

    Parameters:
        inline [str]: a string containing the following tokens
        
            -basic layout: "classes : attributes : methods : options"
            -some incomplete yet accepted alternative basic layouts:
                - "classes : : :"
                - "classes : attributes : methods : "
                - "classes : attributes : : options "
                - any combination including or excluding - attributes, methods, options
                - classes must be included, or the parsing will fail
                as a nameless class cannot be generated.

            -mutliple class layouts
                - "class1, class2 : attributes / attributes : methods / methods : options / options"
                will be parsed into indivdual basic layout:
                ["class1 : attributes : methods : options",
                "class2 : attributes : methods : options"]

            -inheritance hierarchy layout:
            "class1 > class2 : attribute1 > attribute2 : method1 > method2 : options > options" 
            will be parsed to a similar list as above, where class1 is parent of class2.


        -classes : repersents the class to be generated's identifier
        -attributes = None : repersents the class to be generated's attribute(s)
        -methods = None : repersents the class to be generated's method(s)
        -options = None : the options fpr generating the class (-t = testing, -e = exporting)
        each -t and -e can have optional argument lists appened to the end like so:
        -t{ut,cc,sa} - for unit testing, code coverage, static analysis
        -e{send,vsc,tgz,zip} - for sending via email or ssh, vsc - source code management, tgz and zip - compression algorithms


    Return values: Inline object

    Side-effects: creates an Inline object in the scope of the
    invokation/call to the constructor. Memory is consumed while
    the object is in use.

    Exceptions: Unknown at this point.
    '''

    version = 2.1

    def __init__(self, inline : str, verbose = False):
        self.inline = inline.split(":")
        self.options = None
        self.attributes = None
        self.methods = None
        #### cant make class with no name
        if inline[0] is None:
            print("Inline cannot be parsed if no class identifier is provided")
            return None
        else:
            self.classes = self.inline[0].strip().title()
            if verbose:
                print(f"creating inline (human readable representation) for class {self.classes}")
        # defensive prograamming to avoid IndexError
        # in cases where no colons are provided or attr was skipped.
        if len(self.inline) > 1:
            if len(self.inline) >= 2 and self.inline[1] in ('', ' ', None):
                pass
            else:
                self.attributes = self.inline[1].strip()
        else:
            if verbose:
                print(f"class {self.classes}: attributes not provided.")
        if len(self.inline) > 2:
            if len(self.inline) >= 3 and self.inline[2] in ('',' ',None):
                pass
            else:
                self.methods = self.inline[2].strip()
        else:
            if verbose:
                print(f"class {self.classes}: methods not provided.")
        if len(self.inline) > 3:
            if len(self.inline) == 4:
                self.options = self.inline[3].strip()
        else:
            if verbose:
                print(f"class {self.classes}: options not provided.")

    # def set_attributes(self):
    #     try:
    #         self.inline[2]
    #     except IndexError:
    #         return 0
    #     if len(inline) > 1:
    #         if len(inline) >= 2 and inline[1] in ('', ' ', None):
    #             pass
    #         else:
    #             self.attributes = self.inline[1].strip()
    #     else:
    #         print("attributes not provided")


    def has_inheritance(self):
        """checks self.classes to see if it has > token in it.
            having this token indicates inline spec has inheritance.

        Returns:
            Boolean : based off whether inline has inheritance
        """
        if self.classes.count(">"):
            return True
        return False

    def has_packaging(self):
        """checks self.classes to see if it has < token in it.
            having this token indicates inline spec has packaging.
            note: rudimentary check- more parsing required than this.

        Returns:
            Boolean : based off whether inline has packaging
        """
        return True if self.inline.count("<") else False

    def __repr__(self):
        return ":".join(self.inline)

    def __str__(self, single_line=True):
        if single_line:
            return "{} : {} : {} : {}".format(self.classes, self.attributes, self.methods, self.options)
        else:
            return "class(es): {}\n\
attributes: {}\n\
methods: {}\n\
options: {}".format(self.classes, self.attributes,
                      self.methods, self.options)

    @classmethod
    def from_individual_arguments(cls, *args, verbose=False):
        """ turns the 4 components (or less) of Inline 
                (class, attributes, methods and options)
        into an inline object. if any of the items are lists, turn them into
        comma delimited strings that Inline constructor expects. 

        NOTE: that this fn is not robust enough to handle a multiple
        class inline such as 'classA, classB : attr1, attr2 / attrA, attrB'

        Returns:
            [type]: [description]
        """
        items = [*args]
        for i, value in enumerate(items):
            if value is None:
                continue
            if isinstance(value, list):
                items[i] = ",".join(value)
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

    @staticmethod
    def cleanse(items: any):
        """format properties by strip and lowercase of each elements.
        side-effect: coerces ',' delimited string to formatted list.
        """
        if isinstance(items, list):
            return list(map(
                lambda item: item.strip().lower(), items))
        return list(map(
            lambda item: item.strip().lower(), items.split(",")))

if __name__ == "__main__":
    # also not reading -e values now
    print(Inline.from_individual_arguments("ClassA","attr1, attr2"))

    # instead of rewriting the constructor, wrote this
    # classmethod/alt constructor for this use case
    # item = Inline.from_individual_arguments("Biscuit", ['gravy', 'sausage'], ['method1', 'method2'], '-t -e{ut}')
    # print(item)
    # # items = Inline.from_individual_arguments("Biscuit",
    # ['gravy', 'sausage'], ['method1', 'method2'], '-t -e{ut}')
    # print(items)

