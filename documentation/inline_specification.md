
### Inline Specification
##### index:
1. [Inline Mini-Language Full specification](#Inline-Mini-Language)
2. [Extensions](#Extensions)
3. [Prepend arguments](#Prepend-Arguments)
4. [Optional Aruments](#Optional-Arguments)
4. [Withholding Arguments](#A-note-on-withholding-arguments)
5. [Inheritance](#Inheritance)
7. [Packaging Syntax](#Packaging-Inline-Syntax)
8. [Some Common Inline Examples](#Some-Common-Inline-Examples)

# Inline-Mini-Language

`ClassA : attr1, attr2 : method : -t`

A simple inline for generating a single class

`FileA / FileB : A1,A2/B1,B2 : methodA,method1/ functionA,function2 : -te / -me`

A more complex spec that generates a class and a module.

In all cases:

* `:` colons seperates classname, attributes, methods and optional arguments.

* `,` commas seperates the members of an individual files' fields.

* `/` forward slashes in all cases reperesents the borders between one file to the next in a inline describing more than one file- Seperates the different 'families' of members: delimiting one files attributes, methods or options from the next files' attributes, methods or options.

* `>` a rightwards-angle-bracket denotes an inheritance relationship between the
        first operand and the second. For example, in
        `ClassA > ClassB`
        ClassB is ClassA's descendent and inherits its attributes and methods. In the context of packaging inlines, `package1 > package2` means that package2 is contained by package1

* `<p:()>` this packaging syntax this is how we differentiate file inlines from packaging inlines. learn about the packaging inline [here](##Packaging-Inline-Syntax)

# Extensions
You can elaborate your inline by providing parent and package with an 'extension'
        
`ClassA(parent1) (packageA) : attr1, attr2, attr3 : method : -te`

Creates a 'ClassA' which inherits from 'parent1' and is generated in 'package1'

No part of the extension is nessecary,
meaning you can include either, neither or both parts

Inside the parenthesized text, commas are used to seperate members.

`ClassA(parent1,parent2) (packageA,packageB,packageC) : attr1, attr2, attr3 : method : -te`

__Note__ the whitespace seperating the two parenthesized text blocks.

If you were to provide only parents, it would look like:

`ClassA(parent1, parent2): attr1, attr2 : method : -t`

If you were to provide only packages, it would look like this instead:

`ClassA (package1, package2) : attr1, attr2 : method : -t`

# Prepend-Arguments

These are small phrases you prepend to attributes or methods to declare them as a certain type.

* 'CV' class variable
* 'SM' static method
* 'CM' class method
* 'FN' function**
* '_' makes a field private
* '__' name mangles a field

The default behaivor (no prepend arguments) generates instance 
variables and methods for classes and variables and functions for modules.

**NOTE: you can coerce a method to a function with 'FN' prepend method.
For example, to generate a main method for your class

`ClassA : attr1, attr2 : method1, method2, FNmain`


### A note on methods and functions
Because of the limited nature of a utility command line tool, we cannot provide any implementation of methods or functions. However, two things can be done to help:

1. The method signature can be provided in the inline, but is not nescessary.

    `class : attributes : method_name(x,y)`

    However, the mandatory arguments 'self' and 'cls' do not need to be provided and will be filled in automatically in any case, based on method type and whether the file is a class or module.

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
* `-t` for testing, generates the file with testing suite
* `-e` for exporting, export the class after generation by compressing and attaching it to an email.
* `-a` generates the file as an abstract-base-class
* `-m` generates the file as a module (withholding this, generates a class)

1. Append the switch to the end of a inline (as the fourth argument, procceding from methods) to apply the switch to ALL file.

`Class_A / Class_B : A1, A2/ B1, B2  : SMmethod/ CMmethod, method1 : -te` 

Generated files will be generated with testing and then be compressed and sent via email. (non-specific)

2. Or apply it in coordinatation with your identifiers to apply the switch selectively. 


`A/ B/ C: attr1/ _attr2/ __attr3 : SMmethod/ CMmethod / method : -t / / -t`

`A/ B/ C: attr1/ _attr2/ __attr3 : SMmethod/ CMmethod / method : -m / -a / -m`

3. you can include as many switches as needed per file 

`A / B : attrA1, attrA2/ attrB1,attrB2 : method1 / method2 : -tm / -ea`

Generates A as a module with testing.
B is an abstract base class and will be exported.

__NOTE:__ Some combinations are not logical and will cause errors,
such as `-ma or (-m -a)` since a module cannot be an abstract base class.


4. You can collapse switches like possible with bash builtins

`my_cool_module : var1, var2, var3 : mycoolfunction : -mte`

This generates a module with testing and exporting.

# A-note-on-withholding-arguments
While the specific arguments after class name are optional,
the semi colons are fundemental to coherent inlines.


They are needed to designate where one field begins and the other ends.

`sailor` 

This creates an empty class called 'Sailor'

However, to designate it as an abscract base class:

`sailor:::-a` 

To include only methods or only options, you must
provide the right amount of colons, so that the parser can
identify the correct arguments based on their position in the inline.

`sailor : attr1, attr2` 

Good. This works.


`BiscuitFrontier : method1, method2`


`BiscuitFrontier : -a`

both examples above are wrong. Instead do this:

`BiscuitFrontier : : method1, method2`

`BiscuitFrontier : : : -a`

# Inheritance

This inline specifies that class2 is a descendant of class1 and inherits any fields or methods unique to the parent class1.

`class1 > class2 : attr1, attr2 > attr1, attr2 : methodA > methodB : -t > -e`

This same syntax applies to packaging inlines. A '>' indicates that the left operand contains the right.

`<p:(package1 > package2 : class1 / module1 > class2 / module2)>`


When nessecary, use the basic inline grouping syntax to specify multiple inheritances

`classA, classB, classC > classD : A1, A2, A3 / B1, B2,B3 / C1, C2, C3 > D1, D2, D3 : Amethod / Bmethod / Cmethod > Dmethod : -t/-e/-t > -e`

__Note:__ the '>' in arguments other than the class identifier are merely required for organizational reasons, it does NOT mean that, in the case of `attr1 > attr2` that 'attr1' inherits a default value (or anything else) from 'attr2'. However, if Classes A, B and C respectivley define unique attributes or methods, these will be
present in ClassD attributes.

# Packaging-Inline-Syntax

Inlines can also be used to describe a packaging structure, and this uses all the same tokens as a normal inline. Simply add the packaging decorator to distinguish it from a regular inline:

`<p:( package_name : module_name )>`

`<p:( Package1/ Package2 : class1, module1/ class2, module3 )>`

in practice, you will have to append an '-m' to files you want to designate as modules like so 

`<p:( Package1 : file1, file2 -m, file3, file4 -m )>`

This generates file2 and file4 as a module. (this switch attached to identifiers is unique to packaging syntax)

__Note these important guidelines:__

1. Using the full extension for regular inlines is reccomended for seamless coordination of these two types
of inlines (this way, the two inlines can work together to create the packaging and files as specificed, while avoiding duplicate file generation)
2. In the cases where the full extension is not provided for a file to be generated, interactive mode will begin and allow you to fill in where
each file should be generated in the packaging structure.


`<p:(package1 / package2 > package3 (package1) : module1 (package1) / module2 (package2) , ...)>`

The extension is required to tell the parser where each file goes in the packaging hierarchy.

In either case (packaging or regular inlines) the extensions are simply reccomended for seamless generating, when needed.
otherwise, the program will need to ask you for additional input in order to determine where files should be generated.

__NOTE__ that there is not an argument (or functionality) provided for nesting upwards (towards the file system root), or creating a multi package root package (the root of your project having multiple directories- instead, call the program multiple times and generate individual packages in the same directory).


# Some-Common-Inline-Examples

Two basic inlines (class and module) : 

`ClassA : attr1, attr2, attr3 : method1, method2 : -t`

`moduleA : var1, var2 : function1 : -tm`

Examples of prepend arguments and passed in method/function signitures

`CreditCard : CVinterest_rate, __account_number : SMcalculate_apr, CMdo_something_else : -t`

`WaffleMaker : : make_waffles(batter, egg, milk), serve_with_bacon(bacon) : -a`

`math : pi, e  : sqrt(x) :-m`

An Inline describing multiple classes:

`ClassA / ClassB : attr1, attr2 / attr3, attr4 : method1, method2 / method3,method4 : -t / -e`

An Inline with simple inheritance:

`class1 > class2 : attr1, attr2 > attr1, attr2 : methodA > methodB : -t > -e`


An inline spec with complex, hierachircal and/or multiple inheritances:

`classA / classB/ classC > classD : A1, A2, A3/ B1, B2, B3/ C1, C2, C3 > D1, D2, D3 : Amethod/ Bmethod/ Cmethod > Dmethod : -e / -e / -t > -e -t`


package structuring with the inline spec

`<p:( package1 / package2 : module1, class1/ module2, module3)>` 

packaging structuring with multiple tiers (package 1 contains package 2)

`<p:(package1 > package2 : module1, class1 > module2, module3)>` 

__NOTE__: this does not indicate modules1 and class1 are inherited by modules2 and 3. To do so, a regular inline can be used

`<p: (package1 / package 2 > package3 : class1, class2/ class3, module1 -m > class4, module2 -m))>`

the default behvaior places package3, the contained package, within the first parent package seen, but this can be overridden by use of an extension (use the parent OR package as either makes sense)

`<p: (package1 / package 2 > package3 (package2) : class1, class2/ class3, module1 -m > class4, module2 -m))>`
