"""main function for class generator, called at begining of program runtime.
"""

from parsing.inline import Inline
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
    for items in parsed_inline:
        # if isinstance(items[0], Inline):
        #     print("you got da skone da lone!")

        class_generator(items)
    return 1

main()
