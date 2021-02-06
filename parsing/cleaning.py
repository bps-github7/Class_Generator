"""
Programmer: Ben Sehnert
Program: Cleanings module
Date: 2/6/2021
Software: Python class generator

About: This module implements functions pertaining to cleaning of inline members.
meaning, it takes the users input and coerces / constrains it into a format that
the parser is capable of understanding.
"""


# just in case:
import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")


def cleanse(items: any, item_type="field"):
    """format properties by strip and lowercase of each elements.
    side-effect: coerces ',' delimited string to formatted list.
    """
    if isinstance(items, list):
        return list(map(
            lambda item: item.strip().lower(), items))
    return list(map(
        lambda item: item.strip().lower(), items.split(",")))

def cleanse_regular_methods(items):
    """[summary]

    Args:
        items ([type]): [description]
    """
    regular = []
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

def clean_list(args):
    """Turns a list of arguments into a clean list of string arguments.
    This makes it possible to take a machine readable class spec and pass it
    to Inline alternative constructor

    Arguments:
        *args [string []] : up to four pieces of Inline.

    Returns:
        item [list]: A list of comma seperated values
    """
    items = [*args]
    for i, value in enumerate(items):
        if value is None:
            continue
        if isinstance(value, list):
            items[i] = ",".join(value)
    return items
