"""main function for class generator, called at begining of program runtime.
"""
from parsing.inline import Inline
import argparse
import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator\\parsing")


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


# optional switches: -i -abc, -sa, -sm, -sb,
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


def main() -> int:
    """
    Top level function for getting specs, parsing append generating class.

    Returns:
        int: success/failure signal
        1 = success
        0 = failure
    """
    project_name = args.name
    project_path = args.path
    print(f"proposed project path: {project_path}/{project_name}")
    # make dir / file with this ^^^ and change to that directory.
    if args.inline:
        item = Inline.string_to_inline(args.inline)
        if item.has_inheritance():
            # packaging can be nested like this because
            # doesnt make a lot of sense to have a packaging spec
            # without inheritance, otherwise just use name + path.
            if item.has_packaging():
                specs = Inline(item)
                print("building a classdict with a inline with packaging")
                #specs = packaging.main()
            else:
                print("building an class dict with inline with inheritance")
                #specs = inheritancebuilder.main()
        else:
            #specs = inline.main()
            print("building a classdict with standard inline")
    elif args.file:
        print("reading classes from a file...")
        # specs = file.main()
    else:
        print("using interactive mode")
        # specs = interactive.main()
    # generate the class based on the specs
    return 1

# def test() -> int:
#     """
#     """
#     if args.name:
#         print(f"name is : {args.name}")
#         # create a directory for the project with this name
#     if args.path:
#         print(f"recieved path: {args.path}")
#         # change wd to path + \ + name
#         # continue run time
#     else:
#         pass
#         # create file in cwd
#         # change we to cwd
#         # write to file

#     if args.inline:
#         #inline = inline.string_to_inline(args.define)
#         print(f"inline parsed: {args.inline}")

#         # inline.main()
#     else:
#         print("using interactive mode")
#         # interactive.main()
#     if args.abstract_base_class:
#         print(f"abc : {args.abstract_base_class}")
#     if args.skip_attributes:
#         print(f"skip attributes : {args.skip_attributes}")
#     elif args.skip_methods:
#         print(f"skip methods: {args.skip_methods}")
#     else:
#         print(f"skip both: {args.skip_both}")
#     if args.testing:
#         print(f"args.testing {args.testing}")
#     if args.exporting:
#         print(f"args.exporting {args.exporting}")


main()
