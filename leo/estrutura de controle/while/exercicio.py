V1 = int(input('Digite um valor: '))
V2 = int(input('Digite outro valor: '))
opcão= 0
print('Escolha uma dessas opções: ')
print('[1] Para somar')
print('[2] Para multiplicar')
print('[3] Para maior')
print('[4] Novos numeros')
print('[5] Sair do programa')
opção=int(input('Qual você irá escolher?: '))
if opção == 1:
     soma= V1+V2
     print(f'a soma entre {V1} + {V2} é igual a {V1+V2}')
elif opção == 2:
   multi= V1*V2
   print (f'A multiplicação entre {V1} x {V2} é igual a {V1*V2}')
elif opção == 3:
    if V1> V2:
        maior = V1
    else:
        maior = V2
        print(f'Entre {V1} e {V2} o maior valor é {V1, V2}')
elif opcão == 4:
    print('Digite os numeros novamente: ')
    V1= int(input('Digite o novo valor: '))
    V2= int(input('digite o outro novo valor: '))
elif opção == 5:
    print('Terminando...')
else:
    print('opção não disponivel')
print('=-='*10)
print('Finalizado! Volte sempre')