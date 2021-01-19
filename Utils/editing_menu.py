"""
Programmer: Ben Sehnert
Program: editing_menu module
Software: Class generator
Date: 1/7/2021

A utility module for getting feedback from a user about the input they provided
displays class specs in a table, allows them to edit, delete indivudal items
or confirm the whole lot.
"""

# print("skonedalone- this file needs to be debugged big time buster!")

# def display_classes(classes):
#     """[summary]

#     Args:
#         classdict ([type]): [description]
#     """
#     print("Review the following before generation.")
#     print("item no:\tclass name:\t\tAttributes:\t\t\t\
# methods:\t\tparent:\t\tpackage:\ttesting:\texporting:")
#     print(
#         "----------------------------------------------------------------------------" + ("----" * 26))
#     # for num, item in enumerate(class_dict):
#     #     print(f"{num + 1}\t  {(ClassDict.from_tuple((item, class_dict[item]))).__str__()}")
#     # return 1
#     for item in enumerate(classes):
#         current_class = classes[item[0]]
#         print(f"{item[0]+1}\t{current_class.__str__()}")

# def quick_exit():
#     response = input(
#         "action complete. Want to return to previous prompt? type y / yes to do so.\n")
#     print("\n\n")
#     if response in ("y", "yes"):
#         return True
#     return False

# def editing_menu(classes, index):
#     """[summary]

#     Args:
#         classes ([type]): [description]
#         index ([type]): [description]
#     """
#     class_index = int(index) - 1
#     selected_class = classes[class_index]
#     loop = True
#     while loop:
#         print(selected_class.__str__())
#         choice = input("e to edit entry\n\
# d to delete entry.\n\
# c to close this prompt:\n")
#         if choice.lower() in ('e', 'edit'):
#             classes[class_index] = edit_main(selected_class)
#             if input("done editing this class?") in ("y","yes"):
#                 loop=False
#         elif choice.lower() in ('d', 'delete', 'del'):
#             if delete_entry(classes, class_index):
#                 loop = False
#         elif choice.lower() in ('c', 'close'):
#             return classes
#         else:
#             print(
#                 "invalid response- valid choices are e/edit, d/delete, c/close")
#             continue
#         #non standard operating procedure to exit this way, so it returns 0 status code.
#     return classes

# def replace_item(old_details):
#     """
#     helps build new ClassDict to replace an old one.

#     allows user to generate a new class dict on the spot.
#     since class name is key in dict, editing that attribute is impossible during runtime.
#     """

#     building_path = input("want to use the old details \
# (attributes, methods, parent, etc) of the class (y/n)?\n\
# (Note that choosing n/no means you will have to provide a new inline to build it from scratch)")
#     if building_path in ("y", "yes"):
#         # need to use validation fn to enforce case correctness here! and below in attr and methods
#         return ClassDict(input("provide a new name for your class:\n"), *old_details)
#     elif building_path in ("n", "no"):
#         # we should use inline.parse here but it
#         # would create a circular import and tight coupling.
#         # we will use interactive mode fns until this is figured out
#         name = input("provide a new name for your class:\n")
#         attributes = input(f"provide attributes for {name},\
# delimiting with ',', or leave blank for no attributes:\n")
#         methods = input(f"provide methods for {name}, delimiting with ',',\
# or leave blank for no methods:\n")
#         if answer := input("any parents? (defaults to 'object')"):
#             parents = answer
#         else:
#             parents = 'object'
#         if answer := input(f"is {name} contained within a package? (defaults to 'root')"):
#             packages = answer
#         else:
#             packages = 'root'
#         if answer := input(f"generate {name} with testing? (defaults to False)"):
#             if answer in ("yes", "y"):
#                 testing = answer
#             else:
#                 testing = ''
#         if answer := input(f"Should we do anything with {name}\
# after generation (options- vsc, send)? (defaults to None)"):
#             if answer in ("yes", "y"):
#                 exporting = answer
#             else:
#                 exporting = ''
#         options = ''
#         if testing:
#             if isinstance(testing, bool):   
#                 options += "-t"
#             else:
#                 options += f"-t{testing}"
#         if exporting:
#             if isinstance(exporting, bool):
#                 options += " -e"
#             else:
#                 options += f" -e{exporting}"
#         return ClassDict(name, attributes, methods, parents, packages, options)

# def edit_main(cls):
#     """Facilitates the editing of classdict members.

#     Returns:
#         self [ClassDict]: the complete class dict after editing.
#     """
#     opts_dict = {1: "classes", 2: "attributes", 3: "methods",
#             4: "parent", 5: "package", 6: "testing/exporting"}
#     while True:
#         print("enter the corresponding number for the detail you want to edit:")
#         print("item no:\toption:")
#         print("-----------------------------")
#         for number, selection in zip(opts_dict, list(opts_dict.values())):
#             print(f"{number}\t\t\t\t\t{selection}")
#         response = input("c/continue at any time to leave the editing prompt.\n")
#         if response in ("c", "continue"):
#             return cls
#         response = int(response)
#         if response in [1, 2, 3, 4, 5, 6]:
#             return edit_prompt(response, cls)

# def edit_prompt(action_number, cls):
#     if action_number < 6 and action_number > 1:
#         new = input("enter the new values for this class field:\n")
#     if action_number == 1:
#         print(
#             "cannot update the class name in place, as it must be immutable\n")
#         while True:
#             restart = input("delete this entry and provide\
# a corrected replacement (y/n)?\n")
#             print("\n\n")
#             if restart in ("y", "yes"):
#                 return replace_item(cls.get_details())
#             elif restart in ("n", "no"):
#                 break
#             else:
#                 print("sorry, didnt understand that action_number")
#     elif action_number == 2:
#         cls.attributes = ClassDict.cleanse(new)
#     elif action_number == 3:
#         cls.methods = ClassDict.cleanse(new)
#     elif action_number == 4:
#         ### should be:
#         # if valid_parent(new):
#         #     cls.parents = new
#         # else:
#         #     print("Invalid new value- parent must be a valid python class identifier")
#         #     return
#         cls.parents = new
#     elif action_number == 5:
#         cls.packages = str(new)
#     elif action_number == 6:
#         testing = input("testing is set to {cls.testing}, flip the switch (y/n)?\n")
#         if testing in ("y", "yes"):
#             cls.testing = not cls.testing
#         exporting = input(f"exporting has been provided the following options:  {cls.exporting},\n\
# modify them (y/n)? switch the flag (set exporting to false) with (s/switch):\n")
#         if exporting in ("y", "yes"):
#             while True:
#                 new_exporting = input("type the options you\
# want to be applied to this class for exporting\n\
# (options- vsc (source code management), send- (ssh or email):\n")
#                 if new_exporting in ("vsc","send", "vsc,send", "vsc, send", "send,vsc", "send, vsc"):
#                     cls.exporting = new_exporting
#                     break
#                 else:
#                     print("didnt recognize your response- provide options\
# matching the syntax: single_option   or  option1,option2")
#         elif exporting in ("s", "send"):
#             cls.exporting = None
#     ######  such a messy function.
#     # no type of validation or second chances for providing input- 
#     # tsk tsk tsk...
#     return cls

# def delete_entry(classes, index):
#     """[summary]

#     Args:
#         classdict ([type]): [description]
#         line ([type]): [description]
#     """
#     # get the dict key as a string
#     if input("are you sure you want to delete this spec?").lower() in ("yes", "y"):
#         del classes[index]
#         return 1
#     return 0

def get_feedback(classes):
    """[summary]
    """
    return "weasels"
#     while True:
#         # helps format output
#         print("\n\n")
#         display_classes(classes)
#         action = input("Type a row's corresponding 'item no' to select it for editing or deletion\n\
# c / continue to continue with generation\n\
# r / reprint to reprint the table\n")
#         valid_responses = [(i + 1) for i in range(len(classes))]
#         if action.lower() in ('c', 'continue'):
#             return classes
#         elif action.lower() in ('r', 'reprint'):
#             continue
#         elif action.lower() not in ('c', 'continue', 'r', 'reprint'):
#             try:
#                 int(action)
#                 if int(action) in valid_responses:
#                     classes = editing_menu(classes, action)
#             except ValueError:
#                 print("Error- input not recognized. valid responses include r,\
# reprint, c, continue, or an existing item no")
#                 continue
#         else:
#             print(
#                 "invalid response- valid choices are c/continue,\
# r/reprint table or a number in the 'item no' col of the table")
