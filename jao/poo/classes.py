


class Teste():
    def __init__(self):
        self.meta = 100
        self.vendas = 0

    def venda(self, vendas):
        self.vendas = vendas
        print(f"Voce fez um total de {self.vendas} vendas")
        self.bateu_meta()

    def bateu_meta(self):
        if self.vendas > self.meta:
            print("Voce bateu a meta")
        else:
            print("Voce nao bateu a meta")

x = Teste()
x.venda(50)
