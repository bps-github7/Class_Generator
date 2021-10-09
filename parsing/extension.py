"""
Programmer: Ben Sehnert
Program: extesnion.py module
Software: python file generator
Date: 1/29/2021

"""


import re


class Extension:

    """
implements the first part of the Inline
provides dynamic utility, in cases where
either, niether or both argument parts of the extension are provided.
    """
    def __init__(self, ext):
        #TODO: is this really the best way to do this? what if user accidentally puts ) ( in their class name?
        
        if ext.count(") ("):
            classes = ext.split(") (")
            self.class_name = classes[0].split("(")[0].strip()
            self.parents = classes[0].split("(")[1].strip()
            self.packages = classes[1].strip(")")
        ### Only the packaging - example (packages)
        elif ext.count(" ("):
            classes = ext.split(" (")
            self.class_name = classes[0].strip()
            self.parents = object
            self.packages = classes[1].strip(")").strip()
        ### only the parent - example(parents)
        elif re.match(r"(\w)*[()]", ext):
            # the python equivalent of above expression
            # will snag on undesired tokens, resulting in wrong values.
            classes = ext.split("(")
            self.class_name = classes[0].strip()
            self.parents = classes[1].strip(")").strip()
            self.packages = "root"
        else:
            self.class_name = ext.strip()
            self.parents = object
            self.packages = "root"

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
    def from_individual_arguments(cls, class_name, parents = object, packages = "root"):
        if 'object' in str(parents):
            if 'root' in str(packages):
                return Extension(f"{class_name}")
            else:
                return Extension(f"{class_name} ({packages})")
        return Extension(f"{class_name}({parents}) ({packages})")
        
        

def main():
    test = Extension("ClassA(cones,chalpo,poades) (neckmaster,neckattendant)")
    # test.add_parents("bisk, chalp, neckbro")
    # print(test.__str__(show_defaults=True))
    # test = Extension.from_individual_arguments("ClassA", packages='gorge, fist')
    test.add_parents("bisk, chalp, neckbro")
    print(test.parents.split(","))


if __name__ == "__main__":
    main()