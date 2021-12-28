"""
Programmer: Ben Sehnert
Program: Cleanings module
Date: 2/6/2021
Software: Python class generator

About: This module implements functions pertaining to cleaning of inline members.
meaning, it takes the users input and coerces / constrains it into a format that
the parser is capable of understanding.
"""

import re
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

def cleanse_methods(methods, parsed):
    """[summary]

    Args:
        items (str): comma delimited string listing the methods in a class.
    """
    while methods:
        # check if the first item in the string is a signiture

        if re.match(r"(\w+)\s*\((.*?)\)", methods):

            # base case 1. where method sig is last piece of string to parse
            # ie 'example1, example2, some_fn(param1, param2)'
            # then we cannot split the string with comma without messing up the signiture       



            # isolate the signiture
            signature = methods.split("),")[0] + ")"

            new_signature = {
                'name' : signature.split("(")[0],
                'parameters' : ",".join(signature.split("(")[1:]).strip(")")
                }
            parsed.append(new_signature)

            # TODO: check the fn name and params for validity.

            # Prepare the remaining items in string for next recursion
            remaining = ",".join(methods.split("),")[1:])

        # if the first item isnt a signiture,
        # we don't care about split denegrating the integrity of it.
        else:
            if methods.count(","):
                head = methods.split(",")[0]
                remaining = ",".join(methods.split(",")[1:]).strip()
                parsed.append(head.strip().lower())
            else:
                #essentially the base case.
                parsed.append(methods.strip().lower())
                remaining = ""
            cleanse_methods(remaining, parsed)

        # to escape the loop... reconsider where ure placing your recursive calls?
        break
    return parsed
