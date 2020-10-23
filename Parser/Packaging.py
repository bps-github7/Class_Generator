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
import os
import class_dict
import inline
# these should be capitalized...


def main():
    # def main(inline : Inline) -> int:
    '''Parses an inline class spec that specificies packaging structure.'''
    return NotImplemented


def make_package(name: str, class_dict: Class_Dict) -> int:
    '''
    Creates a single python package containing:
        -__init__.py
        -documentation(README.md)
        -classes
        -scripts**
        -unittests**

    Parameters:
        -name -> str : name of package being created
        -class_dict -> Class_Dict : the list of files to construct in this package
        ??? maybe a list arg for name of child packages..    

    '''
    # if cwd is writable:
    os.mkdir(name)
    os.chdir(name)
    # so that python recognizes the package as part of the package directory
    os.mknod("__init__.py")
    for i in
    os.mknod()
