"""Option

Raises:
    NameError: [description]

"""
# import argparse
import os, sys, argparse
from utils.path_testing import NoPathError, fix_relative_path, is_valid_path
from utils.path_testing import make_new_folder

# from parsing.inline import Inline
from parsing.parser import parse_inline
# from utils.interactive import interactive_mode


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
                    help="Use this short option to skip defining instance variables for your\
                    class", action="store_true", required=False)
group.add_argument("-sm", "--skip_methods",
                    help="Use this short option ", action="store_true", required=False)
group.add_argument("-sb",  "--skip_both", help="Use this short option to skip defining both\
                    attributes and methods", action="store_true", required=False)

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

def main():
    """Using args passed in from the cmd line
    further delegates the tasks of the program

    args : None

    returns:

        0 - indicates an error in parsing the arguments
        such as there was no project name provided.

    """
    ### should probably check here if .rc file is provided.


    #     1) complete path : 'project/path' + 'project_name'
    #     2) inlines : [list, of, inlines]
    #     3) statusReport : summary of workflow progress, errors, notes etc
    #     4) options : should we export the finished project and how? verbose mode, etc
    #     5) configs : is there an rc file present? if not, use default settings 
    workflow = {
        "completePath" : "",
        "name" : "",
        "path" : "",
        "verbose" : False,
        "configs" : {},
        "files" : []
    }
    if args.name:
        workflow['name'] = args.name
        if args.path:
            if not args.path.startswith("\\") and os.path.isabs(args.path):
                try:
                    if is_valid_path(args.path):
                        workflow['path'] = args.path
                except NoPathError as error:
                    print(error)
            else:
                path = fix_relative_path(args.path)
                try:
                    if is_valid_path(path):
                        workflow['path'] = path
                except NoPathError as error:
                    print(error)
        else:
            print("then check if we have configuration set for default path. else use CWD")
    else:
        raise NameError("You must provide a project name. (cannot generate a nameless folder.")
    if workflow["name"] and workflow["path"]:    
        tolken = "\\" if (os.name == "nt")  else "/"
        workflow['completePath'] = rf"{workflow['path']}{tolken}{workflow['name']}"
        print(f"proposed project path: {workflow['completePath']}")
        if input("looks good? (y/n)") in ("y", "yes"):
            make_new_folder(workflow["path"], workflow["name"])
        else:
            while True:
                print("ok. how would you like to proceed?")
                print("1) enter a new path")
                print("2) quit the program")
                response = int(input())
                if response == 1:
                    # fix this at some point- user should be able to re enter path, but its a bit of a mess to implement
                    sys.exit("user needs to enter a new path next run time")
                elif response == 2:
                    sys.exit("user wanted to quit the current run time")
    else:
        # shortcut- in reality we can just do that in cwd or config default path
        sys.exit("cannot build your project without a name and path")

    if args.verbose:
        print("determining source of input... (cmd line arg, file or interactive mode)")
    if args.inline:
        print("making an inline")
        # this returns the Inline object as it was just parsed
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

main()
