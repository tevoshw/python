# THE SYSTEM RECEIVES 3 GRADES AND CALCULATE THE MEDIA TO SHOW IF THE STUDENT PASS OR NOT


# GET THE GRADES
some = 0
for x in range(3):
    grade_student = float(input(f"Enter the {x} grade: "))
    some += grade_student

# Calculate the media of the grades
result_media = some / 3
print(f"The media of the student are: {result_media:.2f}")

# VERIFY IF THE STUDENT PASS OR NOT
if result_media * 10 >= 70:
    print("Congratulations, the student pass!!!!!!")
else:
    print("The student didn't pass :(((")
