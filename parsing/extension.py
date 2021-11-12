"""
Programmer: Ben Sehnert
Program: extesnion.py module
Software: python file generator
Date: 1/29/2021

"""

# TODO: would be nice to automate this somehow. __init__ file doesnt work for that currently. why?
import sys
# note in production, this should be something like ${CWD}
sys.path.append("C:\\Users\\Ben\\VsCode\\python\\classgenerator")

from utils.conventions import is_identifier
from utils.path_testing import NoFileNameError

# TODO: need to make sure you try catch where the extension integrates
# with inline for this to be useful.

class Extension:

    """
implements the first part of the Inline
provides resilencey, in cases where
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

    # TODO: see if these arguments are used else where in the program
    # def __str__(self, show_defaults=False, show_extension=True):
    def __str__(self):
        parents = f"({self.parents})" if self.parents != object else ""
        packages = f" ({self.packages})" if self.packages != 'root' else ""
        return f"{self.class_name}{parents}{packages}"
        # if show_extension:
        #     if show_defaults:
        #         return f"{self.class_name}({self.parents}) ({self.packages})" 
        #     if self.parents == object:
        #         if self.packages == 'root':
        #             return f"{self.class_name}"
        #         else:
        #             return f"{self.class_name} ({self.packages})"
        #     else:
        #         if self.packages == 'root':
        #             return f"{self.class_name}({self.parents})"
        #         return f"{self.class_name}({self.parents}) ({self.packages})"
        # else:
        #     return f"{self.class_name}"


    def __repr__(self):
        return repr({
            "classname": self.class_name,
            "parents" : self.parents,
            "packages" : self.packages})

    def add_parents(self, new_parents):
        """
    Appends new parents to existing parent(s).
    Overwrites the existing parents if
    parents is empty or default value.

    Args:
        new_parents (str): the parent or comma delimited str of parents to add.
        """
        if self.parents and self.parents != "<class 'object'>":
            self.parents = ",".join([self.parents, new_parents])
        else:
            self.parents = new_parents

    def add_packages(self, new_packages):
        """
    Appends new packages to existing package(s).
    Overwrites the existing packages if
    parents is empty or default value.

    Args:
        new_parents (str): the parent or comma delimited str of parents to add.
        """
        if self.packages and self.packages != 'root':
            self.packages = ",".join([self.packages, new_packages])
        else:
            self.packages = new_packages

    @classmethod
    def from_individual_arguments(cls, class_name : str, parents = object, packages = "root"):
        """
    Creates an extension based on the three components in the syntax
        classA(parentA,parentB) (package1, package2)
    Args:
        class_name (str): the name of class being defined with this extension.
        parents (str, default=object) *optional:
            comma seperated string listing the
            parent or parents who this class
            inherits from.
        packages (str, default="root" ) *optional:
            comma delimited string listing
            names of directories that contain the file.
    Returns:
        Extension: an object of the extension class, built from the arguments passed in.
        """
        if parents == "<class 'object'>":
            if 'root' in str(packages):
                return Extension(f"{class_name}")
            else:
                return Extension(f"{class_name} ({packages})")
        return Extension(f"{class_name}({parents}) ({packages})")

def main():
    """Running some tests to ensure constructors work as expected.
    """
    test = Extension("ClassA(file1,file2) (package1,package2)")
    # test = Extension.from_individual_arguments("ClassA", parents='eskimo', packages='gorge,fist')


    test.add_parents("bisk,chalp,neckbro")
    test.add_packages("horse,goat,brain")

    print("str:",test.__str__())
    print("repr:",test.__repr__())
    print("parents: ",test.parents)
    print("packages:",test.packages)

if __name__ == "__main__":
    main()
