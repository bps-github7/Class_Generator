
### Inline Specification

`ClassA : attr1, attr2 : method : -t`


**the following demonstrate some of the syntactic feaures of the inline specification:**

basic inline spec: 
`class_name : attrA, attrB, attrC : method1, method2 : -t`


inline spec with multiple classes:
`classA, classB, ... ClassN : attrA1, attrA2 / attrB1, attrB2 / ... / attrN1, attrN2 : methodA / methodB / ... / methodN : -t -e / -t / ... / -t -e`


inline spec with simple inheritance:
`class1 > class2 : attr1, attr2 > attr1, attr2 : methodA > methodB : -t > -e`


inline spec with complex, hierachircal and/or multiple inheritances:
`classA, classB, classC > classD : A1, A2, A3 / B1, B2,B3 / C1, C2, C3 > D1, D2, D3 : Amethod / Bmethod / Cmethod > Dmethod : -e / -e / -t > -e -t`


package structuring with the inline spec

`<p:( package1: module1 / class1, package2 : module2, module3)>` 
where p: stands for packaging. Note that the inside of the parentheses
is a key value pair (much like a dictionary) where key is seperated from value
with `:` (colon) and key value pairs are seperated by `,` (comma).

This means that, like the `/`(forward slash) in multiple class containing inlines
The comma is already in use and forward slashes must be employed to specify
multiple classes or modules in the package, and `//`(double forward slashes)
to seperate the border between one package and the next on the same level of the
file system, like so:

`<p: (package1 / package 2 > package3 : class1/ class2 // class1, module1 > class3, class4))>`


# REM: need to revise the numbering label and link to index- and add those above please.

##### 1.4.1 Syntax for switches within the inline specification:
1. Append the switch to the end of a single class spec to apply the switch to the file.

`class_name : attr1, _attr2, _/_attr3 : SMmethod, CMmethod : -t -e{comp,send}` 
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

## Inline Mini-language tokens:

* ':' <colon> seperates classname, attributes and methods
* ',' <comma> seperates non grouped arguments - list of sibling classes, lone list of attributes or methods
* '/' <forward-slash> delimits groups in grouped arguments-
    * in the second example it is nessecary to denote where class1 attributes end and class2 attributes begin.

> ClassA, ClassB : attrA1, attrA2 / attrB1, attrB2 : methodA / methodB

##### 1.5.2 Leaving Arguments Blank in the Specification:
*NOTE:* that you can withhold either sets of fields, but not the class name. to do so, include the standard 2 colons, but leave a white space, or no text as argument for the fields you want to not include

* class with no fields

> class_name : : 

or

> class_name::

* class with only attributes

> class_name:attr1,attr2:

* class with only methods

> class_name::method1,method2

* class with only testing

> class_name:::-t


##### 1.5.3 Inheritance within the Inline Specification:

This inline specifies that class2 is a descendant of class1 and inherits any fields or methods unique to the parent class1.

> 'class1 > class2 : attr1, attr2 > attr1, attr2 : methodA > methodB : -t > -e'


##### 1.5.4 Multiple Inheritances: 

When nessecary, use the basic inline grouping syntax to specify multiple inheritances

> classA, classB, classC > classD : A1, A2, A3 / B1, B2,B3 / C1, C2, C3 > D1, D2, D3 : Amethod / Bmethod / Cmethod > Dmethod


##### 1.5.5 Package Structuring within inline specification

The base syntax for defining a package structure, where p is the package name and c is the class names

> <p: (key : value, key : value)> 

# Need to work on this here to flesh out the packaging inline before implementing it
I think it would be better to allow users to use a simpler- less unlike the already learned Inline spec,
and then behind the scences, transform input to a more digestable data structure like a dict.

TODO outdated - everything below this todo
> <p: (classA, classB, classC : A1, A2 / B1, B2 / C1, C2 : Amethod / Bmethod / Cmethod)>

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


#NOTE TODO very outdated- we have defined a better way to do this.
note that the full set of arguments in an inline spec denotes differnent meaning.

packaging: <package structuring> : <class file placement within package structuring> : options for classes - using flag and json argument

classes: <class Identifiers> : <atributes for an individual class (delimted by , and grouped by /)> : <methods for an individual class (delimted by , and grouped by /)>  

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Another chunk of weasel bisk ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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