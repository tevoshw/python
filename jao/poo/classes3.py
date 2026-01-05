
class mercado():
    def __init__(self):
            self.carne = 10
            self.bolacha = 17
            self.salgadinho = 32

    def ver_estoque(self):
            print(f"O estoque de carnes é: {self.carne}, o estoque de bolacha é: {self.bolacha} e o estoque de salgadinho é: {self.salgadinho}")

    def retirar_estoque(self):
            retirar = int(input("""Qual produto você deseja retirar do estoque?
1. carne
2. bolacha
3.salgadinho
"""))
            if retirar == 1:
                ret_carne = int(input("Quantas carnes você deseja retirar do estoque?: "))
                if ret_carne > self.carne:
                    print("Você não pode retirar mais itens do que há no estoque!")
                else:
                    self.carne = self.carne - ret_carne
                    print(f"Você retirou {ret_carne} carnes do estoque")

            elif retirar == 2:
                ret_bolacha = int(input("Quantas bolachas você deseja retirar do estoque?: "))
                if ret_bolacha > self.bolacha:
                    print("Você não pode retirar mais itens do que há no estoque!")
                else:
                    self.bolacha = self.bolacha - ret_bolacha
                    print(f"Você retirou {ret_bolacha} carnes do estoque")

            elif retirar == 3:
                ret_salgadinho = int(input("Quantos salgadinhos você deseja retirar do estoque?: "))
                if ret_salgadinho > self.salgadinho:
                    print("Você não pode retirar mais itens do que há no estoque!")
                else:
                    self.salgadinho = self.salgadinho - ret_salgadinho
                    print(f"Você retirou {ret_salgadinho} carnes do estoque")

            else:
                print("Opção não encontrada!")

x = mercado()
x.ver_estoque()
x.retirar_estoque()
x.ver_estoque()
