# Programmer: Ben Sehnert
# Program: Misc_Functions Module
# Software: Python class Generator
# Date: 1/21/2020

import sys
import os
import errno
import tempfile

sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")


def path_main(path = "root"):
    """Main function for validation of path user provided for a session.
    The path tells the program where to generate the files, and when a path
    isn't provided during a session, the program will default on either a custom
    configuration provided in .rc file, else the CWD. in either case, we need
    to ensure that this path exists on the system and is writable to the current user.

    Args:
        path (str, optional): a relative or absolute path to validate. Defaults to "root" (CWD).

    Raises:
        OSError: in the case we can't use the path user provided, 

    Returns:
        validated_path [str]: in the case validation tests passed, a usable path for generation. 
    """
    if path == "root":
        if validate_path(os.getcwd()):
            return os.getcwd()
        raise OSError("there is a problem with the path you provided")
    elif path != os.getcwd():

        if not os.path.isabs('.'):
            path = fix_relative_path(path)

        
        while not validate_path(path):

            if os.path.exists(path):
                path = input("provide a new, valid path to proceed with generation, or type q to quit:\n")
                if path.lower() == "q":
                    return 0
            else:
                break
        return path
        
def validate_path(path):
    """Ensures the path a user provided is valid.

    Args:
        path (str): path to validate

    Returns:
        validated_path (str | 0): returns path if tests pass, else failure signal.
    """
    try:
        os.path.exists(path)
        os.path.isdir(path)
        isWritable(path)
        return path
    except (OSError, NotADirectoryError):
        print("the path you provided is not valid")
        return 0


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

def fix_relative_path(path) :
    """Automatically cleans and concatenates relative paths 
    so it refers to absolute location in system instead.
    meant to robustly handle nuances of unix vs windows paths.

    Args:
        path ([type]): a relative path, starting with any of the following syntax
        - 'some/path'
        - '/some/path'
        - './some/path'
        - '../some/path'
        - or windows alternative of each: 'some\path', '\some\path', etc...

    Returns:
        abs_path : the correct absolute path pointed to by the relative path passed in
    """
    # first things first, set delimiter since this varies between NT and POSIX
    delimiter = "//"
    if os.name == "nt":
        delimiter = "\\"

    base = os.getcwd()
    base_tolkens = base.split(delimiter)

    # if user provides rel path with ./ infront, clean that up.
    if path.startswith("./"):
        path = path[2:]

    # if user wanted to go up file sys tree, truncate abs path to match.
    elif path.startswith("../"):
        base = delimiter.join(base_tolkens[:len(base_tolkens) - path.count("../")])
        path = path[(path.count("../")*3):]
           
    # a final alternative is '/some/path', clean that up as well
    elif path.startswith(delimiter):
        path = path[1:]

    # finally, if windows is OS, and user used unix style path delimiter, swap these out.
    if os.name == "nt" and (path.count("/")):
        path = path.replace("/","\\")
    elif os.name == "nt" and path.count("//"):
        path = path.replace("//","\\")

    # ensure that the relative addition to the base is in format "something/something"
    # to avoid duplicate delimiter in the return value.
    if path.startswith("//") or path.startswith("\\"):
        path = path[1:]

    return base + delimiter + path


if __name__ == "__main__":

    print(fix_relative_path("../../something"))
    print(fix_relative_path("something"))
    print(fix_relative_path("./something"))

    # handles both of these happily
    print(fix_relative_path("\\taco\\burrito"))
    print(fix_relative_path("taco\\burrito"))


    # except compatability testing with unix (ie does this function work the same with / facing slashes)
    # this is the only use case that fix_relative_path isnt working with
    print(fix_relative_path("/taco"))



    # try:
    #     returned = path_main("C:\caluga")
    # except OSError as e:
    #     print(e)

    # print(returned)
