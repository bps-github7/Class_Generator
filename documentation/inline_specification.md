
### Inline Specification
##### index:
1. [Inline Mini-Language Full specification](#Inline-Mini-Language)
2. [Extensions](#Extensions)
3. [Prepend arguments](#Prepend-Arguments)
4. [Optional Aruments](#Optional-Arguments)
4. [Withholding Arguments](#A-note-on-withholding-arguments)
5. [Inheritance](#Inheritance)
7. [Packaging Syntax](#Packaging-Inline-Syntax)
8. [Some Common Inline Examples](#Inline-Examples)

# Inline-Mini-Language

`ClassA : attr1, attr2 : method : -t`

A simple inline for generating a single class

`FileA / FileB : A1,A2/B1,B2 : methodA,method1/ functionA,function2 : -te / -me`

A more complex spec that generates a class and a module.

In all cases:

* ':' <colon> seperates classname, attributes, mAthods and optional arguments.

* ',' <comma> 
    seperates the members of an individual classes' fields, or the members of each family in a multiple inline.

* '/' <forward-slash> seperates the different families of members in a multi class spec.
The comma is needed to seperate ClassA's attributes and methods from ClassB's

* '>' <rightward-anglebracket> denotes an inheritance relationship between the
        first operand and the second. In the above example,
        ClassA is ClassB's parent and inherits its attributes and methods (configurable ***)

* '<p:()>' <packaging-syntax> this is how we differentiate file inlines from packaging inlines. learn about the packaging inline [here](##Packaging-Inline-Syntax)

* 'file_identifier(parents) (packages)' <extension> include either parenthesized text block to specify who the files parents are and where it should be generated (the package(s)).


# Extensions
You can elaborate your inline spec by providing parent and package with an 'extension'
        
`ClassA(parent1) (packageA) : attr1, attr2, attr3 : method : -te`

creates a 'ClassA' which inherits from 'parent1' and is generated in 'package1'

No part of the extension is nessecary,
meaning you can include either, neither or both parts

inside the parenthesized text, commas are used to seperate members.
you can include multiple parents and/or packages like this:

`ClassA(parent1,parent2) (packageA,packageB,packageC) : attr1, attr2, attr3 : method : -te`

Parents : What file(s), if the file is a class, does it inherit from?

Packages: Where should the file be generated?

`ClassA(parent) (package): attr1, attr2 : method : -t`

note the whitespace seperating the two parenthesized text blocks.

`ClassA(parent1, parent2) (package1, package2) : attr1, attr2 : method : -t`

If you were to provide only parents:

`ClassA(parent1, parent2): attr1, attr2 : method : -t`

If you were to provide only packages:

`ClassA (package1, package2) : attr1, attr2 : method : -t`

# Prepend-Arguments

These are small texts you prepend to attributes or methods to declare them as a certain type.

* 'CV' class variable
* 'SM' static method
* 'CM' class method

The default behaivor (no prepend arguments) generates instance 
variables and methods, variables and functions for modules.

### A note on methods and functions
Because of the limited nature of a utility command line tool, we cannot provide any implementation of methods or functions. However, two things can be done to help:

1. The method signature can be provided in the inline, but is not nescessary.

    `class : attributes : method_name(x,y)`

    However, the mandatory arguments 'self' and 'cls' do not need to be provided and will be filled in automatically in any case.

    `class : attributes : method_name(x,y)`

    yields

    `def method_name(self,x,y): ...`

    And in the context of a module:

    `module1 : : function(name, age) : -m`

    yields

    `def function(name, age): ...`

2. A correctly formatted pep8 docstring will be provided by default

3. Both these features can be customized via the .rc file.

# Optional-Arguments
* `-t` <testing> generates the file with testing suite
* `-e` <exporting> export the class after generation
* `-a` <ABC> generate a abstract-base-class
* `-m` <module> generate a module (withholding this, generates a class)

1. Append the switch to the end of a single class spec (as the fourth argument, procceding from methods) to apply the switch to ALL file.

`Class_A / Class_B : A1, A2/ B1, B2  : SMmethod/ CMmethod, method1 : -te` 

Generated files will be generated with testing and then be compressed and sent via email. (non-specific)

2. or apply it in coordinatation with your identifiers to apply the switch selectively. 


`A/ B/ C: attr1/ _attr2/ __attr3 : SMmethod/ CMmethod / CMmethod2 : -t / / -t`

Generates unit testing for classes A and C, but not B (specific).

`A/ B/ C: attr1/ _attr2/ __attr3 : SMmethod/ CMmethod / CMmethod2 : -m / -a / -m`

A and C are modules, B is an abstract base class

3. you can include as many switches as needed per file 

`A / B : attrA1 / attrA2, attrB1 / attrB2 : method1 / method2 : -t -m / -e -a`

Generates A as a module with testing.
B is an abstract base class and will be exported.

__NOTE:__ Some combinations are not logical and will cause errors,
such as `-ma` as a module cannot be an abstract base class.


4. You can collapse switches like possible with bash builtins

`my_cool_module : var1, var2, var3 : mycoolfunction : -mte`

generates a module with testing and exporting.

# A-note-on-withholding-arguments
While the specific arguments after class name are optional,
the semi colons are fundemental to coherent inlines.


They are needed to designate where one field begins and the other ends.

`BiscuitFrontier` 

This creates an empty class called 'BiscuitFrontier'

However, to designate it as an abscract base class:

`BiscuitFrontier:::-a` 

To include only methods or only options, you must
provide the right amount of colons, so that the parser can
identify the correct arguments based on their position in the inline.

`BiscuitFrontier : attr1, attr2` 

Good. This works.


`BiscuitFrontier : method1, method2`


`BiscuitFrontier : -a`

Wrong.

Instead do this:

`BiscuitFrontier : : method1, method2`

`BiscuitFrontier : : : -a`

# Inheritance

This inline specifies that class2 is a descendant of class1 and inherits any fields or methods unique to the parent class1.

`class1 > class2 : attr1, attr2 > attr1, attr2 : methodA > methodB : -t > -e`

This same syntax applies to packaging inlines. A '>' indicates that the left operand contains the right.

`<p:(package1 > package2 : class1 / module1 > class2 / module2)>`


When nessecary, use the basic inline grouping syntax to specify multiple inheritances

`classA, classB, classC > classD : A1, A2, A3 / B1, B2,B3 / C1, C2, C3 > D1, D2, D3 : Amethod / Bmethod / Cmethod > Dmethod`


# Packaging-Inline-Syntax

The inline spec can also be used to describe a packaging structure, and 
uses all the same tokens as a normal inline. Simply add the packaging decorator to distinguish:

`<p:( package_name : module_name )>`

`<p:( Package1 : class1/ module1/ class2 / module3 )>`

in practice, you can append a '-m' to files you want to designate as modules like so 

`<p:( Package1 : file1 / file2 -m/ file3 / file4 -m )>`

This generates file2 and file4 as a module.

Note these important guidelines
1. If you are generating packaging and regular files in the same session, then generate the packaging first
(failure to do so may result in duplicate files ).
2. using the full extension for regular inlines is reccomended for seamless coordination of these two types
of inlines (this way, the two inlines can work together to create the packaging and files as specificed, while avoiding duplicate file generation)

`demonstrate this`

3. you can also use the extension syntax, and this is nescary for multiple inheritances, when it comes to packaging inlines

`<p:(package1 / package2 > package3 (package1) : module1 (package1) / module2 (package2) , ...)>`

The extension is required to tell the parser where each file goes in the packaging hierarchy.

In either case (packaging or regular inlines) the extensions are simply reccomended for seamless generating, when needed.
Withholding that, the program must ask during runtime where each nested package and or file is placed
in the case of a complex packaging structure.

`some more examples of this, showing the inline and the packaging and files it creates`

# Some-Common-Inline-Examples

A basic inline spec: 

`class_name : attrA, attrB, attrC : method1, method2 : -t`

A basic inline with no methods, but options

`ClassA : attr1, attr2 : : -t`

Similarly

`ClassA : : method1`

Optional arguments can always be with withheld, but appropriate colons are needed use them.

`'ClassA : :' = 'ClassA'`


`geometry : : : -tem`

Examples of prepend arguments and passed in method/function signitures

`CreditCard : CVinterest_rate, __account_number : SMcalculate_apr, CMdo_something_else : -t`

`WaffleMaker : : make_waffles(batter, egg, milk)`

`pentagon : var1, var2 : do_a_pentagon_thing(x,y,z) :-m`

Inlines with multiple classes:

`ClassA / ClassB : attr1, attr2 / attr3, attr4 : method1, method2 / method3,method4 : -t / -e`


`classA / classB/ ... ClassN : attrA1, attrA2 / attrB1, attrB2 / ... / attrN1, attrN2 : methodA / methodB / ... / methodN : -t -e / -t / ... / -t -e`


An inline spec with simple inheritance:

`class1 > class2 : attr1, attr2 > attr1, attr2 : methodA > methodB : -t > -e`


An inline spec with complex, hierachircal and/or multiple inheritances:

`classA / classB/ classC > classD : A1, A2, A3/ B1, B2, B3/ C1, C2, C3 > D1, D2, D3 : Amethod/ Bmethod/ Cmethod > Dmethod : -e / -e / -t > -e -t`


package structuring with the inline spec

`<p:( package1 / package2 : module1, class1/ module2, module3)>` 

packaging structuring with multiple tiers (package 1 contains package 2)

`<p:(package1 > package2 : module1, class1 > module2, module3)>` 

__NOTE__: this does not indicate modules1 and class1 are inherited by modules2 and 3. To do so, a regular inline can be used

`<p: (package1 / package 2 > package3 : class1/ class2, class1/ module1 > class3/ class4))>`

Some more packaging examples may be needed here... lots of potential combos


__NOTE__ that the default placement of files is within the first created package.

__NOTE__ if you fail to provide an extension to the files for declaring their package assignemnt, the parser will ask you to provide the name of an existing package, or the name of a package from the current parse.

__NOTE__ that there is not an argument (or functionality) provided for nesting upwards (towards the file system root), or creating a multi package root package (the root of your project having multiple directories- instead, call the program multiple times and generate individual packages in the same directory).

