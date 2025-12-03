usuario = "admin"
senha = 1234

usuario_input = input("Digite o nome de usuário: ")

senha_input = int(input("Digite sua senha: "))

if usuario_input == usuario and senha_input == senha:
    print("Login realizado com sucesso")
elif usuario_input != usuario and senha_input != senha:
    print("Ambas informações estão incorretas.")
elif usuario_input != usuario:
    print("Usuário não encontrado.")
elif senha_input != senha:
    print("Senha incorreta.")