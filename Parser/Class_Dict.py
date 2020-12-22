'''
Programmer: Ben Sehnert
Program: Class_Dict Class
Software: Class Generator
Date: 12/21/2020

Module level docstring: implementation of Class Dict Class
'''

class Class_Dict:
    '''Class Level Docstring: Class_Dict is a dictionary that contains the specifications of a class
    it is the internal repersentation of the Inline class.'''

    def __init__(self, classes=None, attributes=None, methods=None, parents='object'):
        self.classes = classes.title()
        self.attributes = [(x.strip()).lower() for x in attributes.split(',')]
        self.methods = [(x.strip()).lower() for x in methods.split(',')]
        self.parents = parents

    def __repr__(self):
        return {self.classes: (self.attributes, self.methods, "parents = {}".format(self.parents))}

    def __str__(self):
        return str(self.__repr__())

    @classmethod
    def to_classdict(cls, inline):
        return Class_Dict(*inline.split(":"))


print(Class_Dict.to_classdict("american : attr1, attr2 : methodman"))
