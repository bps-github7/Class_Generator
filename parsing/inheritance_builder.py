"""
Program: inheritance_builder module- InheritanceBuilder class
Programmer: Ben Sehnert
Date: 12/24/2020
Purpose:  defines a builder for creating inheritance hierarchies out of
inheritance containing inline specs.
"""
from .inline import Inline


class InheritanceBuilder:
    """Purpose:

        Exceptions:
    """
    version = 1.0

    def __init__(self, inline):
        inline = Inline(inline)
        for cls_fam, attr_fam, method_fam in zip(
                inline.classes.split(">"),
                inline.attributes.split(">"),
                inline.methods.split(">")):
            # for cls, attr, method in (cls)
            print("class family {}".format(cls_fam))
            print("attribute family {}".format(attr_fam))
            print("method family {}".format(method_fam))
