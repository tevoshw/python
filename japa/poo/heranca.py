# herança são atributos e métodos passados de uma classe mãe para outras classes
# CLASSE MÃE
class Jogador:
    def __init__(self, altura, velocidade, potencia, precisao):
        self.altura = altura
        self.velocidade = velocidade
        self.forca = potencia
        self.mira = precisao

    def passar(self):
        print('o jogador passou a bola')

    def chutar(self):
        print('o jogador chutou a bola')

# CLASSE FILHA
class Jogador_Goleiro(Jogador):
    def agarrar(self):
        print('o goleiro pulou e agarrou a bola')

class Jogador_Linha(Jogador):
    pass


jogador1 = Jogador_Goleiro(195, 69, 88, 71)
jogador2 = Jogador_Linha(180, 79, 81, 93)
jogador1.passar()
jogador1.agarrar()
jogador2.chutar()
# jogador2.agarrar() ERROR 