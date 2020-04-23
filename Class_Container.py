###Progammer: Ben Sehnert
###Date: 3/12/2020
###Program: Class_dict class
###Software: Python Class generator

"""
Module Level Docstring:

Module implementing functions for working with
a dictionary (global scope: class_container) containing class_dict objects as the entries

-from_file(f): argument f is a file in the local filesystem, accesible to the script.
    will read each line into a class_dict object, update class_container with the full file contents.
-inheriter(): parses each entry in class_container, handles inheritance by applying inheritance rules
    to the existing class_dicts.
-executor(): uses the class generator to produce the classes specified by existing entries in class_container


"""
import itertools
import datetime
import os

class_container = []

def from_file(f, results = []):
        """
    builds a container out of text file
    containing class dict specifications inline format.
        """
        #need to account for lack of .txt in POSIX systems
        with open("{}.txt".format(f), "r") as file:
            for lines in file:
                if not lines.count(":"):
                    NotImplemented
                    #then the user passed in only class names, or the format is wrong.
                elif lines.count(":") == 1:
                    NotImplemented
                    #methods were skipped (normal), or format is incorrect
                else:
                    #base/default case- for error reporting, but how do we know it's wrong?
                    NotImplemented
                results.append(lines.strip("\n"))
            return results

def inheritance(name, attr, methods, parent = object, new = {}):
    """
Does the same thing as the inherit function in misc_functions.py
    """
    family, family_attr, family_methods = name.split(">"),
    attr.split(">"), methods.split(">")
    if len(family) != len(family_attr):
        print("Did not provide sufficient data to\
            define both parent and child classes.")
        return 0
    parents, parent_attr, parent_methods = family[0].split(","),
    family_attr[0].split("/"), family_methods[0].split("/")
    for a, b, c in zip(parents, parent_attr, parent_methods):
        #this conditional ensures that classes who have parents
        #according to the hierachry arre defined as such
        if parent != object:
            new.update({a : (b,c, "parent = {}".format(parent))})
        else:
            new.update({a : (b,c)})
    #prep work for the next recursive call- 
    # define new arguments and delete irrelevant data
    parent = family[0]
    del family[0], family_attr[0], family_methods[0]
    name, attr, methods = ">".join(family), ">".join(family_attr),
    ">".join(family_methods)
    #recursive call and base case
    if len(family) > 0:
        return inheritance(name, attr, methods, parent = parent)
    else:
        return new

#this function call stack is a pain, looks ugly, doesnt do anything paticularly useful
#BUT it was needed to properly implement inheritance in this file, given scope and dictionary immutability
# keys cannot change while being looped over, so we needed two seperate dictionaries in different scope>>> bad design...
def controller():
    """"""
    for entries in class_container:
        if entries.count(">") > 0:
            new = inheritance(entries, class_container[entries][0], class_container[entries][1])
            old = entries
            break
        else:
            return 0
    del class_container[entries]
    class_container.update(new)
    return True

def top():
    loop = True
    while loop:
        loop = controller()


# del class_container[edited[0]]
# class_container.update

#parse()
#edit()
class_container = from_file("classes")
print(class_container)