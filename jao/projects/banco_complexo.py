class banco:
  def __init__(self):
    self.saldo = 0
    self.ver_historico = []
        
  def escolha(self):
    while True:
      print("""Bem vindo ao banco inteligente. Foi coddado usando lista, class, def e etc
                """)
      opcs = int(input("""Oque o senhor deseja fazer?
1. Saque
2. Deposito
3. Consultar saldo
4. Ver historico de transações
5. Desligar
"""))
      if opcs == 1:
        qtd_saq = int(input("""Qual quantia o senhor deseja sacar?
"""))
        if qtd_saq > self.saldo:
          print("""Você não pode sacar uma quantia maior do que tem na conta!
                """)
        else:
          self.saldo = self.saldo - qtd_saq
          self.ver_historico.append(f"Saque de {qtd_saq}R$ realizado com sucesso!")
          print(f"""Saque de {qtd_saq} realizado com sucesso!
""")

      elif opcs == 2:
        qtd_dep = int(input("""Qual quantia o senhor deseja depositar?
"""))
        if qtd_dep > 100000:
          print("""Você não pode depositar uma quantia maior do que 100.000R$!
                """)
        else:
          self.saldo = qtd_dep + self.saldo
          self.ver_historico.append(f"Deposito de {qtd_dep}R$ realizado com sucesso!")
          print(f"""Deposito de {qtd_dep} realizado com sucesso!
""")
      elif opcs == 3:
        print(f"O seu saldo é de {self.saldo}R$")

      elif opcs == 4:
        for item in self.ver_historico:
          print(item)
      
      elif opcs == 5:
        print("Obrigado por usar o caixa complexo!")
        break



start = banco()
start.escolha()
