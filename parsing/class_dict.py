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

    def str_testing(self):
        if isinstance(self.testing, bool):
            return " -t"
        elif isinstance(self.testing, str):
            return f" -t{self.testing}"
        else:
            return ''

    def str_exporting(self):
        if isinstance(self.exporting, bool):
            return " -e"
        elif isinstance(self.exporting, str):
            return f" -e{self.exporting}"
        else:
            return ''

    def str_switches(self):
        return f"{self.str_testing()}{self.str_exporting()}"

    def __str__(self, switches=False):
        if switches:
            return f"\t{self.classes}\t\t\t{self.attributes}\t\t{self.methods}\t  {self.parents}\t   {self.packages}\t\t  {self.testing}\t\t{self.str_switches()}"
        return f"\t{self.classes}\t\t\t{self.attributes}\t\t{self.methods}\t  {self.parents}\t   {self.packages}\t\t  {self.testing}\t\t{self.exporting}"

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

    # exposing the private interface because python
    # is giving me a confusing error about not being able
    # to set attributes if i write this as a property.
    def get_details(self):
        if self.options is None:
            return [self.attributes, self.methods,
                        self.parents, self.packages]
        else:
            return [self.attributes, self.methods,
                    self.parents, self.packages, self.str_switches()]


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
        if new_values in ("{ut}", "{cc}", "{sa}", "{ut,cc}","{cc,ut}",
        "{ut,sa}","{sa,ut}","{cc,sa}","{sa,cc}","{ut,cc,sa}","{cc,ut,sa}",
        "{sa,ut,cc}","{ut,sa,cc}","{cc,sa,ut}","{sa,cc,ut}") or isinstance(
        new_values, bool):
            self.details[4] = new_values


    @exporting.setter
    def exporting(self, new_values):
        if new_values in ("{send}", "{zip}", "{tgz}", "{vsc}",
        "{send,tgz}","{send,zip}","{send,vsc}","{tgz,send}",
        "{tgz,zip}","{tgz,vsc}","{zip,send}","{zip,tgz}",
        "{zip,vsc}","{vsc,send}","{vsc,tgz}","{vsc,zip}",
       "{send,tgz,zip}", "{send,tgz,vsc}","{send,zip,tgz}",
       "{send,zip,vsc}","{send,vsc,tgz}","{send,vsc,zip}",
       "{tgz,send,vsc}","{tgz,send,zip}","{tgz,zip,vsc}",
       "{tgz,zip,send}","{tgz,vsc,zip}","{tgz,vsc,send}",
       "{zip,send,tgz}","{zip,send,vsc}","{zip,tgz,send}",
       "{zip,tgz,vsc}","{zip,vsc,send}","{zip,vsc,tgz}",
       "{vsc,send,zip}","{vsc,send,tgz}","{vsc,tgz,zip}",
       "{vsc,tgz,send}","{vsc,zip,tgz}","{vsc,zip,send}")\
        or isinstance(new_values, bool):
            self.details[5] = new_values


    
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

    @classmethod
    def from_tuple(cls, item):
        '''Alt constructor for building a class dict out of tuple
        helps with isinstance testing when getting a 
        '''
        return ClassDict(item[0], attributes=item[1][0], methods=item[1][1], parents=item[1][2], packages=item[1][3], options=item[1][4])



def main(cls1: ClassDict, cls2: ClassDict):
    """test all fns the class should handle.
    """

    # # change any value besides class
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
    print(main(ClassDict("waffle", "attr1, attr2", ["methodA", "methodB"], options="-t{ut,cc} -e{tgz,send}"),
    ClassDict("bisk", ["attr3", "attr4"], ["methodC", "methodD"])))


    # item = ClassDict("bisk", ["attr3", "attr4"], ["methodC", "methodD"], options="-e{send} -t{ut}")
    # print(item.exporting)
    # print(item.testing)