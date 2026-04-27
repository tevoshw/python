
#LISTAR SE FOI POSSIVEL OU NAO BATER A META

class Vendedor():
        def __init__(self, nome):
            self.nome  = nome
            self.vendas = 0

        def vendeu(self, vendas):
            self.vendas = vendas


        def bateu_meta(self, meta):
            if self.vendas > meta:
                print(self.nome, "Bateu a meta")
            else:
                print(self.nome, "Nao Bateu meta")


Vendedores = []
meta = 500

while True:
    nome = str(input("Qual o seu nome:  "))
    vendas = float(input("Quanto voce vendeu:  "))

    v = Vendedor(nome)
    v.vendeu(vendas)
    Vendedores.append(v)

    opcao = str(input("Existe outro vendedor ?(y/n):   "))
    if opcao == "n":
        for v in Vendedores:
                if v.vendas > meta:
                    print(v.nome, "Bateu a meta")
                else:
                       print(v.nome, "Nao Bateu a meta")
        break