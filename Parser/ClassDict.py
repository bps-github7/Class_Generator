'''
Programmer: Ben Sehnert
Program: Class_Dict Class
Software: Class Generator
Date: 12/21/2020

Module level docstring: implementation of Class Dict Class
'''

from Inline import Inline


class ClassDict():
    '''Class Level Docstring: Class_Dict is a dictionary that contains the specifications of a class
    it is the internal repersentation of the Inline class.'''

    def __init__(self, classes=None, attributes=None, methods=None, parents='object'):
        self.classes = classes.title()
        self.attributes = [(x.strip()).lower() for x in attributes.split(",")]
        self.methods = [(x.strip()).lower() for x in methods.split(",")]
        self.parents = parents

    def __repr__(self):
        return str({self.classes:
                    (self.attributes, self.methods, "parents = {}".format(self.parents))})

    def __str__(self):
        return str(self.__repr__())

    @classmethod
    def to_classdict(cls, inline):
        """Converts an Inline specification into a ClassDict object.

        Args:
            inline (str | Inline): The Inline you want to convert

        Returns:
            ClassDict: ClassDict matching specification of the Inline argument.
        """
        return ClassDict(*(str(inline).split(":")))

    # @classmethod
    # def from_dict(cls, dict):
    #     class_name = list(dict.keys())[0]
    #     return ClassDict(classes=class_name, attributes=(dict[class_name][0]),
    #     methods=(dict[class_name][1]), parents=(dict[class_name][2].strip("parent =")))


item = Inline.from_inline("american : attr1, attr2 : methodman")
# print(str(item).split(":")[0])

print(ClassDict.to_classdict(item))
# print(ClassDict.to_classdict("package1 : file1, file2 : options"))
# print(Class_Dict.from_dict(
#     {"classA": (['attr1', 'attr2'], ['skonedalone'], "parent = shitcandle")}))
