# PROJETO BANCO DE DADOS 

usuarios = []

def input_usuario():
    escolha_usuario_menu = int(input("Qual opção você deseja selecionar?: "))
    return escolha_usuario_menu
    

def cadastrar():
    nome = input("Digite seu nome: ").lower()
    idade = int(input("Digite sua idade: "))

    # ADICIONAR MAIS COISAS AQUI COMO PROFISSÃO, CIDADE E ETC
    cria_valores_no_banco_de_dados = {  "Nome": f"{nome}",
                        "Idade": f"{idade}"}
    usuarios.append(cria_valores_no_banco_de_dados)

def listar_usuarios(usuarios):
    print("Listando todo os usuários: ")
    for pessoa in usuarios:
        print(f"Nome: {pessoa["Nome"]}, Idade: {pessoa["Idade"]}")    


def buscar_usuarios(usuarios):
    procurar_usuario_especifico = input("Qual usuário você deseja procurar?: ")
    for pessoa in usuarios:
        if pessoa["Nome"] == procurar_usuario_especifico:
            print(f"Usuário encontrado!!")
            for chave, valor in pessoa.items():
                print(f"{chave}: {valor}")
        else:
            print("Usuário não encontrado")
    
def menu():
    # MENU PARA SELECIONAR OPÇÃO

    mensagem = """                    1 - ADICIONAR PESSOAS
                    2 - LISTAR PESSOAS
                    3 - BUSCAR PESSOAS
                    4 - SAIR        """
    
    print(mensagem)


def main():
    menu()
    escolha_usuario_menu = input_usuario()

    match escolha_usuario_menu:
        case 1:
            cadastrar()
            main()
        case 2:
            listar_usuarios(usuarios)
            main()
        case 3:
            buscar_usuarios(usuarios)
            main()
        case 4:
            print("Encerrando programa...")




main()

