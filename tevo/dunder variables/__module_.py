from main import *

def __module_():
    print("Test from the '__module_.py' ")

if __name__ == "__main__":
    print(__name__)
    print(__module_.__module__)
    print(main.__module__)
    main()