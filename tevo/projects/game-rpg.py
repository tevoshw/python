class Personagem:
    def atacar(self, personagem):
        print(f"{personagem.nome} está atacando")

    def status(self, personagem):
        print(f"Nome: {personagem.nome}, Vida: {personagem.vida}, Dano: {personagem.dano}")


class Guerreiro(Personagem):
    def __init__(self):
        self.nome = "Guerreiro"
        self.vida = 200
        self.dano = 0.6
    

    def controle_guerreiro(self):
        resposta_controle_mago = input("GUERREIRO -> O que você deseja fazer ATACAR ou VER STATUS?: ").lower()
        if resposta_controle_mago == "atacar":
            super().atacar(self)
        elif resposta_controle_mago == "status":
            super().status(self)
        else:
            print("Opção não disponível")
   

class Mago(Personagem):
    def __init__(self):
        self.nome = "Mago"
        self.vida = 100
        self.dano = 1.4
    

    def controle_mago(self):
        resposta_controle_mago = input("MAGO -> O que você deseja fazer ATACAR ou VER STATUS?: ").lower()
        if resposta_controle_mago == "atacar":
            super().atacar(self)
        elif resposta_controle_mago == "status":
            super().status(self)
        else:
            print("Opção não disponível")

mago = Mago()
mago.controle_mago()


guerreiro = Guerreiro()
guerreiro.controle_guerreiro()
