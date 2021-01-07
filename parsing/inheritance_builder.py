"""
Program: inheritance_builder module- InheritanceBuilder class
Programmer: Ben Sehnert
Date: 12/24/2020
Purpose:  defines a builder for creating inheritance hierarchies out of
inheritance containing inline specs.
"""
import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")
from parsing.inline import Inline
from parsing.class_dict import ClassDict


class InheritanceBuilder:
    """Purpose:

        Exceptions:
    """
    version = 1.0

    def __init__(self, inline):
        class_fams, attr_fams, method_fams = [], [], []
        for cls, attr, method in zip(
                inline.classes.split(">"),
                inline.attributes.split(">"),
                inline.methods.split(">")):
            class_fams.append(cls.strip())
            attr_fams.append(attr.strip())
            method_fams.append(method.strip())
        classes, attributes, methods = [], [], []
        for cls, attr, method in zip(class_fams, attr_fams, method_fams):
            classes.append(InheritanceBuilder.member_splitter(cls))
            attributes.append(InheritanceBuilder.member_splitter(attr, token="/"))
            methods.append(InheritanceBuilder.member_splitter(method, token="/"))
        print(f"classes:  {classes}\nattributes: {attributes}\nmethods: {methods}")
        new = []
        #might have some kinks to work out with this one here vvv...
        parent = 'object'
        for cls, attr, method in zip(classes, attributes, methods):
            if isinstance(cls, list):
                for x,y,z in zip(cls, attr, method):
                    new.append(ClassDict(x,y,z, parents=parent))
            else:
                new.append(ClassDict(cls, attr, method, parents=parent))
            parent = cls
        self.classes = new


        # parent = 'object'
        # for x,y,z in zip(classes,attributes,methods):
        #     print(f"the parent package of {x} is {parent}")
        #     parent = x



    @staticmethod
    def member_splitter(container, token=","):
        if isinstance(container, list):
            for num, item in enumerate(container):
                if container[num].count(token):
                    container[num] = container[num].split(token)
            return container
        else:
            if container.count(token):
                return container.split(token)
            else:
                return container


# item = Inline("classA > classB : attr1, attr2, attr3 > mastadon, bucket, shallot: method1 > method2 -t -e{ut,cc}")
mulit_item = Inline("folderA, folderB > folderC : A1, A2 / B1, B2 > C1, C2 : Amethod / Bmethod > Cmethod")

# InheritanceBuilder(item)
processed = InheritanceBuilder(mulit_item)

print(processed.classes)

# print(InheritanceBuilder.member_splitter(['Classa, Classb', 'Classc']))
# print(InheritanceBuilder.member_splitter(['A1, A2 / B1, B2', 'C1, C2'], token="/"))