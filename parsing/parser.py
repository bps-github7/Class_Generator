"""
Programmer: Ben Sehnert
Program: Parser module in parsing package
Date: 1/19/21
Software: Python Class Generator

About: handles the parsing of Inlines of various forms.

"""
import os

from inline import Inline
from inheritance_builder import main as inheritance_main
from multiple import main as multiple_main

# def parse_inline(inline : str, verbose=False):
#     """[summary]

#     Args:
#         inline ([type]): [description]

#     Returns:
#         list: A list of all the inlines parsed out of the current inline spec.
#     """

#     ### its important that we test the followin before validating
#     ### because some of the tokens for our syntax would fail basic validation.
#     if not inline.count(":"):
#         print("Error: input you provided is not properly formatted.\n\
# See README.md for more details. Inline specs must have at least one : (colon")
#         return 0
#     copy = inline.split(":")
#     classes = copy[0]
#     parsed_classes = []

#     ### Be wary of whether or not this actually
#     ### works for ALL cases (ie packaging, inheriting, multi inline, w opts)
#     ### AKA UNITTEST!
#     if classes.count(","):
#         if classes.count(">"):
#             if classes.count("<"):
#                 if validate_packaging(inline):
#                     print("doing the packaging thing!")
#                     # parsed_classes.append(packaging_main(Inline(inline)))
#                     if verbose:
#                         print("parsing an packaging inline\n\
#  containing inheritance and multiple classes.")
#             else:
#                 if validate_inheritance(inline):
#                     # this would earase already parsed stuff if you had different types in a session
#                     # ie a normal inline and a multiple inline.
#                     parsed_classes.append(inheritance_main(Inline(inline)))
#                     if verbose:
#                         print("parsing an inline spec containing inheritance hierarchy.")
#         else:
#             if validate_multiple(inline):
#                 # this would earase already parsed stuff if you had different types in a session
#                 # ie a normal inline and a multiple inline.
#                 parsed_classes.append(multiple_main(Inline(inline)))
#                 if verbose:
#                     print("parsing non inheritance inline w multiple classes")
#     else:
#         print("single class ready for validation")
#         # casting to a list for safety reasons.
#         if validate_inline(inline):
#             parsed_classes.append(Inline(inline.classes,
#                 inline.attributes, inline.methods,
#                 object, 'root',
#                 inline.options))
#             if verbose:
#                 print("parsed a single inline specification.")
#     return parsed_classes

def parse_inline(inline : str, verbose=False):
    """Main function for parsing.

    Based on the shape of the inline, sole positional argument,
    figures out what needs to be done to turn the inline into
    an instruction set that the program understands.
    """
    if not inline.count(":"):
        print("Error: input you provided is not properly formatted.\n\
See README.md for more details. Inline specs must have at least one : (colon")
        return 0
    elif inline.count("/"):
        return multiple_main(inline)
    elif inline.count(">"):
        return inheritance_main(inline)
    else:
        return Inline(inline)

def from_file(f, results=[]):
    """
builds a container out of text file
containing class dict specifications inline format.
    """
    # accounting for need for FTYPE extension in windows
    # if OS is windows and .txt is not provided, add it.
    if os.name == 'nt':
        if not f.endswith('.txt'):
            f += '.txt'  
    with open("{}".format(f), "r") as file:
        for num, line in enumerate(file):
            # enables the user to 'comment out' lines with both JS and python style of commenting
            if line.startswith("#") or line.startswith("//"):
                continue
            # ignore lines that are just a new line or whitespace
            if line.strip() in  ("\n", "", " "):
                continue
            copy = line.strip("\n")
            ### need to enforce validation here- reject or correct
            ### lines that dont conform to inline standards.
            results.append(Inline(line))
        return results


def main(inline: Inline) -> int:
    classes = parse_inline(inline)
    return classes
    # return get_feedback(classes)


if __name__ == '__main__':

    # extension syntax doesnt work in this simplified example...
    print(parse_inline("classA(parent1, parent2) (packageA) : attr1, attr2 : method1"))

    # parsing extension still isnt great, 'parents' : 'bisk), classB, classC'

    # would seem the multiple main fn needs some work.
#    print(parse_inline("classA, classB, classC : attr1, attr2 / attr3, attr4 / attr5, attr6 : method1 / method2 / method3 : -t / -e / -t -e"))


# what if the inlines passed in don't have extensions? be warry of bugs caused by this..!
# test = multiple_inline_handler("classA(bisk)/ classB (chalp)/ classC(cyclone,asparagus) (dirty): attr1, attr2 / attr3, attr4 / attr5, attr6 : method1 / method2 / method3 : -t / -e / -t -e")

# for i in test:
#     print(i.parents)