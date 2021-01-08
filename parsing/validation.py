"""
Programmer: Ben Sehnert
Program: validation module
Software: classgenerator program
Date: 1/7/2021

utility functions for validating user input.
"""
import sys
# import os

sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")
import keyword
from parsing.inline import Inline

def ask_case(item, item_type="class"):
    """
    In the case that the user has set the preference of case correction:"ask"
    checks if field has correct case according to pep8, in the case it is not
    if the user agrees, modifies the identifier with the correct case.

    item [str] - the real time value of the identifier.
    item_type="class" [str] - can be class or field.

    Returns:
        item [str]: the same item passed in, stripped of whitespace,
        and with correct case if requested. 
    """
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
    """
    Prompts user whether or not they want to correct errors
    in how their identifier is cased.

    item [str] - the real time value of the identifier.
    item_type="class" [str] - can be class or field.

    returns int:
    1 - user afirms the the mistake should be corrected.
    0 - user denies the mistake should be corrected.
    
    """
    while True:
        if item_type == "class":
            response = input(f"your class name {item} is not capitalized.\n\
        This violates PEP8 guidelines- should this be corrected (y/n)?\n")
        else:
            response = input(f"your attribute or method name {item} is not lowercase.\n\
        This violates PEP8 guidelines- should this be corrected (y/n)\n")
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

    
    item [str] - the real time value of the identifier.
    item_type="class" [str] - can be class or field.
    preference="ask" [str] - what the user prefers
    regarding correction of case.

    return [str] - the modified value of the identifier,
    according to what the user requested.
    """
    if preferences == "ask":
        return ask_case(item, item_type=item_type)
    elif preferences == "none":
        return item
    else:
        return coerce_case(item, item_type=item_type)

def is_identifier(ident: str) -> bool:
    """Determines if string is valid Python identifier.
    
    ident [str] - the real time value of identifier

    returns [bool]- True or False based on whether
    the ident argument is an identifier.
    """

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
            container.append(case_check(item, item_type=item_type))
    print(container)
    return container


def basic_validate(inline : str):
    """
    """
    inline = inline.split(":")
    #fall through test - cant generate class if no class names are provided
    if inline[0].strip():
        classes = basic_validate_members((inline[0].strip()).split(","))
        if len(inline) > 1:
            pass
            if inline[1].strip():
                attributes = basic_validate_members((inline[1].strip()).split(","), item_type="field")
                if len(inline) > 2 and inline[2].strip():
                    methods = basic_validate_members((inline[2].strip()).split(","), item_type="field")
                    # return Inline(classes, attributes, methods)
                else:
                    if missing_field(type="method"):
                        print("missing methods")
                        # print(f"{clas} : {}")
                        # inline(classes, attributes, None)
            else:
                # redundant but prevents methods from being
                #  undefined in if below in same else block.
                if len(inline) > 2 and inline[2].strip():
                    methods = basic_validate_members(inline[2].strip(), item_type="field")
                else:
                    if missing_field(type="none"):
                        print("missing both attr and methods")
                        # return Inline(classes, None, None)
                if missing_field(type="attribute"):
                    print("missing attributes")
                    # return Inline(classes, None, methods)
        else:
            # make an Inline w/ niether fields if user accepts that.
            if missing_field(type="none"):
                print("missing both attributes and methods.")
                # return Inline(classes, None, None)
            else:
                return 0
    else:
        return missing_field()

def missing_field(type="class"):
    """
    prints appropriate message based on one of 3 missing fields.

    field [str] - the real time value of inline field.
    type="class" [str] - what type of field dealt w/ determines error message.

    return [int] -
    1 - proceed with parsing
    0 - do not proceed.
    """
    if type == "class":
        print("Error: cannot make class with no class name.")
        return 0
    elif type == "attribute":
        if continue_prompt():
            return 1
        else:
            return 0
    elif type == "method":
        if continue_prompt(field_type="method"):
            return 1
        else:
            return 0
    elif type == "none":
        if continue_prompt(field_type="none"):
            return 1
        else:
            return 0

        
def continue_prompt(field_type="attribute"):
    if field_type == "none":
        message = "the inline provided has neither attributes or methods"
    else:
        message = f"the inline provided has no {field_type}s."
    while True:
        print(message)
        response = input("proceed with generation (y/n)?")
        if response in ("y", "yes"):
            return 1
        elif response in ("n", "no"):
            return 0
        else:
            print("sorry, didnt understand your response. valid: y or n")

def multiple_validate(items, item_type="class"):
    """
    """
    return NotImplemented

def inheritance_validate(items, item_type="class"):
    """[summary]
    """
    return NotImplemented


def validate(inline: str):
    return NotImplemented

if __name__ == "__main__":
    # Going to be doing this kind of parsing before the inline is cast
    # as an inline object. this avoids having to integrate this validation
    # within the class body and the code bloat it will cause.
    
    basic_validate("class_A : attr1, attr2 : method")