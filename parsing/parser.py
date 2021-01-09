"""
Programmer: Ben Sehnert
Program/software: Python class generator
Date: 10/20/2020

Parser for class gen, reads in class names and
specs, validates them and places them in appropriate container.

Raises:
    TypeError: [description]

Returns:
    [type]: [description]
"""

from parsing.validation import validate, validate_file
from utils.interactive import interactive_mode
# from parsing.inline import Inline
# from parsing.inline import main as inline_main
# from parsing.inheritance_builder import main as inheritance_builder


# from .class_dict import ClassDict
from utils.options import args


# This part of the prg will have to print out a table of the classes to generate
# and bring the user attention to problems with the proposed generations.
# then they can select a row in the table to modify their proposed classes.
# only when they approve/ it is fully validated can they submit it for generating.

version = 1.2

# def parse_inline(inline: Inline):

#     # here we have tests for the full line- when in the format " class name : attr, attr : method, method  "
#     # or " classname : attr, attr" "class name : : method method"

#     if nesting_check(inline):
#         inline = validate_nested(inline)

#     if inheritance_check(inline):
#         inline = validate_inheritance(inline)

#     inline = inline.split(":")
#     return {validate(inline[0]): (validate(inline[1], item_type="attribute"), validate(inline[2], item_type="method"))}

    # what if methods is not provided?
    # classes, attributes, methods = validate(inline[0], item_type="class"), validate(inline[1], item_type="attribute"), validate(inline[2], item_type="method")
    # if classes:
    #     print("skonedalone!")
    #     return { classes : () }


def nesting_check(line):
    return True if line.count("<") else False


def inheritance_check(line):
    return True if line.count(">") else False

def main():
    """Using args passed in from the cmd line
    further delegates the tasks of the program

    args : None

    returns A class_dict or list of class_dicts built out of input specifications.
    """
    ### should probably check here if .rc file is provided.
    #  set the defaults if so
    project_name = args.name
    project_path = args.path
    print(f"proposed project path: {project_path}/{project_name}")
    # make dir / file with this ^^^ and change to that directory.
    if args.verbose:
        print("determining source of input... (cmd line arg, file or interactive mode)")
    if args.inline:
        return validate(args.inline)
    elif args.file:
        if args.verbose:
            print("reading classes from a file...")
        return validate_file(args.file)
    else:
        if args.verbose:
            print("using interactive mode")
        return interactive_mode()

    # Reaching here means the parsing was unsuccessful
    # and class will not be generated
    return 0