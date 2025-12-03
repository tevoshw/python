for x in range (10):
    if x % 3 == 0:
        continue
    print(x)

for x in range (10):
    pass

x = int(input("Digite um número: "))

while True:
    if x > 20:
        print(f"O número escolhido foi: {x}")
        break
    print (x)
    break