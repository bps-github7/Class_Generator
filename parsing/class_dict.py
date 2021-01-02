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
    parents='object', packages='root', testing=False, exporting=None):
        """It's assumed we recieve correct, propetly formated values at this junction
        since the values will have been formatted prior to sending to ClassDict"""
        self.classes = classes
        self.details = [ClassDict.cleanse(attributes), ClassDict.cleanse(methods),
                        parents, packages, testing, exporting]
        # TypeError: unhashable type: 'list' is a big problem... design oversight.
        #  hopeful some workaround hiding in the code.

        ### Doesnt make a lot of sense really- quick google search says list cannot be key in a dict. value can be any datatype
        ### is there anwhere in the code where details is assumed to be the key instead of value? weird bug time to debugggg, yay
        self.dict = dict({self.classes: self.details})
        super(ClassDict, self).__init__(self.dict)

    def __repr__(self):
        return repr(self.dict)

    def __str__(self):
        return str(self.dict)

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

    # Does not work- obviously. but its also very buggy
    # for unknown reason - iterates 3 times upon invokation
    
    # @property
    # def classes(self):
    #     return NotImplemented
    #     # return str(self.dict)

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

    @attributes.setter
    def attributes(self, new_values):
        self.details[0] = ClassDict.cleanse(new_values)

    @methods.setter
    def methods(self, new_values):
        self.details[1] = ClassDict.cleanse(new_values)

    @parents.setter
    def parents(self, new_values):
        """any/all forms of validation can be applied outside the object runtime."""
        # if the arg is a list,
        # convert it to a string delimted by ,
        if isinstance(new_values, list):
            self.details[2] = ",".join(new_values)
        else:
            self.details[2] = new_values

    @packages.setter
    def packages(self, new_values):
        if isinstance(new_values, list):
            self.details[3] = ",".join(new_values)
        else:
            self.details[3] = new_values

    @testing.setter
    def testing(self, new_values):
        self.details[4] = new_values

    @exporting.setter
    def exporting(self, new_values):
        self.details[5] = ClassDict.cleanse(new_values)

    @classmethod
    def replace_item(self, old_details=None):
        """[summary]
        """
        # parse a new line and instantiate a classdict using it,
        # then replace in table

        # alternatively, if they want to keep all the old details the same.
        # then just get the name and instantiate a bew class w old details
        pass


    def edit_main(self):
        """Facilitates the editing of classdict members.

        Returns:
            [type]: [description]
        """
        opts_dict = {1: "classes", 2: "attributes", 3: "methods",
                4: "parent", 5: "package", 6: "testing/exporting"}
        while True:
            print("enter the corresponding number for the detail you want to edit:\n\n")
            print("item no:\toption:")
            print("-----------------------------")
            for number, selection in zip(opts_dict, list(opts_dict.values())):
                print(f"{number}\t\t\t\t\t{selection}")
            response = int(input("type c/continue at any time to leave the editing prompt."))
            if response in [1, 2, 3, 4, 5, 6]:
                new = input("enter the new values for this detail:\n")
                # this would be so much less of a pain if claassdict was an iterable object.,,,
                # class_dict[key].
                if response == 1:
                    print(
                        "cannot update the class name at this time, as it must be immutable")
                    while True:
                        restart = input("delete this entry and provide a corrected replacement (y/n)?")
                        if restart in ("y", "yes"):
                            # how do i get return from this to change table?
                            # rebuild it with the new values...
                            if ClassDict.replace_item():
                                break
                        elif restart in ("n", "no"):
                            return 0
                        else:
                            print("sorry, didnt understand that response")

                elif response == 2:
                    self.attributes = ClassDict.cleanse(new)
                elif response == 3:
                    self.methods = ClassDict.cleanse(new)
                elif response == 4:
                    ### should be:
                    # if valid_parent(new):
                    #     self.parents = new
                    # else:
                    #     print("Invalid new value- parent must be a valid python class identifier")
                    #     return
                    self.parents = new
                elif response == 5:
                    self.packages = str(new)
                elif response == 6:
                    testing = input("testing is set to {self.testing}, flip the switch (y/n)?")
                    if testing in ("y", "yes"):
                        self.testing = not self.testing
                    exporting = input("exporting has been provided the following options:  {self.exporting}, modify them (y/n)? switch the flag (set exporting to false) with (s/switch)")
                    if exporting in ("y", "yes"):
                        while True:
                            new_exporting = input("type the options you want to be applied to this class for exporting (options- vsc (source code management), send- (ssh or email)")
                            if new_exporting in ("vsc","send", "vsc,send", "vsc, send", "send,vsc", "send, vsc"):
                                self.exporting = new_exporting
                                break
                            else:
                                print("didnt recognize your response- provide options matching the syntax: single_option   or  option1,option2")
                    elif exporting in ("s", "send"):
                        self.exporting = None
            elif response in ("c", "continue"):
                return 1
            else:
                print(f"sorry- {response} is not a valid choice. Try again.")


                        



    # these are 'best practices' modifications, so we will make them
    # involuntary by default and add a .rc setting to turn it off.

    # only other modification is non-optional - validation:
    # handle this in input retrival stage of program

    @classmethod
    def from_tuple(cls, item):
        '''Alt constructor for building a class dict out of tuple
        helps with isinstance testing when getting a 
        '''
        return ClassDict(item[0], item[1][0], item[1][1], item[1][2], item[1][3], item[1][4])


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

def main(cls1: ClassDict, cls2: ClassDict):
    """test all fns the class should handle.
    """

    # change any value besides class
    cls1.attributes = "monkey, weasel, cat"
    cls2.methods = "wombatBBQ, zebracorn"
    cls1.parents = "elchapo, pabloesbo"
    cls2.packages = "biscuit, frontier"
    cls1.testing = True
    cls2.exporting = ['vsc','send']

    # update a dict with clsdict, tests-
    # 1. is it iterable?
    # 2. does it override dict correctly?
    new = {}
    new.update(cls1)
    new.update(cls2)

if __name__ == "__main__":
    # print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(
    #     __file__, __name__, str(__package__)))
    print(main(ClassDict("waffle", "attr1, attr2", ["methodA", "methodB"]),
    ClassDict("bisk", ["attr3", "attr4"], ["methodC", "methodD"])))
