# declaração da classe
class Biscoito:
    # atributos da classe
    def __init__(self):
        self.temperatura = 59
        self.formato = 'circular'
        self.peso = 8.9


    # métodos
    def Mastigar(self):
        self.mordida = self.peso - 3.5

    def mensagem(self):
        print(f'''O biscoito possuia as seguintes características
                temperatura: {self.temperatura}
                formato: {self.formato}
                peso(anterior da mordida): {self.peso}
                peso(posterior da mordida): {self.mordida}''')


# declaração do objeto
comida = Biscoito()
comida.formato = 'coração' # substituição de um atributo
comida.Mastigar()
print(comida.mensagem())