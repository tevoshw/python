# pass serve para ignorar o loop
numero1 = int
for numero1 in range(0, 25):
    pass



# continue irá apenas pular uma etapa
numero2 = int(input('Digite um valor inicial: '))
numero3 = int(input('Digite um valor final: '))
if numero2 < numero3:
    for sequencia in range(numero2, numero3+1):
        if sequencia % 2 == 0:
            continue
        print(sequencia)



# break irá encerrar o loop
for numeros in range(21):
    if numeros == 21:
        break