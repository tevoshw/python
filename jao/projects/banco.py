class Banco():
    def __init__(self):
        self.dinheiro = 1000

    def sacar(self):
        quantidade_sacar = int(input("Digite a quantidade de dinheiro que vocẽ deseja sacar: "))
        if quantidade_sacar > self.dinheiro:
            print("Vocẽ não possui esse dinheiro suficiente na sua conta!")
        else:
            self.dinheiro -= quantidade_sacar
            print(f"Seu dinheiro agora é de: {self.dinheiro}")


    def ver_dinheiro(self):
        print(f"O dinheiro disponível na sua conta é de: {self.dinheiro}")
    
    def depositar(self):
        quantidade_depositar = int(input("Digite a quantidade que você deseja depositar: "))
        if quantidade_depositar <= 0:
            print("Você não pode depositar esse valor, por ser 0 ou menor que ele!")
        else:
            self.dinheiro += quantidade_depositar
            print(f"Seu dinheiro agora é de: {self.dinheiro}")





