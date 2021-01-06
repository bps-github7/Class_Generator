# Programmer: Ben Sehnert
# Program: Misc_Functions Module
# Software: Python class Generator
# Date: 1/21/2020

import sys
import os
import errno
import tempfile

sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")


"""Module defines miscellaneous functions used for the class generator"""


def get_confirmation(opt_code, line):
    """Asks user if they are satisfied with their choice"""
    opts = {1: "line no.{} has no colons- meaning your class has no attributes or methods,\
        \n or this line was incorrectly defined".format(line),
            2: "No attributes provided for specs on line no. {}".format(line),
            3: "No methods provided for specs on line no. {}".format(line)}
    print(opts[opt_code])
    while True:
        ans = input("Do you wish to proceed with generating this line? (y/n)")
        if ans in ("y", "yes"):
            return True
        elif ans in ("n", "no"):
            return False

def isWritable(path):
    try:
        testfile = tempfile.TemporaryFile(dir=path)
        testfile.close()
    except OSError as e:
        if e.errno == errno.EACCES:  # 13
            return False
        e.filename = path
        raise
    return True


def make_new_folder(path, project_name):
    os.chdir(path)
    new = os.path.join(path, project_name)
    if not os.path.exists(new):
        os.mkdir(new)
        os.chdir(new)
        return 1
    else:
        ### why not just change dir to this existing one?
        print("Error: a folder already exists with this name.")
        return 0

# Seems like there is a  logic/ exception error somewhere- keep getting this error message in cmdline mode

def test_paths(paths):
    """like the test_path fn but works on an array of potential paths

    Args:
        paths ([list]): list of potential paths for validating
    """
    valid, invalid = [], []
    for item in paths:
        if os.path.exists(item) and os.path.isdir(item) and isWritable(item):
            valid += item
        else:
            invalid += item
    if invalid:
        print("the following are not valid packages for use in this program:")
        for i in invalid:
            print(i)
        # response = input("Learn more (y/n) ?")
        # if response in ("y", "yes"):
        #     path_error_message(path)
    return valid if len(valid) > 0 else 0

def test_path(path, first=True):
    """checks if a path is valid for use in generating class files
    
    returns 1 for root, 0 for invalid root, validated path or list of validated paths
    depeding on if path argument is string or list.
    """
    if path == 'root':
        return 1
    if isinstance(path, list) and len(path) > 0:
        return test_paths(path)
    if os.path.exists(path) and os.path.isdir(path) and isWritable(path):
        return path
    else:
        if first:
            # avoids redundant printing of error messages
            print("error with the path for a package or default path you provided.")
            response = input("learn more (y/n)?")
            if response in ("y", "yes"):
                path_error_message(path)
        return 0


def path_error_message(path):
    print("Error: there is an issue with the path provided")
    print("Please check the following:")
    issues = ["1. Is the default path: {} a valid, fully qualified path?".format(path),
                "2. Does the default path lead to a valid directory in the file system? (ie. not a file, filesystem, shortcut. etc...)",
                "3. Is the default path provided a writable directory? (ie. does the current user have the nescesary privalleges to write in this directory?)"]
    for issue in issues:
        print(issue)


def from_file(f, results=[]):
    """
builds a container out of text file
containing class dict specifications inline format.
    """
    # need to account for lack of .txt in POSIX systems
    with open("{}.txt".format(f), "r") as file:
        for num, line in enumerate(file):
            if line.startswith("#") or line.startswith("//"):
                # enables the user to 'comment out' lines with both JS and python style of commenting
                continue
            copy = line.strip("\n")
            line = line.split(":")
            if line[0] in ("", " ", "\t", "\t\t", None):
                print("Cannot produce a class/classes without name(s).\n\
Please review/revise the following class specification:\n {}on line no.{}\n".format(copy, num))
            elif line[1] in ("", " ", "\t", "\t\t", None):
                if get_confirmation(2, num):
                    results.append(copy)
            elif line[2] in ("", " ", "\t", "\t\t", " \n", " \t\n", "\t\t\n" "\n", None):
                if get_confirmation(3, num):
                    results.append(copy)
            else:
                """ 
                should call Inline.to_dict
                 """
                results.append(copy)
        return results




def list_to_str(a, delimiter=","):
    """
Takes a list and returns a string.
    """
    return '{}'.format(delimiter).join(map(str, a))


def custom_strip(string):
    """
Dumb I know, but strip is a method, not a callable function
    """
    return string.strip()


def str_to_list(a, delimiter=","):
    """
Takes a string and returns  a list
    """
    # have u tried switching custom_strip with a.strip
    # try on REPL cuz dont know why a object method isnt a callable
    return list(map(custom_strip, a.split(delimiter)))


# def inheritance(name, attributes, methods=None, parent='object', runs=0):
#     """
# <Abstract: >
#     Handles inheritance. Breaks up passed in string argument, that tells us
#     the names and attribute lists for a class.
# <Dev notes: >
#     last updated Thursday 2/20/2020 9:27pm EST
#     everything is working as hoped/expected.
#     would be wise to modularize and test drive develop this some more.
#     im sure there are unexpected issues lurking.
#    """
#     # methods = list_to_str(methods)
#     family = name.split(">")
#     family_attributes = attributes.split(">")
#     #family_methods = methods.split(">")
#     if len(family) != len(family_attributes):
#         print("Error: mismatch in number of classes and attributes\n\
#         Make sure that occurences of /'>/' are consistent on \n\
#         both sides of : in -c option's dictionary")
#         return 0
#     # we now have a family of class names and class attributes,
#     # belonging to the first family in the list
#     parents = family[0]
#     parent_attr = family_attributes[0]
#     # we will enumerate the current members, delimited by a
#     # comma, or backslash for attribute listings
#     inheriter(parents, parent_attr, parent=parent.strip(), runs=runs)
#     del family[0]
#     del family_attributes[0]
#     name = " > ".join(family)
#     attr = " > ".join(family_attributes)
#     # calling it with runs = 1 so that function knows it's been called before.
#     if len(family) > 0:
#         inheritance(name, attr, parent=parents.strip(), runs=1)
#     else:
#         # finished succesfully!
#         return 0


# def inheriter(parents, parent_attr, parent='object', runs=0):
#     for x, y in zip(parents.split(","), parent_attr.split("/")):
#         if runs == 0:
#             modified_generator(x.strip(), str_to_list(y))
#         # case where the inheritance function has already been invoked once.
#         else:
#             modified_generator(x.strip(), str_to_list(y), parent=parent)

# additional command line options.


def make_unittest(name, attr):
    with open("Test_{}.py".format(name), "a+") as file:
        file.write("import unittest \n\nfrom {} import {}".format(name, name))
        file.write("\n\n'''Module Level Docstring goes here'''\nclass Test_{}\
(unittest.TestCase):\n    '''Class Level DocString goes here'''\n    Version = 0.1\n")
        file.write(
            "    def setUp(self):\n        self.m = {}('need to enter test values here before your unittest can be run')\n\n")


def export():
    '''Implements options for exporting the finished class file via email, ssh, tgz and etc'''
    pass

# make_methods("walp,chalp,skone,SMmode,CMnode")
#inheritance("skone, chalp, bisk > apricot, fritter", "skn1, skn2, skn3 / chalp1,chalp2,chalp3,chalp4 / bisk1,bisk2,bisk3 > apc1,apc2,apc3 / frit1,frit2,frit3,frit4,frit5,frit6")
