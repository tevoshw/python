h3 = None
h2 = None
h1 = None

while True:
    alt = int(input("1= Somar 2- Subtrair 3- Multiplicar 4- Dividir 5- Mostrar Histórico 6- Sair\n"))

    if alt == 1:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        print(f"O resultado da soma dos dois valores é: {n1 + n2}")
        resultado = n1 + n2
        h3 = h2
        h2 = h1
        h1 = resultado

    elif alt == 2:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        print(f"O resultado da subtração dos dois valores é: {n1 - n2}")
        resultado = n1 - n2
        h3 = h2
        h2 = h1
        h1 = resultado

    elif alt == 3:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        print(f"O resultado da multiplicação dos dois valores é: {n1 * n2}")
        resultado = n1 * n2
        h3 = h2
        h2 = h1
        h1 = resultado

    elif alt == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        if n2 == 0:
            print("Não é possivel dividir por 0.")
            continue
        else:
            print(f"O resultado da divisão dos dois valores é: {n1 / n2}")
            resultado = n1 / n2

        h3 = h2
        h2 = h1
        h1 = resultado

    elif alt == 5:
        print(f"Histórico 1 = {h1}")
        print(f"Histórico 2 = {h2}")
        print(f"Histórico 3 = {h3}")
        
    elif alt == 6:
        print("Encerrando...")
        break

    else:
        print("Opção inválida. Tente novamente!")
        continue