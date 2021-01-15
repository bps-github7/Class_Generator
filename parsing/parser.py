"""[summary]
"""

from parsing.class_dict import ClassDict
import sys

sys.path.insert(0,"C:\\Users\\Ben\\VsCode\\python\\classgenerator")

from parsing.inline import Inline, multiple_inline_handler
from parsing.validation import validate_inheritance, validate_file,\
validate_inline, validate_multiple, validate_packaging
from parsing.inheritance_builder import main as inheritance_main
from parsing.packaging import main as packaging_main
from utils.editing_menu import get_feedback

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
                    parsed_classes.append(packaging_main(inline))
                    if verbose:
                        print("parsing an packaging inline\n\
 containing inheritance and multiple classes.")
            else:
                if validate_inheritance(inline):
                    parsed_classes.append(inheritance_main(inline))
                    if verbose:
                        print("parsing an inline spec containing inheritance hierarchy.")
        else:
            if validate_multiple(inline):
                parsed_classes.append(multiple_inline_handler(inline))
                if verbose:
                    print("parsing non inheritance inline w multiple classes")
    else:
        print("single class ready for validation")
        # casting to a list for safety reasons.
        if validate_inline(inline):
            parsed_classes.append(ClassDict(inline.classes,
                inline.attributes, inline.methods,
                object, 'root',
                inline.options))
            if verbose:
                print("parsed a single inline specification.")
    return parsed_classes



def main(inline: Inline) -> int:
    classes = parse_inline(inline)
    return get_feedback(classes)
