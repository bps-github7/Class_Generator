'''
Programmer: Ben Sehnert
Program: inline class for ClassGen program
Date: 10/28/2020
Module level docstring: implements the Inline class
'''
from .class_dict import ClassDict


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


def main(inline: Inline) -> int:

    if inline.classes.count(","):
        classes, attributes, methods = [], [], []
        for x, y, z in zip(
                inline.classes.split(","),
                inline.attributes.split("/"),
                inline.methods.split("/")):
            classes.append(x), attributes.append(y), methods.append(z)
        class_container = {}
        for cls, attr, method in zip(classes, attributes, methods):
            # It is nesecary to use class dict.__repr__ instead of tuple.
            # maybe u could make a tuple class (attr, methods, parent, testing, exporting) with custom str for formatting
            class_container.update(
                {cls: (attr, method, f"{object}\t{inline.global_testing}\t{inline.global_exporting}")})
        print("item no:\tclass name:\tAttributes:\tmethods:\tparent:\ttesting:\texporting:")
        print("----------------------------------------------------------------------------" + ("----" * 6))
        for num, item in enumerate(class_container):
            print(f"{num}\t\t{item}\t\t" + class_container[item].__str__())


if __name__ == "__main__":
    main(Inline("classA : attr1, attr2, attr3 : method1 -t -e{ut,cc}"))
