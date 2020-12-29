'''
Programmer: Ben Sehnert
Program: Class_Dict Class
Software: Class Generator
Date: 12/21/2020

Module level docstring: implementation of Class Dict Class

this might actually be the useless class. but maybe worthwhile figuring out how to make it iterable
'''
from classgenerator.parsing.details import Details
import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python")


# __package__ = "parsing"


class ClassDict(dict):
    '''Class Level Docstring: Class_Dict is a dictionary that contains the specifications of a class
    it is the internal repersentation of the Inline class.'''

    def __init__(self, classes, details=None):
        self.classes = classes.title()
        self.details = details
        self.details.attributes = [(x.strip()).lower()
                                   for x in self.details.attributes.split(",")]
        self.details.methods = [(x.strip()).lower()
                                for x in self.details.methods.split(",")]
        self.dict = {classes: details}
        super(ClassDict, self).__init__(self.dict)

    @property
    def classes(Self):
        return self.classes

    @classes.setter
    def classes(self, cls):
        #
        self.classes = cls
        self.dict = {self.classes: self.details}

    def __repr__(self):
        return repr(self.dict)

    def __str__(self):
        return str(self.dict)

    def __iter__(self):
        return iter(self.dict)

    def __next__(self):
        return next(self.dict)

    def keys(self):
        return self.dict.keys()

    def items(self):
        return self.dict.items()

    def values(self):
        return self.dict.values()


def main(cls1: ClassDict, cls2: ClassDict):
    """Tests wether we can add two dicts together

    Args:
        cls1 (ClassDict): [description]
        cls2 (ClassDict): [description]
    """

    new = {}
    new.update(cls1)
    new.update(cls2)
    print(new)


if __name__ == "__main__":
    b = ClassDict("moth", details=Details("attr1, attr2",
                                          "method1, method2", options=[True, '{ut,cc}']))
    c = ClassDict("tooth", details=Details("attrA, attrB",
                                           "methodA, methodB", options=[False, '{cc}']))

    # print(b.update(c))
    b.classes = "bicuit_boy"

    main(b, c)

    # print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(
    #     __file__, __name__, str(__package__)))
