senha = "1234"
tentativas = 3
#serve para que o codigo rode 3 vezes, ou seja, 3 oportunidades de acertar a senha
for x in range(3):
    #colocar o input dentro de uma variavel para assim poder comparar com a senha correta
    login = input("Me forneça a sua senha: ")
    #compara a senha colocada pelo usuario com a senha correta, assim verificando o certo ou errado
    if login == senha:
        print("Senha correta! Acesso liberado.")
        break
    else:
        #cria um novo significado para a variavel tentativa, onde agora é subtraida por 1, possibilitando colocala no print diminuindo
        tentativas = tentativas-1
        print(f"Senha incorreta! Voce só tem mais {tentativas} tentativas")
