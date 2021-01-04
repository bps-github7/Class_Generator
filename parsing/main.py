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
import parsing
import generator
import utils


import sys
import keyword
from .inline import Inline
from .inline import main as inline_main

# from .class_dict import ClassDict
from utils.options import args


# This part of the prg will have to print out a table of the classes to generate
# and bring the user attention to problems with the proposed generations.
# then they can select a row in the table to modify their proposed classes.
# only when they approve/ it is fully validated can they submit it for generating.

version = 1.2


def is_identifier(ident: str) -> bool:
    """Determines if string is valid Python identifier."""

    if not isinstance(ident, str):
        raise TypeError("expected str, but got {!r}".format(type(ident)))

    if not ident.isidentifier():
        return False

    if keyword.iskeyword(ident):
        return False

    return True


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


def validate_nested(line):
    '''carefully design packaging structure as to not interfere with the already established inheritance syntax!'''
    # ideas: remodel inheritance language so that -> marks inheritance </> marks package- <p: package_name c: ( class spec)>
    # nested package : <p: c:(...) <p  <p: c: > <p: c: > <p: c: > >   > this would mean the space after class specs denotes nested packages, and must be left blank otherwise.
    # rootward nesting: should advise against it. suggest to users they start at their project root and work downwards.
    # coerce against this by not providing operator/ syntax for supporting this.


def validate(items, item_type="class"):
    ''' expects a single string param
        validates either class, attr, or method specs
    '''
    container = []

    # this line only applies if there is inheritance nesting- test it seperately!!!
    # token = "," if (item_type == 'class' ) else "/"
    token = ","
    for i in items.split(token):
        trimmed = i.strip()
        if is_identifier(trimmed):
            continue
        else:
            print("{} is not a valid identifier.".format(trimmed))
            return 0
        container.append(case_check(trimmed))
    return container


def case_check(item, item_type="class"):
    if item_type == "class":
        if item.istitle():
            return item.strip()
        else:
            answer = input(
                "your class name {} is not capitalized.\
Would you like this corrected? (y/n)".format(item))
            return (item.title() if (answer.lower() in ('yes',
            'y', 'yea', 'yeah', 'yup')) else item).strip()
    elif item_type in ("attribute", "method"):
        if item.islower():
            return item.strip()
        else:
            answer = input(
                "your attribute or method {} is not lowercase.\
Would you like this corrected? (y/n)".format(item))
            return (item.lower() if (answer.lower() in ('yes',
            'y', 'yea', 'yeah', 'yup')) else item).strip()


def main():
    """Using args passed in from the cmd line
    further delegates the tasks of the program

    args : None

    returns None at this time.
    """
    project_name = args.name
    project_path = args.path
    print(f"proposed project path: {project_path}/{project_name}")
    # make dir / file with this ^^^ and change to that directory.
    if args.inline:
        item = Inline(args.inline)
        if item.has_inheritance():
            if item.has_packaging():
                print("building a classdict with a inline with packaging")
                #specs = packaging.main()
            else:
                print("building an class dict with inline with inheritance")
                #specs = inheritancebuilder.main()
        else:
            return inline_main(item)
    elif args.file:
        print("reading classes from a file...")
        # specs = file.main()
    else:
        print("using interactive mode")
        # specs = interactive.main()
    # # for testing purpose\
    # print("\n\n")
    # print("parsed inlines' str method:\n-------------------------")
    # print(item.__str__())
    # print("\n\n")
    # print("parsed inlines repr method:\n-------------------------")
    # print(item.__repr__())
    # print("\n\n")
