while True:

    senha = input("Digite a senha:")

    if senha == "sair":
        break
    elif senha == "admin":
        print("Senha válida!")
        print("Cadastro concluído.")
        break
    elif len(senha) < 6:
        continue