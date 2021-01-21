
### Inline Specification
##### index:
* Inline Mini language Full Specification (link)
* 



`ClassA : attr1 / attr2 : method : -t`

##### 1. Inline Mini-Language Full Specifications


`ClassA / ClassB : attrA1/attrA2,attrB1/attrB2 : methodA1/methodA2, methodB1/methodB2 : -te / -e`

* ':' <colon> seperates classname, attributes, methods and optional arguments.

* '/' <forward-slash> seperates the members of an individual classes' fields

* ',' <comma> seperates the different families of members in a multi class spec
    the comma is needed to seperate ClassA's attributes and methods from ClassB's

* '>' <rightward-anglebracket> denotes an inheritance relationship between the
        first operand and the second- in the case of the above example.
        ClassA is ClassB's parent and inherits its attributes and methods (configurable ***)

* '<p:()>' <packaging-syntax> this is how we differentiate file inlines from packaging inlines.

* 'file_identifier(parents) (packages)' <extension> include either parenthesized text block
to specify who the files parents are and where it should be generated.


##### 2 Extensions
Extensions: you can elaborate with your inline spec by providing parent and package with an 'extension'
        
`ClassA(parent1) (packageA) : attr1, attr2, attr3 : method : -te`

creates a 'ClassA' which inherits from 'parent1' and is generated in 'package1'

- No part of the extension is nessecary,
meaning you can include either, neither or both parts

-inside the parenthesized text, commas are used to seperate members
you can include multiple parents and/or packages like this:

`ClassA(parent1,parent2) (packageA,packageB,packageC) : attr1, attr2, attr3 : method : -te`

synopsis:

`class identifier(parent(s,)) (package(s,))`

parents : What file(s), if the file is a class, does it inherit from?
packages: Where should the file be generated?

`ClassA(parent) (package): attr1 / attr2 : method : -t`

note the whitespace seperating the two parenthesized text blocks.

`ClassA(parent1, parent2) (package1, package2) : attr1 / attr2 : method : -t`

if you were to provide only parents
`ClassA(parent1, parent2): attr1 / attr2 : method : -t`

if you were to provide only packages
`ClassA (package1, package2) : attr1 / attr2 : method : -t`

you must respect the adherence to whitespace
in order to delineate parents from packages.
much like you must respect the adherence to
colons to designate where attributes end and methods begin.

NOTE that providing the extension of parents and packaging
is not nessecary but is helpful. without it, classes will 
inherit from object unless told otherwise, and all files
will be generated in the default directory 
(C://project//path//project_name)
unless told otherwise

##### 3 Some Common Inline Examples

basic inline spec: 
`class_name : attrA / attrB / attrC : method1 / method2 : -t`


inline spec with multiple classes:
`classA / classB, ... ClassN : attrA1, attrA2 / attrB1, attrB2 / ... / attrN1, attrN2 : methodA / methodB / ... / methodN : -t -e / -t / ... / -t -e`


inline spec with simple inheritance:
`class1 > class2 : attr1 / attr2 > attr1 / attr2 : methodA > methodB : -t > -e`


inline spec with complex, hierachircal and/or multiple inheritances:
`classA / classB/ classC > classD : A1/ A2/ A3 , B1/ B2/ B3 , C1/ C2/ C3 > D1/ D2/ D3 : Amethod / Bmethod / Cmethod > Dmethod : -e / -e / -t > -e -t`


package structuring with the inline spec

`<p:( package1 / package2 : module1/ class1, module2/ module3)>` 

packaging structuring with multiple tiers (package 1 contains package 2)

`<p:( package1 > package2 : module1 / class1 > module2 / module3)>` 
NOTE that this does not indicate modules1 and class1 are inherited by modules2 and 3.
To do so, an class specifying inline can be used

`<p: (package1 / package 2 > package3 : class1/ class2, class1/ module1 > class3/ class4))>`


##### 4 Optional Arguments

`-t` <testing> generates the file with testing suite
`-e` <exporting> export the class after generation
`-a` <ABC> generate a abstract-base-class
`-m` <module> generate a module (withholding this, generates a class)

1. Append the switch to the end of a single class spec (as the fourth argument, procceding from methods) to apply the switch to ALL file.

`Class_A / Class_B : A1 / A2, B1 / B2  : SMmethod/ CMmethod, method1 : -t -e{comp,send}` 

generated files will be generated with testing and then be compressed and sent via email. (non-specific)

2. or apply it in coordinatation with your identifiers to apply the switch selectively. 


`A/ B/ C: attr1/ _attr2/ __attr3 : SMmethod/ CMmethod / CMmethod2 : -t / / -t`

generates unit testing for classes A and C, but not B.

Elaborate example demonstrating the -m and -a flags

`A/ B/ C: attr1/ _attr2/ __attr3 : SMmethod/ CMmethod / CMmethod2 : -m / -a / -m`

A and C are modules, B is an abstract base class

3. you can include as many switches as needed per file 

`A / B : attrA1 / attrA2, attrB1 / attrB2 : method1 / method2 : -t -m / -e -a`

generates A as a module with testing
B is an abstract base class and will be exported.

NOTE some combinations are not logical and will cause errors,
such as -m -a (module cannot be an abstract base class)


4. you can collapse switches like possible with bash builtins

`my_cool_module : var1, var2, var3 : mycoolfunction : -mte`

generates a module with testing and exporting.

/*
//change//

TODO: Need to make a decision whether or not to eliminate the { optional,arguments} thing
on the end of flags- is cool but would be a huge pain to program

need to revise the numbering label and link to index- and add those above please.

*/



3. note the default/keyword argument dictionary at the end of the -e option.

Withholding any of the arguments in the dictionary deselects them

`-e{vsc}` 
exports with source code management, but not compression or email/ssh send

withhold the keyword dictionary entirely to choose all the options with their default arguments
`-e` 
This switch selects source code management default of initializing a new repo for the project, compression to a .tgz tarball and sending via email

To switch the keyword to an option other than its default, assign a valid choice to it with a string arugment.

`-e{vsc='commit; merge HEAD'}`
assuming the program is aware of the repository and git account in use, runs the supplied commands with git.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Have you made a decision- delete or keep? ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Do you want to do anything with these newly generated packages- compress, send to an email address, init git repo?
* attach this dictionary to the end of the inline for exportation of your class files

`-e{vsc : default = 'git init', comp : default = 'tgz', send : default = '' }`

for:
1. vcs- git init, branch, stage or commit 
2. comp- compression options: tar, tgz, zip 
3. send- email, (ssh in the future) 



for exporting, apply the switch only by name (no keyword argument) to generate the class with each option switched on.

`class A : attr1, attr2 : method : -t -e`
produces ClassA with unittests, version control, compressed and not sent to an email (because default email is blank)

Note that you will need to supply an email address to correctly use the following flag and configuration:
` class A : attr1, attr2, attr3 : method1 : -e{send}` 

no email will be sent if the email address argument is not provided, nor will it work if no viable email account is supplied.

You may either supply an email in the .rc file or supply it at program run time. the program will ask for one if
the send option is provided. Thus, the effective use of this flag and configuration is as follows:

` class A : attr1, attr2, attr3 : method1 : -e{send : 'from: youremail@gmail.com to: example@aol.com' }` 

the parser can infer what type of send option you want to use based on the value you provide for the send key:

The above example will cause the generated classes/packages to be sent from email
whereas the following will use ssh to send the generated classes/packages with ssh:

` class A : attr1, attr2, attr3 : method1 : -e{send : 'username@a:/path/to/destination' }` 

note that any send option will by default have to compress the generated classes for sake of efficiency and avoiding complications. 

... end of section ~ delete until here if additional args are possible with the switches are eliminated ~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~ Withholding arguments ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NOTE: that while the specific arguments after class name are optional
the semi colons fundemental to coherent inlines.
They are needed to designate where one field begins and the other ends.
(exception being optional fields. for example:)

`BiscuitFrontier` 

creates an empty class called 'BiscuitFrontier'

however, to designate it as an abscract base class:

`BiscuitFrontier::-a` 

Meaning, to include only methods or only options, you must
provide the right amount of colons, so that the parser can
identify the correct arguments based on their position in the inline.

`BiscuitFrontier : attr1, attr2` 
    good


`BiscuitFrontier : method1, method2`
`BiscuitFrontier : -a`
    wrong

instead:

`BiscuitFrontier : : method1, method2`

`BiscuitFrontier : : : -a`


##### 6 Inheritance with the Inline Specification

This inline specifies that class2 is a descendant of class1 and inherits any fields or methods unique to the parent class1.

`class1 > class2 : attr1, attr2 > attr1, attr2 : methodA > methodB : -t > -e`

This same syntax applies to packaging inlines. a '>' indicates that the left operand contains the right

`<p:(package1 > package2 : class1 / module1 > class2 / module2)>`


When nessecary, use the basic inline grouping syntax to specify multiple inheritances

`classA, classB, classC > classD : A1, A2, A3 / B1, B2,B3 / C1, C2, C3 > D1, D2, D3 : Amethod / Bmethod / Cmethod > Dmethod`

##### 7 Packaging Inline

The inline spec can also be used to describe a packaging structure, and 
uses all the same tokens as a normal inline. just add the packaging decorator to distinguish:

`<p:( package_name : module_name )>`

`<p:( Package1 : class1/ module1/ class2 / module3 )>`

in practice, you can append a '-m' to files you want to designate as modules like so 

`<p:( Package1 : file1 / file2 -m/ file3 / file4 -m )>`

generates file2 and file4 as a module.

Note these important guidelines
1. If you are generating packaging and regular files in the same session, then generate the packaging first
(failure to do so may result in duplicate files ).
2. using the full extension for regular inlines is reccomended for seamless coordination of these two types
of inlines (this way, the two inlines can work together to create the packaging and files as specificed)

`demonstrate this`

3. you can also use the extension syntax, and this is nescary for multiple inheritances, when it comes to packaging inlines

`<p:(package1 / package2 > package3 (package1) : module1 (package1) / module2 (package2) , ...)>`

the extension is required to tell the parser where each file goes in the packaging hierarchy.

In either case (packaging or regular inlines) the extensions are simply reccomended for seamless generating.
withholding that, the program must ask during run time where each nested package and or file is placed
in the case of a complex packaging structure.

`some more examples of this, showing the inline and the packaging and files it creates`

~~~~~~~~~~~~~~~~~~~~~~~~~ link to: fully fleshed out inline, and package placement ~~~~~~~~~~~~~~~~

### fully fleshed out inline. (not nessecary but you can provide input like:)
 
`ClassA(parent) (package) : attributes : methods : opts`

Please note the difference in whitespace between the parenthesized string that
denotes parent versus package. without one or the other, it would instead look like:

`ClassA (package) : ...`
`ClassB(parent) : ...`

parent parenthesized text always touches the class identifier, much like a function signature or 
python's method for denoting the parent of a class `class Chef(Employee):`

Like noted above, this syntax is NOT nessecary, but may be helpful in some instances.
In all cases, the two examples below will produce the same inheritance hierarchy:

`ClassA > ClassB > ClassC : ...`
`ClassA(object), ClassB(ClassA), ClassC(ClassB) : ...`

To avoid providing the package for a class in parenthesized text:
1. Provide packaging inlines FIRST, then upon generation, the program will ask
   if each class should be generated in a specific package.
2. Do nothing and the classes will be generated in the directory or package where the class generator file was run.

The above practices are commonly manifested in denoting what package
each file in a multiple file inline belong in. like so

assume we have the following packaging structure
/*changes*/
<dir package 1>
    __init__.py
    README.md
    some_module.py
    some_class.py
    <dir package 2>
        __init__.py
        README.md
        some_module.py
        some_class.py
<dir package 3>
    __init__.py
    README.md
    some_module.py
    some_class.py

when the main script is run inside one of the packages, it will create
the generated files there by default, in a sub directory with the project name.

you can override this by configuration(***), or by using packaging part of extension to
denote where the file(s) should be generated.


###### 8 Common examples of Packaging Inlines

`<p:(package1 : classA, ClassB : moduleA : -t/ /-e)>`
creates: 

DIR <package_name>
* __init__.py
* README.md
* classA.py
* classB.py
* moduleA.py




/* changes: eliminate this part of the syntax- outdated... * /
Note that you can nest an inline spec to define package structuring using
the inheritance syntax for classes, where > denotes a child package


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


