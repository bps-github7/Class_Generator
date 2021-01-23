#### File Generator Program: A Software Development utility that generates files.
#### Programmer: Ben P. Sehnert
#### Date: 2/11/2020

## Index:
1. Usage
2. Features
3. Customization with .rc file
4. Running in command line mode
5. Running in interactive mode

## Usage:
_Input of class specifications_ can be provided through three different methods:
1. command line arguments
2. input file(s)
3. interactive mode

List all arguments below vvv 

to get to this screen:
`$ python -m classgenerator.py --help`

#### 1.1 INPUTS:
In most cases, the program takes a **inline specification** 
(put a link to section 1.5 on inline specification text)
Here are some quick examples:  

`BiscuitFactory : attr1/ _attr2/ __attr3 : SMmethod/ CMmethod : -t -e`

`my_cool_module : some / variables : some / functions : -t -m`

`undefined_mess : : : -a`

In order of appearance, the following inline specs will create the following files:

1. a class named 'BiscuitFactory' with 3 attributes, a static method, a class method
generated with a testing suite (unittest and code coverage report) and prepared for exporting.
NOTE: The default behavior is to generate a class

2. a module called 'my_cool_module' with 2 variables and 2 functions, generated with a
testing suite. The '-m' flag declares a module.

3. an abscract base class called 'undefined_mess' with no attributes or methods. 
the '-a' flag declares an abstract base class

#### 1.2 OUTPUTS: 
Generates a directory, or series of directories of files, unit tests,
documentation structuring that matches the specification provided through input.

#### 1.3 DETAILS: 
This program defaults to creating a new directory, 
labeled with project name, that contains all generated files. 

* This directory will be produced as a subdirectory in the
 same directory where the script is run.

* You can custom where the output will be generated with command line
arguments or the use of .rc file for customization 
(add link here: see 'customization with .rc file' or 'Running in cmd line mode')

##### 1.4 ADDITIONAL features include:
* Generate simple to sophisticated classes/modules and directory (packaging)
  structuring with a simple, easy to learn and understand syntax.

* Choice of 3 modes for providing input, ranging from on the go (command line),
  mass production (input file) and ease of use orieinted, assited (interactive mode)

* Create multiple, fleshed out classes with a single argument (link: see inline specification)

* Create simple or complex multiple inheritance hierarchies with a single argument (link - text: see inheritance)

* Create packaging structure/ hierachy with a single argument (link - text: see packaging inline).

* Easily generate additional files and perform actions with generated classes (link: see optional arguments)

* Easily customize and persist multiple users preferences with .rc file (link: customization with .rc file)


##### 1.5 Inline Quick Reference:
Note this is a light introduction for purpose of providing a basic understanding
of the Inline. For a detailed, full specification, see this section (link: inline_specification.md)


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

3. NOTE: pre-pend arguments exist for applying slight changes to the to-be-generated class:
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


**the following tokens/ operators have the folllowing meaning in an inline spec:**
* ':' <colon> seperates classname, attributes and methods
* ',' <comma> seperates non grouped identifiers - list of sibling classes, lone list of attributes or methods
* '/' <forward-slash> delimits groups in grouped identifiers-
* '>' <rightwards-anglebracket> denotes an inheritance relationship (parent) > (child)
* '<p:()>' is the encasing membrane for packaging inline.
* '-t -e -m' <optional-flags/switches> Include any of the following as the fourth argument 
                                        in the inline to activate the corresponding option
    * '-t' <testing> automatically generate testing suite with the specified class(es). (**)
    * '-e' <exporting> automatically zip (compress) the specified class and attach it to a blank email (**)
    * '-m' <module> generate a module rather than a class (see- link)
    * '-a' <Abstract-base-class> generate the class as an abstract base class (no implmenetation details) 


    ** testing and exporting will execute the default behaivor noted above, but this can be controlled
    with the .rc file. See the complete Inline spec to learn more about potential behaivors.

`classA, classB : A_attr1, A_attr2 / B_attr1, B_attr2`
* in this example, a '/' <forward-slash> is nessecary to denote where class1 attributes end and class2 attributes begin.

`<p:(package1 : class1,class2,class3)>`
`<p:(package1, package2 : class1, class2 / class3, class4)>`
`<p:(package1 > package2 : class1, class2 > class3, class4)>`
`<p:(package1, package2 > package3 (package1): class1, class2 / class3, module1 > class4)>`
* packages use the same syntax are inlines do in inheritance. The last example
will result in the following directory structuring:

<dir> package1
        <file> class1.py
        <file> class2.py
        <dir> package3
                <file> class4.py
<dir> package2
        <file> class3.py
        <file> module1.py



**Throughout these examples, we must keep in mind the following rules...**
1. either attributes or methods can be blank in the inline, but not the class identifier (can't make a nameless class).
2. to leave either attributes or methods blank, include the typical amount of colons but leave the section blank
> ClassA::                                      creates a classA with no methods or fields       
> ClassA : : method                             creates a classA with only a method
> ClassA : attr1, attr2 :                       creates a classA with only attributes

3. the fourth, optional field can always be left out, unless one wants to use these switches/ optional arguments like so:
> ClassA : attr1, attr2 : method1 : -t -e       creates a ClassA with attributes, method and optional arguments for testing and exporting
> ClassA : : : -t -e                            creates a ClassA with only testing and exporting (no attributes or methods)


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