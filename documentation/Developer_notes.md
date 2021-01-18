
### Im pretty sure this one is very outdated
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


###