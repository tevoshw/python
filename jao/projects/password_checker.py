
def password_checker():
    print("""Hi User! Welcome to our site.
          
""")
    #the code will know if theres an letter or a number, so its not necessesary to put int()
    password = input("""Create you new password to login: 
""")

    if not no_number(password):
            print("Invalid! Your password MUST contain numbers.")

    elif not no_letter(password):
        print("Invalid! Your password MUST contain letters.")
    
    else:
        print("Congratulations! Your password was successfully created.")
        return True
    

def no_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def no_letter(password):
    for char in password:
        if char.isalpha():
            return True
    return False

while True:
    if password_checker():
        break