"""
Programmer: Ben Sehnert
Program: Options module- deals with parts of the command that are optional - switches, default args etc...
Date: 12/27/2020
Software: Python class generator


Defining various methods that facilitate cmd line execution of class generator"""
import argparse
from parsing.inline import Inline
from parsing.parser import parse_inline
from utils.interactive import interactive_mode


parser = argparse.ArgumentParser(
    description="Generate classes automatically using command line options or interactive prompt")
group = parser.add_mutually_exclusive_group()


# positional (required) arguments- name
parser.add_argument(
    "name", help="Provide the name for the project\
                        you are creating.")

# positional-y (non-required) arguments: --inline, --path, --file
parser.add_argument("--inline",
                    help="provide class specification as an inline\
                    spec argument", required=False)
parser.add_argument("--path",
                    help="Provide a valid system path which project directory\n\
                    can be created in\nDefaults to the folder scipt is executed in",
                    dest="path", required=False)
parser.add_argument("--file",
                    help="Provide a file as input, for supplying classes\n\
                    to generate via inline specification.",
                    dest="file", required=False)

# future- L for language selection- choices = python(default), Java, C++, C#, Php, JAvascript typescript


# optional switches: -v, -i -abc, -sa, -sm, -sb,
parser.add_argument("-v", "--verbose",
                    help="program will provide output to \n\
                    detail all operations taken during runtime",
                    action="store_true", required=False)

parser.add_argument("-i", "--interactive-mode",
                    help="Use this short option to generate classes in\n\
                    interactive mode. CLI app will guide you through\n\
                    the process of creating classes.",
                    action="store_true", required=False)


parser.add_argument("-abc", "--abstract_base_class",
                    help="Use this short option to generate class as abscract base class \n\
                    (can also prepend ABC to classname in inline spec).",
                    action="store_true", required=False)


# this should be a mutually exclusive group- can be -sa, -sm or -sb
group.add_argument("-sa", "--skip_attributes",
                   help="Use this short option to skip defining instance variables for your class", action="store_true", required=False)
group.add_argument("-sm", "--skip_methods",
                   help="Use this short option ", action="store_true", required=False)
group.add_argument("-sb",  "--skip_both", help="Use this short option to skip defining both attributes and methods",
                   action="store_true", required=False)

# -t, -e are keyword switches- have a default, but can take {args = 'choice'} too
parser.add_argument("-t", "--testing", help="generate tests to your class(es)",
                    choices=["ut", "sa", "cc"], dest="testing", required=False)
parser.add_argument("-e", "--exporting", help="export your generated class(es)",
                    choices=["comp", "send"], dest="exporting", required=False)

# parse the the arguments
args = parser.parse_args()


# def switches(inline):
#     '''Can tell if a inline spec has switch arguments'''
#     new = Inline.fromInline(inline)
#     print(new.attributes)


# switches("classA : attr1, attr2 : method")

# This could be the main function in utils.options.py  
def main():
    """Using args passed in from the cmd line
    further delegates the tasks of the program

    args : None

    returns:

        0 - indicates an error in parsing the arguments
        such as there was no project name provided.

    """
    ### should probably check here if .rc file is provided.
    
    if not args.name:
        print("Name Error: You must provide a project name.")
        return 0
    
    if not args.path:
        print("files will be generated in the current working directory")


    project_name = args.name
    project_path = args.path
    print(f"proposed project path: {project_path}/{project_name}")
    # make dir / file with this ^^^ and change to that directory.
    if args.verbose:
        print("determining source of input... (cmd line arg, file or interactive mode)")
    if args.inline:
        ### be v. careful to note- here inline is str
        #  after validation its type == Inline
        ### do not treat them as the same.
        return parse_inline(args.inline)
    elif args.file:
        if args.verbose:
            print("reading classes from a file...")
        # if validate_file(args.file):
            # return parse(Inline)
    else:
        if args.verbose:
            print("using interactive mode")
        # return interactive_mode()

    # Reaching here means the parsing was unsuccessful
    # and class will not be generated
    return 0
