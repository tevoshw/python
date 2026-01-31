print('Olá bem vindo a sua calculadora digital')
escolha = input('Gostaria de fazer alguns cálculos? ').lower()
if escolha == 'sim':
    while True:
        calculo = str(input('''Que tipo de cálculo você gostaria?
                    1- adição
                    2- subtração
                    3- multiplicação
                    4- divisão
                    5- potenciação
                    6- radiciação
                    Resposta: ''')).lower()
        
        match calculo:
            case '1' | 'adição':
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
                print(f'A soma dos números {num1} e {num2} equivale a {num1+num2:.2f}')
            case '2' | 'subtração':
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
                print(f'A subtração dos números {num1} e {num2} equivale a {num1-num2:.2f}')
            case '3' | 'multiplicação':
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
                print(f'A multiplicação dos números {num1} e {num2} equivale a {num1*num2:.2f}')
            case '4' | 'divisão':
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
                print(f'A divisão dos números {num1} e {num2} equivale a {num1/num2:.2f}')
            case '5' | 'potenciação':
                num1 = int(input('Digite o número base: '))
                num2 = int(input('Digite o expoente: '))
                print(f'A potência de {num1} elevado a {num2} equivale a {num1**num2}')
            case '6' | 'radiciação':
                num1 = int(input('Digite o radicando: '))
                num2 = int(input('Digite o índice da radiciação: '))
                print(f'A radiciação de {num1} equivale a {num1**(1/num2)}')
        
        sim_ou_nao = input('Gostaria de fazer mais contas? ').lower()
        if sim_ou_nao == 'sim':
            pass
        elif sim_ou_nao == 'não' or sim_ou_nao == 'nao':
            print('Entendi, volte quando quiser!')
            break

elif escolha == 'não' or escolha == 'nao':
    print('Ok, estou aqui para ajudar se necessário')

else:
    print('Ops, sua resposta é inválida')