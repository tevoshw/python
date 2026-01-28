user_id = input('Digite o seu nome: ')
age = int(input('Digite sua idade: '))
weight = float(input('Seu peso: '))

# dicionários idetificam elementos por nomes e não por números como as listas
pessoas = {'nome': user_id,
           'idade': age,
            'peso': weight,
           }

print(pessoas.keys()) # vai me dar a identificação do elemento
print(pessoas.values()) # vai me dar o valor
print(pessoas.items()) # vai me dar tanto a identificação quanto o valor
print(f'Você se chama {pessoas["nome"]}, possui {pessoas["idade"]} anos e pesa {pessoas["peso"]:.1f}kg')