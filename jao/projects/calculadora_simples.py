print(" Opção 1: Soma \
 Opção 2: Subtração \
 Opção 3: Multiplicação \
 Opção 4: Divisão \
 Opção 5: Sair")
p1 = input("Escolha alguma das opções acima: ")
if p1 == "1":
    v1 = int(input("Escolha um numero: "))
    v2 = int(input("Escolha outro numero: "))
    print(f"Seu resultado é: {v1+v2}")
elif p1 == "2":
    v1 = int(input("Escolha um numero: "))
    v2 = int(input("Escolha outro numero: "))
    print(f"Seu resultado é: {v1-v2}")
elif p1 == "3":
    v1 = int(input("Escolha um numero: "))
    v2 = int(input("Escolha outro numero: "))
    print(f"Seu resultado é: {v1*v2}")
elif p1 == "4":
    v1 = int(input("Escolha um numero: "))
    v2 = int(input("Escolha outro numero: "))
    if v2 == 0:
        print("Nenhuma divisão é possivel por 0")
    else:
        print(f"Seu resultado é: {v1/v2}")
elif p1 == "5":
    print("Obrigado por usar a calculadora")



