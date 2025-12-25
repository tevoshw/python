def main():
    print("Seja bem vindo ao painel da escola!")
    receber()



def calcular_notas(x,y):
    media = (x+y)/2
    print(f"A sua nota é: {media}")


def receber():
    nota1 = int(input("A sua primeira nota foi: "))
    nota2 = int(input("A sua segunda nota foi: "))
    calcular_notas(nota1,nota2)

main()



