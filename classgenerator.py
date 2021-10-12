"""main function for class generator, called at begining of program runtime.
"""
import sys
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
    parsed_inline = options_main()
    # try:
    #     parsed_inline = options_main()
    # except OptionError:
    #     print("could not parse your options. ")
    #     return 0
    for items in parsed_inline:
        class_generator(items)
    return 1

main()
