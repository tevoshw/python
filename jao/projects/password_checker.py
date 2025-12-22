def password_checker():
    print("Hi User! Welcome to our site. ")
    #the code will know if theres an letter or a number, so its not necessesary to put int()
    password = input("Create you new password to login: ")
    if not password.isdigit():
        no_number()
    elif not password.isalpha():
        no_char()
    else:
        congratulations()
    


while True:

    def no_number():
        print("Invalid password! Your password must contain numbers.")


    def no_char():
        print("Invalid password! Your password must contain letters.")


    def congratulations():
        print("Congratulations! You password were successfully crated.")


    password_checker()
