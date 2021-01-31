"""
Programmer: Ben Sehnert
Program: conventions module
Software: Python Class Generator
Date: 1/9/2021

"Conventions" implies the things which are considered 'best practice'
for that reason, all changes to identifiers imposed by side effects of
this module will require the users input unless instructed otherwise ("coereced")

all identifiers (when instructed / prefered to) will abide by the following pep8 guidelines:

1. class name: all first letters of words capitalized, no spaces between words.
2. attributes and methods: all lowercase with underscores seperating words when nescesary.
3. packages: all lowercase with no spaces between words.
4. modules: all lowercase with underscores seperating words when nescesary.

the main functions of the module are

-check_case(item : str, item_type="class", preference="ask")
    returns -> a potentially case corrected name.
-is_identifier(ident)
    returns -> bool based on whether or not a given identifier is valid.

Functions implemented in Conventions.py module:

-is_identifier(ident) -> [bool] : returns True if the argument
    provided is a valid python identifier.

-ask_case(item, item_type="class") -> [return value(s)] : asks if user wants 
    to correct case of an identifier provided with incorrect case.

-case_prompt(item, item_type="class") -> [return value(s)] : about

-coerce_case(item, item_type="class") -> [return value(s)] : about

-case_check(positional, keyword) -> [return value(s)] : about

-class_correct_convention(positional, keyword) -> [return value(s)] : about

-field_correct_convention(positional, keyword) -> [return value(s)] : about

-package_correct_convention(positional, keyword) -> [return value(s)] : about

-module_correct_convention(positional, keyword) -> [return value(s)] : about
"""
import keyword

version=1.2

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
    ### classes- uppercase begin of words, no spaces or underscores.
    if item_type == "class":
        if item[0].islower() or item.count(" ") or item.count("_"):
            if case_prompt(item):
                return coerce_case(item)
            return item.strip()
        return item.strip()
    elif item_type == "parent":
        if item[0].islower() or item.count(" ") or item.count("_"):
            if case_prompt(item):
                return coerce_case(item)
            return item.strip()
        return item.strip()
    
    # need to distingush between attributes and methods!
    # methods can and should have _ between words.
    elif item_type == "field":
        if not item.islower() or item.count(" "):
            if case_prompt(item, item_type=item_type):
                return coerce_case(item, item_type=item_type)
            return item.strip()
        return item.strip()
    ### shoudl be all lowercase with no spaces, underscores btw words.
    elif item_type == "package":
        if not item.islower() or item.count(" ") or item.count("_"):
            if case_prompt(item, item_type=item_type):
                return coerce_case(item, item_type=item_type)
            return item.strip()
        return item.strip()
    ### all lowercase with underscores between words.
    elif item_type == "module":
        if not item.islower() or item.count(" "):
            if case_prompt(item, item_type=item_type):
                return coerce_case(item, item_type=item_type)
            return item.strip()
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
            response = input(f"your class name {item} violates naming\n\
conventions\nsuch as improper capitalization or incorrect use of whitespace\n\
(classes should have no whitespace between words and words beginning with\
uppercase letter)\n\
This violates PEP8 best practices- should this be corrected (y/n)?\n")
        elif item_type == "field":
            response = input(f"your field name {item} violates naming\
conventions\nsuch as improper capitalization or incorrect use of whitespace\
(attributes and methods should be all uppercase and have no whitespace\
between words)\nThis violates PEP8 best \
practices- should this be corrected (y/n)?\n")
        elif item_type == "package":
            response = input(f"your package name {item} violates naming\
conventions\nsuch as improper capitalization or incorrect use of whitespace\
(packages should be lowercase with no whitespace between words)\n\
This violates PEP8 best practices- should this be corrected (y/n)?\n")
        elif item_type == "module":
            response = input(f"your module name {item} violates naming\
conventions\nsuch as improper capitalization or incorrect use of whitespace\
(modules should be lowercase with underscores between words when needed)\n\
This violates PEP8 best practices- should this be corrected (y/n)?\n")
        if response in ("y", "yes"):
            return 1
        return 0

def coerce_case(item, item_type="class"):
    if item_type == "class":
        return class_correct_convention(item)
    elif item_type == "field":
        return field_correct_convention(item)
    elif item_type == "package":
        return package_correct_convention(item)
    elif item_type == "module":
        return module_correct_convention(item)


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

def class_correct_convention(item):
    """
    I suspect this function is causing
    problems down the line (see test_validation.py)
    test_validate_four_piece_inline-

    ClassA is getting mapped to all four
    arguments for inline- check here, validate_members
    and Inline.from_individual_arguments alt constructor.

    Args:
        item ([type]): [description]

    Returns:
        [type]: [description]
    """
    if item.count(" ") or item.count("_"):
        # checking whether space or underscore was used as word delimiter.
        if item.count(" ") > item.count("_"):
            item = item.split(" ")
        elif item.count(" ") < item.count("_"):
            item = item.split("_")
        item = list(map(lambda x: x.title(), item))
        return ("".join(item)).replace("_", "").replace(" ","")
    # if there is no white space, best we can do it capitalize first letter 
    return item[0].upper() + item[1:]

def field_correct_convention(item):
    # the best we can do for correcting field word spacing.
    return item.strip().lower().replace(" ","_")

def package_correct_convention(item):
    return item.strip().lower().replace(" ","").replace("_","")

def module_correct_convention(item):
    return item.strip().lower().replace(" ","_")
