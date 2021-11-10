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
        self.class_name = None
        self.parents = None
        self.packages = 'root'
        if ext.count("("):
            if is_identifier(ext.split("(")[0]):
                self.class_name = ext.split("(")[0].strip()
                
                
                rest = ext.split("(")
                
                # remove the class name
                del rest[0]

                # get the parents and packages as two comma delimted strings.
                remove_parens = lambda token : token.strip().strip(")")
                rest = list(map(remove_parens, rest))
                if len(rest) == 2:
                    self.parents = rest[0]
                    self.packages = rest[1]
                else:
                    #TODO: how do we know which is which?
                    self.packages = rest[0]
                

                print("this too shall pass and rest is", rest)
            else:
                # no point generating extension if we cant generate a file
                print(f"Cannot produce a file with name {ext.split('(')[0]}.\n\
Not a valid identifier")
                raise NoFileNameError("Invalid Identifier", ext.split('(')[0])
            # have parents been defined?
            # if rest[0] == "(" and rest.count(")"):
            #     #get the parents, strip parenthesis and make it a list
            #     self.parents = (rest.split(")")[0].strip("(")).split(",")
            #     rest = rest.split(")")[1]
            #     # have packages been defined?
            #     if rest[0] == " " and rest.count(")"):
            #         self.packages = (rest.split("(")[1].strip(")")).split(",")
            #         del rest
            # # have packages been defined, but not parents?
            # elif rest[0] == " " and rest.count(")"):
            #     self.packages = (rest.split("(")[1].strip(")")).split(",")

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
        return repr({"classname": self.class_name, "parents" : self.parents, "packages" : self.packages})

    def add_parents(self, new_parents):
        ### we are going to add stuff to parents, we
        ### need to get rid of object (the default)
        if 'object' in str(self.parents):
            # careful with this- what if object is accidentally
            # in self.parents but not the only parent
            self.parents = ''
        else:
            self.parents = f", {self.parents}"
        if isinstance(new_parents, list):
            if len(new_parents) > 1:
                new_parents = ",".join(new_parents)
            else:
                new_parents = new_parents[0]
        self.parents = f"{new_parents}{self.parents}"

    def add_packages(self, new_packages):
        ### we are going to add stuff to packages, we
        ### need to get rid of root (the default)
        if 'root' in self.packages:
            self.packages = ''
        else:
            self.packages = f", {self.packages}"

        if isinstance(new_packages, list):
            if len(new_packages) > 1:
                new_packages = ",".join(new_packages)
            else:
                new_packages = new_packages[0]
        self.packages = f"{new_packages}{self.packages}"



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
    # # no bueno- confused parents for packaging
    # test = Extension("ClassA(neckmaster,neckattendant)")

    # # throws an error, tried to test whole thing as class ident
    # test = Extension("ClassA (neckmaster,neckattendant)")

    # # same as above here. doesnt like " (" i think
    # test = Extension("ClassA(blah,bleh) (neckmaster,neckattendant)")

    

    # really the only one that works for now
    # test = Extension("ClassA")


    # test.add_parents("bisk, chalp, neckbro")
    # print(test.__str__(show_defaults=True))
    # test = Extension.from_individual_arguments("ClassA", packages='gorge, fist')

    # fortunately, this works fine
    test.add_packages("bisk, chalp, neckbro")
    print(test.packages)


if __name__ == "__main__":
    main()