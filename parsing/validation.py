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
from parsing.inline import Inline
from parsing.class_dict import ClassDict
from parsing.class_dict import ClassDict
from utils.conventions import is_identifier, case_check

def validate_options(items):
    """[summary]

    Args:
        items ([type]): [description]
    """
    items = items.split("-")
    for item in items:
        if item.startswith("e") or item.startswith("t") or item.startswith("{"):
            continue
        # ignore white space
        elif item in (""," "):
            del item
        else:
            print(f"invalid option detected: {item}")
            print(f"please only use accepted switches: -t, -e")
            print("or their attached argument list -t{ut,cc,sa} -e{send,vsc,zip,tgz}")
            return 0
    return "-".join(items)

def basic_validate_members(items, item_type="class"):
    """does basic validation for a standard inlines' members
        1. ensure each item is identifier
        2. ensure it has appropriate case

    items [list | str] : class name or attributes/methods to validate.
    item_type="class" [str] : which type of identifier to validate- class or field.

    returns:  
    """
    if item_type == "options":
        return validate_options(items)
    container = []
    for item in items:
        item = item.strip()
        if is_identifier(item):
            container.append(case_check(item, item_type=item_type))
    return container


def basic_validate(inline : str, verbose=False):
    """ needs revision- only return 0 or 1 based on whether the tests succeeded
    """
    inline = inline.split(":")
    #fall through test - cant generate class if no class names are provided
    if inline[0].strip():
        classes = basic_validate_members((inline[0].strip()).split(","))
        if len(inline) > 1:
            if inline[1].strip():
                attributes = basic_validate_members((inline[1].strip()).split(","), item_type="field")
                # Most desirable condition- classes, attributes, methods have all been provided.
                if len(inline) > 2 and inline[2].strip():
                    methods = basic_validate_members((inline[2].strip()).split(","), item_type="field")
                    if len(inline) > 3 and inline[3].strip():
                        options = basic_validate_members((inline[3].strip()), item_type="options") 
                    else:
                        return Inline.from_individual_arguments(classes, attributes, methods, verbose=verbose)
                    return Inline.from_individual_arguments(classes, attributes, methods, options, verbose=verbose)
                else:
                    if missing_field(type="method"):
                        if len(inline) > 3 and inline[3].strip():
                            options = basic_validate_members((inline[3].strip()), item_type="options") 
                        else:
                            return Inline.from_individual_arguments(classes, attributes, None, verbose=verbose)
                        return Inline.from_individual_arguments(classes, attributes, None, options, verbose=verbose)
            else:
                # redundant but prevents methods from being
                #  undefined in if below in same else block.
                if len(inline) > 2 and inline[2].strip():
                    methods = basic_validate_members(inline[2].strip().split(","), item_type="field")
                else:
                    if missing_field(type="none"):
                        if len(inline) > 3 and inline[3].strip():
                            options = basic_validate_members((inline[3].strip()), item_type="options") 
                        else:
                            return Inline.from_individual_arguments(classes, None, None, verbose=verbose)
                        return Inline.from_individual_arguments(classes, None, None, options, verbose=verbose)
                if missing_field(type="attribute"):
                    if len(inline) > 3 and inline[3].strip():
                        options = basic_validate_members((inline[3].strip()), item_type="options") 
                    else:
                        return Inline.from_individual_arguments(classes, None, methods, verbose=verbose)
                    return Inline.from_individual_arguments(classes, None, methods, options, verbose=verbose)
        else:
            # make an Inline w/ niether fields if user accepts that.
            if missing_field(type="none"):
                if len(inline) > 3 and inline[3].strip():
                    options = basic_validate_members((inline[3].strip()), item_type="options") 
                else:
                    return Inline.from_individual_arguments(classes, None, None, verbose=verbose)
                return Inline.from_individual_arguments(classes, None, None, options, verbose=verbose)
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
        response = input("proceed with generation (y/n)?\n")
        if response in ("y", "yes"):
            return 1
        elif response in ("n", "no"):
            return 0
        else:
            print("sorry, didnt understand your response. valid: y or n")


def validate_mulitple(inline: str):
    """
    """
    inline = Inline.from_individual_arguments(*inline.split(":"))
    if inline.classes.count(",") < inline.attributes.count("/"):
        print("Error: too many attributes.\n\
make sure the number of ',' in classes is equal to num of '/' in attributes.")
        return 0
    if inline.classes.count(",") > inline.attributes.count("/"):
        print("Error: not enough attributes.\n\
make sure the number of ',' in classes is equal to num of '/' in attributes.")
        return 0
    if inline.classes.count(",") < inline.methods.count("/"):
        print("Error: too many methods.\n\
make sure the number of ',' in classes is equal to num of '/' in methods.")
        return 0
    if inline.classes.count(",") > inline.methods.count("/"):
        print("Error: not enough methods.\n\
make sure the number of ',' in classes is equal to num of '/' in methods.")
        return 0
    if inline.classes.count(",") < inline.options.count("/"):
        print("Too many options.\n\
make sure the number of ',' in classes is equal to num of '/' in options.")
        return 0
    ### What else could go wrong with multiple class inline spec?
    return 1

def validate_inheritance(inline: str):
    """[summary]
    """
    return NotImplemented

def validate_file(filename : str):
    """[summary]

    Args:
        filename (str): [description]
    """

def validate_packaging(inline : str):
    """[summary]

    Args:
        inine (str): a packaging inline of the format <p:( package : files )
        or <p:{package1 : files, package2 : files, ... packageN : files}
    """
    # have to be careful when parsing- not to confuse
    #  inheritance w/ packaging because of closing >
    if not inline.startswith('<p:(') and not inline.endswith('>'):
        print("Error- invalid format of packaging inline")
        return 0
    else:
        #expose content of syntax/ expression
        # by removing '<p:(' and ')>'
        contents = inline[3:-1]
        print(contents)
        print(contents[1:-1])
        if contents.startswith("(") and contents.endswith(")"):
            return validate_single_packaging_inline(contents[1:-1])
        else:
            # can just take the first version of contents & treat it as dict.
            return validate_multiple_packaging_inline(contents)

def validate_multiple_packaging_inline(inline):
    """

    Args:
        inline ([type]): [description]
    """

def validate_single_packaging_inline(inline):
    inline = inline.split(":")
    if len(inline) == 2:
        if is_identifier(inline[0]):
            if corrected := case_check(inline[0],item_type="package"):
                print(corrected)
        else:
            print(f"Error- title you provided for package {inline[0]}\
is invalid. see pep8.")
            return 0
        if is_identifier(inline[1]):
            if corrected := case_check(inline[1], item_type="module"):
                print(corrected)
        else:
            print(f"Error- module name you provided for\
module/file {inline[1]} is invalid. see pep8")
    else:
        return validate_multiple_packaging_inline({inline[x] : inline[x+1] for x in range(0, len(inline), 2)})


if __name__ == "__main__":
    ### unit testing

    # testing multiple_validate:
    # testing = validate_mulitple("classA, classB : attr1, attr2 / attr3, attr4 : methodA / methodB : -e{vsc} / -e -t{ut,cc}")
    # print(testing)

    # are these values case corrected and indeed identifiers?
    # print(basic_validate_members(['  attr1', ' attr2 '], item_type="field"))

    # print(ask_case("Shite", item_type="field"))
    # print(case_check("Shite", item_type="field"))



    # tests to see if fails when no class is provided
    # basic_validate(": attr1, attr2 : method")

    # what happens when no attributes are provided?
    # item = basic_validate("biscuit : : method1, leaftrap")
    # print(item)

    # what happens when no methods are provided?
    # basic_validate("biscuit : gravy, sausage : ")

    # when niether fields are provided?
    # basic_validate("Biscuit : :")

    # complete and correct inline
    # item = basic_validate("Biscuit : gravy, sausage : method1, method2 : -t -e{ut,cc}")
    # print(item)

    # #accepts valid options only- returning them in correct format
    # print(basic_validate_members(" -t -e{ut,cc}", item_type="options"))
    # print(basic_validate_members("-e -t{ut,cc}", item_type="options"))
    # print(basic_validate_members(" -t{ut,cc} -e", item_type="options"))


    # #denies anything but -t, -e or -t{args}, -e{args} or combination of them
    # print(basic_validate_members(" -z{ut,cc} -f", item_type="options"))


    # does it case correct all incorrect claSSES, attributes and methods?
    # basic_validate("biscuit : Gravy, SAusage : MAthod1, meTHOod2")

    validate_packaging("<p:(skone : nard)>")