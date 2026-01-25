try:
    user_id = str(input('Cadastre o id do usuário: '))
    password = int(input('Crie uma senha com números: '))
    print(f'O usuário {user_id}, foi cadastrado com sucesso')
except:
    print('senha invalidada')
finally:
    print('É um prazer ti conhecer')