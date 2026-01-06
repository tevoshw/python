lista = [1, 3, 2, 9, 10, 20, 34]


print(lista[0])
print(lista[1])
print(lista[2])


for int in lista:
    print(int)


for x in range(len(lista)):
    print(lista[x])


for y in range(len(lista)):
    if lista[y] % 2 == 0:
        print(f"O index {y} é par, e o numero é: {lista[y]}")
    else:
        print(f"O index {y} é impar, e o numero é: {lista[y]}")