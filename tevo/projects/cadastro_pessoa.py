cadastro = []


def registro(**kwargs):
    pessoa = {}

    if 'nome' in kwargs:
        pessoa['nome']  = kwargs['nome']
    if 'idade' in kwargs:
        pessoa['idade']  = kwargs['cidade']
    if 'cidade' in kwargs:
        pessoa['cidade;']  = kwargs['cidade']

    
    cadastro.append(pessoa)
   


for x in range(3):
    nome_input = input("Digite seu nome: ")
    idade_input = int(input("Digite sua idade: "))
    cidade_input = input("Digite sua cidade: ")

    registro(nome = nome_input, idade =  idade_input, cidade =  cidade_input)

for p in cadastro:
        print(p)
