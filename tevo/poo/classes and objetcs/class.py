""" 


vendedor = "Jonh"
vendas = 1000
meta = 600

if vendas > meta:
    print("Bateu a meta")
else:
    print("Não bateu a meta")

    BUT THIS IR FOR LITTLE THINS, IF HAVE OTHER VENDEDOR YOU NEED TO DO THAT AGAIN, AGAIN AND AGAIN.

"""

class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_metas(self, meta):
        if self.vendas > meta:
            print(self.nome, "Bateu a meta")
        else:
            print(self.nome, "Não bateu a meta")

vendedor1 = Vendedor("John")
vendedor1.vendeu(1000)
vendedor1.bateu_metas(600)