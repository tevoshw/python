def add(quantidade = 1):
    quantidade += 1
    print(quantidade)


def add2(quantidade):
    quantidade += 1
    print(quantidade)

add() # NOT ERROR, BECAUSE THE VARIABLE ITS DENIFED LIKE A PARAMETRER
add(500)
# add2() GOES ERRO
add2(500)