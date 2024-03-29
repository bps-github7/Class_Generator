"""Dedicated to path related functions. If all tests are passed,
main fn will create a directory with project name, in location pointed to by user's path.
"""
import os
import errno
import tempfile
# from interactive import confirm_prompt

class NoPathError(Exception):
    def __init__(self, message):
        self.message = message

class NoFileNameError(Exception):
    '''
exception for cases where user is trying
to generate a file but
1) did not provide file name
2) did not provide a valid file name (invalid idenfier)
    '''
    def __init__(self, error, value):
        self.error = error
        self.value = value

def validate_path(path = "root"):
    """The path tells the program where to generate the files, and when a path
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
        if is_valid_path(os.getcwd()):
            return os.getcwd()
        raise OSError("there is a problem with the path you provided")
    while True:
        if is_valid_path(path):
            return is_valid_path(path)
        else:
            while True:
                print("provide a new, valid path to proceed with generation, or type q to quit:")
                path = input()
                if os.path.exists(path):
                    break
                elif path == "q":
                    raise NoPathError("user chose to not validate a path")
                else:
                    print("Try again: your input is not a valid path. you can enter absolute or relative path.")


def is_valid_path(path):
    """Ensures the path a user provided is valid.

    Args:
        path (str): path to validate

    Returns:
        validated_path (str | 0): returns path if tests pass, else failure signal.
    """
    if os.path.exists(path) and os.path.isdir(path):
        if is_writable(path):
            return 1
        else:
            msg = "We do not have sufficient privalleges to generate files here."
    else:
        msg = f"path- {path} does not exist or does not point to a directory."
    raise NoPathError(msg)

def is_writable(path):
    """Checks if we can write to the folder pointed to by users path

    Args:
        path (str): the path to check
    Returns:
        boolean: true if we can write a file, false otherwise
    """
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
    """using project name and path, change path
    to project home. path/directory if it exists
    else first create folder then change to it.

    Args:
        path ([type]): [description]
        project_name ([type]): [description]

    Returns:
        [type]: [description]
    """
    os.chdir(path)
    new = os.path.join(path, project_name)
    if not os.path.exists(new):
        os.mkdir(new)
        os.chdir(new)
        return 1
    else:
        os.chdir(new)
        return 1


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
    print(fix_relative_path("./something"))
