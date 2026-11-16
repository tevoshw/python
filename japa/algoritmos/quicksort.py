lista = [1, 5, 3, 2, 6, 9]

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        # LIST COMPREHENSION
        menores = [numero for numero in array[1:] if numero <= pivo]
        maiores = [numero for numero in array[1:] if numero > pivo]
        return quickSort(menores) + [pivo] + quickSort(maiores)

print(quickSort(lista))