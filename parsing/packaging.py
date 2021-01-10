'''
Programmer: Ben Sehnert
Project: Class_Generator
Package: Parser, Module: Packaging module
Date: 10/23/2020

Module Level Docstring: parses packaging specificiations in order to construct 
package structuring for a project.

internally, uses the same mini language syntax used for parsing inheritance containing inline specs.
package name, package_sibling_name : all, files, contained / all, files, contained : options - unittesting, export preferences

or

package1, package2 > package3 : p1, p2 / p3, p4 > p5, p6 : options / options > options 

and parsed into a class_dict, repurposed for this.
add this to documentation.
'''
#from Parser.Class_Dict import Class_Dict
import os

def packaging():
    print("skonedalone")

def main():
    print("nard")

#class Packaging_Inline:
#    def __init__(self, packages, files, options):
#        self.packages = [(x.strip()).lower() for x in packages.split(',')]
#        self.files = [(x.strip()).lower() for x in files.split(',')]
#        self.options = [(x.strip()).lower() for x in options.split(',')]
#
#    def __repr__(self):
#        # return '<{} : {} : {} >'
#        return
#
#    def __str__(self):
#        return self.__repr__()
#
#    def to_classdict(self):
#        return Class_Dict
