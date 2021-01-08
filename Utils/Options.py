"""
Programmer: Ben Sehnert
Program: Options module- deals with parts of the command that are optional - switches, default args etc...
Date: 12/27/2020
Software: Python class generator


Defining various methods that facilitate cmd line execution of class generator"""

# from parsing.inline import Inline
import argparse


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


