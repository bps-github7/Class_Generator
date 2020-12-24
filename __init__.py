"""
Programmer: Ben Sehnert
Program: Init file for top level package Class generator software
Date: 12/24/2020
Purpose: initialize environment for program run time, ensures that
the needed sub modules are appeneded to the syspath.
"""

from something import main
import sys


sys.path.insert(0, r"C:\Users\Ben\VsCode\Class_Generator\something.py")

print(something.main())
