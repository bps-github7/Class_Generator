'''
Programmer: Ben Sehnert
Program: Class_Dict Class
Software: Class Generator
Date: 12/21/2020

Module level docstring: implementation of Class Dict Class
'''

from Inline import Inline


class Class_Dict(dict):
    '''Class Level Docstring: Class_Dict is a dictionary that contains the specifications of a class
    it is the internal repersentation of the Inline class.'''

    def __init__(self, classes=None, attributes=None, methods=None, parents='object'):
        self.classes = classes.title()
        self.attributes = [(x.strip()).lower() for x in attributes.split(",")]
        self.methods = [(x.strip()).lower() for x in methods.split(",")]
        self.parents = parents

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __repr__(self):
        return {self.classes: (self.attributes, self.methods, "parents = {}".format(self.parents))}

    def __str__(self):
        return str(self.__repr__())

    @classmethod
    def to_classdict(cls, inline):
        return Class_Dict(*inline.split(":"))

    @classmethod
    def from_dict(cls, dict):
        class_name = list(dict.keys())[0]
        return Class_Dict(classes=class_name, attributes=(dict[class_name][0]), methods=(dict[class_name][1]), parents=(dict[class_name][2].strip("parent =")))


# print(Class_Dict.to_classdict("american : attr1, attr2 : methodman"))
# print(Class_Dict.to_classdict("package1 : file1, file2 : options"))
# print(Class_Dict.from_dict(
#     {"classA": (['attr1', 'attr2'], ['skonedalone'], "parent = shitcandle")}))
