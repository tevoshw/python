num = 2
print('\nOperação ternária simples')
print('par\n') if num % 2 == 0 else print('ímpar\n') # expressão if condição else expressão2


# TAMBÉM É POSSÍVEL ENCADEAR EXPRESSÕES CONDICIONAIS, PARA SIMULAR UMA TERCEIRA CONDIÇÃO. ISSO SE DEVE PORQUE OS OPERADOREES TERNPÁRIOS NÃO SUPORTAM A SINTAXE 'elif'
print('Operação ternária encadeada')
nota = 5
resultado = (
    'Excelente' if nota >= 9
    else 'Aprovado' if nota > 5
    else 'Reprovado'
)
print(f'Status: {resultado} \nExperimente mexer na nota e ver as diferentes saídas\n')