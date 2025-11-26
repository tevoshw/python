# BREAK STOP THE CODE AND ONLY WORKS IN LOOPS CASES


number = 5
number2 = 0

""" WRONG WAY
if number == 5:
    break
"""


for x in range(10):
    if x < number:
        x += 1
        print(x)
    else:
        break

while True:
    if x < number:
        x += 1
        print(x)
    else:
        break




# CONTINUE IGNORES SOMETHING

number = 0
for x in range(11):
    if x % 2 == 0:
        continue
    print(x)

# PASS DO NOTHING, JUST A TEMPORARY THING
for x in range(10):
    pass
    