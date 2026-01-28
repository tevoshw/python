class ContaBancaria:
    def __init__(self, id, nome, saldo=0 ):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f'ID da conta: {self.id};\nTitular: {self.titular};\nSaldo: R${self.saldo:.2f}'
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'O valor R${valor} foi depositado na sua conta')

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print(f'O valor R${valor} foi sacado da sua conta')
        else:
            print('Permissão negada')

id = int(input('Digite seu id de usuário: '))
titular = str(input('Digite seu nome: '))
saldo = float(input('Digite seu saldo: '))
conta = ContaBancaria(id, titular, saldo)
conta.depositar(400)
conta.sacar(50000000)
conta.sacar(800)
print(conta)