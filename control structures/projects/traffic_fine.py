# THE SYSTEM RECEIVES A SPEED AND VERIFY IF IT'S IN THE ALLOWED

# Getting the spped
speed = float(input("Enter the speed: "))
speed_limit = 120

if speed > speed_limit:
    print("Fined")
else:
    print("Not fined")