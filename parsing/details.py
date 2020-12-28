"""
Details class provides a constructor for describing the details of a class.
it is meant to be used as the value in a ClassDict object key value pair.
Pass in each detail as a positional parameter.

Program: Details class
Programmer: Ben Sehnert
Date: 12/27/2020
Software: 
"""


class Details(dict):
    """[summary]

    parent class:
        dict (dict): [description]
    """

    def __init__(self, attributes, methods, parents=object, package="root", options=None):
        # super(Details, self).__init__()
        self.attributes = attributes
        self.methods = methods
        self.parents = parents
        self.package = package
        self.options = options

    # def __setitem__(self, key, item):
    #     super().__setitem__(key, item)

    # def __getitem__(self, key):
    #     return super().__getitem__(key)

    def __repr__(self):
        return repr({"attributes": self.attributes, "methods": self.methods,
                     "parents": self.parents, "package": self.package, "options": self.options})

    def __str__(self):
        return f"{self.attributes}\t\t{self.methods}\t\
        {self.parents}\t{self.package}\t{self.options}"

# not a fully fledged custom dict because you cant set with subscript notation- note test below
# should not be a problem.


if __name__ == "__main__":
    d = Details("monkey, patch", "biscuit")
    # d.attributes = "weasel, wistle"
    d["attributes"] = "weasel, wistle"
    print(d.attributes)
