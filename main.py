"""main function for class generator, called at begining of program runtime.
"""
from parsing.main import main as parse


def main() -> int:
    """
    Top level function for getting specs, parsing append generating class.

    Returns:
        int: success/failure signal
        1 = success
        0 = failure
    """
    parse()
    # generate the class based on the specs
    return 1


main()
