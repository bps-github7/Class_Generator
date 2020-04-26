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
"""
import itertools
import datetime
import os

def get_confirmation(opt_code, line):
    """Asks user if they are satisfied with their choice"""
    opts = {1: "line no.{} has no colons- meaning your class has no attributes or methods,\
        \n or this line was incorrectly defined".format(line),
    2: "No attributes provided for specs on line no. {}".format(line), 
    3: "No methods provided for specs on line no. {}".format(line)}
    print(opts[opt_code])
    while True:
        ans = input("Do you wish to proceed with generating this line? (y/n)")
        if ans in ("y","yes"):
            return True
        elif ans in ("n","no"):
            return False

def from_file(f, results = []):
        """
    builds a container out of text file
    containing class dict specifications inline format.
        """
        #need to account for lack of .txt in POSIX systems
        with open("{}.txt".format(f), "r") as file:
            for num, line in enumerate(file):
                copy = line.strip("\n")
                line = line.split(":")
                if line[0] in (""," ","\t","\t\t",None):
                    print("Cannot produce a class/classes without name(s).\n\
Please review/revise the following class specification:\n {}on line no.{}\n".format(copy, num))
                elif line[1] in (""," ","\t","\t\t",None):
                    if get_confirmation(2, num):
                        results.append(copy)
                elif line[2] in (""," ","\t","\t\t"," \n"," \t\n","\t\t\n" "\n",None):
                    if get_confirmation(3, num):
                        results.append(copy)
                else:
                    results.append(copy)
            return results

def inheritance(line, parent = object, new = {}):
    """
Does the same thing as the inherit function in misc_functions.py
    """
    #would be nice to have the conditional tuple unpacking here.
    # TODO: can we define something like that? (not sure how to define new language syntax)
    line = line.split(":")
    family, family_attr, family_methods = line[0].split(">"), line[1].split(">"), line[2].split(">")
    if len(family) != len(family_attr):
        print("Did not provide sufficient data to\
            define both parent and child classes.")
        return 0
    parents, parent_attr, parent_methods = family[0].split(","), family_attr[0].split("/"), family_methods[0].split("/")
    for a, b, c in zip(parents, parent_attr, parent_methods):
        #this conditional ensures that classes who have parents
        #according to the hierachry arre defined as such
        if parent != object:
            new.update({a : (b,c, "parent = {}".format(parent))})
        else:
            new.update({a : (b,c)})
    #prep work for the next recursive call- 
    # define new arguments and delete irrelevant data

    #family[0] is a list 
    parent = family[0]
    del family[0], family_attr[0], family_methods[0]
    name, attr, methods = ">".join(family), ">".join(family_attr), ">".join(family_methods)
    #recursive call and base case
    if len(family) > 0:
        return inheritance(name, attr, methods, parent = parent)
    else:
        return new

    
def only_name_inheritance(line, parent = object, new = {}):
    """Custom inheritance engine for only when name is provided in inline"""
    if line.count(":") == 1:
        #allot of ambiguity to work around here...
        # need to strip whitespace out of second item first.
        pass
    elif line.count(":") == 2:
        pass

def no_attribute_inheritance(line, parent = object, new = {}):
    """Custom inheritance engine for attributeless class specs"""
    NotImplemented

def no_method_inheritance(line, parent = object, new = {}):
    """Custom inheritance engine for methodless class specs"""

def inheriter(line):
    """
top level function for error handling with inheritance

so that it wont freak out if it gets undefined attr, method,
if name is undefined then return False- that shouldnt happen @ this point
    """
    copy = line
    line = line.split(":")
    if not copy.count(":"):
        NotImplemented
        # only_name_inheritance()
    elif line[1] in (""," ","  ","   ","\t","\t\t"," \n"," \t\n","\t\t\n" "\n",None):
        NotImplemented
        # no_attribute_inheritance()
    elif line[2] in (""," ","  ","   ","\t","\t\t"," \n"," \t\n","\t\t\n" "\n",None):
        NotImplemented
        # no_method_inheritance()
    #ideal case- fully specified inline spec
    else:
        inheritance(copy)


#<input: file, cmdline argument or user input> ---<list: each element is an inline format spec> -> -> <inheritance()> -> 
#<one inline format spec == 1 to many specs in dictionary> -> <each line gets updated() to main dict containing all classes 2b generated>

def controller():
    """
Does the overhead work for inheritance.
Turns inline format strings into class specification dict.
creates specific class hierarchies if inline specs call for this. 
    """
    for items in inline:
        if items.split(":")[0].count(">"):
            class_dict.update(inheritance(items))
        else:
            items = items.split(":")
            if len(items) == 1:
                class_dict.update({items : ("parent = {}".format("Object"))})
            elif len(items) == 2:
                #how can we assure that items[1] is attributes, not methods?
                class_dict.update({items[0] : (items[1],"parent = {}".format("Object"))})
            else:
                class_dict.update({items[0] : (items[1], items[2], "parent = {}".format("Object"))})




class_dict = {}
inline = from_file("classes")
# controller()
# print(class_dict)
