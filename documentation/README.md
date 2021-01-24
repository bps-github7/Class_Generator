# File Generator Program
### A utility tool that generates files for python development.
### Programmer: Ben P. Sehnert

# Index:
1. [Usage](#Usage)
2. [Features](#Features)
3. [Customization with .rc file](#Customization)
4. [Running in command line mode](#Command-line-mode)
5. [Running with a file as input](#File-as-input)
5. [Running in interactive mode](#Interactive-mode)

# Usage
Input can be provided through three different methods:
1. [command line arguments](#Command-line-mode)
2. [input file(s)](#File-as-input)
3. [interactive mode](#Interactive-mode)

```
List all arguments below vvv 
to get to this screen:
`$ python -m classgenerator.py --help`
```

## Input
In most cases, the program takes a *inline specification* as input 

`BiscuitFactory : attr1/ _attr2/ __attr3 : SMmethod/ CMmethod : -t -e`

`my_cool_module : some / variables : some / functions : -t -m`

`undefined_mess : : : -a`

In order of appearance, the following inline specs will create the following files:

1. a class named 'BiscuitFactory' with 3 attributes, a static method, a class method generated with a testing suite (unittest and code coverage report) and prepared for exporting.
*NOTE: The default behavior is to generate a class*

2. a module called 'my_cool_module' with 2 variables and 2 functions, generated with a testing suite. The '-m' flag declares a module.

3. an abscract base class called 'undefined_mess' with no attributes or methods. The '-a' flag declares an abstract base class

## Output 
Generates a directory, or series of directories of files, unit tests,
documentation structuring that matches the specification provided through input.

## Details 
This program defaults to creating a new directory, 
labeled with project name, that contains all generated files. 

* This directory will be produced as a subdirectory in the
 same directory where the script is run.

* You can custom where the output will be generated with command line
arguments or the use of .rc file for customization 
(add link here: see 'customization with .rc file' or 'Running in cmd line mode')

##### 1.5 Inline Quick Reference:
Note this is a light introduction for purpose of providing a basic understanding
of the Inline. For a detailed explanation, see the [full specification](classgenerator\documentation\inline_specification.md)


__Inline Summary__: the inline spec is used for quick writing of class specs. 
it consists of a single line of text with 1-4 sets of identifiers and optional
arguments, delimited by colons, which seperate file names from optional (but helpful)
attributes/variables and methods/functions.

Inline Specification can also be used to produce design of your packaging structure,
with slight adjustments to the syntax.

###### In short: 

1. identifier (class name, attributes and methods)
and optional arguments are seperated by `:` (colons)

`Class_name : attributes : methods`
`classA : attributes : methods : -t -e`
`Mandatory : optional : optional : optional`

(link- inline_specification.md/ withholding arguments)

2. Members of the file (such as attributes, class variables, methods of all types) are seperated by 
`/`(forward-slash)


`ClassA : attr1/attr2 : method1/method2 `
`ClassA : attr1/attr2 : method1/method2 : -t -e`

3. NOTE: [pre-pend arguments](##prepend-options) exist for applying slight changes to the to-be-generated class:
    * CVattr1   : generates attr1 as a class variable
    * SMmethod1 : generates method1 as a static method
    * CMmethod2 : generates method2 as a Class method


4. if multiple classes are generated in the same inline- use comas to seperate the class identifier and `/` (forward slash)
    to seperate the sets of multiple identifiers (because comma is already in use seperating individual members)

5. `>` (right carrot) is used to denote a parent child relationship (for both classes and packages)
`ClassA > ClassB : attr1, attr2 > attr3, attr4 : method1 > method2 : -t > -e`
`<p:(package1 > package2 : class1/ class2, class3, module4)>`

5. `<p: ( keys : values)>` is used to describe a packaging structure, where keys are package names and values are
    `/`( forward slash) seperated module/class file identifiers

6. The Inline spec is designed to be robust. You can withhold any argument except the class name,
    however, be sure to include the correct amount of colons so that the correct arguments are parsed.
    (attributes get recognized as attributes, methods get recognized as methods, etc...)

7. The final area of the inline, following the third colon is for optional arguments (switches)
    providing -e or -t there will apply exporting or testing to the generated class. 
    

Recap:
`class_name_1 / ...class_name_N : attribute1_A, attribute2_B / ...attributeN_1 : `


**we must keep in mind the following rules...**
1. either attributes or methods can be blank in the inline, but not the class identifier (can't make a nameless class).

2. to leave either attributes or methods blank, include the typical amount of colons but leave the section blank

`ClassA::`                                      

creates a classA with no methods or fields       


`ClassA : : method`

creates a classA with only a method

`ClassA : attr1, attr2 :`

creates a classA with only attributes

3. the fourth, optional field can always be left out, unless one wants to use these switches/ optional arguments like so:

`ClassA : attr1, attr2 : method1 : -t -e`       

creates a ClassA with attributes, method and optional arguments for testing and exporting

`ClassA : : : -t -e`                            

creates a ClassA with only testing and exporting (no attributes or methods)

# Features

* Generate simple to sophisticated classes/modules and directory (packaging)
  structuring with a [simple, easy to learn and understand syntax](#).

* Choice of 3 modes for providing input- [command line](#), [input file](#) and [interactive mode](#)

* Create multiple, fleshed out classes with a single argument.

* Create [simple or complex multiple inheritance hierarchies with a single argument](#)

* Create [packaging structure/ hierachy with a single argument](#).

* Easily generate [additional files and perform actions with generated classes](#)

* Easily customize and persist multiple users preferences with [.rc file](#)


## Classes
### all components of PEP8 new style class are generated, including:
* constructor(__init__)
* dundr str and dundr repr
* header/script stub (if desired)
* All classes are generated in new object syntax, meaning:
    * getters and setters are not implemented by default.
    * if the class is specified as 'protected' (see [prepended arguments](#)) then its attributes will be generated with (@property and @setter)methods.

## prepend-options
* 'SM' prepended to a method identifier will generate the method as a static method.
* 'CM' prepended to a method identifier will generate the method as a class method.
* 'CV' prepended to a attribute identifier will generate the attribute as a class variable (NOTE only works with class inlines, not modules)
* '_' prepended to a attribute identifier will generate it as protected (needs confirmation) (NOTE only works with class inlines, not modules)
* '__' prepended to a attribute identifier will generate it as a name mangled attribute (NOTE only works with class inlines, not modules)

# Customization
Using an .rc file (in the format of what? csv, json, xhtml (no)?)

customize the following:
* testing- what should the '-t' option do?
* exporting- what should the '-e' option do?
* default-package- what is it?

# Command-line-mode:

to use the command line, the following arguments are mandatory:

-name: pass it in as a positional argument
`python -m filegenerator.py 'my_cool_project'`

--path: its an optional argument
`python -m filegenerator.py 'my_cool_project' --path 'C://some//path'`

--inline: its an optional argument
`python -m filegenerator.py 'my_cool_project' --path 'C://some//path' --inline 'ClassA : attr1, attr2 : method1 : -t'`

additional optional arguments can be passed in as switches/flags

* '-abc' generate the class as an abstract base class
* '-m' generate the file as a module
* '-sa' generate file(s) without attributes/variables *
* '-sm' generate file(s) without methods/functions *
* '-sb' generate file(s) with no fields of any kinds *  
* '-t'  generates the file with testing suite
* '-e' generates the file and exports it.



## Default-package

is created based on the 'name' and 'path (optinal)' arguments provided
by command line invokation:


`python -m filegenerator.py 'myexampleproject' --path 'C://path//to//here'`

creates a default package of:

`C://path//to//here//myexampleproject`

this is the path where files generated in the current session are created (unless otherwise specified by a provided packaging inline)


# File-as-input
    
you can pass a file in as the sole argument to the file generator, where each line of the file is a inline spec. 

`#Unix`

`$ ./cls_gen example`

`#NT / Windows`

`$ python cls_gen.py -f example.txt`

* Input file syntax

in the input file, seperate inline specifications with a single newline character:
`class_1 : attr1, attr2, attr3 : method1, method2, method3 : -te`

`class_2 : attr1, attr2, attr3 : method1, method2, method3: -e`

`...`

`class_n : attr1, attr2, attr3 : method1, method2, method3 : -t`

# Interactive-mode

* Running in interactive mode is the default user interface when the program is run without arguments or the option -i is used.

* You can either provide inlines to the interactive prompt until done,
or be guided through the process of creating a class or package step by step.

## Getting to know Inlines with Interative mode:  

Interactive mode is reccomended for first time users. The process of building the classes or modules from the ground up will help users understand the logical construction of inlines. Because packaging inlines are required first in the interactive mode, this enforces rules presumed as 'best practices' in the alternative modes. 

As explained in previous sections, packaging is required first because it creates files. While regular inlines also create files, the parser can fill in the gaps by determining which generated classes from the packaging get filled with what data from the regular inputs. 

for example:

`<p:(package1 : classA, moduleA)>`
`ClassA : attr1, attr2 : method1 : -te`

creates a 'ClassA' with the specified members, and assumes that
the extension is:

`ClassA (package1): attr1, attr2 : method1 : -te`

because of the previously provided class file. 

A more problematic example would be:

`ClassA / classB : attr1/attr2, attr3,attr4 : method1 , method2 : -t / -e`
`<p:(package1 : ClassA, ClassB)>`

unless the packaging is explicitly provided and declares that ClassA and ClassB are members of a different package, then a duplicate version of ClassA and ClassB will be created in the [default package](##default-package)



