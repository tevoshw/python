# LISTS ALLOWS STORE DIFERENTES VALUES, MUTABLES, ORDERED AND DUPLICATE ITENS, USING []


# CREATE A SIMPLE AND PRINT
list1 = ["Hello World", True, 1,]
print(list1)
print(list1[0])

# CHANGE THE VALUES (SIMPLE)
list1[0] = "HelloWorld"
print(list1[0])

# ADD OR REMOVE VALUES 1
list1.append(1.7)
print(list1)

list1.remove(1.7)
print(list1)


# ADD OR REMOVE VALUES BY INDEX
list1.insert(1, 1.7)
print(list1)

list1.pop(1)
print(list1)

# PRINT ALL THE LIST
for x in list1:
    print(x)

# SEE THE LENGHT OF THE LIST
print(len(list1))