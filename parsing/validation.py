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
# from parsing.inline import Inline
from utils.conventions import class_correct_convention, is_identifier, case_check

class Error(Exception):
    pass

class InvalidOptionError(Error):
    pass

def validate_options(items : str):
    """validates options by rejecting all
    that do not match the followning:
        -e
        -t
        -m
        -a

    Args:
        items [str]: option string needing validation.

    Returns:
        items [str]: validated option string
                    with no leading/trailing white space.

        failure code [int] : returns 0 if validation tests fail.
    """
    valid = ("m","a","t","e")
    items = items.split("-")
    try:
        for item in items:
            if item in ('',' '): continue
            if len(item) > 1:
                for i in item:
                    if i not in valid:
                        # print(f"Error: {i} is not a valid option. See README for list of valid options. ")
                        # return 0
                        print(f"{i} is not recognized as an option")
                        raise InvalidOptionError()   
            else:
                if item not in valid:
                    # print(f"Error: {item} is not a valid option. See README for list of valid options. ")
                    # return 0
                    print(f"{item} is not recognized as an option")
                    raise InvalidOptionError()
    except InvalidOptionError:
        print("see README for a list of valid options")
        return 0
    return 1

    #     if item.startswith("e") or item.startswith("t") or item.startswith("{"):
    #         continue
    #     # ignore white space
    #     elif item in (""," "):
    #         del item
    #     else:
    #         print(f"invalid option detected: {item}")
    #         print(f"please only use accepted switches: -t, -e")
    #         print("or their attached argument list -t{ut,cc,sa} -e{send,vsc,zip,tgz}")
    #         return 0
    #     items = list(map(lambda x : x.strip(), items))
    # return "-".join(items)



def missing_field(typ="class"):
    """
    prints appropriate message based on one of 4 missing fields.

    field [str] - the real time value of inline field.
    type="class" [str] - what type of field dealt w/ determines error message.

    return [int] -
    1 - proceed with parsing
    0 - do not proceed.
    """
    if type == "class":
        print("Error: cannot make class with no class name.")
        return 0
    else:
        if continue_prompt(field_type = typ):
            return 1
        else:
            return 0

def continue_prompt(field_type="attributes"):
    """Asks users if they want to continue with generation,
    if a certain field or combination of fields is missing.

    Args:
        field_type (str, optional): [description]. Defaults to "attributes".
        NOTE: a field type other than None
        results in the execution of else block,
        therefore, type the literal value of the missing fields
        delimited by or, as a string.
        like so:
            # if methods and options are missing
            field_type = "methods or options"

            # this will properly output:
            "the inline provided has no methods or options"

    Returns:
        success code [int]:
        1 indicates the user confirmed the prompt - create the inline
        0 indicates the user denied the prompt - do not create it.
    """
    if field_type == "none":
        message = "the inline provided has no attributes, methods\
 or options"
    else:
        message = f"the inline provided has no {field_type}."
    while True:
        print(message)
        response = input("proceed with generation (y/n)?\n")
        if response in ("y", "yes"):
            return 1
        elif response in ("n", "no"):
            return 0
        else:
            print("sorry, didnt understand your response. valid: y or n")
              
def validate_class_name(cls, ):
    """
Sub function for coercing class names to proper state.

cls : the class name identifier

get_valid=False : the default coerces cls to validity.
flipping this makes the fn ask user for replacement value
until a correct one is provided.
    """
    # whitespace makes identifiers invalid
    cls = cls.replace(" ","_")
    if is_identifier(cls):
        if corrected := class_correct_convention(cls):
            return corrected
        else:
            return cls
    else:
        print("invalid identifier:", cls)
        return 0


def class_name_main(cls, get_valid=False):
    """
overseer function for validating class names

cls : the class name identifier to validate

get_valid : default arg makes the fn
return 0 if the identifier is invalid.

Flipping this switch makes the fn
loop until we get a correct class name.
    """
    if get_valid:
        if validated := validate_class_name(cls):
            return validated
        else:
            while True:
                new = input("enter new class name for replacing \
    invalid identifier {}\n".format(cls))
                if validated := validate_class_name(new):
                    break
        return validated
    else:
        if validated := validate_class_name(cls):
            return validated
        else:
            return 0

def attributes_main(attr : list):
    """
    overseer fn for ensuring validity of each attr.
    
    Args:
        attr ([type]): [description]
    """
    # y is the actual value
    for x,y in enumerate(attr):
        if is_identifier(y):
            # heres where you would override the default
            # arg if you wanted to coerce the case
            if returned := case_check(y, item_type="field"):
                attr[x] = returned
            # dont think we need an else block because ^^ always return truthy
        else:
            response = input(f"the attribute {y} is not a valid identifier\n\
delete {y} from attribute set {attr} (y/n)?")
            if response in ("y","yes"):
                del attr[x]
    if len(attr):
        return attr
    return None


def methods_main(methods : list):
    """
    overseer fn for ensuring the validity of each method.

    

    Args:
        method ([type]): [description]
    """
    # y is the actual value
    for x,y in enumerate(methods):
        if is_identifier(y):
            # heres where you would override the default
            # arg if you wanted to coerce the case
            if returned := case_check(y, item_type="field"):
                methods[x] = returned
            # dont think we need an else block because ^^ always return truthy
        else:
            response = input(f"the method {y} is not a valid identifier\n\
delete {y} from method set {methods} (y/n)?")
            if response in ("y","yes"):
                del methods[x]
    if len(methods):
        return methods
    return None

def validate_members(items, item_type="class"):
    """does basic validation for a standard inlines' members
        1. ensure each item is identifier
        2. ensure it has appropriate case

    items [list | str] : class name or attributes/methods to validate.
    item_type="class" [str] : which type of identifier to validate- class or field.

    returns:

    """

    # this ibnky=
    if item_type == "class":
        return class_correct_convention(items)
    elif item_type in ("attribute","method"):
        # This is a lil weird.
        item_type = "field"
    container = []
    for item in items:
        item = item.strip()
        if is_identifier(item):
            container.append(case_check(item, item_type=item_type))
    if len(container):
        return container
    return None

def validate_signiture(signiture : str):
    """unimplemented- checks that the name part of a signiture
    is a valid identifier and has the correct naming conventions
    lowercase, underscores seperating words.

    Args:
        signiture (str): [description]

    Returns:
        [type]: [description]
    """
    if signiture.count("("):
        signiture = signiture.split("(")
        name = signiture[0].strip()
        params = signiture[1].strip(")").split(",")
        for x,y in enumerate(params):
            # deals w default args
            if y.count("="):
                parameter = y.split("=")[0]
                default = y.split("=")[1]
                if is_identifier(parameter):
                    pass
                else:
                    response = input(f"the default parameter {y} is invalid. remove (y/n) ?")
                    if response in ("yes", "y"):
                        del params[x]
                # need to check both sides of the expression.
                if is_identifier(default):
                    pass
                else:
                    response = input(f"the default {default} in default arg: '{y}' is invalid. remove this parameter (y/n) ?")
                    if response in ("yes", "y"):
                        del params[x]
                    else:
                        pass    
            else:
                if is_identifier(y):
                    pass
                else:
                    response = input(f"the parameter {y} is invalid. remove (y/n) ?")
                    if response in ("yes", "y"):
                        del params[x]
                    else:
                        continue
    params = ",".join(params)
    return f"{name}({params})"


def validate_field(field : str):
    """Unimplemented- check that a class field identifier
    is valid- lowercase with underscores seperating words.

    Args:
        field (str): [description]

    Returns:
        [type]: [description]
    """
    return field.lower()

def validate_package_name(title):
    if is_identifier(title):
        if corrected := case_check(title,item_type="package"):
            return corrected
        else:
            return title
    print(f"Error: invalid package called '{title}'\nPackage name\
must conform to python identifier naming rules:\nno numbers, whitespace\
or special chars except for underscores.")
    return 0

def validate_module_name(title):
    if is_identifier(title):
        if corrected := case_check(title, item_type="module"):
            return corrected
        else:
            return title
    print(f"Error: invalid module called '{title}'\nModule name must\
conform to python identifier naming rules:\nno numbers, whitespace\
or special chars except for underscores.")
    return 0


def validate_parent_name(title):
    """Need a special fn for this
    because classes are auto coerced to uppercase by default."""
    if is_identifier(title):
        if corrected := case_check(title, item_type="class"):
            return corrected
        else:
            return title
    print(f"Error: invalid parent called '{title}'\nClasses name must\
conform to python identifier naming rules:\nno numbers, whitespace\
or special chars except for underscores.")
    return 0


if __name__ == "__main__":
    print("you're running a module!")