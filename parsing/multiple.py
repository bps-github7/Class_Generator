"""
Programmer: Ben Sehnert
Program: multiple module
Software: python file Generator
date: 1/28/2021

About: Houses all validation, parsing and general utilities
pertinent to multiple inlines, that is, inlines which contain 
specs for building more than onr inline.


??? this whole module ???
just do this recursively classes.split('/') for each create a file to be generated.
"""
import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")

from parsing.inline import Inline


def test():
    """[summary]
    """
    print(validate_multiple("classA / ClassB / ClassC / classD /\
     ClassE / ClassF: attr1, attr2 / attr3, attr4"))

def validate_multiple(inline: str):
    """
    """
    ### these are very rudiementary tests/ NOTE: needs to ne tested
    inline = inline.split(":")
    classes, attributes = inline[0], inline[1]
    if classes.count("/") > attributes.count("/"):
        response = input("Note: your multi-inline is missing an attribute\
        family. Fix this (y/n)?")
        if response in ("n", "no"):
            slashes_needed = classes.count("/") - attributes.count("/")
            inline[1] = inline[1] + ("/" * slashes_needed)
            # At the end, we need to join all the inline fields together with colon.
        elif response in ("y", "yes"):
            # print("sweaty fox")
            starting, needed = classes.count("/"), classes.count("/") - attributes.count("/")
            classes = inline[0].split("/")
            print(starting, needed)
            for i in range(needed, starting):
                # print(i)
                print(classes[i])

                # inline[1] += interactive_mode.get_attributes(attributes[i]) + "/"
        print(inline)

    # if classes.count("/") < attributes.count("/"):


        
#     if classes.count("/") < methods.count("/"):
#         print("Error: too many methods.\n\
# make sure the number of '/' in classes is equal to num of '/' in methods.")
#         return 0
#     if classes.count("/") > methods.count("/"):
#         print("Error: not enough methods.\n\
# make sure the number of '/' in classes is equal to num of '/' in methods.")
#         return 0
#     if classes.count("/") < options.count("/"):
#         print("Too many options.\n\
# make sure the number of '/' in classes is equal to num of '/' in options.")
#         return 0
    ### What else could go wrong with multiple class inline spec?
    # return 1


def four_piece_multiple(inline : list):
    """[summary]

    Args:
        inline (list): [description]

    Returns:
        [type]: [description]
    """
    specs = []
    for i, value in enumerate(inline):
        inline[i] = value.split("/")
    for cls,attr,method,option in zip(inline[0], inline[1], inline[2], inline[3]):
        ### stuff needs to be validated before this point
        specs.append(Inline("{}:{}:{}:{}".format(cls,attr,method,option)))
    return specs



def three_piece_multiple(inline : list):
    """[summary]

    Args:
        inline (list): [description]

    Returns:
        [type]: [description]
    """
    specs = []
    for i, value in enumerate(inline):
        inline[i] = value.split("/")
    for cls,attr,method in zip(inline[0], inline[1], inline[2]):
        specs.append(Inline("{}:{}:{}".format(cls,attr,method)))
    return specs

# what about missing attributes

# what about missing methods

# what about missing options



def two_piece_multiple(inline : list):
    """[summary]

    Args:
        inline (list): [description]

    Returns:
        [type]: [description]
    """
    specs = []
    for i, value in enumerate(inline):
        inline[i] = value.split("/")
    for cls,attr in zip(inline[0], inline[1]):
        specs.append(Inline("{}:{}".format(cls,attr)))
    return specs

# what about missing attr and methods

# what about missing attr and opt

def one_piece_multiple(inline : list):
    """[summary]

    Args:
        inline (list): [description]

    Returns:
        [type]: [description]
    """
    specs = []
    inline = inline.split("/")
    for items in inline:
        specs.append(Inline(items))
    return specs

def main(inline : str):
    """Takes a string containing a multi file inline.
    turns it into an array of inlines 
    by following the mini language syntax rules.

    Args:
        inline (str): A multi family inline containing string.
    """
    inline = inline.split(":")
    if len(inline) == 4:
        return four_piece_multiple(inline)
    elif len(inline) == 3:
        return three_piece_multiple(inline)
    elif len(inline) == 2:
        return two_piece_multiple(inline)
    elif len(inline) == 1:
        return one_piece_multiple(inline)
    else:
        print("Cannot parse this thing. sorry.")
        return 0

if __name__ == '__main__':
    test()
    print(main("classA / ClassB / ClassC : attr1, attr2 / attr3, attr4 /: method1 / method2 /: -t / -m/"))