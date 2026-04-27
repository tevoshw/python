# CRIAR UMA LISTAD DE ALUNOS DE QUEM FOI APROVADO OU NAO

class Aluno():
    def __init__(self, nome):
        self.nome = nome
        self.nota = []
    
    def adcionar_nota(self, nota):
        self.nota.append(nota)
    
    def media(self):
        return sum(self.nota)/len(self.nota) 

    def aprovado(self):
       if self.media() >= 7: 
        print(self.nome, "Foi aprovado")
       else:
        print(self.nome, "Foi repovado")
Alunos = []

while True:
    Nome =  str(input("Qual o nome do aluno?: "))
    a = Aluno(Nome)

    Nota1 = float(input("Qual foi sua nota?: "))
    Nota2 = float(input("Qual foi sua nota?: "))

    a.adcionar_nota(Nota1)
    a.adcionar_nota(Nota2)

    a.aprovado()
    Alunos.append(a)


    opcao = str(input("Existe mais alunos?(y/n):  "))
    if opcao == "n":
        for a in Alunos:
            a.aprovado()
        break
