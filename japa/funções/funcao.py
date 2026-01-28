def dobro(a, b, c):
    x = a*2
    y = b*2
    z = c*2
    print(x, y, z)

dobro(5, 2, 4)
dobro(2, 6) # erro pela ausência de um dos parâmetros


# a ausência de um parâmetro não interfere na execução, pois foi explicitado um valor anteriormente
def soma(m=0, n=0):
    s = m + n
    return s

soma1 = soma(3)
soma2 = soma(4, 5)
print(soma1, soma2)



# o * permite ter um número variado de parâmetros
# *args
def numero(*x):
    total = 0
    for num in x:
        total += num
    print(total)

numero(4, 7, 32, 8)
