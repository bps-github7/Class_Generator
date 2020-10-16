#!/usr/bin/python3

'''Trying to figure out how to tell if no arg was passed
to trigger i mode, vs 1 arg for file input mode and > 1 for cmd line
should I design a better way to do this

TODO also start using git'''

import re
from Misc_Functions import list_to_str
import argparse
import sys
import os

parser = argparse.ArgumentParser(description="Generate classes automatically using command line options or interactive prompt")

#file mode- the star of the show here
parser.add_argument("--file", type = str, nargs="?", required=False)
##note that -- makes an argument non positional- this way it can be non-required.


#what are alternative constructors and should they be included in this tool?
#parser.add_argument("-A", "--Alternative Constructor", help="")

#testing
parser.add_argument("-t", "--testing", type=str, metavar='', help="Automatically generate unittests, static analysis, code coverage, additional documentation?", required=False)

#exportng
parser.add_argument("-e", "--exporting", type=str, metavar='', choices=['tgz', 'zip', 'tgz and email', 'tgz and zip', 'tgz and SSH', 'zip and SSH'], help="What should be done with the generated project {tgz, zip, tgz & email req arg: 'name@mail.com', zip and email, tgz and ssh, zip and ssh }", required=False)


#interactive mode
parser.add_argument("-i", "--interactive", help="Run the program in interactive mode!", action= "store_true" , required = False)


args = parser.parse_args()

#Global that holds all classes parsed via application use.
container = {}

def interactive_main():
    """What a user sees when they fire up the program in -i mode"""
    print("\nWelcome to Class Generator interactive mode!\n")
    help = "Default mode- Sequentially list your classes in the desired 'inline' format.\n\
example_class : attr1, attr2, attr3 : method1, method.\n\
Prompt Mode- Build your class or classes with the help of an interactive prompt.\n\
Note that you can leave any time by entering q, e, quit or exit.\n\
Type d for default mode or p for Prompt mode, h repeats these instructions."
    print(help)
    response = input()
    while (response not in ("quit","exit","e","q")):
        if response in ("h", "help"):
            print(help)
            response = input()
        elif response in ("d","default","default mode"):
            default_mode()
            # if default_mode():
            #     print("You picked in ")            
                #answer = default_mode()?

                # container.update(answer)
        elif response in ("p","prompt","prompt mode"):
            prompt_mode()
            # if answer := prompt_mode():
            #     container.update(answer)
        else:
            response = input("Did not recoginize your input. Please try again: ")

def default_mode():
    """
collects class specs from user
by reading them in the inline format
    """
    cont = {}
    lines = []
    help = "Default mode- enter class specifications in 'inline' format\n\
class_name : attr1, attr2, attr3 : method1, method2, SMmethod1, CMmethod1\n\
Note that you can denote inheritance relationships (see README for howto)\n\
methods types with a prepended SM/CM for static or class methods\n\
leaving attributes or methods sections will result in classes without respective attributes or method\n\
type c, d, continue or done to exit this mode\n"
    print(help)
    response = input()
    while response not in ("quit","exit","e","q"):
        if response.lower() in ("c","d","continue","done"):
            print("Were done parsing inline class dicts")
            print(lines)
            #gonna have to botch the class_dict design AGAin
            # inline = response.split(":")
            # print(*inline)
            #cont.update(Class_Dict.to_dict(response))
        elif response.lower() in ("q","e","quit","exit"):
            sys.exit(1)
        response = input()
        if validate_inline(response):
            lines.append(response)
            continue


def validate_classes(classes):
    for item in classes:
        if item[0] == '0':
            print("first character of identifier cannot be 0")
        for i in item:
            if i not in re.match('[a-zA-Z_][a-zA-Z0-9_]*'):
                return "a class provided contained an illegal character."



def validate_inline(inline):
    classes = inline.split(":")[0]
    if len(classes):
        validate_classes(classes)
    else:
        print("cannot define a class with no name. ")

def prompt_mode():
    """
Main subroutine for interactive mode.
takes no arguments, returns None.
autonomously generates classes when user correctly follows prompt.
    """
    cls = get_classes()
    for item in cls:
        #would like to have used Class Dict, but it not iterable- how to fix
        container.update({item : build_class_specs(item)})
    print(container)

    
def get_classes(classes = []):
    """get classes from user"""
    help = "enter a name of a class. Keep on entering until\n\
you have enumerated all class names in your project\n\
Key- move forward : [c,d,continue,done], help : [h,help], leave prompt : [q,e,quit,exit]"
    print("List the names of classes to be generated. When done enter 'continue','done','c','q'")
    classes = input()
    while classes not in ("q","e","quit","exit"):
        if classes in ("c","d","continue","done"):
            if get_confirmation(classes, member="class"):
                return classes
            classes = input()
        elif cls in ("h","help"):
            print(help)
            classes = input()
        #assuming user didnt enter a recognized keyword, appends the response to classes
        #need to parse cls to check compliance with class naming rules/conventions.
        classes.append(cls)
    
def build_class_specs(cls):
    """
builds a class specification [attributes, methods, parent = ?]
for a single class, cls, returns a Class_Dict dictionary element.
    """
    parent=input("list parents of the class {}, \
delimit multiple parents with comma, \
or leave blank to inherit from object: ".format(cls))
    return [get_data(cls), get_data(cls,member="method"), "parent={}".format(parent)]     

def get_data(cls, member="attribute"):
    """
get attributes/methods for a given class, cls
returns a list of attributes
    """
    container = []
    help = "key- next step : [c,d,continue,done], help :\
[h,help], exit prompt: [q,e,quit,exit]\n\n\
Otherwise, type names for your attribute, one per line, and type <enter> to move to next line/ attribute"
    print("list {} for class named {} : ".format(member, cls))
    response = input()
    while response not in ("q","e","quit","exit"):
        #this i suspect will be a problem area...
        if response in ("c","d","continue","done"):
            if get_confirmation(container, member=member):
                return container
            else:
                continue
        elif response in ("h","help"):
            print(help)
            response = input()
            continue
        #assuming user didnt enter a recognized keyword, appends the response to classes
        container.append(response)
        response = input()
    #kill the program if the loop was exited. user wants to quit.
    sys.exit(1)

def get_confirmation(items, member=None):
    """Asks user if they are satisfied with current list"""
    print("\n")
    for elements in items:
        print(elements)
    print("satisfied with your current {} list?(y/n)".format(member))
    while True:
        ans = input()
        if ans in ("y","yes"):
            return True
        elif ans in ("n","no"):
            if abort_state():
                if get_confirmation(items, member):
                    return True


def abort_state():
    print("What would you like to do ? >>> 1) complete this entry 2) abort this generation/ close the application")
    response = input()
    if response == "1":
        return True
    elif response == "2":
        print("Careful: proceed with caution!")
        print("Executing this command will result in erasure of classes specified in this session.")
        choice = input("and no classes will be generated! are you sure you want to do this? (y/n)")
        if choice.lower() in ("y","yes","yeah","yea","ya"):
            sys.exit(1)
        else:
            return True
    




#Dev notes: 3/29/2020 @ 5:24pm EST
# Made a huge update to this interactive prompt/
#it should work, baring some minor logic mistakes/
#definitely needs debugging and stylizing/ efficiency rewrites.

#after that, we'll need to finalize actual class generator functions, 
# make sure all the different UIs work and small details/ update README, git init


#test_file(args.file)

#test the first guy at least...
####expected one or more argument?
# interactive_main()
# print(get_confirmation(["bisk","chalp","skone","POADES"]))
# print(get_data("Shaat"))
interactive_main()