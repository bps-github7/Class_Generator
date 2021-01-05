'''
Programmer: Ben Sehnert
Program: inline class for ClassGen program
Date: 10/28/2020
Module level docstring: implements the Inline class
'''
import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")
from parsing.class_dict import ClassDict
# from .details import Details


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
        self.classes = self.inline[0].strip().title()
        self.attributes = self.inline[1].strip()
        self.methods = self.inline[2].strip()
        if self.has_options():
            self.global_exporting = Inline.exporting(self.methods)
            if self.global_exporting:
                # we want the first half= [1] is the keyword arg dict.
                self.methods = self.methods.split("-e")[0]
            self.global_testing = Inline.testing(self.methods)
            # cleanup - get rid of switches on methods once their existence is confirmed.
            if self.global_testing:
                self.methods = self.methods.split(" -t")[0]
        else:
            self.global_testing = False
            self.global_exporting = None



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
    def cleanse(items: any):
        """format properties by strip and lowercase of each elements.
        side-effect: coerces ',' delimited string to formatted list.
        """
        if isinstance(items, list):
            return list(map(
                lambda item: item.strip().lower(), items))
        return list(map(
            lambda item: item.strip().lower(), items.split(",")))

def multiple_inline_handler(inline : str):
    """[summary]

    Args:
        inline ([type]): [description]
    """
    specifications = []
    classes, attributes, methods = [], [], []
    for single_class, its_attributes, its_methods in zip(
            inline.classes.split(","),
            inline.attributes.split("/"),
            inline.methods.split("/")):
        classes.append(single_class)
        attributes.append(its_attributes)
        methods.append(its_methods)
    # setting parent and package to defaults in this and else block below
    # until we sophisticate the packaging and inheritance functionality a bit more.
    specifications = [ClassDict(class_title, attribute_group, method_group, object, 'root')\
    for class_title, attribute_group, method_group in zip(classes, attributes, methods)]
    return specifications

def parse_inline(inline):
    """[summary]

    Args:
        inline ([type]): [description]

    Returns:
        list: A list of all the inlines parsed out of the current inline spec.
    """
    if inline.classes.count(","):
        parsed_classes = multiple_inline_handler(inline)
    else:
        # casting to a list for safety reasons.
        parsed_classes = [ClassDict(inline.classes,
            inline.attributes, inline.methods,
            object, 'root',
            inline.global_testing, inline.global_exporting)]
    return parsed_classes

def display_classes(classes):
    """[summary]

    Args:
        classdict ([type]): [description]
    """
    print("Review the following before generation.")
    print("item no:\tclass name:\t\tAttributes:\t\t\t\
methods:\t\tparent:\t\tpackage:\ttesting:\texporting:")
    print(
        "----------------------------------------------------------------------------" + ("----" * 26))
    # for num, item in enumerate(class_dict):
    #     print(f"{num + 1}\t  {(ClassDict.from_tuple((item, class_dict[item]))).__str__()}")
    # return 1
    for item in enumerate(classes):
        current_class = classes[item[0]]
        print(f"{item[0]+1}\t{current_class.__str__()}")

def quick_exit():
    response = input(
        "action complete. Want to return to previous prompt? type y / yes to do so.\n")
    print("\n\n")
    if response in ("y", "yes"):
        return True
    return False

def editing_menu(classes, index):
    """[summary]

    Args:
        classes ([type]): [description]
        index ([type]): [description]
    """
    class_index = int(index) - 1
    selected_class = classes[class_index]
    loop = True
    while loop:
        print(selected_class.__str__())
        choice = input("e to edit entry\n\
d to delete entry.\n\
c to close this prompt:\n")
        if choice.lower() in ('e', 'edit'):
            classes[class_index] = selected_class.edit_main()
            if input("done editing this class?") in ("y","yes"):
                loop=False
        elif choice.lower() in ('d', 'delete', 'del'):
            if delete_entry(classes, class_index):
                loop = False
        elif choice.lower() in ('c', 'close'):
            return classes
        else:
            print(
                "invalid response- valid choices are e/edit, d/delete, c/close")
            continue
        #non standard operating procedure to exit this way, so it returns 0 status code.
        return classes



def get_feedback(classes):
    """[summary]
    """
    while True:
        # helps format output
        print("\n\n")
        display_classes(classes)
        action = input("Type a row's corresponding 'item no' to select it for editing or deletion\n\
c / continue to continue with generation\n\
r / reprint to reprint the table\n")
        valid_responses = [(i + 1) for i in range(len(classes))]
        if action.lower() in ('c', 'continue'):
            return classes
        elif action.lower() in ('r', 'reprint'):
            continue
        elif action.lower() not in ('c', 'continue', 'r', 'reprint'):
            try:
                int(action)
                if int(action) in valid_responses:
                    classes = editing_menu(classes, action)
            except ValueError:
                print("Error- input not recognized. valid responses include r,\
reprint, c, continue, or an existing item no")
                continue
        else:
            print(
                "invalid response- valid choices are c/continue,\
r/reprint table or a number in the 'item no' col of the table")

def delete_entry(classes, index):
    """[summary]

    Args:
        classdict ([type]): [description]
        line ([type]): [description]
    """
    # get the dict key as a string
    if input("are you sure you want to delete this spec?").lower() in ("yes", "y"):
        del classes[index]
        return 1
    return 0

def main(inline: Inline) -> int:
    classes = parse_inline(inline)
    return get_feedback(classes)


if __name__ == "__main__":
    # also not reading -e values now
    main(Inline("classA : attr1, attr2, attr3 : method1 -t -e{ut,cc}"))

    # a = Inline("classA : attr1, attr2, attr3 : method1 -t -e{ut,cc}")
    # b = Inline("biscuit : attrA, attrB, attrC : methodA, methodB -t")
    # items = [a, b]
    # for i in range(0, len(items)):
    #     print(items[i].methods)


    # test = Inline("classA : attr1, attr2, attr3 : method1 -t -e{ut,cc}")
    # print(test.global_testing)