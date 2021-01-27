"""
Program: inheritance_builder module- InheritanceBuilder class
Programmer: Ben Sehnert
Date: 12/24/2020
Purpose:  defines a builder for creating inheritance hierarchies out of
inheritance containing inline specs.
"""
import re
import sys
sys.path.insert(0, "C:\\Users\\Ben\\VsCode\\python\\classgenerator")
from parsing.inline import Inline
from utils.misc_functions import get_extension
# print(sys.path)

class InheritanceBuilder:
    """Purpose:

        Exceptions:
    """
    version = 1.0

    def __init__(self, inline : str):
        """
        At this point, the inline will be validated.
        So we dont have to worry about attr, method, option being
        null or unequal.

        Args:
            inline ([type]): [description]
        """
        class_fams, attr_fams, method_fams, options_fams = [], [], [], []
        inline = inline.split(":")
        if not len(inline) == 4:
            print("dont have time for your not full inlines rn sir!")
            return
        all_classes, all_attributes, all_methods, all_options = inline[0], inline[1], inline[2], inline[3] 
   
        ### splits the parts of the inline into 'families'
        ### (if there are multiple parents/ inheritances)
        ### like so:
        # parent1, parent2 > child1, child2 > sub-child-1 ... sub-child-N
        for cls, attr, method, opts in zip(
                all_classes.split(">"),
                all_attributes.split(">"),
                all_methods.split(">"),
                all_options.split(">")):
            class_fams.append(cls.strip())
            attr_fams.append(attr.strip())
            method_fams.append(method.strip())
            options_fams.append(opts.strip())
        
        
        ### Make a list of all the classes in the "family"
        ### that need to be generated,
        ###  like so:
        # [parent1, parent2] > [ child  ,... child-N] 
        classes, attributes, methods, options = [], [], [], []
        for cls, attr, method, option in zip(class_fams, attr_fams, method_fams, options_fams):
            # note the singular for looping variables.
            classes.append(InheritanceBuilder.member_splitter(cls, token="/"))
            attributes.append(InheritanceBuilder.member_splitter(attr, token="/"))
            methods.append(InheritanceBuilder.member_splitter(method, token="/"))
            options.append(InheritanceBuilder.member_splitter(option, token="/"))
        
        ### generate classes 
        new = []
        parent = 'object'
        for cls, attr, method, opts in zip(classes, attributes, methods, options):
            # insert the parents into the extension if the class name has one.
            if parent != object and re.match(r"(\w)*[(]", cls):
                ### need a foolproof way of getting inheritance working with OR without extensions in class name! aloha!
                pass
                # extensions = get_extension(cls)
                # parents = extensions[1].split(",")
                # parents.extend(parent.split(","))
                # extensions = ",".join(parents)
            else:
                print("no tienes un extension")
            new.append(Inline.from_individual_arguments(cls, attr, method, opts))
            parent = cls
        
        # only attribute in this class that matters.
        # does this even need to be a class?
        self.classes = new

    @staticmethod
    def member_splitter(container, token=","):
        """Not really sure what this method does to be honest
        D O C U M E N T A T I O N POR FAVOR!

        Args:
            container ([type]): [description]
            token (str, optional): [description]. Defaults to ",".

        Returns:
            [type]: [description]
        """
        if isinstance(container, list):
            for num, item in enumerate(container):
                if container[num].count(token):
                    container[num] = container[num].split(token)
            return container
        else:
            if container.count(token):
                return container.split(token)
            else:
                return container


def main(inline : Inline):
    """parses an inheritance tree according to classgenerator mini language
    typically returns a list of ClassDict objects. The only instance where it
    would not would be if a non-inheritance 
    containing inline was passed in by mistake.

    Args:
        inline (Inline): an inline specification containing inheritance tree.

    Returns:
        list<ClassDict> | ClassDict: multiple classes parsed out of inheritance Inline.
    """
    return InheritanceBuilder(inline).classes

item = "classA (banana) > classB(weasel) (wombat, purse) : attr1, attr2, attr3 > mastadon,\
bucket, shallot: method1 > method2 : -t -e > -t -e"
# multi_item = Inline("Person1, Person2 > Employee > Dish_washer,\
# Short_Order_Cook, Sous_Chef : P1A, P1B / P2A, P2B > E1, E2, E3 >\
# D1, D2 / S1, S2 / SC1, SC2 : P1method / P2method > SMmethod\
# > CMmethod / SMmethod / method : -t / -e > -t -e > -t / -e{vsc,send} / -t")

processed = InheritanceBuilder(item)
# processed = InheritanceBuilder(multi_item)
print(processed.classes)
# result = main(multi_item)

# for i in result:
#     print(i.classes)

# # print(InheritanceBuilder.member_splitter(['Classa, Classb', 'Classc']))
# # print(InheritanceBuilder.member_splitter(['A1, A2 / B1, B2', 'C1, C2'], token="/"))
