# EXAMPLE 1

class Animal:
    def som(self):
        print("Animal produz som")

class Gato(Animal):
    def miar(self):
        print("Gato está miando")



gato = Gato()
gato.som()
gato.miar()
# THIS IS A WAY TO USE HERENÇA



# EXAMPLE 2
class Animal2:
    def som(self):
        print("Animal está produzindo som 2")

class Gato2(Animal2):
    def som(self):
        super().som() #  A WAY TO USE METHODS FROM THE FATHER CLASS
        print("Gato está miando 2")

gato2 = Gato2()
gato2.som()
# PYTHON CHOOSE IN THIS CASE gato2.som() WHO FUNCTION GONNA USE, IF IS THE FATHER OR SON CLASS, AND ALWAYS GONNA BE THE CLASS WITH WE INSTANCIENT THE OBJECT, IS THIS CASE Gato2
