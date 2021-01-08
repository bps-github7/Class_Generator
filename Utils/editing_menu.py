"""
Programmer: Ben Sehnert
Program: editing_menu module
Software: Class generator
Date: 1/7/2021

A utility module for getting feedback from a user about the input they provided
displays class specs in a table, allows them to edit, delete indivudal items
or confirm the whole lot.
"""


def display_classes(classes):
    """[summary]

    Args:
        classdict ([type]): [description]
    """
    print("Review the following before generation.")
    print("item no:\tclass name:\t\tAttributes:\t\t\t\
methods:\t\tparent:\t\tpackage:\ttesting:\texporting:")
    print(
        "----------------------------------------------------------------------------" + ("----" * 26))
    # for num, item in enumerate(class_dict):
    #     print(f"{num + 1}\t  {(ClassDict.from_tuple((item, class_dict[item]))).__str__()}")
    # return 1
    for item in enumerate(classes):
        current_class = classes[item[0]]
        print(f"{item[0]+1}\t{current_class.__str__()}")

def quick_exit():
    response = input(
        "action complete. Want to return to previous prompt? type y / yes to do so.\n")
    print("\n\n")
    if response in ("y", "yes"):
        return True
    return False

def editing_menu(classes, index):
    """[summary]

    Args:
        classes ([type]): [description]
        index ([type]): [description]
    """
    class_index = int(index) - 1
    selected_class = classes[class_index]
    loop = True
    while loop:
        print(selected_class.__str__())
        choice = input("e to edit entry\n\
d to delete entry.\n\
c to close this prompt:\n")
        if choice.lower() in ('e', 'edit'):
            classes[class_index] = selected_class.edit_main()
            if input("done editing this class?") in ("y","yes"):
                loop=False
        elif choice.lower() in ('d', 'delete', 'del'):
            if delete_entry(classes, class_index):
                loop = False
        elif choice.lower() in ('c', 'close'):
            return classes
        else:
            print(
                "invalid response- valid choices are e/edit, d/delete, c/close")
            continue
        #non standard operating procedure to exit this way, so it returns 0 status code.
        return classes

def delete_entry(classes, index):
    """[summary]

    Args:
        classdict ([type]): [description]
        line ([type]): [description]
    """
    # get the dict key as a string
    if input("are you sure you want to delete this spec?").lower() in ("yes", "y"):
        del classes[index]
        return 1
    return 0

def get_feedback(classes):
    """[summary]
    """
    while True:
        # helps format output
        print("\n\n")
        display_classes(classes)
        action = input("Type a row's corresponding 'item no' to select it for editing or deletion\n\
c / continue to continue with generation\n\
r / reprint to reprint the table\n")
        valid_responses = [(i + 1) for i in range(len(classes))]
        if action.lower() in ('c', 'continue'):
            return classes
        elif action.lower() in ('r', 'reprint'):
            continue
        elif action.lower() not in ('c', 'continue', 'r', 'reprint'):
            try:
                int(action)
                if int(action) in valid_responses:
                    classes = editing_menu(classes, action)
            except ValueError:
                print("Error- input not recognized. valid responses include r,\
reprint, c, continue, or an existing item no")
                continue
        else:
            print(
                "invalid response- valid choices are c/continue,\
r/reprint table or a number in the 'item no' col of the table")

