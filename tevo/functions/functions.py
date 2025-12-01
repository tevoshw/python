# TO USE A FUNCTION IN PYTHON WE USE DEF (), AND WE NEED TO CALL THE FUNCTION NAME()

# FIRST EXAMPLE
def HelloWorld():
    print("Hello World")
HelloWorld()


# SECOND EXAMPLE
def calculator(x,y): # x and y are parameters
    print(x + y)

def receive_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    calculator(num1,num2) # num1 and num2 are arguments

receive_numbers()


# THIRD EXAMPLE
passe = False
def verify_pass(x):
    if x:
        return "Acess garanted"
    else:
        return "Acessed denied"
result = verify_pass(passe) # WHEN WE USE RETURN IN A FUNCTION WE NEED TO USE LIKE A VARIABLE // ARGUMENTS
print(result)

