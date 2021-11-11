"""
Programmer: Ben Sehnert
Program: extesnion.py module
Software: python file generator
Date: 1/29/2021

"""


import re



# from utils.conventions import is_identifier

# grabbed this from conventions because... language server in vscode needs configuring, cant find imports clearly in sys path
import keyword

def is_identifier(ident: str) -> bool:
    """Determines if string is valid Python identifier.

    ident [str] - the real time value of identifier

    returns [bool]- True or False based on whether
    the ident argument is an identifier.
    """

    if not isinstance(ident, str):
        raise TypeError("expected str, but got {!r}".format(type(ident)))

    if not ident.isidentifier():
        return False

    if keyword.iskeyword(ident):
        return False

    return True

class NoFileNameError(Exception):
    '''
exception for cases where user is trying
to generate a file but
1) did not provide file name
2) did not provide a valid file name (invalid idenfier)
    '''
    def __init__(self, error, value):
        self.error = error
        self.value = value


class Extension:

    """
implements the first part of the Inline
provides dynamic utility, in cases where
either, niether or both argument parts of the extension are provided.
    """
    def __init__(self, ext):
        """Constructs an extension based off a plain string
        containing the correct extension syntax

        Args:
            ext (string): plain string which contains the extension syntax.
            this may define the parent, package or both, but will always associate
            these values with a class name, which inherits from these parents and
            is located in the list of directories named in the packages.
        """
        cls_name = (ext.split("(")[0]).strip()
        self.class_name = None
        self.parents = object
        self.packages = 'root'
        if is_identifier(cls_name):
            self.class_name = ext.split("(")[0].strip()
        else:
            # no point generating extension if we cant generate a file
            # strip the parens if invalid class name has them
            invalid = ext.split('(')[0].strip() if ext.count("(") else ext            
            print(f"Cannot produce a file with name {invalid}.\n\
Not a valid identifier")
            raise NoFileNameError("Invalid Identifier", invalid)    
        if ext.count("("):
            if " (" in ext:
                # take the packages portion of ext and strip all parens
                self.packages = ext[ext.find(" ("):].strip(" (").strip(")")
                rest = ext[:ext.find(" (")]
                if "(" in rest:
                    self.parents = rest.split("(")[1].strip(")")
                    del rest
            else:
                if "(" in ext:
                    self.parents = ext.split("(")[1].strip(")")

    def __str__(self, show_defaults=False, show_extension=True):
        if show_extension:
            if show_defaults:
                return f"{self.class_name}({self.parents}) ({self.packages})" 
            if self.parents == object:
                if self.packages == 'root':
                    return f"{self.class_name}"
                else:
                    return f"{self.class_name} ({self.packages})"
            else:
                if self.packages == 'root':
                    return f"{self.class_name}({self.parents})"
                return f"{self.class_name}({self.parents}) ({self.packages})"
        else:
            return f"{self.class_name}"


    def __repr__(self):
        return repr({"classname": self.class_name, "parents" : self.parents,
"packages" : self.packages})


    def replace_parents(self, replacement):
        """[summary]

        Args:
            replacement ([type]): [description]
        """
        if self.parents == "<class 'object'>":
            self.parents = ''
        else:
            self.parents = f"{self.parents}"

    def replace_package(self, replacement):
        """[summary]

        Args:
            replacement ([type]): [description]
        """
        self.packages = f"{self.packages}{','}"

    def add_parents(self, new_parents):
        """remove existing parents entry and provide a new one.

        Args:
            new_parents (str): the parent or comma delimited str of parents to replace. 
        """
        # double quotes are required for truthful test of whether something is an object
        isObject = lambda obj : isinstance(obj,object)

        if self.parents and isinstance(self.parents,object):

        # without the lambda, double quotes inside f-str...
        # self.parents =f"{f'{self.parents},' if not isObject(self.parents) and self.parents else ''}{new_parents}"

    def add_packages(self, new_packages):
        """[summary]

        Args:
            new_packages ([type]): [description]
        """
        # dont forget your ,
        self.packages = f"{self.packages}{new_packages}"



    @classmethod
    def from_individual_arguments(cls, class_name : str, parents = object, packages = "root"):
        """Creates an extension based on the three components in the syntax
            classA(parentA,parentB) (package1, package2)

        Args:
            class_name (str): the name of class being defined with this extension.
            parents (str or object, optional): the parent or parents who this class
             inherits from. Defaults to object.
            packages (str, optional): comma delimited string of names of directories
             that should contain the file. Defaults to "root".

        Returns:
            Extension: [description]
        """
        if 'object' in str(parents):
            if 'root' in str(packages):
                return Extension(f"{class_name}")
            else:
                return Extension(f"{class_name} ({packages})")
        return Extension(f"{class_name}({parents}) ({packages})")

def main():
    """Running some tests to ensure constructors work as expected.
    """
    test = Extension("ClassA(file1,file2) (package1,package2)")


    # test.add_parents("bisk, chalp, neckbro")
    # print(test.__str__(show_defaults=True))
    # test = Extension.from_individual_arguments("ClassA", packages='gorge, fist')

    # fortunately, this works fine
    test.add_parents("bisk,chalp")
    print(test.parents)


if __name__ == "__main__":
    main()