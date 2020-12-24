"""main function for class generator, called at begining of program runtime.
"""
import argparse
#from inline import string_to_inline
parser = argparse.ArgumentParser(description="Generate classes automatically using\command line options or interactive prompt")
group = parser.add_mutually_exclusive_group()

## #get the project name {mandatory}
#parser.add_argument(
#    "--name","--project-name",
#    type=str,metavar='',
#    help='Provide the name for the project you are creating.',
#    required=True)
#
## #Have this disabled for now, for conveinece/ testing sake.
## #indistro it will be required and testing will run automatically
#parser.add_argument(
#    "--path", "--project-path",
#    dest="default", type=str,
#    metavar='',
#    help="Provide a valid system path which project directory can be created in\nDefaults to the folder scipt is executed in",
#    required=False)
#
### #get class and attributes from a dictionary passed in through a string- write function to evaluate...
#parser.add_argument(
#     "--define", "--define-as-inline",
#     type=str, metavar='', dest="inline",
#     help="provide class specification as an inline spec argument",
#     required=False)
#
#parser.add_argument(
#    "-abc", "--abstract-base-class",
#    metavar='',  help="Use this option to generate class as abscract base class (can also prepend ABC to classname in inline spec).",
#    required=False)

#parser.add_argument(
#    "-f", "--skip-fields",
#    metavar='',
#    help="use this option to skip defining instance variables for your class",
#    required=False)
#
#parser.add_argument(
#    "-m", "--skip-methods",
#    metavar='',
#    help="use this option to skip defining methods for your class",
#    required=False)
#
#parser.add_argument(
#    "-b", "--skip-both",
#    metavar='',
#    help="use this option to skip defining both instance variables andmethods for your class",
#    required=False)
#

#parser.add_argument(
#    "-a", "--Alternative Constructor",
#    metavar='', 
#    help="Use this option to generate an alternative (class method) constructor for your class.",
#    required=False)
#

##### these args will require a bit of tinkering because they take a {keyword} shaped argument 
#
## #testing
#parser.add_argument(
#     "-t", "--testing",
#     type=str, metavar='',
#     help="Automatically generate unittests, static analysis, code coverage, additional documentation?",
#     choices=['ut','sa','cc','doc'],
#     required=False)
#
## #exportng
#parser.add_argument(
#     "-e", "--exporting",
#     type=str, metavar='',
#     choices=['tgz', 'zip', 'tgz and email', 'tgz and zip', 'tgz and SSH', 'zip and SSH'],
#     help="What should be done with the generated project {tgz, zip, tgz & email req arg: 'name@mail.com', zip and email, tgz and ssh, zip and ssh }",
#     required=False)

# #read arguments passed to the console.

#positional arguments- name and inline definition
parser.add_argument("name", help="Provide the name for the project you are creating.")
parser.add_argument("--inline", help="provide class specification as an inline spec argument", required=False)
parser.add_argument("--path", help="Provide a valid system path which project directory can be created in\nDefaults to the folder scipt is executed in",dest="path",required=False)

#optional switches: -abc, -sa, -sm, -sb, 
parser.add_argument("-abc", "--abstract_base_class", help="Use this short option to generate class as abscract base class (can also prepend ABC to classname in inline spec).", action="store_true",required=False)


#this should be a mutually exclusive group- can be -sa, -sm or -sb
group.add_argument("-sa", "--skip_attributes", help="Use this short option to skip defining instance variables for your class", action="store_true", required=False)
group.add_argument("-sm", "--skip_methods", help="Use this short option ", action="store_true", required=False)
group.add_argument("-sb",  "--skip_both", help="Use this short option to skip defining both attributes and methods", action="store_true", required=False)

# -t, -e are keyword switches- have a default, but can take {args = 'choice'} too
parser.add_argument("-t", "--testing", help="generate tests to your class(es)", choices=["ut","sa","cc"], dest="testing", required=False)
parser.add_argument("-e", "--exporting", help="export your generated class(es)", choices=["comp","send"], dest="exporting", required=False)

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
    if args.name:
        print(f"name is : {args.name}")
        #create a directory for the project with this name
        
    if args.path:
        print(f"recieved path: {args.path}")
        #change wd to path + \ + name
        #continue run time
    else:
        pass
        # create file in cwd
        # change we to cwd
        # write to file


    if args.inline:
        #inline = inline.string_to_inline(args.define)
        print(f"inline parsed: {args.inline}")
        
        #inline.main()
    else:
        print("using interactive mode")
        #interactive.main()
    if args.abstract_base_class:
        print(f"abc : {args.abstract_base_class}")
    if args.skip_attributes:
        print(f"skip attributes : {args.skip_attributes}")
    elif args.skip_methods:
        print(f"skip methods: {args.skip_methods}")
    else:
        print(f"skip both: {args.skip_both}")
    if args.testing:
        print(f"args.testing {args.testing}")        
    if args.exporting:
        print(f"args.exporting {args.exporting}")

main()