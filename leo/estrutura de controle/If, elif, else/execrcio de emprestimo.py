casa= float(input('Qual o valor da casa?:'))
salário= float(input('salario mesal do comprador: R$'))
anos= int(input('Quantos anos de financiamento?:'))
prestação = casa / (anos*12)
minimo= salário *30/100
print(f'Para pagar a casa de {casa} em {anos}')
print(f'A prestação sera de R${prestação}')
if prestação<=minimo:
    print('Este emprestimo é possivel')
else: 
    print('O emprestimo não sera possivel de ser realizado') 