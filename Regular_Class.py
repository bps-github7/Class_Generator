###Programmer: Ben Sehnert
###Program: Regular_class module
###Software: Python Class Generator

"""Defines the functions used for writing regular class files."""

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
    #if protected is true, name mangle all attributes
    #sort of a bandaid solution- should be able to make individual attributes private...
    if protected:
        for i in attributes:
            file.write("\t\tself.__{} = {}\n".format(i,i))
        file.write("\n")
    else:
        for i in attributes:
            file.write("\t\tself.{} = {}\n".format(i,i))
        file.write("\n")
    
def make_repr(file, attributes):
    '''
writes class repr method to a file,
given the file object and attribute list
    '''
    file.write("\tdef __repr__(self):\n\t\treturn {")
    for i in attributes:
        if i == attributes[len(attributes)-1]:
            file.write("\"{}\" : self.{}".format(i,i))
        else:
            file.write("\"{}\" : self.{}, ".format(i,i))
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
    
#implmenent descriptor protocols
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
    #name mangling attr setter according to descriptor protocol
    if a.startswith("__"):
        file.write("\t@{}.setter\n\tdef {}(self, {}):\n\
        \tself._{} = {}\n\n".format(a, a, a, a, a))
        return
    file.write("\t@{}.setter\n\tdef {}(self, {}):\n\
    \tself._{} = {}\n\n".format(a, a, a, a, a))


def make_methods(file, methods):
    """
parses the methods to determine
which type of method to create.
Returns None. methods should be
a comma delimited string.
"""
    for m in methods.split(","):
        if m.startswith("SM"):
            file.write("\t@staticmethod\n\tdef {}():\
                \n\t\t\"\"\"\n\tmethod docstring:\n\
    \t\"\"\"\n\t\treturn NotImplemented\
                \n\n".format(m[2:]))
        elif m.startswith("CM"):
            file.write("\t@classmethod\n\tdef {}(cls):\
                \n\t\t\"\"\"\n\tmethod docstring:\n\t\
    \"\"\"\n\t\treturn NotImplemented\
                \n\n".format(m[2:]))
        else:
            #default case makes instance method
            file.write("\tdef {}(self):\
                \n\t\t\"\"\"\n\tmethod docstring:\
            \n\t\t\"\"\"\n\t\treturn NotImplemented\
                \n\n".format(m[2:]))

def make_class(name, attributes, methods, parent=object, protected=False):
    """
main subroutine for class generator
creates a file with the provided class name
outputs the appropriate class syntax for what is specified.
    """
    with open("{}.py".format(name), "a+") as file:
        file.write("class {}({}):\n".format(name, parent))
        make_init(file, name, attributes, protected=protected)
        make_repr(file, attributes)
        make_str(file, name, attributes)
        if protected:
            #use descriptor protocol- implement __get__(), __set__(), __delete__
            for attribute in attributes:
                make_getter(file, attribute)
            for attribute in attributes:
                make_setter(file, attribute)
        if len(methods) > 0:
            make_methods(file, methods)
        file.write("if __name__ == '__main__':\
        \n\tprint('Running class file. Nothing to do here')")

make_class("employer", ["employeeID","name","salary"], "SMmethod1,SMmethod2,CMmethod1,CMmethod2,normalmethod1", parent="Person")  
#make_regularclass("Testing", ["skone","bisk","chalp"])