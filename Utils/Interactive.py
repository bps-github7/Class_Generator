#!/usr/bin/python3

'''Trying to figure out how to tell if no arg was passed
to trigger i mode, vs 1 arg for file input mode and > 1 for cmd line
should I design a better way to do this

'''

import argparse
import sys
import os


def confirm_prompt(prompt : str):
    """A helper method with interactive flavor,
    it simply asks user for a yes no response, where they have
    option to quit as well

    Returns:
        1 - confirm
        0 - reject
        { err : false } - user wants to quit
        { err : true, response = "..."}
    """
    print(prompt)
    print("choose one of the following:")
    print("c - to confirm")
    print("r - to reject")
    print("q - to exit this prompt")
    response = input().lower()
    if response in ("c","confirm", "continue"):
        return 1
    elif response in ("r", "reject", "no"):
        return 0
    elif response in ("q", "quit"):
        return { "error" : False }
    else:
        return { "error" : True, "response" : response }



#Global that holds all classes parsed via application use.
container = {}

def interactive_mode():
    """What a user sees when they fire up the program in -i mode
    
    returns a validated list of classdicts parsed from the
    user input attained during interactive session.
    """
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
        # if validate_inline(response):
        #     lines.append(response)
        #     continue

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
        # elif cls in ("h","help"):
            # print(help)
            # classes = input()
        #assuming user didnt enter a recognized keyword, appends the response to classes
        #need to parse cls to check compliance with class naming rules/conventions.
        # classes.append(cls)
    
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


def get_attributes(cls):
    """A very slimmed versiion of the above get_members."""
    # should we validate? check if commas delimit it?
    return input("enter new attributes, seperated by commas,\n\
(type 'enter' when done)\n")


def get_methods(cls):
    # should we validate? check if commas delimit it?
    return input("enter new methods, seperated by commas,\n\
(type 'enter' when done)\n")


def get_options(cls):
    # should we validate? check if commas delimit it?
    return input("enter new options, seperated by whitespace if needed,\n\
(type 'enter' when done)\n")

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
# interactive_mode()