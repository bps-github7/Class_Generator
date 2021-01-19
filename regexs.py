Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> tests = ["example", "example(parent)", "example (package)", "example(parent) (package)", "example(parent1, parent2)", "example (package1, package2)", "example(p1,p2,p3)", "example (p1,p2)"]
>>> tests
['example', 'example(parent)', 'example (package)', 'example(parent) (package)', 'example(parent1, parent2)', 'example (package1, package2)', 'example(p1,p2,p3)', 'example (p1,p2)']
>>> for i in tests:
	print(i)

	
example
example(parent)
example (package)
example(parent) (package)
example(parent1, parent2)
example (package1, package2)
example(p1,p2,p3)
example (p1,p2)
>>> for i in tests:
	if re.match(r"\(\w*\,\s\w*\)\s|\(\w*\)|\(\w*\,\w*\)\s", i):
		print(i)

		
>>> for i in test:
	if re.match(r"\((\w*)\,\s*(\w)*\)", i):
		print(i)

		
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    for i in test:
NameError: name 'test' is not defined
>>> for i in tests:
	if re.match(r"\((\w)*\)|\((\w)*\,\s*(\w)*\)",i):
		print(i)

		
#### We need to get the (parents) (packages) part out of inline class names. 
### this approach using regex is not really working. not sure why. maybe
### design something into the class to help = a version of the class names without
### the extension. what we were trying to do here, but on the fly. 