from banco import Banco
banco = Banco()
def escolher_opcao():
    opcs = int(input("""Bem vindo ao painel do banco! Oque deseja fazer hoje?
1. Sacar
2. Depositar
3. Ver saldo
"""))
    return opcs

def acoes(escolha):
    if escolha == 1:
        banco.sacar()
    elif escolha == 2:
        banco.depositar()
    elif escolha == 3:
        banco.ver_dinheiro()
    else:
        print("Opcão não disponivel")

    

escolha = escolher_opcao()
acoes(escolha)