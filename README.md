#### Class Generator Program: A utillity program written in

#### Python 3.8 which automatically generates class files.

###### Programmer: Ben P. Sehnert

###### Date: 2/11/2020

## Index:

    1. Usage
    2. Features
    3. Customization with .rc file
    4. Running in command line mode
    5. Running in interactive mode
    6. Developer notes, miscelaneous, software specifications

## 1) Usage: varies according to user preference.

    -1.1 INPUTS: methods include (1)command line arguments, (2)input file(s) and (3)interactive mode
    -1.2 OUTPUTS: Generates a (optionally nested) directory containing class files, unit tests, documentation structuring.
    -1.3 DETAILS: defaults to creation of a new directory, labeled with project name, that contains
    all generated files. This directory will be produced as a subdirectory in the same directory
    where the Class_Generator.py script is run. Options exist to customize the path for output
    (see 'customization with .rc file' or 'Running in cmd line mode')

    -1.4 ADDITIONAL: features include:
        - allows specification of nested packages, for organization of the generated classes.
            note that this overrides the default behaivor of generating files in a new directory
            created in the current working directory. All new packages are generated with __init__.py
        - testing- with use of a switch, you can generate unit tests for any or all class files.
            the specifics of unittesting can be configured in the .rc file, but
            default to unittests in a parralel sibbling directory with name test_<directory_name> and all classes titled Test_<class_name>
        -exporting- do you want to do anything with these newly generated packages- compress, send to an email address, init git repo?
            need to worry about this feature at the end.

    Quick reference for easy use:

        inline Summary: the inline spec is used for quick writing of class specs. it consists of a single line
        of text with 1-3 sets of identifiers, delimited by colons, which seperate class names from attributes or methods

        class_dict: implementation details- optionally you can use as an Command line argument. but it is cumbersome


        #basic inline

        class_name : attrA, attrB, attrC : method1, method2

        class1, class2, ... ClassN : attr1, attr2 / attr1, attr2 / ... / attr1, attr2 : method / method / ... / method

        # colon seperates classname, attributes and methods
        # comma seperates non grouped arguments - list of sibling classes, lone list of attributes or methods
        # / forward slash delimits groups in grouped arguments- in the second example it is nessecary to denote where class1 attributes end and class2 attributes begin.

        NOTE: that you can withhold either sets of fields, but not the class name. to do so, include the standard 2 semicolons,
        but leave a white space, or no text as argument for the fields you want to not include

        # class with no fields

        class_name : : or class_name::

        # class with only attributes

        class_name:attr1,attr2:

        # class with only methods

        class_name::method1,method2


        # inline with inheritance specifications

        class1 > class2 : attr1, attr2 > attr1, attr2 : methodA > methodB
        # - this inline specifies that class2 is a descendant of class1 and inherits any fields or methods unique to the parent class1.


        #when nessecary, use the basic inline grouping syntax to specify multiple inheritances

        classA, classB, classC > classD : A1, A2, A3 / B1, B2,B3 / C1, C2, C3 > D1, D2, D3 : Amethod / Bmethod / Cmethod > Dmethod


        # specification of package structuring

        <p: c:> is the base syntax for defining a package structure, where p is the package name and c is the class names

        you can either write a name or names delimited by comas, or supply either or both argumements as inline specs nested inside parentheses
        note that you can nest an inline spec to define package structuring using the inheritance syntax for classes, where > denotes a child package



        <p: package_name c: (classA, classB, classC : A1, A2 / B1, B2 / C1, C2 : Amethod / Bmethod / Cmethod)>

        # creates

        DIR <package_name>
        -__init__.py
        -classA.py
        -classB.py
        -classC.py


        <p: ( project_name > sounds, textures ) c: (classA, classB > classC : attrA, attrB / attrC, attrD > attrE, attrF : method1 / method2 > method3)>
        <p: ( project_name > sounds, textures  : ClassA, classB > classC : -t {ut,cc,st}, -e {email,zip,git} / ... >) c: (classA, classB > classC : attrA, attrB / attrC, attrD > attrE, attrF : method1 / method2 > method3)>



        DIR <package_name>
        -__init__.py
        -classA.py
        -classB.py
        -classC.py
        -DIR<sounds>
        -DIR<textures>

        # the interpretter will double back and get the specifications for the nested directories, if all you had provided was their names.
        # You have the option of providing the specification inline, but this proves to be very cumbersome for a command line argument ( it will surely span multiple lines )

        #NOTE: that there is not an argument (or functionality) provided for nesting upwards (towards the file system root)

        alternately, you can nest an inline spec for the packaging structure, and use the inheritance syntax for classes for structuring your

        note that the full set of arguments in an inline spec denotes differnent meaning.

        package structuring : class file placement within package structuring : options for classes - using flag and json argument

## 2) Features:

    2.1 all components of PEP8 new style class are generated, including:
        -constructor(__init__)
        -__str__, __repr__
        -script stub:
    ```
    if __name__ == "__main__":
            print("Running class file. Nothing to do here", {or a customizable message})
    ```
    2.2 All classes are generated in new object syntax, meaning
        getters and setters are not implemented by default.

    if the class is specified as 'protected' (by prepending the class name with one or two dashed)
    its attributes will be generated with methods, in accordance with the descriptor protocol.
    2.3 the base generator can implement the following:
        -multiple inheritance
            commas to delimit multiple parents or children
            > arrow to delimit a parent>child relationship
            -in attributes and methods
                , to enumerate members
                / to delimit class groups
                see the 'notes on inheritance' section for further details.
        -abstract base classes
            -by prepending ABC to class names
        -static methods, class methods
            -by prepending SM or CM to method names

## 3) Customization with .rc file:

    TODO need to implement functionality for this

## 4) Running in cmd line mode:

    4.1 interpret the file, passing in the following positional arguments

        $ python Class_Generator.py --name "my project" -c
        "{'class 1' : ('attrA, attrB, attrC','method1,SMmethod2,CMmethod3') 'class 2': 'attrA, attrB, attrC'}" -d '/some/new/path'

        ^^^this is bad.. see if you can get rid of extra quotation marks among other things
    4.2 Command line mode:

            Optional Arguments:

                -h, --help                  show this message and exist

                -n, --project-name          Provide the name for the project you are creating. Program execution will
                                            create a new directory with the provided name, located in the default directory
                                            to contain newly generated class files.

                -c, --class-and-attr        pass in class information string containing dict SYNTAX: '{ "class_name" : "attr, _attr, __attr",
                                            "ABCclass_name" : 'attr1' #abstract base class , "parentclass_name -> childclass_name" : 'p_attr, p_attr2 -> ...child attributes' #inheritance }'


                -s, --skip-attributes       Use this option to skip defining instance variables for your class.

                -t, --testing               automatically generate unittests, static analysis, code coverage for generated classes

                -e, --exporting             What should be done with the generated project {tgz, zip, tgz and email req arg : 'name@mail.com', zip and email, tgz and ssh, zip and ssh}

    4.3 note on inheritance:

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

    4.6 input file for argument

        <Unix>
        $ ./cls_gen example

        <NT>
        $ python cls_gen.py -f example.txt

        <syntax for the input file>

        in the input file, seperate classes with a single newline character
    (type <ENTER> on most systems while in typing mode)
        class, attribute and methods should be delimited with a colon (:)
        individual attributes or methods should be delimited with a comma (,)

        class_1 : attr1, attr2, attr3 : method1, method2, method3
        class_2 : attr1, attr2, attr3 : method1, method2, method3
        ...
        class_n : attr1, attr2, attr3 : method1, method2, method3

        inheritance and method designation follows the same syntax used in traditional cmd line mode

        class_1, class_2 > class_3 > class_4 : attr1, attr2 / attr3, attr4 > attr5, attr6 > attr7, attr8
        class_1 > class_2, class_3, class_4 : attr1, attr2 > attr3, attr4 / attr5, attr6 / attr7, attr8

        class_1 : attr1, attr2, attr3 : method_1, method_2, SMmethod_3, CMmethod_4 //where method 1 and 2 are regular methods, 3 and 4 are static and class methods

## 5) Running in interactive mode

    5.1 How To:
        Running in interactive mode is the default user interface
        when the program is run without arguments or the option -i is used.
    5.2
        note that using the -i flag in conjunction with other options
        currently will result in errors.

## 6) Specificiations, Developer notes, miscelaneous:

    6.1 files in this software include the following:
        -Misc
        -special_class
        -regular_class
        -options
        -main
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
