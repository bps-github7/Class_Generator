#!/usr/bin/python3

'''Trying to figure out how to tell if no arg was passed
to trigger i mode, vs 1 arg for file input mode and > 1 for cmd line
should I design a better way to do this

TODO also start using git'''

from Misc_Functions import list_to_str
from Class_Dict import Class_Dict
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


#read arguments passed to the console.
args = parser.parse_args()

#global variable for all functions to access.
container = {}

def interactive_main():
    """What a user sees when they fire up the program in -i mode"""
    print("\nWelcome to class generator interactive mode!\n")
    help = "Default mode- Sequentially list your classes in the desired 'inline' format.\n\
example_class : attr1, attr2, attr3 : method1, method.\n\
Prompt Mode- Build your class or classes with the help of an interactive prompt.\n\
Note that you can leave any time by entering q, e, quit or exit.\n\
Type d for default mode or p for Prompt mode, h repeats these instructions."
    print(help)
    while (response := input()) and response not in ("quit","exit","e","q"):
        if response in ("h", "help"):
            print(help)
            continue
        elif response in ("d","default","default mode"):
            if answer := default_mode():
                container.update(answer)
        elif response in ("p","prompt","prompt mode"):
            if answer := prompt_mode():
                container.update(answer)
        #Fallthrough/ default- input provided was not an option. 
        else:
            print("Did not recoginize your input. Please try again.")
            continue

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
    while (response := input()) and response not in ("quit","exit","e","q"):
        lines.append(response)
        if response.lower() in ("c","d","continue","done"):
            #gonna have to botch the class_dict design AGAin
            inline = response.split(":")
            print(*inline)
            #cont.update(Class_Dict.to_dict(response))
        elif response.lower() in ("q","e","quit","exit"):
            sys.exit(1)


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
    while (cls := input()) not in ("q","e","quit","exit"):
        if cls in ("c","d","continue","done"):
            if get_confirmation(classes, member="class"):
                return classes
            continue
        elif cls in ("h","help"):
            print(help)
            continue
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
[h,help], exit prompt: [q,e,quit,exit]\n\n"
    print("list {} for class named {} : ".format(member, cls))
    while (response := input()) not in ("q","e","quit","exit"):
        #need to parse cls to check compliance with class naming rules/conventions.
        if response in ("c","d","continue","done"):
            if get_confirmation(container, member=member):
                return list_to_str(container)
            else:
                continue
        elif response in ("h","help"):
            print(help)
            continue
        #assuming user didnt enter a recognized keyword, appends the response to classes
        container.append(response)
    #kill the program if the loop was exited. user wants to quit.
    sys.exit(1)

def get_confirmation(items, member=None):
    """Asks user if they are satisfied with current list"""
    for elements in items:
        print(elements)
    print("satisfied with your current {} list?(y/n)".format(member))
    while True:
        ans = input()
        if ans in ("y","yes"):
            return items
        elif ans in ("n","no"):
            return False


#Dev notes: 3/29/2020 @ 5:24pm EST
# Made a huge update to this interactive prompt/
#it should work, baring some minor logic mistakes/
#definitely needs debugging and stylizing/ efficiency rewrites.

#after that, we'll need to finalize actual class generator functions, 
# make sure all the different UIs work and small details/ update README, git init


#test_file(args.file)

#test the first guy at least...
####expected one or more argument?
interactive_main()
