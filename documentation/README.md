# File Generator Program
### A utility tool that generates files for python development.
### Developed by Ben P. Sehnert

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

`BiscuitFactory : attr1, _attr2, __attr3, CVattr4 : SMmethod(x), CMmethod(x,y,z), method(height) : -te`

`my_cool_module : some, variables : some(x,y), function(length, height) : -tm`

`undefined_mess : : : -a`

In order of appearance, the following inline specs will create the following files:

1. a class named 'BiscuitFactory' with 3 instance variables, a class variable, a static method, class method, and regular method, generated with a testing suite (unittest and code coverage report) and prepared for exporting by compressing and attaching to an email.
*NOTE: The default behavior is to generate a class*

2. a module called 'my_cool_module' with two variables and two functions, generated with a testing suite. The '-m' flag declares a module. Note that you can pass in either function names alone or their signatures.

3. an abscract base class called 'undefined_mess' with no attributes or methods. The '-a' flag declares an abstract base class

## Output 
Generates a directory, or series of directories of files, unit tests,
documentation structuring that matches the specification provided through input.

### Details 
* Defaults to creating a [default package](#): a new directory, 
labeled with project name, that contains all generated files. 

* With no '--path' argument, the default package will be produced as a subdirectory in the same directory where the script is run.

* You can customize where the output will be generated with 
[command line arguments](#) or the use of [.rc file for customization](#) 


### Inline Quick Reference:
Note this is a light introduction for purpose of providing a basic understanding. For a detailed explanation, see the [full specification](..documentation\inline_specification.md) link does not work

The regular inline generates classes unless instructred otherwise with the '-m' or '-a' flags for modules or abstract-base-classes (interfaces)

### Basic Inline:
`File1 : var1, var2 : function(x,y) : -t`

Consists of a single line of text with 1-4 sets of identifiers and optional arguments, delimited by colons


### Inline generating multiple files:
`ClassA / ClassB : attr1,attr2/ attr3,attr4 : method1 / method2 : -t/-e`

Forward slashes seperate multiple classes, whereas the comma delimits the individual members of each classes fields (seperating the individual attributes per one class)

### Inline with basic inheritance:
`ClassA > ClassB : attr1,attr2 > attr3,attr4 : method1 > method2 : -t > -e`

same rules as the basic inline, except that '>' has been used to indicate a `parent > child` relationship

### Inline with multiple inheritance:

`ClassA / ClassB > ClassC : attr1,attr2/ attr3,attr4 > attr5,attr6 : method1/ method 2 > method3 : -t / -e > -e`

Essentially a Multi-Inline and Inheritance Inline in one- forward slashes and commas still have the same purpose, but in this case, ClassC is a child of both ClassA and ClassB. 

*NOTE the '>'* in attribute, method and option fields __does not__ indicate inheritance relationship between the terms but rather an aid to organization and readability

## Packaging Inline
`<p:(package:module)`

this enhanced Inline follows all the syntax rules of previous examples, but the 'package:module' part only takes these two arguments.

### Simle example
`<p:(package1:file1,file2)>`

### denote a file as  a module with `-m`

`<p:(package1:file1 -m,file2)>`

again, default behavior is to assume the files are classes

### Multiple Packages

`<p:(package1/package2:file1,file2 / file3,file4)`

### Package Containing Other Packages

`<p:(package1 > package2 : file1,file2 > file3)`

### When there are multiple containing packages
you need to declare what package a contained package belongs to

`<p:(package1 / package2 > package3 (package1) : ...)>`

This is only nessecary if it is ambiguous which package a contained package belongs to

If the containing package can be assumed based on position, then this syntax is not needed.

### A multiple-inheritance packaging-inline

`<p:(package1 / package > package3 (package2): file1, file2 / file3, file4 > file5, file6)>`

## Summary: 

1. identifier (class name, attributes and methods)
and optional arguments are seperated by colons

    `Mandatory : optional : optional : optional`

    (link- inline_specification.md/ withholding arguments)

2. use comma to seperate individual attributes, forward slashes to seperat multiple classes, and > to indicate inheritance.

    `ClassA : attr1,attr2 : method1,method2 `

    `ClassA : attr1,attr2 : method1,method2 : -t -e`

3. NOTE: [pre-pend arguments](##prepend-options) exist for applying slight changes to the to-be-generated class:
    * CVattr1   : generates attr1 as a class variable
    * SMmethod1 : generates method1 as a static method
    * CMmethod2 : generates method2 as a Class method

6. The Inline spec is designed to be robust. You can withhold any argument except the class name. However, you need to be sure to include the correct amount of colons so that the correct arguments are parsed.

7. The final area of the inline, following the third colon is for optional arguments (switches) including '-t', '-e', '-m', '-a' for testing, exporting, modules and abstract base classes
    
Rules:

1. either attributes or methods can be blank in the inline, but not the class identifier (can't make a nameless class).

2. to leave either attributes or methods blank, include the typical amount of colons but leave the section blank

    `ClassA::`                                      

    creates a classA with no methods or fields       

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

__note:__ when the main script is run inside one of the packages, it will create
the generated files there by default, in a sub directory with the project name.

you can override this by configuration(***), or by using packaging part of extension to denote where the file(s) should be generated. (link : inline_spec/extensions)

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



