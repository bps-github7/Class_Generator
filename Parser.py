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
    classes = inline.split(":")[0]
    validate(classes)
            

def validate(items, item_type="class"):
    container = []
    for i in items.split(("," if (item_type == 'class' ) else "/")):
        trimmed = i.strip()
        if is_identifier(trimmed):
            continue
        else:
            print("{} is not a valid identifier.".format(trimmed))
        container.append(case_check(trimmed))

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
    parse_inline("skone, fuckme, shitspread : shit, bisk, chalp : asspie, dessert")

main()