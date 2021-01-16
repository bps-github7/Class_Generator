#### Class Generator Program: A utillity program written in Python 3.5 that generates class files.
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
In most cases, the program takes a **inline specification** (put a link to section 1.5 on inline specification text) like so:  

`class_name : attr1, _attr2, __attr3 : SMmethod, CMmethod`

The only exception being interactive mode, where you can choose to be walked through building a class, piece by piece.

#### 1.2 OUTPUTS: 
Generates a directory, or series of directories of class files, unit tests, documentation structuring that matches the specifcation provided through input.

#### 1.3 DETAILS: 
Defaults to creation of a new directory, labeled with project name, that contains all generated files. 
    * This directory will be produced as a subdirectory in the same directory where the Class_Generator.py script is run.
    * Options exist to customize the path for output (see 'customization with .rc file' or 'Running in cmd line mode')

##### 1.4 ADDITIONAL: features include:
Allows specification of nested packages, for organization of the generated classes, containing __init__.py and README.md.
  * Note that this overrides the default behaivor of generating files in a new directory created in the current working directory

##### 1.4.1 Syntax for switches within the inline specification:
1. Append the switch to the end of a single class spec to apply the switch to the file.

`class_name : attr1, _attr2, _/_attr3 : SMmethod, CMmethod -t -e{comp,send}` 
generated class will be generated with testing and then be compressed and sent via email.

2. For more complex inline specs, you can apply this technique globally to the package/ generated files (like the above example).
3. Alternatively, you can apply the switch on a class by class basis

`classA -e{send}, classB -t > classC -e{vcs,comp,send} -t : ...`

4. note the default/keyword argument dictionary at the end of the -e option.

Withholding any of the arguments in the dictionary deselects them

`-e{vsc}` 
exports with source code management, but not compression or email/ssh send

withhold the keyword dictionary entirely to choose all the options with their default arguments
`-e` 
This switch selects source code management default of initializing a new repo for the project, compression to a .tgz tarball and sending via email

To switch the keyword to an option other than its default, assign a valid choice to it with a string arugment.

`-e{vsc='commit; merge HEAD'}`
assuming the program is aware of the repository and git account in use, runs the supplied commands with git.

##### 1.4.2 Testing
With use of the `-t` switch, you can generate unit tests for any or all class files.

1. attach this to the end of a multi-class inline for including testing in ALL your class files

`A, B, C : attr1, _attr2, _/_attr3 : SMmethod, CMmethod / CMmethod2 -t`

generates unit testing for all the generated classes A, B and C.

2. or apply at the end of the class identifier to apply testing selectively. 


`A -t, B, C -t : attr1, _attr2, _/_attr3 : SMmethod, CMmethod / CMmethod2`

generates unit testing for classes A and C, but not B.

##### 1.4.3 Exporting
Do you want to do anything with these newly generated packages- compress, send to an email address, init git repo?
* attach this dictionary to the end of the inline for exportation of your class files

`-e{vsc : default = 'git init', comp : default = 'tgz', send : default = '' }`

for:
1. vcs- git init, branch, stage or commit 
2. comp- compression options: tar, tgz, zip 
3. send- email, (ssh in the future) 



for exporting, apply the switch only by name (no keyword argument) to generate the class with each option switched on.

`class A : attr1, attr2 : method -t -e`
produces ClassA with unittests, version control, compressed and not sent to an email (because default email is blank)

Note that you will need to supply an email address to correctly use the following flag and configuration:
` class A : attr1, attr2, attr3 : method1 -e{send}` 

no email will be sent if the email address argument is not provided, nor will it work if no viable email account is supplied.

You may either supply an email in the .rc file or supply it at program run time. the program will ask for one if
the send option is provided. Thus, the effective use of this flag and configuration is as follows:

` class A : attr1, attr2, attr3 : method1 -e{send : 'from: youremail@gmail.com to: example@aol.com' }` 

the parser can infer what type of send option you want to use based on the value you provide for the send key:

The above example will cause the generated classes/packages to be sent from email
whereas the following will use ssh to send the generated classes/packages with ssh:

` class A : attr1, attr2, attr3 : method1 -e{send : 'username@a:/path/to/destination' }` 

note that any send option will by default have to compress the generated classes for sake of efficiency and avoiding complications. 

##### 1.5 Inline Quick reference:
* inline Summary *: the inline spec is used for quick writing of class specs. 
it consists of a single line of text with 1-3 sets of identifiers, delimited by colons, which seperate class names from attributes or methods

##### 1.5.1 Basic Inline Specification:
See the developer notes for full documentation.

You can use the 'inline specification' ( the ClassGen's primary/prefered input ) for
1. specification of classes and their attributes and or fields ( optionally, with multi level or multiple inheritance(s)).
2. specification of packaging within your project.
3. both of these purposes at once

`<identifier -> class name>(,)* : <identifier -> attributes>(,)* : <identifier -> methods>(,)*`

**Throughout these examples, we must keep in mind the following rules...**
1. either attributes or methods can be blank in the inline, but not the class identifier (can't make a nameless class).
2. to leave either attributes or methods blank, include the typical amount of colons but leave the section blank
> ClassA::                    creates a classA with no methods or fields       
> ClassA : : method           creates a classA with only a method
> ClassA : attr1, attr2 :     creates a classA with only attributes      

**the following tokens/ operators have the folllowing meaning in an inline spec:**
* ':' <colon> seperates classname, attributes and methods
* ',' <comma> seperates non grouped identifiers - list of sibling classes, lone list of attributes or methods
* '/' <forward-slash> delimits groups in grouped identifiers-
    `classA, classB : A_attr1, A_attr2 / B_attr1, B_attr2`
    * in this second example, a '/' <forward-slash> is nessecary to denote where class1 attributes end and class2 attributes begin.

**the following demonstrate some of the syntactic feaures of the inline specification:**

basic inline spec: 
`class_name : attrA, attrB, attrC : method1, method2`


inline spec with multiple classes:
`classA, classB, ... ClassN : attrA1, attrA2 / attrB1, attrB2 / ... / attrN1, attrN2 : methodA / methodB / ... / methodN`


inline spec with simple inheritance:
`class1 > class2 : attr1, attr2 > attr1, attr2 : methodA > methodB`


inline spec with complex, hierachircal and/or multiple inheritances:
`classA, classB, classC > classD : A1, A2, A3 / B1, B2,B3 / C1, C2, C3 > D1, D2, D3 : Amethod / Bmethod / Cmethod > Dmethod`


package structuring with the inline spec

`<p: my_project  c: classA >` 
where p: stands for packaging and c: stands for classes

effectively, this inline spec prevents you from having to provide the package/project name upon invoking the program
However, because classA is not provided with a nested inline spec, the class will be uninitialized/unimplemented.

you can nest an inline spec inside each of these arguments for p and c,

`<p: package_name c: (classA, classB, classC : A1, A2 / B1, B2 / C1, C2 : Amethod / Bmethod / Cmethod)>`


## 2) Features:
##### 2.1 all components of PEP8 new style class are generated, including:
* constructor(__init__)
* __str__, __repr__
* header/script stub: `if name == main: ...`

##### 2.2 All classes are generated in new object syntax, meaning
* getters and setters are not implemented by default.
* if the class is specified as 'protected' (by prepending the class name with one or two dashed)
  its attributes will be generated with methods, in accordance with the descriptor protocol.

##### 2.3 the base generator can implement the following:
* multiple inheritance
  * `,` to delimit multiple parents or children 
  
  `classA, classB > classC`  classC inherits from both A and B.

  `classA > classB, classC` classA is a parent of both B and C
  
    more generally: `A, B, C : :` creates a directory with three non-related sibling classes A, B and C inside.


  * `>` to delimit a `parent > child` relationship

    note that the amount of arrows must be strictly equivilent within the class identifier, attribute and methods
    for the inheritance specification to be properly translated into classes. __for example__:

    ` A > B : attr1, attr2 > attr3, attr4` is correct- builds class two classes with two attributes each

    ` A > B > C : attr1, attr2 > attr3, attr4` is ambiguous but works- class C has no attributes to generate

    `A > B > C : attr1 > attr2 > attr3 > attr4` is incorrect, as there are more attribute inheritances
                                                than classes (exception will be thrown) 

    a more complex, instructive example:

    `A, B > C > D, E : attr1, attr2 / attr3, attr4 > attr5 > attr6` again, ambiguous, but the parser can handle this
        generated class E will have no attributes

* in attributes and methods
  * `,` to enumerate members
  * `/` to delimit class groups
  * see the 'notes on inheritance' section for further details.
  * attribute and method inheritance, for children, is performed using pythons default mechanism, using the super() method.

* abstract base classes
  * by prepending ABC to class names
  
  `ABCmonster : attr1,attr2,attr : SMstaticmethod1 `       
  
  This creates an abstract base class called Monster, with 3 attributes and an unimplemented static method `staticmethod1` 

* static methods, class methods
  * by prepending SM or CM to method names

  `classA : attr1,attr2,attr3 : SMmethod1, CMmethod2, method3`
  
  creates a ClassA with 3 methods, a static, class and regular method
 

* Package Structuring within inline specification

The base syntax for defining a package structure where p is the package name and c is the class names

> <p: ( package_name : module_names)>

use forward slash "/" (member delimiting token) to enumerate the modules in a package. like so

> <p: ( sounds : iguana / belt / tire)>

this way, the comma can be used to denote multiple packages in the same inline:

> <p: ( dinosaurs : velociraptor / stegasaurus, lizards : iguana / snake, mamals : human / monkey)>



### TODO: these examples need to be revised per the above noted changes
### ALSO: consider making the inline follow the same convention-
### ++ uniformity, and user comprehension- plus it will more easily be able to be parsed to a dictionary **
> <p: package_name c: (classA, classB, classC : A1, A2 / B1, B2 / C1, C2 : Amethod / Bmethod / Cmethod)>

creates: 

DIR <package_name>
* __init__.py
* README.md
* classA.py
* classB.py
* classC.py


Note that you can nest an inline spec to define package structuring using
the inheritance syntax for classes, where > denotes a child package


`<p: ( audio > sounds, textures ) c: (classA, classB > classC : attrA, attrB / attrC, attrD > attrE, attrF : method1 / method2 > method3)>`

creates: 

DIR audio
* __init__.py
* README.md
* classA.py
* classB.py
* classC.py
* DIR<sounds>
* DIR<textures>

_The interpretter will double back_ and get the specifications for the nested directories,
if all you had provided was their names. You have the option of providing the specification inline,
but this proves to be very cumbersome for a command line argument ( it will surely span multiple lines )

`<p: ( audio > sounds, textures  : ClassD, classE > classF (sounds), classD (textures) : -t -e {vsc, comp, send} / ... >) c: (classA, classB > classC : attrA, attrB / attrC, attrD > attrE, attrF : method1 / method2 > method3)>`

in this case, nesting two inline specs (for both the package structuring and classes) is adventageous for two reasons- the third argument within the packaging inline can be used as a space for designating switches on a class per class basis (rather than providing this info in the first argument of the class inline spec, after a specific identifier).
secondly, we can describe WHERE in the packaging each class will be generated. In the case of the above spec, the generated packaging will look like this:

DIR audio
* __init__.py
* README.md
* classA.py
* classB.py
* classC.py
* DIR<sounds>
  * __init__.py
  * README.md
  * classC.py
* DIR<textures>
  * __init__.py
  * README.md
  * classD.py

* _NOTE:_ that there is not an argument (or functionality) provided for nesting upwards (towards the file system root), or creating a multi package root package (the root of your project having multiple directories- instead, call the program multiple times and generate individual packages in the same directory).

note that the full set of arguments in an inline spec denotes differnent meaning.

packaging: <package structuring> : <class file placement within package structuring> : options for classes - using flag and json argument

classes: <class Identifiers> : <atributes for an individual class (delimted by , and grouped by /)> : <methods for an individual class (delimted by , and grouped by /)>  

careful because your syntax for identifying tokens (in this doc) just narrowly collides with how the packaging structure inline spec looks and works.
## 3) Customization with .rc file:
TODO need to implement functionality for this

## 4) Running in cmd line mode:
* 4.1 interpret the file, passing in the following positional arguments

_double back when the program is finished and replace this_
        
* 4.2  moved to the top of the file/ index

* 4.3 dev note on inheritance:

main inheritance function works recursively to instantiate classes
according to the hierarchy described by passed in arguments

argument list: names, attributes, methods = None, parent = 'object', runs = 0

4.5 note on methods:
method body functionality cannot be implemented due to the limited nature of this small CLI program.
however, all method bodies instantiated via passing in argument via cmd line or input file
will return only the keyword 'NotImplemented' and a auto-generated function stub in adherence to PEP8 standards.

In cmd line mode or by using the file, you can designate a method as static or class method
by prepending SM for static methods or CM for class method to the class name, for example

static methods: SMstatic_method_1, SMthis_is_an_example
class methods: CMclass_method_1, CMyadda_yadda_yadda

doing so will cause the method to be generated in adherence to the typical way these methods are written.
making use of decorator, and a first parameter of cls for class methods

* 4.6 input file for argument
> <Unix>
> $ ./cls_gen example

> <NT>
> $ python cls_gen.py -f example.txt

* <syntax for the input file>

in the input file, seperate inline specifications with a single newline character
(type <ENTER> on most systems while in typing mode)
class, attribute and methods should be delimited with a colon (:)
individual attributes or methods should be delimited with a comma (,)

`
class_1 : attr1, attr2, attr3 : method1, method2, method3
class_2 : attr1, attr2, attr3 : method1, method2, method3
...
class_n : attr1, attr2, attr3 : method1, method2, method3
`
inheritance and method designation follows the same syntax used in traditional cmd line mode

`
class_1, class_2 > class_3 > class_4 : attr1, attr2 / attr3, attr4 > attr5, attr6 > attr7, attr8
class_1 > class_2, class_3, class_4 : attr1, attr2 > attr3, attr4 / attr5, attr6 / attr7, attr8

class_1 : attr1, attr2, attr3 : method_1, method_2, SMmethod_3, CMmethod_4
`
where method 1 and 2 are regular methods, 3 and 4 are static and class methods

## 5) Running in interactive mode
* 5.1 How To:
    * Running in interactive mode is the default user interface when the program is run without arguments or the option -i is used.
* 5.2
    * note that using the -i flag in conjunction with other options. currently will result in errors.

## 6) Specificiations, Developer notes, miscelaneous:

    6.1 files in this software include the following:

    6.2 inheritance specifications

    <parameter: name>
        <type: str>
        <arguments denotes inheritance
        relationship between classes>
    <Desired input: >
        /"parent class 1, parent class 2 , parent class 3
        > child class 1, child class 2, child class 3/"
    <operators: >
        < '>' denotes an inheritance relationship:
            <pre operand members are parents>
            <post operand members are children>
            <note: As of now, specific inheritances are not supported- ALL children will inherit from ALL parents>
        < ',' delimits an individual class name>

    <parameter: attributes>
        <type: str>
        <argument denotes the inheritance
        relation among instance variables>
        <note: total number of classes must be consistent with name argument
        failing to do so will cause certain unexpected errors or production of classes with no instance variables>
    <Desired input: >
        /"P1, P2, P3 / Q1, Q2,Q3/ Y1, Y2, Y3 > A1,A2,A3 / B1,B2,B3 / C1,C2,C3/"
    <Operators: >
        < '>' denotes an inheritance relationship>
        < '/' delimits an individual classes\' attribute list>
        < ',' delimits the attributes in a classes\' attribute list>

    <Parameter: methods = None>
        <type: default = None, passed in = str>
        <argument denotes inheritance relation among methods of the passed in classes>
        <note: syntax behaves identically to method list since multiple methods per class delimited by ',' classes delimited by '/'>
    <desired input: >
        /"P1, SMP2, CMP3 / Q1, Q2,Q3/ Y1, SMY2, CMY3 > CMA1,A2,SMA3 / SMB1,CMB2,B3 / C1,C2,C3/"
    <Operators: >
            < '>' denotes an inheritance relationship>
        < '/' delimits an individual classes\' attribute list>
        < ',' delimits the attributes in a classes\' attribute list>
        < memeber starts with 'CM' Class method>
            < member starts with 'SM' Static method>
    <Dev notes: >
        no way of implementing specific functionality for any classes' methods
        therefore body of any instantiated methods will read 'pass', or 'NotImplemented'

    <parameter: parent = 'object'>
        <type: str>
        <argument denotes who the classes' parents are, by default it is set to object>
    <desired input: >
        /"Parent1, parent2, parent3/"
        < where ',' delimits individual parent class name>

    <parameter: runs = 0>
        <type: int>
        <argument specifies whether the inheritance function has been invoked before
        because it is a recursive, we must shunt unintentional secondary calls to avoid an infinite loop>

    <Syntax semantics>
        <exception list: >
            *difference in numbers of > ',', [] or / indicates there is insufficient classes or attributes to complete generation
            *if there are 3 parent classes (two commas on left of >) but only 1 slash in respective attr list,
            then the respective class can generate with no attributes, or throw an exception
        <developer notes: >
            the key in class dict contains class names, referred to here as class-string
            the value in class dict contains attributes and methods for each class,  reffered to here as attribute-string
        <SYNTAX: >
            "{'class A, class B > child C > ...' : 'attr, attr/ attr, attr > attr > attr', 'regular method, Class method, Static method' }"
            -- TODO: THIS IS OLD, neeeds to get updated with uptodate syntax
            --  > (greter than symbol). designates parent > child relationship: pre op operands are parent class(es), post op operands are child class(es)
            -- , (comma) multiclass inheritance: possible that there are multiple parents or multiple children, these are seperated by comma in class-string
            --[], [] in attribute-string designates attributes (list one) and methods/behaivors (list two). leaving out methods list means the class will generate with init, repr, str, getters and setters only
            --attr prepended by __ will create name mangled attribute.
            -- since comma seperates attributes in first list, / will seperate attribute lists of each parent (exception #2)
            --if the method list is included: regular identifier creates instance method, identifier prepended by CM creates class method,  identifier prepended by SM will create static method



> class_name : attrA, attrB, attrC : method1, method2

> classA, classB, ... ClassN : AttrA1, attrA2 / attrB1, attrB2 / ... / attrN1, attrN2 : methodA / methodB / ... / methodN

* ':' <colon> seperates classname, attributes and methods
* ',' <comma> seperates non grouped arguments - list of sibling classes, lone list of attributes or methods
* '/' <forward-slash> delimits groups in grouped arguments-
    * in the second example it is nessecary to denote where class1 attributes end and class2 attributes begin.

##### 1.5.2 Leaving Arguments Blank in the Specification:
*NOTE:* that you can withhold either sets of fields, but not the class name. to do so, include the standard 2 semicolons, but leave a white space, or no text as argument for the fields you want to not include

* class with no fields

> class_name : : 

or

> class_name::

* class with only attributes

> class_name:attr1,attr2:

* class with only methods

> class_name::method1,method2


##### 1.5.3 Inheritance within the Inline Specification:

This inline specifies that class2 is a descendant of class1 and inherits any fields or methods unique to the parent class1.

> 'class1 > class2 : attr1, attr2 > attr1, attr2 : methodA > methodB'


##### 1.5.4 Multiple Inheritances: 

When nessecary, use the basic inline grouping syntax to specify multiple inheritances

> classA, classB, classC > classD : A1, A2, A3 / B1, B2,B3 / C1, C2, C3 > D1, D2, D3 : Amethod / Bmethod / Cmethod > Dmethod


##### 1.5.5 Package Structuring within inline specification

The base syntax for defining a package structure, where p is the package name and c is the class names

> <p: c:> 

you can either write a name or names delimited by comas,
or supply either or both argumements as inline specs nested inside parentheses.

> <p: package_name c: (classA, classB, classC : A1, A2 / B1, B2 / C1, C2 : Amethod / Bmethod / Cmethod)>

creates: 

DIR <package_name>
* __init__.py
* README.md
* classA.py
* classB.py
* classC.py


Note that you can nest an inline spec to define package structuring using
the inheritance syntax for classes, where > denotes a child package


`<p: ( audio > sounds, textures ) c: (classA, classB > classC : attrA, attrB / attrC, attrD > attrE, attrF : method1 / method2 > method3)>`

creates: 

DIR audio
* __init__.py
* README.md
* classA.py
* classB.py
* classC.py
* DIR<sounds>
* DIR<textures>

_The interpretter will double back_ and get the specifications for the nested directories,
if all you had provided was their names. You have the option of providing the specification inline,
but this proves to be very cumbersome for a command line argument ( it will surely span multiple lines )

`<p: ( audio > sounds, textures  : ClassA, classB > classC (sounds), classD (textures) : -t {ut,cc,st}, -e {email,zip,git} / ... >) c: (classA, classB > classC : attrA, attrB / attrC, attrD > attrE, attrF : method1 / method2 > method3)>`

in this case, nesting two inline specs (for both the package structuring and classes) is adventageous for two reasons- the third argument within the packaging inline can be used as a space for designating switches on a class per class basis (rather than providing this info in the first argument of the class inline spec, after a specific identifier).
secondly, we can describe WHERE in the packaging each class will be generated. In the case of the above spec, the generated packaging will look like this:

DIR audio
* __init__.py
* README.md
* classA.py
* classB.py
* classC.py
* DIR<sounds>
  * __init__.py
  * README.md
  * classC.py
* DIR<textures>
  * __init__.py
  * README.md
  * classD.py

* _NOTE:_ that there is not an argument (or functionality) provided for nesting upwards (towards the file system root), or creating a multi package root package (the root of your project having multiple directories- instead, call the program multiple times and generate individual packages in the same directory).

note that the full set of arguments in an inline spec denotes differnent meaning.

packaging: <package structuring> : <class file placement within package structuring> : options for classes - using flag and json argument

classes: <class Identifiers> : <atributes for an individual class (delimted by , and grouped by /)> : <methods for an individual class (delimted by , and grouped by /)>  

careful because your syntax for identifying tokens (in this doc) just narrowly collides with how the packaging structure inline spec looks and works.