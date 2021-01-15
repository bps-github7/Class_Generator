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

from parsing.packaging import packaging
from parsing import inheritance_builder
from parsing.inline import Inline
from parsing.class_dict import ClassDict
from parsing.validation import validate, validate_file, validate_inheritance, validate_multiple, validate_packaging, validate_packaging
from utils.interactive import interactive_mode
from utils.options import args
from utils.editing_menu import get_feedback

# This part of the prg will have to print out a table of the classes to generate
# and bring the user attention to problems with the proposed generations.
# then they can select a row in the table to modify their proposed classes.
# only when they approve/ it is fully validated can they submit it for generating.

version = 1.2

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


def parse_inline(inline : Inline, verbose=False):
    """[summary]

    Args:
        inline ([type]): [description]

    Returns:
        list: A list of all the inlines parsed out of the current inline spec.
    """

    ### its important that we test the followin before validating
    ### because some of the tokens for our syntax would fail basic validation.
    parsed_classes = []
    if inline.classes.count(","):
        if inline.classes.count(">"):
            if inline.classes.count("<"):
                if validate_packaging(inline):
                    parsed_classes.append(packaging.main(inline))
                    if verbose:
                        print("parsing an packaging inline\n\
 containing inheritance and multiple classes.")
            else:
                if validate_inheritance(inline):
                    parsed_classes.append(inheritance_builder.main(inline))
                    if verbose:
                        print("parsing an inline spec containing inheritance hierarchy.")
        else:
            if validate_multiple(inline):
                parsed_classes.append(multiple_inline_handler(inline))
                if verbose:
                    print("parsing non inheritance inline w multiple classes")
    else:
        print("single class ready for validation")
        # casting to a list for safety reasons.
        if validate(inline):
            parsed_classes.append(ClassDict(inline.classes,
                inline.attributes, inline.methods,
                object, 'root',
                inline.options))
            if verbose:
                print("parsed a single inline specification.")
    return parsed_classes

### worried you are criss crossing responsbilities
### this might have been better left in inline.
### and called 'main'- who calls it tho?
def parse(inline: Inline) -> int:
    classes = parse_inline(inline)
    return get_feedback(classes)

def nesting_check(line):
    return True if line.count("<") else False


def inheritance_check(line):
    return True if line.count(">") else False

### confusing how you seem to have 3 differnet functions
### that do a job that would indicate being the main function

# This could be the main function in utils.options.py  
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
        return parse(Inline(args.inline))
    elif args.file:
        if args.verbose:
            print("reading classes from a file...")
        # if validate_file(args.file):
            # return parse(Inline)
    else:
        if args.verbose:
            print("using interactive mode")
        return interactive_mode()

    # Reaching here means the parsing was unsuccessful
    # and class will not be generated
    return 0