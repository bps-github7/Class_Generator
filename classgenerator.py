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
    print("starting the file generator:")
    print("vvvvvroooooop")
#     try:
#         options = options_main()
#     except (NameError):
#         print("you did not provide a name for your project. this argument is required.")
#         return 0
#     for file in options.inlines:
#         # options.inlines += generate(file)
#         print("")
#     if options.config.exporting:
#         []
#         # export the files
#     print(status_report(options.workflow))
