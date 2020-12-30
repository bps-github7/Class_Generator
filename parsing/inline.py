'''
Programmer: Ben Sehnert
Program: inline class for ClassGen program
Date: 10/28/2020
Module level docstring: implements the Inline class
'''
from .class_dict import ClassDict
from .details import Details


class Inline:
    '''
Class Level Docstring: this is a class that repersents inline class
specifications.

constructor: creates an instance of the Inline class. performs cleansing to
strip white space from fields, which is noise in the classGen mini language.

    Parameters:
        -classes = None : repersents the class to be generated's identifier(s)
        -attributes = None : repersents the class to be generated's attribute(s)
        -methods = None : repersents the class to be generated's method(s)
        -global_testing = False : should unit tests be generated for all files
        -global_export = None : What should be done to the project after generation.
        if the field is not set to None, it will be a set of arguments/directives (what to do next?)

    Return values: None

    Side-effects: creates an Inline object in the scope of the
    invokation/call to the constructor. Memory is consumed while
    the object is in use.

    Exceptions: Unknown at this point.
    '''

    version = 2.1

    def __init__(self, inline):
        self.inline = inline.split(":")
        self.classes = Inline.cleanse(self.inline[0].strip())
        self.attributes = Inline.cleanse(self.inline[1].strip())
        self.methods = Inline.cleanse(self.inline[2].strip())
        if self.has_options():
            self.global_exporting = Inline.exporting(self.methods)
            if self.global_exporting:
                # we want the first half= [1] is the keyword arg dict.
                self.methods = self.methods.split("-e")[0]
            self.global_testing = Inline.testing(self.methods)
            # cleanup - get rid of switches on methods once their existence is confirmed.
            if self.global_testing:
                self.methods = self.methods.split(" -t")[0]

    def has_options(self):
        """[summary]
        """
        return True if ("-e" or "-t") in self.methods else False

    def has_inheritance(self):
        """checks self.classes to see if it has > token in it.
            having this token indicates inline spec has inheritance.

        Returns:
            Boolean : based off whether inline has inheritance
        """
        if self.classes.count(">"):
            return True
        return False

    def has_packaging(self):
        """checks self.classes to see if it has < token in it.
            having this token indicates inline spec has packaging.
            note: rudimentary check- more parsing required than this.

        Returns:
            Boolean : based off whether inline has packaging
        """
        return True if self.inline.count("<") else False

    def __repr__(self):
        return ":".join(self.inline)

    def __str__(self, single_line=True):
        if single_line:
            return "{}\t{}\t{}\t{}\t{}".format(self.classes, self.attributes, self.methods, self.global_testing, self.global_exporting)
        else:
            return "class(es): {}\n\
attributes: {}\n\
methods: {}\n\
testing: {}\n\
exporting: {}".format(self.classes, self.attributes,
                      self.methods, self.global_testing, self.global_exporting)

    @staticmethod
    def testing(arg):
        """returns true if arg contains -t flag
        args (Inline.method : str): method section of inline"""
        return True if arg.count("-t") else False

    @staticmethod
    def exporting(arg):
        """returns the keyword dict argument of -e flag if present
        args (Inline.method : str): method section of inline
        """
        return arg.split("-e")[1] if arg.count("-e") else False

    @staticmethod
    def cleanse(items: str):
        """Cleanses a list of stirngs of whitespace and junk text
        """
        def clean(item):
            """ applies strip function on a per token basis.
            """
            return item.strip()
        items = map(clean, items.split(","))
        return ",".join(items)


def parse_inline(inline) -> list:
    """[summary]

    Args:
        inline ([type]): [description]

    Returns:
        list: [description]
    """
    class_dict = {}
    # if there are multiple classes in a single inline,
    # distinguish them into a multi nested, multi element dictionary
    if inline.classes.count(","):
        classes, attributes, methods = [], [], []
        for x, y, z in zip(
                inline.classes.split(","),
                inline.attributes.split("/"),
                inline.methods.split("/")):
            classes.append(x), attributes.append(y), methods.append(z)
        for x, y, z in zip(classes, attributes, methods):
            class_dict.update(ClassDict(x, Details(y, z, options=[
                              inline.global_testing, inline.global_exporting])))
    else:
        class_dict.update(ClassDict(inline.classes, Details(
            inline.attributes, inline.methods,
            options=[inline.global_testing, inline.global_exporting])))
    return class_dict


def display_classes(class_dict):
    """[summary]

    Args:
        classdict ([type]): [description]
    """
    print("item no:\tclass name:\tAttributes:\t\t\
methods:\t\tparent:\t\t\tpackage:   testing, exporting:")
    print(
        "----------------------------------------------------------------------------" + ("----" * 15))
    for num, item in enumerate(class_dict):
        print(f"{num + 1}\t\t{item}\t\t{class_dict[item]}")
    return 1


def quick_exit():
    response = input(
        "action complete. Want to return to previous prompt? type y / yes to do so.")
    if response in ("y", "yes"):
        return True


def get_feedback(class_dict):
    """[summary]
    """
    while True:
        display_classes(class_dict)
        print("everything look up to spec?")
        response = input("type c to continue with generation, r to reprint the table, or an\
entries corresponding 'item no' to edit or delete:\n")
        valid_responses, keys = [
            m+1 for m, n in enumerate(class_dict)], [items for items in class_dict]
        if response.lower() == 'c':
            return class_dict
        elif response.lower() == 'r':
            display_classes(class_dict)
        elif int(response) in valid_responses:
            cls = keys[int(response)-1]
            loop = True
            while loop:
                response = input(
                    "type e / edit to edit entry, d / delete to delete.\n\
close this prompt with c / close")
                if response.lower() in ('e', 'edit'):
                    class_dict = edit_entry(class_dict, cls)
                    if quick_exit():
                        loop = False
                elif response.lower() in ('d', 'delete', 'del'):
                    delete_entry(class_dict, cls)
                    if quick_exit():
                        loop = False
                elif response.lower() in ('c', 'close'):
                    break
                else:
                    print(
                        "invalid response- valid choices are e/edit, d/delete, c/close")
                    continue
        else:
            print(
                "invalid response- valid choices are c/continue, r/reprint table or a n0umber in the 'item no' col of the table")


def delete_entry(class_dict, key):
    """[summary]

    Args:
        classdict ([type]): [description]
        line ([type]): [description]
    """
    # get the dict key as a string
    if input("are you sure you want to delete this spec?").lower() in ("yes", "y"):
        del class_dict[key]
    return 1


def edit_entry(class_dict, key):
    """[summary]

    Args:
        classdict ([type]): [description]
        opt ([type]): [description]
    """
    while True:
        opts_dict = {1: "classes", 2: "attributes", 3: "methods",
                     4: "parent", 5: "package", 6: "testing/exporting"}
        print("enter the corresponding number for the detail you want to edit:\n\n")
        print("item no:\toption:")
        print("-----------------------------")
        for x, y in zip(opts_dict, list(opts_dict.values())):
            print(f"{x}\t\t{y}")
        response = int(input())
        if response in [1, 2, 3, 4, 5, 6]:
            # new = input("enter the new values for this detail:\n")
            # this would be so much less of a pain if claassdict was an iterable object.,,,
            # class_dict[key].
            if response == 1:
                print(
                    "cannot update the class name at this time, as it must be immutable")
                return 0
            else:
                new_values = input(f"enter new values for {opts_dict[response]}\n\
delimit multiple items with , token:\n")
                field = opts_dict[response]
                #this not working,
                class_dict[key][field] = new_values
                print(class_dict)
                return class_dict
        else:
            print(f"sorry- {response} is not a valid choice. Try again.")
                


def main(inline: Inline) -> int:
    classes = parse_inline(inline)
    get_feedback(classes)


if __name__ == "__main__":
    main(Inline("classA : attr1, attr2, attr3 : method1 -t -e{ut,cc}"))
