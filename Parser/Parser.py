# Programmer: Ben Sehnert
# Date: 10/20/2020
# Program: Parser for class gen, reads in class names and
# specs, validates them and places them in appropriate container.

import sys
import keyword
from Inline import Inline
from ClassDict import Class_Dict


def is_identifier(ident: str) -> bool:
    """Determines if string is valid Python identifier."""

    if not isinstance(ident, str):
        raise TypeError("expected str, but got {!r}".format(type(ident)))

    if not ident.isidentifier():
        return False

    if keyword.iskeyword(ident):
        return False

    return True


def parse_inline(inline: Inline):

    # here we have tests for the full line- when in the format " class name : attr, attr : method, method  "
    # or " classname : attr, attr" "class name : : method method"

    if nesting_check(inline):
        inline = validate_nested(inline)

    if inheritance_check(inline):
        inline = validate_inheritance(inline)

    inline = inline.split(":")
    return {validate(inline[0]): (validate(inline[1], item_type="attribute"), validate(inline[2], item_type="method"))}

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
                "your class name {} is not capitalized. Would you like this corrected? (y/n)".format(item))
            return (item.title() if (answer.lower() in ('yes', 'y', 'yea', 'yeah', 'yup')) else item).strip()
    elif item_type in ("attribute", "method"):
        if item.islower():
            return item.strip()
        else:
            answer = input(
                "your attribute or method {} is not lowercase. Would you like this corrected? (y/n)".format(item))
            return (item.lower() if (answer.lower() in ('yes', 'y', 'yea', 'yeah', 'yup')) else item).strip()


def main():
    return parse_inline("skone, fuckme, shitspread : shit, bisk, chalp : asspie, dessert")