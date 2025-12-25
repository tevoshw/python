saldo = 0
while True:
    opcs = input("""
    1. Saldo atual
    2. Saque
    3. Depósito
    4. Sair
    """)
    if opcs == "1":
        print(f"O seu saldo atual é: {saldo}")
    elif opcs == "2":
        saque = int(input("""Qual quantia deseja sacar?:
 """))
        saldo -= saque
        if saque <= saldo:
            print(f"Foi sacado {saque}R$ da sua conta!")
        else:
            print("O valor  solicitado excede o saldo.")
    elif opcs == "3":
        deposito = int(input("""Qual valor deseja ser depositado?:
 """))
        saldo += deposito
        if deposito <= 50000:
            print(f"A quantia de {deposito}R$ foi depositada com sucesso!")
        else:
            print("O valor desejado excede o limite possível de depósito")
    elif opcs == "4":
        print("Obrigado por usar o caixa bancario!")
        break


    