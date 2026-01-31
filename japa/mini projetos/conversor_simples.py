print('Olá, bem-vindo ao seu conversor digital')
decisao = input('Você deseja converter algum valor? \nRESPOSTA: ').lower()
if decisao == 'sim':
    medidas = {
        'km': 1000,
        'hm': 100,
        'dam': 10,
        'm': 1,
        'dm': 0.1,
        'cm': 0.01,
        'mm': 0.001
    }

    valor = float(input('Digite o valor a ser convertido: '))
    print('Nosso sistema possui essas medidas: KM - HM - DAM - M - DM - CM - MM')
    unidade_de_entrada = input('Qual seria a unidade de entrada? ').lower()
    unidade_de_saida = input('Qual seria a unidade de saida? ').lower()


    valor_em_metros = valor * medidas[unidade_de_entrada]
    valor_final = valor_em_metros / medidas[unidade_de_saida]

    print('Seu valor foi calculado com sucesso!')
    print(f'O valor de {valor}{unidade_de_entrada} equivale a {valor_final}{unidade_de_saida}')

elif decisao == 'não' or decisao == 'nao':
    print('Beleza, volte quando precisar')
    print('ADEUS')

else:
    print('Sua resposta é inválida para o sistema!')