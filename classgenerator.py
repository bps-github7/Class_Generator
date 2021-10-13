"""main function for class generator, called at begining of program runtime.
"""
import sys
from parsing.inline import Inline
sys.path.insert(0,"C:\\Users\\Ben\\VsCode\\python")
# from parsing.inline import Inline
from utils.options import main as options_main
from generation.generator import class_generator

def main() -> int:
    """
    Top level function for getting specs, parsing append generating class.

    Returns:
        int: success/failure signal
        1 = success
        0 = failure
    """
    # parsed_inline = options_main()
    # for items in parsed_inline:
    #     class_generator(items)
    # return 1
    try:
        generate_workflow()
    except Exception:
        print("something bad happened while you were doing the thing")




main()



def generate_workflow():
    try:
        options = options_main()
    except (NameError):
        print("you did not provide a name for your project. this argument is required.")
        return 0
    # for file in options.inlines:
    #     # options.inlines += generate(file)
    #     print("")
    # if options.config.exporting:
    #     []
    #     # export the files
    status_report(options.workflow)


def status_report(workflow):
    """prints a summary of all work to be done in a session. including:
    status | file name | type | members | packages | parents | notes
    ----------------------------------------------------------------
    parsed | classA    | cls  | [...]   | [...]    | [...]   | none
    gen    | classB    | mdl  | ...                          | error (see logs) 

    Args:
        workflow ([type]): [description]

    Returns: 
        1 - failure
        0 - success


    """
    header()
    body(workflow.files)

# need a python  refresher first- isnt there some native way of doing this? with print?
def header():
    print("f{}")

def body(files):
    for f in files:
        print("")