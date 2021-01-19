"""
Programmer: Ben Sehnert
Program: Parser module in parsing package
Date: 1/19/21
Software: Python Class Generator

About: handles the parsing of Inlines of various forms.

"""
import sys
sys.path.insert(0,"C:\\Users\\Ben\\VsCode\\python\\classgenerator")

import re
from parsing.inline import Inline
from parsing.validation import validate_inheritance,\
validate_inline, validate_multiple, validate_packaging
# validate_file,
from parsing.inheritance_builder import main as inheritance_main
# from parsing.packaging import main as packaging_main
# from utils.editing_menu import get_feedback

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
    # until we sophisticate the packaging and inheritance functionality a bit more

    ### Two things to note here- 1 is this fn returning a nested list which is then
    ### appended to another list? messy complicated JA? 2. how to do the same as above
    ### with packaging and parents? make a mini fn for parsing parent and package out of class?
    ### these attributes should be accessible from out here...

    classes = list(map(get_extension, classes))

    specifications = [Inline.from_details(class_title[0], attribute_group, method_group, class_title[1],
    class_title[2], options_group) for class_title, attribute_group, method_group,
    options_group in zip(classes, attributes, methods, options)]
    return specifications


def get_extension(cls):
    """
takes class string and gets parent and packaging out of it
    """

    ### NOTE: args must be passed in like they appear in the string
    ### ie. finished = ['class_name', 'parents', 'packages']
    finished = []
    ### example(parents) (packages)
    if cls.count(") ("):
        classes = cls.split(") (")
        finished.append(classes[0].split("(")[0].strip())
        finished.append(classes[0].split("(")[1].strip())
        finished.append(classes[1].strip(")"))
    ### Only the packaging - example (packages)
    elif cls.count(" ("):
        classes = cls.split(" (")
        finished.append(classes[0].strip())
        finished.append(object)
        finished.append(classes[1].strip(")").strip())
    ### only the parent - example(parents)
    elif re.match(r"(\w)*[()]", cls):
        classes = cls.split("(")
        finished.append(classes[0].strip())
        finished.append(classes[1].strip(")").strip())
        finished.append("root")
    else:
        finished.append(cls.strip())
        finished.append(object)
        finished.append("root")
    return finished

def parse_inline(inline : str, verbose=False):
    """[summary]

    Args:
        inline ([type]): [description]

    Returns:
        list: A list of all the inlines parsed out of the current inline spec.
    """

    ### its important that we test the followin before validating
    ### because some of the tokens for our syntax would fail basic validation.
    if not inline.count(":"):
        print("Error: input you provided is not properly formatted.\n\
See README.md for more details. Inline specs must have at least one : (colon")
        return 0
    copy = inline.split(":")
    classes = copy[0]
    parsed_classes = []

    ### Be wary of whether or not this actually
    ### works for ALL cases (ie packaging, inheriting, multi inline, w opts)
    ### AKA UNITTEST!
    if classes.count(","):
        if classes.count(">"):
            if classes.count("<"):
                if validate_packaging(inline):
                    print("doing the packaging thing!")
                    # parsed_classes.append(packaging_main(Inline(inline)))
                    if verbose:
                        print("parsing an packaging inline\n\
 containing inheritance and multiple classes.")
            else:
                if validate_inheritance(inline):
                    # this would earase already parsed stuff if you had different types in a session
                    # ie a normal inline and a multiple inline.
                    parsed_classes.append(inheritance_main(Inline(inline)))
                    if verbose:
                        print("parsing an inline spec containing inheritance hierarchy.")
        else:
            if validate_multiple(inline):
                # this would earase already parsed stuff if you had different types in a session
                # ie a normal inline and a multiple inline.
                parsed_classes.append(multiple_inline_handler(Inline(inline)))
                if verbose:
                    print("parsing non inheritance inline w multiple classes")
    else:
        print("single class ready for validation")
        # casting to a list for safety reasons.
        if validate_inline(inline):
            parsed_classes.append(Inline(inline.classes,
                inline.attributes, inline.methods,
                object, 'root',
                inline.options))
            if verbose:
                print("parsed a single inline specification.")
    return parsed_classes



def main(inline: Inline) -> int:
    classes = parse_inline(inline)
    return classes
    # return get_feedback(classes)

print(main("classA(bisk), classB, classC : attr1, attr2 / attr3, attr4 / attr5, attr6 : method1 / method2 / method3 : -t / -e / -t -e"))