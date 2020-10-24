###Programmer: Ben Sehnert
###Program: Options module
###Software: Python class generator

import os
import sys
import errno
import tempfile
import argparse

"""Defining various methods that facilitate cmd line execution of class generator"""

def isWritable(path):
    try:
        testfile = tempfile.TemporaryFile(dir = path)
        testfile.close()
    except OSError as e:
        if e.errno == errno.EACCES:  # 13
            return False
        e.filename = path
        raise
    return True

def make_new_folder(path):
    os.chdir(path)
    new = os.path.join(path, args.name)
    if not os.path.exists(new):
        os.mkdir(new)
        os.chdir(new)
        return 1
    else:
        print("Error: a folder already exists with this name.")
        return 0

#Seems like there is a  logic/ exception error somewhere- keep getting this error message in cmdline mode
def test_path(path):
    if os.path.exists(path) and os.path.isdir(path) and isWritable(path):
        if make_new_folder(path):
            return 1
    else:
        print("Error: there is an issue with the default path provided")
        print("Please check the following:")
        issues = ["1. Is the default path: {} a valid, fully qualified path?".format(path),\
                  "2. Does the default path lead to a valid directory in the file system? (ie. not a file, filesystem, shortcut. etc...)",\
                  "3. Is the default path provided a writable directory? (ie. does the current user have the nescesary privalleges to write in this directory?)"]
        for issue in issues:
            print(issue)
