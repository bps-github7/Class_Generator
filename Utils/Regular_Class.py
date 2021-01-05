# Programmer: Ben Sehnert
# Program: Regular_class module
# Software: Python Class Generator

"""Defines the functions used for writing regular class files."""


def make_imports(file, parents, path_to_parents="./"):
    '''
Writes the import statements so that a child class
can properly inherit from its parents
    '''
    for items in parents:
        # any considerations here for system path? do we need to append
        # to it to import from parent dir? not normally i presume
        file.write("from {} import {}\n".format(items, items))
    file.write("\n")


def make_init(file, name, attributes, protected=False):
    """
Completes the init statement by writing attributes to the file
    """
    file.write("\tdef __init__(self, ")
    for i in attributes:
        if i == attributes[len(attributes)-1]:
            file.write("{}".format(i))
        else:
            file.write("{}, ".format(i))
    file.write("):\n")
    # if protected is true, name mangle all attributes
    # sort of a bandaid solution- should be able to make individual attributes private...
    if protected:
        for i in attributes:
            file.write("\t\tself.__{} = {}\n".format(i, i))
        file.write("\n")
    else:
        for i in attributes:
            file.write("\t\tself.{} = {}\n".format(i, i))
        file.write("\n")


def make_repr(file, attributes):
    '''
writes class repr method to a file,
given the file object and attribute list
    '''
    file.write("\tdef __repr__(self):\n\t\treturn {")
    for i in attributes:
        if i == attributes[len(attributes)-1]:
            file.write("\"{}\" : self.{}".format(i, i))
        else:
            file.write("\"{}\" : self.{}, ".format(i, i))
    file.write("}\n\n")


def make_str(file, name, attributes):
    '''
Writes class __str__ method to a file,
given the file object and attribute list
    '''
    file.write("\tdef __str__(self):\n\t\treturn \"{}(".format(name))
    for i in attributes:
        if i == attributes[len(attributes)-1]:
            file.write("{} = ".format(i))
            file.write("{}")
        else:
            file.write("{} = ".format(i))
            file.write("{}, ")
    file.write(")\".format(")
    for i in attributes:
        if i == attributes[len(attributes)-1]:
            file.write("self._{})\n\n".format(i))
        else:
            file.write("self._{}, ".format(i))

# implmenent descriptor protocols


def make_getter(file, a):
    '''
Writes the getter for one attribute in pip 3.8 syntax,
given the file object and attribute a.
    '''
    file.write("\t@property\n\tdef {}(self):\n\
    \treturn self._{}\n\n".format(a, a))


def make_setter(file, a):
    '''
Writes the setter for one attribute in the new syntax,
given the file object and attribute a
    '''
    # name mangling attr setter according to descriptor protocol
    if a.startswith("__"):
        file.write("\t@{}.setter\n\tdef {}(self, {}):\n\
        \tself._{} = {}\n\n".format(a, a, a, a, a))
        return
    file.write("\t@{}.setter\n\tdef {}(self, {}):\n\
    \tself._{} = {}\n\n".format(a, a, a, a, a))


def duplicate_check(provided):
    seen = set()
    for x in provided:
        if x in seen:
            return True
        seen.add(x)
    return False


def make_methods(file, methods):
    """
parses the methods to determine
which type of method to create.
Returns None. methods should be
a comma delimited string.
    """
    NM, CM, SM = [], [], []
    for m in methods:
        if m.startswith("SM"):
            SM += [m[2:]]
        elif m.startswith("CM"):
            CM += [m[2:]]
        else:
            NM += [m]
    possible_duplicates = NM + CM + SM
    if duplicate_check(possible_duplicates):
        print("Error while writing methods- method names cannot be duplicates (after stripping SM, CM)\n\
Please revise your class definition so that there are no duplicates in method names")
        # you should catch an exception here rather than passing value up the call stack.
        return 0
    # assumed at this point that method names are non-duplicates
    # write the specific method
    for items in NM:
        # default case makes instance method
        file.write("\tdef {}(self):\
            \n\t\t\"\"\"\n\tmethod docstring:\
        \n\t\t\"\"\"\n\t\treturn NotImplemented\
            \n\n".format(items))
    for items in SM:
        file.write("\t@staticmethod\n\tdef {}():\
            \n\t\t\"\"\"\n\tmethod docstring:\n\
\t\"\"\"\n\t\treturn NotImplemented\
            \n\n".format(items))
    for items in CM:
        file.write("\t@classmethod\n\tdef {}(cls):\
            \n\t\t\"\"\"\n\tmethod docstring:\n\t\
    \"\"\"\n\t\treturn NotImplemented\
            \n\n".format(items))
    return None


# why is attributes passed in as a list but methods a string?
def make_class(name, attributes, methods, parent=object, package='root', protected=False):
    """
main subroutine for class generator
creates a file with the provided class name
outputs the appropriate class syntax for what is specified.
    """
    # coerce adherence to PEP8 by making class identifier titlecase
    name = name.title()
    if package not in ('root', None):
        full_name = f"{package}/{name}.py"
    else:
        full_name = f"{name}.py"    
    with open(full_name, "a+") as file:
        if parent != object:
            make_imports(file, [parent])
        else:
            # prevent writing object as internal type representation.
            parent = "object"
        file.write("class {}({}):\n".format(name, parent))
        make_init(file, name, attributes, protected=protected)
        make_repr(file, attributes)
        make_str(file, name, attributes)
        if protected:
            # use descriptor protocol- implement __get__(), __set__(), __delete__
            for attribute in attributes:
                make_getter(file, attribute)
            for attribute in attributes:
                make_setter(file, attribute)
        if len(methods) > 0:
            # what to do if value is passed up here? suppose its sufficient to assume user will use command successful second time round.
            make_methods(file, methods)
        file.write("if __name__ == '__main__':\
        \n\tprint('Running class file. Nothing to do here')")


# # these should be able to take class_dict as an argument!
# make_class("employer", ["employeeID", "name", "salary"],
#            ["SMstaticmethod1","SMstaticmethod2","CMclassmethod1","CMclassmethod2","normalmethod1"], parent="Person")
# make_class("person", ["name", "age", "weight",
#                       "height"], ["mystical_beansprout"])
