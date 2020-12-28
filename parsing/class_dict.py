'''
Programmer: Ben Sehnert
Program: Class_Dict Class
Software: Class Generator
Date: 12/21/2020

Module level docstring: implementation of Class Dict Class

this might actually be the useless class. but maybe worthwhile figuring out how to make it iterable
'''


class ClassDict(dict):
    '''Class Level Docstring: Class_Dict is a dictionary that contains the specifications of a class
    it is the internal repersentation of the Inline class.'''

    def __init__(self, classes, details=None):

        self.classes = classes.title()
        self.details = details
        # self.attributes = [(x.strip()).lower() for x in attributes.split(",")]
        # self.methods = [(x.strip()).lower() for x in methods.split(",")]
        # self.parents = parents
        # self.testing = testing
        # self.exporting = exporting

    # def __repr__(self):
    #     return str({self.classes:
    #                 (self.attributes, self.methods, f"parents: {self.parents}, testing: {self.testing}, exporting: {self.exporting}")})

    # def __str__(self):
    #     return str(self.__repr__())

    # @classmethod
    # def to_classdict(cls, inline):
    #     """Converts an Inline specification into a ClassDict object.

    #     Args:
    #         inline (str): The Inline you want to convert.
    #         Treat as string to avoid circular import

    #     Returns:
    #         ClassDict: ClassDict matching specification of the Inline argument.
    #     """
    #     return ClassDict(*(str(inline).split(":")))
