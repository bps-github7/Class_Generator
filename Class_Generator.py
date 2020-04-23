#!/usr/bin/python3
###Programmer: Ben Sehnert
###Date: 1/8/2020
###Program: main file for automatic class generator
###Software: Nil

"""
Module level docstring: This is a program designed to automatically generate class files after being provided the relevant information by a user
Capable of being run as a interactive prompt which queries the user or a low profile command line tool
"""

import errno
import tempfile
import argparse
import sys
import os
from Options import *
from Regular_Class import *
from Special_Class import *
from Misc_Functions import inheritance  
from Misc_Functions import class_generator

parser = argparse.ArgumentParser(description="Generate classes automatically using command line options or interactive prompt")
#any mutually exculsive groups? I don't think so at this time

#get the project name {mandatory}
parser.add_argument("--name", "--project Name", type=str, metavar='', help="Provide the name for the project you are creating.\nProgram execution will create a new directory with the provided name, located in default path, to contain newly generated class files.", required=True)

#Have this disabled for now, for conveinece/ testing sake.
#indistro it will be required and testing will run automatically
#parser.add_argument("-d", "--default", dest="default", type=str, metavar='', help="Provide a valid system path which project directory can be created in\nDefaults to the folder scipt is executed in", required=False)

#get class and attributes from a dictionary passed in through a string- write function to evaluate...
parser.add_argument("-c", "--class_and_attributes", type=str, metavar='', dest="cls", help="pass in class info into string containing dict\nSYNTAX: '{'class_name':'attr, _attr, __attr', 'ABC=class_name':'attribute' #abstract base class, 'parentclass_name -> childclass_name':'parent_attr, parent_attr -> child_attr, child_attr' #inheritence }'")

#probably a stupid argument- who needs a class with no instance variables?
parser.add_argument("-s", "--skip-attributes", metavar='', help="use this option to skip defining instance variables for your class", required=False)

#what are alternative constructors and should they be included in this tool?
#parser.add_argument("-A", "--Alternative Constructor", help="")

#testing
parser.add_argument("-t", "--testing", type=str, metavar='', help="Automatically generate unittests, static analysis, code coverage, additional documentation?", required=False)

#exportng
parser.add_argument("-e", "--exporting", type=str, metavar='', choices=['tgz', 'zip', 'tgz and email', 'tgz and zip', 'tgz and SSH', 'zip and SSH'], help="What should be done with the generated project {tgz, zip, tgz & email req arg: 'name@mail.com', zip and email, tgz and ssh, zip and ssh }", required=False)

#read arguments passed to the console.
args = parser.parse_args()

#default path for testing purposes- 
default = r"C:\Users\Ben\Desktop\Grad school- MSIS program\misc"



def main():
    if test_path(default):
        data = eval(args.cls)
        for i in data:
            class_generator(i, data[i].split(","))

#main()
