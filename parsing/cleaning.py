"""
Programmer: Ben Sehnert
Program: Cleanings module
Date: 2/6/2021
Software: Python class generator

About: This module implements functions pertaining to cleaning of inline members.
meaning, it takes the users input and coerces / constrains it into a format that
the parser is capable of understanding.
"""


import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")


def cleanse(items: any):
    """format multiple properties, ie:
    ' somethingA, somethingB, somethingC  '
    by strip and lowercase of each elements.
    side-effect: coerces ',' delimited string to formatted list.
    WARNING: properties in camelCase will lose inherent readability.
    items (str | list) : a set of properties to be cleansed.
    """
    if isinstance(items, list):
        return list(map(
            lambda item: item.strip().lower(), items))
    return list(map(
        lambda item: item.strip().lower(), items.split(",")))

def cleanse_methods(methods,cleansed):
    """[summary]

    Args:
        items (str): comma delimited string listing the methods in a class.
    """
    if methods.count(","):
        new_method = methods.split(",")[0]
        remaining = ",".join(methods.split(",")[1:])
        if new_method.count("("):
            components = new_method.split("(")
            new_method = { 'name' :components[0], 'args'  : components[1].strip(")")}        
        cleansed += new_method
        cleanse_methods(remaining, cleansed)
    return cleansed

### TODO: think we can nix these when finished above method.
def cleanse_regular_methods(items):
    """[summary]

    Args:
        items ([type]): [description]
    """
    regular = []
    # why is this test needed for regular methods ? (would make an invalid identifier)
    if items.count(")"):
        for item in items.split(")"):
            if item.count("("):
                regular.append((item.split("(")[0]).split(",")[:-1])
        for x,y in enumerate(regular):
            # wut is this? what does it do?
            if len(y):
                if y[0] == '':
                    del y[0]
            else:
                # remove empty lists
                del regular[x]
        regular = [item for item in regular if item != ['']] 
        regular = regular[0]
        return list(map(lambda x: x.strip().lower(), regular))
    else:
        return cleanse(items)


def cleanse_with_signitures(items):
    """Modified version of cleanse that deals
    with the fact that method signitures have ','
    when there are multiple parameters

    Args:
        items ([type]): [description]
    """
    sigs, signitures = [],[]
    items = items.split(")")
    for item in items:
        if item.count("("):
            params = item[item.find("("):]
            name = (item.split("(")[0]).split(",")[-1]
            sigs.append(f"{name}{params})")

    for sig in sigs:
        name = sig.split("(")[0]
        rest = (sig.split("(")[1]).split(")")[0]
        signitures.append(f"{name.lower().strip()}({rest})")
    return signitures

print(cleanse_methods("bisk, froggo(tomato, hat, gun), iceage", []))