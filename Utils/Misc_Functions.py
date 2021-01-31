# Programmer: Ben Sehnert
# Program: Misc_Functions Module
# Software: Python class Generator
# Date: 1/21/2020

import re
import sys
import os
import errno
import tempfile

sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")


"""Module defines miscellaneous functions used for the class generator"""

def get_extension(cls):
    """
takes class string and gets parent and packaging out of it
    """

    ### NOTE: args must be passed in like they appear in the string
    ### ie. finished = ['class_name', 'parents', 'packages']
    finished = []
    ### example(parents) (packages)
    if cls.count(") ("):
        classes = cls.split(") (")
        finished.append(classes[0].split("(")[0].strip())
        finished.append(classes[0].split("(")[1].strip())
        finished.append(classes[1].strip(")"))
    ### Only the packaging - example (packages)
    elif cls.count(" ("):
        classes = cls.split(" (")
        finished.append(classes[0].strip())
        finished.append(object)
        finished.append(classes[1].strip(")").strip())
    ### only the parent - example(parents)
    elif re.match(r"(\w)*[(]", cls):
        classes = cls.split("(")
        finished.append(classes[0].strip())
        finished.append(classes[1].strip(")").strip())
        finished.append("root")
    else:
        finished.append(cls.strip())
        finished.append(object)
        finished.append("root")
    return finished


def cleanse(items: any, item_type="field"):
    """format properties by strip and lowercase of each elements.
    side-effect: coerces ',' delimited string to formatted list.
    """
    if isinstance(items, list):
        return list(map(
            lambda item: item.strip().lower(), items))
    return list(map(
        lambda item: item.strip().lower(), items.split(",")))


def clean_list(args):
    """Turns a list of arguments into a clean list of string arguments.
    This makes it possible to take a machine readable class spec and pass it
    to Inline alternative constructor

    Arguments:
        *args [string []] : up to four pieces of Inline.

    Returns:
        item [list]: A list of comma seperated values
    """
    items = [*args]
    for i, value in enumerate(items):
        if value is None:
            continue
        if isinstance(value, list):
            items[i] = ",".join(value)
    return items



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
    # accounting for need for FTYPE extension in windows
    # if OS is windows and .txt is not provided, add it.
    if os.name == 'nt':
        if not f.endswith('.txt'):
            f += '.txt'  
    with open("{}".format(f), "r") as file:
        for num, line in enumerate(file):
            # enables the user to 'comment out' lines with both JS and python style of commenting
            if line.startswith("#") or line.startswith("//"):
                continue
            # ignore lines that are just a new line or whitespace
            if line.strip() in  ("\n", "", " "):
                continue
            copy = line.strip("\n")
            ### need to enforce validation here- reject or correct
            ### lines that dont conform to inline standards.
            results.append(line)
        return results

# print(from_file("classes.txt"))