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
# print(sys.path)

class InheritanceBuilder:
    """Purpose:

        Exceptions:
    """
    version = 1.0

    def __init__(self, inline : str):
        """
        Taking in a string of the `Inheritance Inline` format (see README.md)
        does two jobs in succession:
            -validate the inline and the inheritances
            -parse the validated inheritance inline
            into an array of regular inlines
        parses into an array of inlines that match the specs
        given in the inheritance inlines (sets parents based on
        placement of '>' tokens and their operators.)

        Args:
            inline ([type]): [description]
        """
        class_fams, attr_fams, method_fams, options_fams = [], [], [], []
        inline = inline.split(":")
        if not len(inline) == 4:
            print("dont have time for your not full inlines rn sir!")
            return
        all_classes, all_attributes, all_methods, all_options = \
        inline[0], inline[1], inline[2], inline[3]
        ### splits the parts of the inline into 'families'
        ### (if there are multiple parents/ inheritances)
        ### like so:
        # parent1, parent2 > child1, child2 > sub-child-1 ... sub-child-N
        for classes, attr, method, opts in zip(
                all_classes.split(">"),
                all_attributes.split(">"),
                all_methods.split(">"),
                all_options.split(">")):
            class_fams.append(classes.strip())
            attr_fams.append(attr.strip())
            method_fams.append(method.strip())
            options_fams.append(opts.strip())
        
        
        ### Make a list of all the classes in the "family"
        ### that need to be generated,
        ###  like so:
        # [parent1, parent2] > [ child  ,... child-n] 
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
            if parent != "<class 'object'>" and re.match(r"(\w)*[(]", cls):
                class_name, parents, rest = cls.split("(")[0], (cls.split("(")[1]).split(")")[0], "fart-bean"
                # print(f"class name : {class_name} rest : {parents}")
                # cls = f"{class_name}({parent},{rest}"
            else:
                parent = cls
            # are you sure this is a super effective test? cases you are forgetting about?
            new.append(Inline(f"{cls} : {attr} : {method}  : {opts}"))
            # new.append(Inline.from_individual_arguments(cls, attr, method, opts))
            
        
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
            for num,item in enumerate(container):
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