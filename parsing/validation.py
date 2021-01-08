"""
Programmer: Ben Sehnert
Program: validation module
Software: classgenerator program
Date: 1/7/2021

utility functions for validating user input.
"""
# import sys
import keyword

def ask_case(item, item_type="class"):
    if item_type == "class":
        if item.istitle():
            return item.strip()
        else:
            if case_prompt(item, item_type=item_type):
                return item.title().strip()
            return item.strip()
    else:
        if item.islower():
            return item.strip()
        else:
            if case_prompt(item, item_type=item_type):
                return item.lower().strip()
            return item.strip()

def case_prompt(item, item_type="class"):
    while True:
        if item_type == "class":
            response = input(f"your class name {item} is not capitalized.\n\
        This violates PEP8 guidelines- should this be corrected (y/n)?")
        else:
            response = input(f"your attribute or method name {item} is not lowercase.\n\
        This violates PEP8 guidelines- should this be corrected (y/n)")
        if response in ("y", "yes"):
            return 1
        return 0

def coerce_case(item, item_type="class"):
    # class names are cast to title case
    if item_type == "class":
        # not sufficient testing- but works for now
        # really, we want to title case and remove spaces between words.
        if item.istitle():
            return item.strip()
        else:
            return item.title().strip()
    # methods are casted to lowercase.
    else:
        if item.islower():
            return item.strip()
        else:
            return item.lower().strip()


def case_check(item, item_type="class", preferences="ask"):
    """
    based on user preferences, set in rc file:
    either coerce, ask user or do nothing about
    incorrectly cased identifiers.
    """
    if preferences == "ask":
        return ask_case(item, item_type=item_type)
    elif preferences == "none":
        return item
    else:
        return coerce_case(item, item_type=item_type)

def is_identifier(ident: str) -> bool:
    """Determines if string is valid Python identifier."""

    if not isinstance(ident, str):
        raise TypeError("expected str, but got {!r}".format(type(ident)))

    if not ident.isidentifier():
        return False

    if keyword.iskeyword(ident):
        return False

    return True

def basic_validate_members(items, item_type="class"):
    """does basic validation for a standard inlines' members
        1. ensure each item is identifier
        2. ensure it has appropriate case

    items [list | str] : class name or attributes/methods to validate.
    item_type="class" [str] : which type of identifier to validate- class or field.

    returns:  
    """
    container = []
    for item in items:
        if is_identifier(item):
            container.append(case_check(item))
    return container


def basic_validate(items, item_type="class"):
    """validates basic inline-
        1. does it have Classes
        2. does it follow syntax
        3. does it fail basic validation member tests?
    """
    return NotImplemented


def multiple_validate(items, item_type="class"):
    """
    """
    return NotImplemented

def inheritance_validate(items, item_type="class"):
    """[summary]
    """
    return NotImplemented

# def validate_nested(line):
#     '''carefully design packaging structure as to not interfere with the already established inheritance syntax!'''
#     # ideas: remodel inheritance language so that -> marks inheritance </> marks package- <p: package_name c: ( class spec)>
#     # nested package : <p: c:(...) <p  <p: c: > <p: c: > <p: c: > >   > this would mean the space after class specs denotes nested packages, and must be left blank otherwise.
#     # rootward nesting: should advise against it. suggest to users they start at their project root and work downwards.
#     # coerce against this by not providing operator/ syntax for supporting this.

################################################################

if __name__ == "__main__":
    
    ### check if validation works for class identiers
    # print(validate("cls1, cls2, abracadabra"))

    ### check if validation works for class fields- attr, method
    # print(validate("attr1, attr2 #!@$@", item_type="method"))
    
    print(case_check("cls"))