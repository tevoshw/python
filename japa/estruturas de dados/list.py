# substituição de itens
minha_lista = ['ola', 'tudo', 'bem']
minha_lista[0] =  'oi'
print(minha_lista)


# tamanho da lista
lista = [4, 'biscoito', 3.14, True]
print(len(lista))


# .append() é uma estrutura que adiciona item para uma lista
lista.append('loucura')
print(lista)


# .insert() estrutura que adiciona item por meio da posição
presentes = ['computador', 'brinquedo', 'ps4', 'celular']
presentes.insert(0, 'casa')
print(presentes)


# .sort() permite sequenciar os itens de modo crescente ou decrescente
ordem_crescente = [5000, 3000, 1500]
ordem_crescente.sort()
# ordem_crescente.sort(reverse = True), ordem decrescente
print(ordem_crescente)


# estruturas de remoção de itens
sonhos = ['ps5', 'carro', 'celular', 'mendigo']
sonhos.remove('mendigo') # remoção de item pelo conteúdo
del sonhos[3]   # remoção de item pela posição
print(sonhos)


# estrutura que permite "pegar" um item da lista
frutas = ['maçã', 'laranja', 'pitaya', 'macarrão']
comida_de_massa = frutas.pop(-1)
print(frutas)
print(comida_de_massa)