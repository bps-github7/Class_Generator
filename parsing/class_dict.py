'''
Programmer: Ben Sehnert
Program: Class_Dict Class
Software: Class Generator
Date: 12/21/2020

Module level docstring: implementation of Class Dict Class

this might actually be the useless class. but maybe worthwhile figuring out how to make it iterable
'''
# __package__ = "parsing"


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
        self.dict = {self.classes: self.details}
        super(ClassDict, self).__init__(self.dict)

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

    # should not be able to modify classes as its the key in a dict.
    # we'll have to export this responsility to whoever tries to call
    # this method- its buggy and cause infinite recursive call
    # @classes.setter
    # def classes(self, cls):
    #     print("class attribute cannot be changed.")
    #     return 1


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
        # I think the {} keyword dict for passing args is
        #  wrong/ anti-syntax-sugar. naturally. just use a string or list.


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




def main(cls1: ClassDict, cls2: ClassDict):
    """test all fns the class should handle.
    """

    # change any value besides class

    # all these work besides classes getter and setter, as expected.
    # not totally desirable but work arounds are possible.

    # cls1.classes = "leprechaun"
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

    return new

if __name__ == "__main__":
    # print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(
    #     __file__, __name__, str(__package__)))
    print(main(ClassDict("waffle", "attr1, attr2", ["methodA", "methodB"]),
    ClassDict("bisk", ["attr3", "attr4"], ["methodC", "methodD"])))
