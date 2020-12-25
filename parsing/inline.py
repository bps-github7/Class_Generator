'''
Programmer: Ben Sehnert
Program: inline class for ClassGen program
Date: 10/28/2020
Module level docstring: implements the Inline class
'''


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

Alternative Constructor: class method that generates the 
inline from (validated) user input.

    Parameters:
        -inline : str - the inputted inline class spec, of the format:
        'class : attribute(s), : method(s), (switches: -t -e{arg})'

    Return values: a reference to a freshly generated Inline instance,
    matching the specifications of the inline argument provided.

    Side-effects: creates an Inline object in the scope of the
    invokation/call to the constructor. Memory is consumed whule
    the object is in use.

    Exceptions: Unknown at this point.
    '''

    version = 2.1

    # wouldnt it make more sense to
    def __init__(self, classes=None, attributes=None, methods=None, global_testing=False, global_exporting=None):
        def cleanse(items: str):
            def clean(x):
                return x.strip()
            items = map(clean, items.split(","))
            return ",".join(items)
        self.classes = cleanse(classes.strip())
        self.attributes = cleanse(attributes.strip())
        self.methods = cleanse(methods.strip())
        self.global_testing = global_testing
        self.global_exporting = global_exporting

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
        if self.classes.count("<"):
            return True
        return False

    # no need for str method here. repr will just read the inline back to users
    def __repr__(self):
        return "{} : {} : {} {}".format(self.classes, self.attributes, self.methods,
                                        "{}{}".format(("-t" if self.global_testing else ""),
                                                      (" -e{}".format(self.global_exporting)
                                                       if self.global_exporting else "")))

    @classmethod
    def string_to_inline(cls, inline: str):
        """Alternative constructor for building an Inline object
        out of a string that uses the Inline spec mini-language.

        Args:
            inline (str): [description]
        """
        def testing(arg):
            return True if arg.count("-t") else False

        def exporting(arg):
            return inline.split("-e")[1] if arg.count("-e") else 0
        new_line = inline.split(":")
        modified_methods = new_line[2].split("-t")[0]
        return Inline(classes=new_line[0],
                      attributes=new_line[1],
                      methods=modified_methods,
                      global_testing=testing(inline),
                      global_exporting=exporting(inline))

    # if global testing/ global exporting set to false, will need to parse
    # for these later, when translating into a class dict from here


# if __name__ == "__main__":
#     new_line = Inline.from_inline(
#         "classA : attr1, attr2, attr3, attr4 : method1, method2 -t -e{us,ts,er}")
#     print(new_line.__repr__())

# actually not sure how useful this class is since we wont need do any operation on inline except translate it into class_dict
