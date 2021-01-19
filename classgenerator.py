"""main function for class generator, called at begining of program runtime.
"""
# # from parsing.class_dict import ClassDict
import sys
sys.path.insert(0,"C:\\Users\\Ben\\VsCode\\python")
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
        # print(items)
        class_generator(items)
    # class_generator(parsed_inline)
    # generate the class based on the specs
    return 1

# for debugging...
# print(main())
main()
