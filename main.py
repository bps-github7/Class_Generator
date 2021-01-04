"""main function for class generator, called at begining of program runtime.
"""
from parsing.main import main as parse
from utils.misc_functions import class_generator

def main() -> int:
    """
    Top level function for getting specs, parsing append generating class.

    Returns:
        int: success/failure signal
        1 = success
        0 = failure
    """
    parsed_inline = parse()
    for items in parsed_inline:
        class_generator(items, parsed_inline[items][0], parsed_inline[items][1])
    # class_generator(parsed_inline)
    # generate the class based on the specs
    return 1


main()
