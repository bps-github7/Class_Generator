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
from parsing.inline import Inline


"""Module defines miscellaneous functions used for the file generator

Remaining files in here (with one exception) are relevant to the first
step of run time, which is determining the location in file system where
the workflow should be generated

"""


def path_main(path = "root"):
    if path == "root":
        if test_path(os.getcwd()):
            return os.getcwd()
        raise OSError("there is a problem with the path you provided")
    elif path != os.getcwd():
        while True:
            if not validate_path(path):
                path = input("provide a new, valid path to proceed with generation, or type q to quit:\n")
                if path.lower() == "q":
                    return 0
            else:
                break
        return validate_path(path)
        
def validate_path(path):

    # handle relative paths 
    if os.path.isabs('.'):
        print("abs path. YAY!")
    else:
        path = fix_relative_path(path)    
    # run tests to see 
    try:
        os.path.exists(path)
        os.path.isdir(path)
        isWritable(path)
        return path
    except (OSError, NotADirectoryError):
        print("the path you provided is not valid")
        return 0

def fix_relative_path(path) :
    """automatically concatenates relative paths so they
    refer to absolute location in system instead

    handles nuances of windows vs unix based systems.

    Args:
        path ([type]): [description]

    Returns:
        [type]: [description]
    """
    if path.startswith("./"):
        path = path[2:]
    # ooof this is a another headache
    # elif path.startswith("../")
    elif path.startswith("\\") or path.startswith('/'):
        path = path[1:]

    if os.name == "nt":
        if "/" in path:
            path = path.replace("/","\\")
        return os.getcwd() + "\\" + path
    return os.getcwd() + "/" + path

    
    # realizing now, we can skip checking the OS and getting a matching symbol. just look at what symbol is used in the path already!
    
    # if os.name == "nt":
    #     join_symbol = '\\'
    # return os.getcwd() + join_symbol        


def isWritable(path):
    try:
        testfile = tempfile.TemporaryFile(dir=path)
        testfile.close()
    except OSError as err:
        if err.errno == errno.EACCES:  # 13
            return False
        err.filename = path
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

def test_path(path, first=True):
    """checks if a path is valid for use in generating class files
    
    returns: 
        1 for root, 
        0 for invalid root, validated path or list of validated paths
    depeding on if path argument is string or list.
    """
    if path == 'root':
        return 1
    # if isinstance(path, list) and len(path) > 0:
    #     return test_paths(path)
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

# not sure this is super useful - user cant generate in multiple locations in the same session.
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




#this should be in parsing module - check who depends on it before you move it.
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
            results.append(Inline(line))
        return results

# todo: check references this could be outdated. im pretty sure the extension class deals with it
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

if __name__ == "__main__":
    try:
        returned = path_main("C:\caluga")
    except OSError as e:
        print(e)

    print(returned)
