def calculadora():
    print("""Olá! Você está usando a calculadora feita pelo João garoto de programa
          
""")
    num = int(input("""Forneça o primeiro numero: 
"""))
    num2 = int(input("""Forneça o segundo numero: 
"""))
    print("""Opção 1: Soma 
Opção 2: Subtração 
Opção 3: Multiplicação 
Opção 4: Divisão 
Opção 5: Sair""")
    p1 = input("""Escolha alguma das opções acima: 
""")
    if p1 == "1":
        soma(num,num2)
    elif p1 == "2":
        subtracao(num,num2)
    elif p1 == "3":
        multiplicacao(num,num2)
    elif p1 == "4":
        divisao(num,num2)
    elif p1 == "5":
        sair()

def soma(num,num2):
    print(f"O resultado da soma é: {num + num2}")

def subtracao(num,num2):
    print(f"O resultado da subtracao é: {num - num2}")

def multiplicacao(num,num2):
    print(f"O resultado da multiplicacao é: {num * num2}")

def divisao(num,num2):
    while True:
        if num2 or num == 0:
            print("É impossivel dividir um numero por 0!")
        else:
            print(f"O resultado da divisao é: {num/num2}")
            break
    
def sair():
    print("Obrigado por testar a minha calculadora!")

calculadora()