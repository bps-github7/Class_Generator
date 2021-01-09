'''
Programmer: Ben Sehnert
Program: inline class for ClassGen program
Date: 10/28/2020
Module level docstring: implements the Inline class
'''
import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")
from parsing.class_dict import ClassDict
from utils.editing_menu import get_feedback
# from .details import Details


class Inline:
    '''
Class Level Docstring: this is a class that repersents inline class
specifications.

constructor: creates an instance of the Inline class. performs cleansing to
strip white space from fields, which is noise in the classGen mini language.

    Parameters:
        -classes = None : repersents the class to be generated's identifier(s)
        -attributes = None : repersents the class to be generated's attribute(s)
        -methods = None : repersents the class to be generated's method(s)
        -global_testing = False : should unit tests be generated for all files
        -global_export = None : What should be done to the project after generation.
        if the field is not set to None, it will be a set of arguments/directives (what to do next?)

    Return values: None

    Side-effects: creates an Inline object in the scope of the
    invokation/call to the constructor. Memory is consumed while
    the object is in use.

    Exceptions: Unknown at this point.
    '''

    version = 2.1

    def __init__(self, inline):
        self.inline = inline.split(":")
        # Inline cannot be parsed if no class identifier is provided.
        if inline[0] is None:
            return None
        else:
            self.classes = self.inline[0].strip().title()
        # handles if attribute or methods are None
        if inline[1] is None:
            self.attributes = None
        else:
            self.attributes = self.inline[1].strip()
        if inline[2] is None:
            self.methods = None
        else:
            self.methods = self.inline[2].strip()
        if inline[3] is None:
            self.options = None
        else:
            # for backwards compatibility.
            if len(inline) > 3:
                self.options = self.inline[3].strip()

    def has_inheritance(self):
        """checks self.classes to see if it has > token in it.
            having this token indicates inline spec has inheritance.

        Returns:
            Boolean : based off whether inline has inheritance
        """
        if self.classes.count(">"):
            return True
        return False

    def has_packaging(self):
        """checks self.classes to see if it has < token in it.
            having this token indicates inline spec has packaging.
            note: rudimentary check- more parsing required than this.

        Returns:
            Boolean : based off whether inline has packaging
        """
        return True if self.inline.count("<") else False

    def __repr__(self):
        return ":".join(self.inline)

    def __str__(self, single_line=True):
        if single_line:
            return "{}\t{}\t{}\t{}".format(self.classes, self.attributes, self.methods, self.options)
        else:
            return "class(es): {}\n\
attributes: {}\n\
methods: {}\n\
options: {}".format(self.classes, self.attributes,
                      self.methods, self.options)

    @classmethod
    def from_individual_arguments(cls, *args):
        """ turns the 3 components of Inline (class, attributes and methods)
        into an inline object. if any of the items are lists, turn them into
        comma delimited strings that Inline constructor expects. 

        Returns:
            [type]: [description]
        """
        items = [*args]
        for i, value in enumerate(items):
            if value is None:
                continue
            if isinstance(value, list):
                items[i] = ",".join(value)
        return Inline(f"{items[0]}:{items[1]}:{items[2]}:{items[3]}")

    @staticmethod
    def cleanse(items: any):
        """format properties by strip and lowercase of each elements.
        side-effect: coerces ',' delimited string to formatted list.
        """
        if isinstance(items, list):
            return list(map(
                lambda item: item.strip().lower(), items))
        return list(map(
            lambda item: item.strip().lower(), items.split(",")))

def multiple_inline_handler(inline : Inline):
    """[summary]

    Args:
        inline ([type]): [description]
    """
    specifications = []
    classes, attributes, methods, options = [], [], [], []
    ### need to validate the inline before using this
    ### to confirm number of / and , match up correctly.
    for single_class, its_attributes, its_methods, its_options in zip(
            inline.classes.split(","),
            inline.attributes.split("/"),
            inline.methods.split("/"),
            inline.options.split("/")):
        classes.append(single_class)
        attributes.append(its_attributes)
        methods.append(its_methods)
        options.append(its_options)
    # setting parent and package to defaults in this and else block below
    # until we sophisticate the packaging and inheritance functionality a bit more.
    specifications = [ClassDict(class_title, attribute_group, method_group, object, 'root', options_group)\
    for class_title, attribute_group, method_group, options_group in zip(classes, attributes, methods, options)]
    return specifications

def parse_inline(inline):
    """[summary]

    Args:
        inline ([type]): [description]

    Returns:
        list: A list of all the inlines parsed out of the current inline spec.
    """


    if inline.classes.count(","):
        parsed_classes = multiple_inline_handler(inline)
    else:
        # casting to a list for safety reasons.
        parsed_classes = [ClassDict(inline.classes,
            inline.attributes, inline.methods,
            object, 'root',
            inline.options)]
    return parsed_classes

def main(inline: Inline) -> int:
    classes = parse_inline(inline)
    return get_feedback(classes)

if __name__ == "__main__":
    # also not reading -e values now
    # main(Inline("classA : attr1, attr2, attr3 : method1 -t -e{ut,cc}"))

    # instead of rewriting the constructor, wrote this
    # classmethod/alt constructor for this use case
    main(Inline.from_individual_arguments("Biscuit", ['gravy', 'sausage'], ['method1', 'method2'], '-t -e{ut}'))
    
    # items = Inline.from_individual_arguments("Biscuit",
    # ['gravy', 'sausage'], ['method1', 'method2'], '-t -e{ut}')
    # print(items)

