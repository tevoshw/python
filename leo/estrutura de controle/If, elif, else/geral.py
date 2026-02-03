nome = str(input('Qual o seu nome?: '))
if nome =='Leonardo':
    print('Nosaa que nome lindo!')
elif nome == 'João' or nome == 'Estevao' or nome == 'Matheus':
    print('vamos ser amigos.')
elif nome in 'Pedro Maria Fernando Paula':
    print('seu nome é comum')
    print(f'vai embora ent')  
else:
    print(f'bora jogar ent, {nome}')