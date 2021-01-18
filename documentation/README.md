#### Class Generator Program: A utillity program written in Python 3.9 that generates class files.
###### Programmer: Ben P. Sehnert   ~   Date: 2/11/2020
1. Usage
2. Features
3. Customization with .rc file
4. Running in command line mode
5. Running in interactive mode
6. Developer notes, miscelaneous, software specifications

## Usage:
_Input of class specifications_ can be provided through three different methods:
1. command line arguments
2. input file(s)
3. interactive mode

#### 1.1 INPUTS:
In most cases, the program takes a **inline specification** 
(put a link to section 1.5 on inline specification text) like so:  

`class_name : attr1, _attr2, __attr3 : SMmethod, CMmethod : -t -e`

The only exception being interactive mode, where you can choose
to be walked through building a class, piece by piece.

#### 1.2 OUTPUTS: 
Generates a directory, or series of directories of class files, unit tests,
documentation structuring that matches the specifcation provided through input.

#### 1.3 DETAILS: 
This program defaults to creating a new directory, labeled with project name, that contains all generated files. 
    * This directory will be produced as a subdirectory in the same directory where the Class_Generator.py script is run.
    * You can custom where the output will be generated with command line arguments or
      the use of .rc file for customization (add link here: see 'customization with .rc file' or 'Running in cmd line mode')

##### 1.4 ADDITIONAL: 
* features include:
    * Generate simple to sophisticated classes and directory (packaging) structuring with a simple, easy to learn and understand syntax.
    * Choice of 3 modes for providing input, ranging from on the go (command line), mass production (input file) and ease of use orieinted, assited (interactive mode)
    * Create multiple, fleshed out classes with a single argument (link - text: see inline specification)
    * Create simple or complex multiple inheritance hierarchies with a single argument (link - text: see inheritance)
    * Create packaging structure/ hierachy with a single argument (link - text: see packaging inline).
    * Easily generate additional files and perform actions with generated classes (link - text: see optional arguments specifications)
    * Easily customize and persist multiple users preferences with .rc file (link - text: see customization with .rc file)


##### 1.5 Inline Quick reference:
Note this is a light introduction for purpose of providing a basic understanding of the Inline.
For a detailed, full specification, see this section (link- inline spec)


__Inline Summary__: the inline spec is used for quick writing of class specs. 
it consists of a single line of text with 1-4 sets of identifiers and optional arguments, delimited by colons,
which seperate class names from attributes or methods. Inline Specification can also be used to produce
design of your packaging structure, with slight adjustments to the syntax.

In short: 

1. identifier (class name, attributes and methods) and optional arguments are seperated by `:` (colons)

> ClassA : attributes : methods
> classA : attributes : methods : -t -e

2. Members of identifier sets (such as multiple attributes or multiple methods) are seperated by `,` (comas)


> ClassA : attr1, attr2 : method1, method2
> classA : attr1, attr2 : method1, method2 : -t -e

3. NOTE: pre-pend arguments exist for applying slight changes to the to-be-generated class:
*ABCClassA : generates ClassA as an abscract Base Class
*SMmethod1 : generates method1 as a static method
*CMmethod2 : generates method2 as a Class method

4. if multiple classes are generated in the same inline- use comas to seperate the class identifier and `/` (forward slash)
    to seperate the sets of multiple identifiers (because comma is already in use seperating individual members)

5. `>` (right carrot) is used to denote a parent child relationship (for both classes and packages)
> ClassA > ClassB : attr1, attr2 > attr3, attr4 : method1 > method2 : -t > -e
> `<p:(package1 > package2 : class1/ class2, class3, module4)>`

5. `<p: ( keys : values)>` is used to describe a packaging structure, where keys are package names and values are
    `/`( forward slash) seperated module/class file identifiers


##### 1.5.1 Basic Inline Specification:

You can use the 'inline specification' ( the ClassGen's primary/prefered input ) for
1. specification of classes and their attributes and or fields ( optionally, with multi level or multiple inheritance(s)).
2. specification of packaging within your project.
3. NOT both of these purposes at once

`<identifier -> class name>(,)* : <identifier -> attributes>(,)* : <identifier -> methods>(,)* : <?-t?{?ut,?cc,?sa}> <-e{}>`

    key:
'*' denotes repition,` attribute(,)*` means there can be N many attributes seperated by commas
'?' denotes optional arguments- `<?-t?{?ut,?cc,?sa}>` means that -t is optional, as well as the curly brackets and enclosed text. (link to optional arguments)

**Throughout these examples, we must keep in mind the following rules...**
1. either attributes or methods can be blank in the inline, but not the class identifier (can't make a nameless class).
2. to leave either attributes or methods blank, include the typical amount of colons but leave the section blank
> ClassA::                                      creates a classA with no methods or fields       
> ClassA : : method                             creates a classA with only a method
> ClassA : attr1, attr2 :                       creates a classA with only attributes

3. the fourth, optional field can always be left out, unless one wants to use these switches/ optional arguments like so:
> ClassA : attr1, attr2 : method1 : -t -e       creates a ClassA with attributes, method and optional arguments for testing and exporting
> ClassA : : : -t -e                            creates a ClassA with only testing and exporting (no attributes or methods)

**the following tokens/ operators have the folllowing meaning in an inline spec:**
* ':' <colon> seperates classname, attributes and methods
* ',' <comma> seperates non grouped identifiers - list of sibling classes, lone list of attributes or methods
* '/' <forward-slash> delimits groups in grouped identifiers-
    `classA, classB : A_attr1, A_attr2 / B_attr1, B_attr2`
    * in this second example, a '/' <forward-slash> is nessecary to denote where class1 attributes end and class2 attributes begin.

see Inline_specifications.md (link to exact line no.) for examples of the mini langauge in use for 
describing classes or packages about to be generated.

## 2) Features:
##### 2.1 all components of PEP8 new style class are generated, including:
* constructor(__init__)
* __str__, __repr__
* header/script stub: `if name == main: ...`

##### 2.2 All classes are generated in new object syntax, meaning
* getters and setters are not implemented by default.
* if the class is specified as 'protected' (by prepending the class name with one or two dashed)
  its attributes will be generated with methods, in accordance with the descriptor protocol.

## 3) Customization with .rc file:
TODO need to implement functionality for this

## 4) Running in cmd line mode:
* 4.1 interpret the file, passing in the following positional arguments

_double back when the program is finished and replace this_
        
* 4.2  moved to the top of the file/ index

* 4.6 input file for argument
> <Unix>
> $ ./cls_gen example

> <NT>
> $ python cls_gen.py -f example.txt

* <syntax for the input file>

in the input file, seperate inline specifications with a single newline character


> class_1 : attr1, attr2, attr3 : method1, method2, method3
> class_2 : attr1, attr2, attr3 : method1, method2, method3
> ...
> class_n : attr1, attr2, attr3 : method1, method2, method3

inheritance and method designation follows the same syntax used in traditional cmd line mode


> class_1, class_2 > class_3 > class_4 : attr1, attr2 / attr3, attr4 > attr5, attr6 > attr7, attr8
> class_1 > class_2, class_3, class_4 : attr1, attr2 > attr3, attr4 / attr5, attr6 / attr7, attr8
> class_1 : attr1, attr2, attr3 : method_1, method_2, SMmethod_3, CMmethod_4


## 5) Running in interactive mode
* 5.1 How To:
    * Running in interactive mode is the default user interface when the program is run without arguments or the option -i is used.
You can either provide inlines to the interactive prompt until done,
or be guided through the process of creating a class or package step by step.