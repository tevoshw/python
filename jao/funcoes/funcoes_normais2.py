def calculadora(um,dois):
    return um + dois
numero = calculadora(7,8)
print(numero)

def hello_world(oi,tchau):
    print(oi + tchau)
hello_world(oi = 5, tchau = 9)


def armazem(a,b,c):
    return a*b*c
print(armazem(2,5,3))


def calcula_nota(x,y):
    media = (x+y)/2
    print(media)
calcula_nota(9,8)

def juncao(x,y,z):
    soma = x + y + z
    print(soma)
juncao("oi","sou","joao")

def geral(nome,idade):
    print(f"Olá, eu sou o {nome} e tenho {idade} anos")
geral("joao",17)
