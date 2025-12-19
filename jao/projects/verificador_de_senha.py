senha = "1234"
tentativas = 3
for x in range(3):
    login = input("Me forneça a sua senha: ")
    if login == senha:
        print("Senha correta! Acesso liberado.")
        break
    else:
        tentativas = tentativas-1
        print(f"Senha incorreta! Voce só tem mais {tentativas} tentativas")
