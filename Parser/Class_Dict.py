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
        self.attributes = [(x.strip()).lower() for x in attributes]
        self.methods = [(x.strip()).lower() for x in methods]
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

    def inheritance(self, new={}):
        cls, attr, methods = self.classes.split(
            ">"), self.attributes.split(">"), self.methods.split(">")
        if len(cls) != len(attr):
            print(
                "Error: mismatch in number of class identifiers to attribut identifiers")
            return 0
        parent_cls, parent_attr, parent_method = cls[0].split(
            ','), attr[0].split('/'), methods[0].split('/')
        for x, y, z in zip(parent_cls, parent_attr, parent_method):
            new_dict = Class_Dict.from_dict({x: (y, z)})
            new.update(new_dict)
        parent = parent_cls
        del cls[0], attr[0], methods[0]
        name, attr, methods = ">".join(cls), ">".join(attr), ">".join(methods
        if len(cls) > 0:
            return inheritance()
            # this where it gets complicated, because the cls is being assigned from self.
        else:
            return new


# c = Class_Dict.to_classdict("american > lesbian : attr1 > attr2 : methodman > redman")
# c.inheritor()
# print(Class_Dict.to_classdict("american : attr1, attr2 : methodman"))
# print(Class_Dict.to_classdict("package1 : file1, file2 : options"))



# def inheritance(inline, parent=object, new={}):
#     inline = Inline.from_inline(inline)
#     class_family, attr_family, method_family = inline.classes.split(
#         ">"), inline.attributes.split(">"), inline.methods.split(">")
#     parents, parent_attr, parent_methods = class_family[0].split(
#         ","), attr_family[0].split("/"), method_family[0].split("/")
#     for x, y, z in zip(parents, parent_attr, parent_methods):
#         # this conditional ensures that classes who have parents
#         # according to the hierachry arre defined as such
#         class_dict = Class_Dict.from_dict(
#             {x: (y, z, "parent = {}".format(parent))})
#         new.update(class_dict)

#         if parent != object:
#             new.update(class_dict)
#         else:
#             # dont need to supply parent arg here because object is the default
#             new.update(class_dict)
#     # prep work for the next recursive call-
#     # define new arguments and delete irrelevant data

#     # family[0] is a list
#     parent = class_family[0]
#     del class_family[0], attr_family[0], method_family[0]
#     name, attr, methods = ">".join(class_family), ">".join(
#         attr_family), ">".join(method_family)
#     # recursive call and base case
#     if len(class_family) > 0:
#         return inheritance("{} : {} : {}".format(name, attr, methods), parent=parent, new=new)
#     else:
#         return new


# new = inheritance(
#     "classA, classB > classC : attr1, attr2 / attr3, attr4 > attr5 : skonedalone / pollywog > fucknard")
# print(new)


print(Class_Dict.from_dict(
    {"classA": (['attr1', 'attr2'], ['skonedalone'], "parent = shitcandle")}))
