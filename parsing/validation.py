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

def validate_options(items : str):
    """validates options by rejecting all
    that do not match the followning:
        -t 
        -e
        -t{value(s,)}
        -e{value(s,)}
        -2 part combination of any of the above.

    Args:
        items [str]: option string needing validation.

    Returns:
        items [str]: validated option string
                    with no leading/trailing white space.

        failure code [int] : returns 0 if validation tests fail.
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
    elif item_type in ("attribute","method"):
        item_type = "field"
    container = []
    for item in items:
        item = item.strip()
        if is_identifier(item):
            container.append(case_check(item, item_type=item_type))
    return container


def basic_validate(inline : str, verbose=False):
    """ needs revision- only return 0 or 1 based on whether the tests succeeded

    unlike typical validation functions in the module, revises inline
    correcting for incorrect case.

    returns:
    1. inline [Inline] - generates an inline w/ one to all arguments included.

    """
    inline = inline.split(":")
    # need to loop over here and strip whitespace from each element
    # the conditional below not specific enough to work correctly.

    #fall through test - cant generate class if no class names are provided
    if inline[0].strip():
        classes = basic_validate_members((inline[0].strip()).split(","))
        # need to figure out which arguments are provided
        if len(inline) > 1:
            # class + attributes
            if inline[1].strip() and len(inline) == 2:
                attributes = basic_validate_members(
                    (inline[1].strip()).split(","), item_type="attribute")
                if missing_field("methods or options"):
                    return Inline.from_individual_arguments(classes,
                    attributes, None, None)
            # class + methods
            elif inline[2].strip():
                methods = basic_validate_members(
                    (inline[2].strip()).split(","), item_type="method")
                if missing_field("attributes or options"):
                    return Inline.from_individual_arguments(classes,
                    None, methods, None)
            # class + options
            elif inline[3].strip():
                options = basic_validate_members(
                    (inline[3].strip()), item_type="options")
                if missing_field("attributes or methods"):
                    return Inline.from_individual_arguments(classes, None,
                    None, options)

            # class + attributes + methods
            elif inline[1].strip() and inline[2].strip():
                attributes = basic_validate_members(
                    (inline[1].strip()).split(","), item_type="attribute")
                methods = basic_validate_members(
                    (inline[2].strip()).split(","), item_type="method")
                if missing_field("options"):
                    return Inline.from_individual_arguments(classes,
                    attributes, methods, None)
            # class + attributes + options
            elif inline[1].strip() and inline[3].strip():
                attributes = basic_validate_members(
                    (inline[1].strip()).split(","), item_type="attribute")
                options = basic_validate_members(
                    (inline[3].strip()), item_type="options")
                if missing_field("methods"):
                    return Inline.from_individual_arguments(classes,
                    attributes, None, options)
            # class + methods + options
            elif inline[2].strip() and inline[3].strip():
                methods = basic_validate_members(
                    (inline[2].strip()).split(","), item_type="method")
                options = basic_validate_members(
                    (inline[3].strip()), item_type="options")
                if missing_field("attributes"):
                    return Inline.from_individual_arguments(classes,
                    None, methods, options)

            # class + attributes + methods + options
            else:
                print("the else block executed in basic_validate-\
all inline args provided")
                attributes = basic_validate_members(
                    (inline[1].strip()).split(","), item_type="field")
                methods = basic_validate_members(
                    (inline[2].strip()).split(","), item_type="field")
                options = basic_validate_members(
                    (inline[3].strip()), item_type="options")
                return Inline.from_individual_arguments(classes, attributes,
                methods, options)
        else:
            pass
    else:
        return missing_field()

def missing_field(type="class"):
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
        if continue_prompt(field_type = type):
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
        # print(contents)
        # print(contents[1:-1])
        if contents.count(","):
            # can just take the first version of contents & treat it as dict.
            inline = {}
            for items in contents[1:-1].split(","):
                inline.update({str(items.split(":")[0].strip()) : str(items.split(":")[1].strip())})
            return validate_multiple_packaging_inline(inline)
        else:
            return validate_single_packaging_inline(contents[1:-1])


def validate_multiple_packaging_inline(inline):
    """

    Args:
        inline ([type]): [description]
    """
    validated = {}
    for item in inline:
        if (valid := validate_single_packaging_inline(f"{item}:{inline[item]}")):
            if isinstance(valid, dict):
                validated.update(valid)
            else:
                return 0
        else:
            return 0
    return validated

def validate_single_packaging_inline(inline):
    inline = inline.split(":")
    # strip leading and trailing whitespace
    # that could make it fail is_identifier test.
    inline = list(map(lambda x: x.strip(), inline))
    # check that it is indeed a single package inline
    if len(inline) == 2:
        if (package := validate_package_name(inline[0])) and (module := validate_module_name(inline[1])):
            # does the above test fail if either return 0? ensure this!
            return {package : module}
        else:
            return 0
    else:
        return validate_multiple_packaging_inline({inline[x] : inline[x+1] for x in range(0, len(inline), 2)})

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
    item = basic_validate("Biscuit : gravy, sausage : method1, method2 : -t -e{ut,cc}")
    print(item)

    # #accepts valid options only- returning them in correct format
    # print(basic_validate_members(" -t -e{ut,cc}", item_type="options"))
    # print(basic_validate_members("-e -t{ut,cc}", item_type="options"))
    # print(basic_validate_members(" -t{ut,cc} -e", item_type="options"))


    # #denies anything but -t, -e or -t{args}, -e{args} or combination of them
    # print(basic_validate_members(" -z{ut,cc} -f", item_type="options"))


    # does it case correct all incorrect claSSES, attributes and methods?
    # basic_validate("biscuit : Gravy, SAusage : MAthod1, meTHOod2")

    # does validate_packaging work for a single package spec
    # if valid := validate_packaging("<p:(skone : n%ard)>"):
    #     print(f"validated package: {valid}")
    
    # # what about a multiple package spec?
    # if validate_packaging("<p:(skone : !nard, moofy : mofty, shitpike : w90easel, monkey : orangutang)>"):
    #     print("we did it\n"*2)
    # else:
    #     # seems the test works. consider further nuances.
    #     print(validate_packaging("<p:(skone : nard, moofy : mofty, shitpike : w90easel, monkey : orangutang)>"))
    # validate_multiple_packaging_inline({'skone' : 'nard', 'moofy' : 'mofty', 'shitpike' : 'weasel', 'monkey' : 'orangutang'})