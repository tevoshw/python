# CREATE A SIMPLES BANK ACCOUNT CLASS UTILIZING OBJECT ORIENTED PROGRAMMING CONCEPTS

class BankAccount:
    def __init__(self, saldo, titular):
        self._saldo: float = saldo
        self._titular: str = titular


    def sacar(self, valor):
        self._saldo -= valor
        print(self._saldo)
    def depositar(self, valor):
        self._saldo += valor
        print(self._saldo)
    def mostrar_saldo(self):
        print(self._saldo)


usuario = BankAccount(1000.0, "João Silva")
usuario.sacar(200.0)
usuario.depositar(500.0)
usuario.mostrar_saldo()
