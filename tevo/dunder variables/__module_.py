from main_folder import *

def __module_():
    print("Test from the '__module_.py' ")

if __name__ == "__main__":
    print(__name__)
    print(__module_.__module__)
    print(main_folder_function.__module__)
    main_folder_function()