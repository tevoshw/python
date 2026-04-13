def pesquisaBinaria(array, item):
    # baixo e alto acompanham a parte da lista que você está procurando
    baixo = 0
    alto = len(array)-1

    while baixo <= alto: # enquanto não conseguiu achar um único elemento
        meio = int((baixo+alto)/2) # verifica o elemento central
        chute = array[meio]
        if chute == item: # acha o item
            return meio
        if chute < item: # o chute foi baixo
            baixo = meio + 1
        else: # o chute foi alto
            alto = meio - 1
    return None # caso o item não exista

lista_numerica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Encontre o número')
print(lista_numerica)
guess = int(input("Escolha seu número: "))

print(pesquisaBinaria(lista_numerica, guess)) # vai retornar a posição do item na lista