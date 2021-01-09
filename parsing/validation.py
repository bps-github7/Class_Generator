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
from parsing.class_dict import ClassDict
from parsing.class_dict import ClassDict
from utils.editing_menu import get_feedback

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
            if case_prompt(item):
                return item.title().strip()
            return item.strip()
    else:
        if item.islower():
            return item.strip()
        else:
            if case_prompt(item, item_type="field"):
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
    """
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

def multiple_inline_handler(inline : Inline):
    """[summary]

    Args:
        inline ([type]): [description]
    """
    specifications = []
    classes, attributes, methods, options = [], [], [], []
    ### need to validate the inline before using this
    ### to confirm number of / and , match up correctly.
    for single_class, its_attributes, its_methods, its_options in zip(
            inline.classes.split(","),
            inline.attributes.split("/"),
            inline.methods.split("/"),
            inline.options.split("/")):
        classes.append(single_class)
        attributes.append(its_attributes)
        methods.append(its_methods)
        options.append(its_options)
    # setting parent and package to defaults in this and else block below
    # until we sophisticate the packaging and inheritance functionality a bit more.

    ### should call basic_Validate here instead of classdict- do that later..
    specifications = [ClassDict(class_title, attribute_group,
    method_group, object, 'root', options_group)\
    for class_title, attribute_group, method_group, options_group\
    in zip(classes, attributes, methods, options)]
    return specifications

def validate_mulitple(inline: str):
    """
    """
    # inline = inline.split(":")
    return multiple_inline_handler(Inline.from_individual_arguments(*inline.split(":")))

def validate_inheritance(inline: str):
    """[summary]
    """
    return NotImplemented


def validate(inline: str, verbose=False):
    """

    Args:
        inline (str): [description]

    Returns:
        [type]: [description]
    """
    if verbose:
        print("inline succesfuly parsed")
    if inline.count(">"):
        # if item.has_packaging():
            # if args.verbose:
                # print("building a classdict with a inline with packaging")
            #return packaging.main()
        # else:
            # if args.verbose:
                # print("building an class dict with inline with inheritance")
        return validate_inheritance(inline)
    else:
        return basic_validate(inline)

def validate_file(filename : str):
    """[summary]

    Args:
        filename (str): [description]
    """

def parse_inline(inline):
    """[summary]

    Args:
        inline ([type]): [description]

    Returns:
        list: A list of all the inlines parsed out of the current inline spec.
    """

    ### its important that we test the followin before validating
    ### because some of the tokens for our syntax would fail basic validation.
    if inline.classes.count(","):
        if inline.classes.count(">"):
            if inline.classes.count("<"):
                print("packaging inline containing inheritance and multiple classes.")
            else:
                print("non packaging inline with inheritance and multiple classes.")
                # inheritance fn handles multiple classes by default- what about a singleton
        else:
            print("non inheritance inline w multiple classes")
    else:
        print("single class ready for validation")
        parsed_classes = multiple_inline_handler(inline)
    return parsed_classes
    # note the finished program will expect a classdict from here- or will require modification otherwise.    
    ### note that the above conditionals handle mutually exclusive conditions 
    ### meaning we have all the possible sets of condtions, but not every possible
    ### combination (aye aye ayye) see basic_validate for example of how we handled
    ### this in the basic inline.
    # else:
    #     # casting to a list for safety reasons.
    #     parsed_classes = [ClassDict(inline.classes,
    #         inline.attributes, inline.methods,
    #         object, 'root',
    #         inline.options)]
    # return parsed_classes

def main(inline: Inline) -> int:
    classes = parse_inline(inline)
    return get_feedback(classes)


if __name__ == "__main__":
    ### unit testing

    # testing multiple_validate:
    testing = validate_mulitple("classA, classB : attr1, attr2 / attr3, attr4 : methodA / methodB : -e{vsc} / -t{ut,cc}")
    print(testing)

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