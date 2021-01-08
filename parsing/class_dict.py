'''
Programmer: Ben Sehnert
Program: Class_Dict Class
Software: Class Generator
Date: 12/21/2020

Module level docstring: implementation of Class Dict Class
'''

class ClassDict(dict):
    '''Class Level Docstring: Class_Dict is a dictionary that contains the specifications of a class
    it is the internal repersentation of the Inline class.'''

    def __init__(self, classes, attributes=None, methods=None,
    parents='object', packages='root', options=None):
        """It's assumed we recieve correct, propetly formated values at this junction
        since the values will have been formatted prior to sending to ClassDict"""
        self.classes = classes
        if options is None:
            self.options = None
            self.details = [ClassDict.cleanse(attributes), ClassDict.cleanse(methods),
                        parents, packages, False, False]  
        else:
            self.options = options.split("-")
            self.details = [ClassDict.cleanse(attributes), ClassDict.cleanse(methods),
                        parents, packages, *self.get_args()]    
        self.dict = dict({self.classes: self.details})
        super(ClassDict, self).__init__(self.dict)


    def get_args(self):
        """[summary]
        """
        testing, exporting = False, None
        for item in self.options:
            if item in ("", " "):
                continue
            elif item.startswith("t"):
                args = item[1:]
                if args in ("", " ", "{}", "{ }"):
                    testing = True
                else:
                    testing = args
            elif item.startswith("e"):
                args = item[1:]
                if args in ("", " ", "{}", "{ }"):
                    exporting = True
                else:
                    exporting = args
        return list([testing, exporting])

    def __repr__(self):
        return repr(self.dict)

    # def __str__(self):
    #     return f"\t{self.classes}\t\t\t{self.attributes}\t\t{self.methods}\t  {self.parents}\t   {self.packages}\t\t  {self.testing}\t\t{self.exporting}"

    def __iter__(self):
        return iter(self.dict)

    def __next__(self):
        return next(self.dict)

    def keys(self):
        return self.dict.keys()

    def items(self):
        return self.dict.items()

    def values(self):
        return self.dict.values()

    # accessing these is funny so we'll define computed properties for all fields
    @property
    def attributes(self):
        return self.details[0]

    @property
    def methods(self):
        return self.details[1]

    @property
    def parents(self):
        return self.details[2]

    @property
    def packages(self):
        return self.details[3]

    @property
    def testing(self):
        return self.details[4]

    @property
    def exporting(self):
        return self.details[5]

    # @attributes.setter
    # def attributes(self, new_values):
    #     self.details[0] = ClassDict.cleanse(new_values)

    # @methods.setter
    # def methods(self, new_values):
    #     self.details[1] = ClassDict.cleanse(new_values)

    # @parents.setter
    # def parents(self, new_values):
    #     """any/all forms of validation can be applied outside the object runtime."""
    #     # if the arg is a list,
    #     # convert it to a string delimted by ,
    #     if isinstance(new_values, list):
    #         self.details[2] = ",".join(new_values)
    #     else:
    #         self.details[2] = new_values

    # @packages.setter
    # def packages(self, new_values):
    #     if isinstance(new_values, list):
    #         self.details[3] = ",".join(new_values)
    #     else:
    #         self.details[3] = new_values

    # @testing.setter
    # def testing(self, new_values):
    #     if new

    # @exporting.setter
    # def exporting(self, new_values):
    #     return NotImplemented


#     @classmethod
#     ##### this can be exported to parser.parsing module
#     def replace_item(self, old_details):
#         """
#         Alt constructor- build new ClassDict to replace an old one.

#         allows user to generate a new class dict on the spot.
#         since class name is key in dict, editing that attribute is impossible during runtime.
#         """

#         building_path = input("want to use the old details \
# (attributes, methods, parent, etc) of the class (y/n)?\n\
# (Note that choosing n/no means you will have to provide a new inline to build it from scratch)")
#         if building_path in ("y", "yes"):
#             return ClassDict(input("provide a new name for your class:\n"), *old_details)
#         elif building_path in ("n", "no"):
#             # we should use inline.parse here but it
#             # would create a circular import and tight coupling.
#             # we will use interactive mode fns until this is figured out
#             name = input("provide a new name for your class:\n")
#             attributes = input(f"provide attributes for {name},\
#  delimiting with ',', or leave blank for no attributes:\n")
#             methods = input(f"provide methods for {name}, delimiting with ',',\
#  or leave blank for no methods:\n")
#             if answer := input("any parents? (defaults to 'object')"):
#                 parents = answer
#             else:
#                 parents = 'object'
#             if answer := input(f"is {name} contained within a package? (defaults to 'root')"):
#                 packages = answer
#             else:
#                 packages = 'root'
#             if answer := input(f"generate {name} with testing? (defaults to False)"):
#                 if answer in ("yes", "y"):
#                     testing = answer
#                 else:
#                     testing = ''
#             if answer := input(f"Should we do anything with {name}\
#  after generation (options- vsc, send)? (defaults to None)"):
#                 if answer in ("yes", "y"):
#                     exporting = answer
#                 else:
#                     exporting = ''
#             options = ''
#             if testing:
#                 if isinstance(testing, bool):   
#                     options += "-t"
#                 else:
#                     options += f"-t{testing}"
#             if exporting:
#                 if isinstance(exporting, bool):
#                     options += " -e"
#                 else:
#                     options += f" -e{exporting}"
#             return ClassDict(name, attributes, methods, parents, packages, options)

#     def edit_main(self):
#         """Facilitates the editing of classdict members.

#         Returns:
#             self [ClassDict]: the complete class dict after editing.
#         """
#         opts_dict = {1: "classes", 2: "attributes", 3: "methods",
#                 4: "parent", 5: "package", 6: "testing/exporting"}
#         while True:
#             print("enter the corresponding number for the detail you want to edit:")
#             print("item no:\toption:")
#             print("-----------------------------")
#             for number, selection in zip(opts_dict, list(opts_dict.values())):
#                 print(f"{number}\t\t\t\t\t{selection}")
#             response = input("c/continue at any time to leave the editing prompt.\n")
#             if response in ("c", "continue"):
#                 return self
#             response = int(response)
#             if response in [1, 2, 3, 4, 5, 6]:
#                 if response < 6 and response > 1:
#                     new = input("enter the new values for this class field:\n")
#                 if response == 1:
#                     print(
#                         "cannot update the class name in place, as it must be immutable\n")
#                     while True:
#                         restart = input("delete this entry and provide\
#  a corrected replacement (y/n)?\n")
#                         print("\n\n")
#                         if restart in ("y", "yes"):
#                             return ClassDict.replace_item(self.details)
#                         elif restart in ("n", "no"):
#                             break
#                         else:
#                             print("sorry, didnt understand that response")
#                 elif response == 2:
#                     self.attributes = ClassDict.cleanse(new)
#                 elif response == 3:
#                     self.methods = ClassDict.cleanse(new)
#                 elif response == 4:
#                     ### should be:
#                     # if valid_parent(new):
#                     #     self.parents = new
#                     # else:
#                     #     print("Invalid new value- parent must be a valid python class identifier")
#                     #     return
#                     self.parents = new
#                 elif response == 5:
#                     self.packages = str(new)
#                 elif response == 6:
#                     testing = input("testing is set to {self.testing}, flip the switch (y/n)?\n")
#                     if testing in ("y", "yes"):
#                         self.testing = not self.testing
#                     exporting = input(f"exporting has been provided the following options:  {self.exporting},\n\
# modify them (y/n)? switch the flag (set exporting to false) with (s/switch):\n")
#                     if exporting in ("y", "yes"):
#                         while True:
#                             new_exporting = input("type the options you\
#  want to be applied to this class for exporting\n\
# (options- vsc (source code management), send- (ssh or email):\n")
#                             if new_exporting in ("vsc","send", "vsc,send", "vsc, send", "send,vsc", "send, vsc"):
#                                 self.exporting = new_exporting
#                                 break
#                             else:
#                                 print("didnt recognize your response- provide options\
#  matching the syntax: single_option   or  option1,option2")
#                     elif exporting in ("s", "send"):
#                         self.exporting = None
#             else:
#                 print(f"sorry- {response} is not a valid choice. Try again.")

    # these are 'best practices' modifications, so we will make them
    # involuntary by default and add a .rc setting to turn it off.

    # only other modification is non-optional - validation:
    # handle this in input retrival stage of program
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

    # @classmethod
    # def from_tuple(cls, item):
    #     '''Alt constructor for building a class dict out of tuple
    #     helps with isinstance testing when getting a 
    #     '''
    #     return ClassDict(item[0], attributes=item[1][0], methods=item[1][1], parents=item[1][2], packages=item[1][3], testing=item[1][4], exporting=item[1][5])



def main(cls1: ClassDict, cls2: ClassDict):
    """test all fns the class should handle.
    """

    # # change any value besides class
    # cls1.attributes = "monkey, weasel, cat"
    # cls2.methods = "wombatBBQ, zebracorn"
    # cls1.parents = "elchapo, pabloesbo"
    # cls2.packages = "biscuit, frontier"
    # cls1.testing = True
    # cls2.exporting = ['vsc','send']

    # update a dict with clsdict, tests-
    # 1. is it iterable?
    # 2. does it override dict correctly?
    new = {}
    new.update(cls1)
    new.update(cls2)
    return new

if __name__ == "__main__":
    # print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(
    #     __file__, __name__, str(__package__)))
    print(main(ClassDict("waffle", "attr1, attr2", ["methodA", "methodB"], options="-t{ut,cc} -e{tgz,send}"),
    ClassDict("bisk", ["attr3", "attr4"], ["methodC", "methodD"])))


    item = ClassDict("bisk", ["attr3", "attr4"], ["methodC", "methodD"], options="-e{send}")
    print(item.exporting)