"""
Programmer: Ben Sehnert
Program: Parser module in parsing package
Date: 1/19/21
Software: Python Class Generator

About: handles the parsing of Inlines of various forms.

"""
import sys
sys.path.insert(0,"C:\\Users\\Ben\\VsCode\\python\\classgenerator")

# from utils.misc_functions import get_extension
from parsing.inline import Inline
from parsing.validation import validate_inheritance,\
validate_inline, validate_multiple, validate_packaging
# validate_file,
from parsing.inheritance_builder import main as inheritance_main
from parsing.multiple import main as multiple_main
# from parsing.packaging import main as packaging_main
# from utils.editing_menu import get_feedback

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
                parsed_classes.append(multiple_main(Inline(inline)))
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

# print(main("classA(bisk), classB, classC : attr1, attr2 / attr3, attr4 / attr5, attr6 : method1 / method2 / method3 : -t / -e / -t -e"))


# what if the inlines passed in don't have extensions? be warry of bugs caused by this..!
# test = multiple_inline_handler("classA(bisk)/ classB (chalp)/ classC(cyclone,asparagus) (dirty): attr1, attr2 / attr3, attr4 / attr5, attr6 : method1 / method2 / method3 : -t / -e / -t -e")

# for i in test:
#     print(i.parents)