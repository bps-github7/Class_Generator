### Programmer: Ben Sehnert
### Date: 10/20/2020
### Program: Parser for class gen, reads in class names and 
### specs, validates them and places them in appropriate container.

import sys
import keyword

def is_identifier(ident: str) -> bool:
    """Determines if string is valid Python identifier."""

    if not isinstance(ident, str):
        raise TypeError("expected str, but got {!r}".format(type(ident)))

    if not ident.isidentifier():
        return False
    
    if keyword.iskeyword(ident):
        return False

    return True

def parse_inline(inline):
    inline = inline.split(":")
    return { validate(inline[0]) : (validate(inline[1], item_type="attribute"), validate(inline[2], item_type="method")) }

    #what if methods is not provided?
    # classes, attributes, methods = validate(inline[0], item_type="class"), validate(inline[1], item_type="attribute"), validate(inline[2], item_type="method")
    # if classes:
    #     print("skonedalone!")
    #     return { classes : () }



            

def validate(items, item_type="class"):
    container = []
    ### this line only applies if there is inheritance nesting- test it seperately!!!
    # token = "," if (item_type == 'class' ) else "/"
    token = ","
    for i in items.split(token):
        trimmed = i.strip()
        if is_identifier(trimmed):
            continue
        else:
            print("{} is not a valid identifier.".format(trimmed))
            return 0
        container.append(case_check(trimmed))
    return container

def case_check(item, item_type="class"):
    if item_type == "class":
        if item.istitle():
            return item
        else:
            answer = input("your class name is not capitalized. Would you like this corrected? (y/n)")
            return (item.title() if (answer.lower() in ('yes','y','yea','yeah','yup')) else item)
    elif item_type in ("attribute","method"):
        if item.islower():
            return item
        else:
            answer = input("your attribute or method is not lowercase. Would you like this corrected? (y/n)")
            return (item.lower() if (answer.lower() in ('yes','y','yea','yeah','yup')) else item)

        
            


def main():
    return parse_inline("skone, fuckme, shitspread : shit, bisk, chalp : asspie, dessert")

print(main())