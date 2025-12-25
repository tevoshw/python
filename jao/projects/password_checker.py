
def password_checker():
    print("""Hi User! Welcome to our site.
          
""")
    #the code will know if theres an letter or a number, so its not necessesary to put int()
    password = input("""Create you new password to login: 
""")

    #if not is verifying in the input if theres an number by the def no_number(password)
    if not no_number(password):
            print("Invalid! Your password MUST contain numbers.")

    #elif not is verifying in the input if theres an letter by the def no_letter(password)
    elif not no_letter(password):
        print("Invalid! Your password MUST contain letters.")
    
    else:
        print("Congratulations! Your password was successfully created.")
        return True
    

def no_number(password):
    for char in password:
        #verifying in every character of the input password if theres an digit, if not return the message, if yes ignores
        if char.isdigit():
            return True
    return False

def no_letter(password):
    for char in password:
        #verifying in every character of the input password if theres an letter, if not return the message, if yes ignores
        if char.isalpha():
            return True
    return False

#this is an loop, while the password dont match with the requirements the code will run
while True:
    if password_checker():
        break