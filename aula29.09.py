class Animal:
    def __init__(self, reino, filo, classe, familia, genero, especie):  # -------- toda classe precisa de um INICIALIZADOR/CONSTRUTOR (__init__)
        self.reino = reino
        self.filo = filo
        self.classe = classe
        self.familia = familia
        self.genero = genero
        self.especie = especie
        
        
    def emitirSom(self):
        if(self.especie == "Panthera leo"):
            print("Rugir!")


meu_animal = Animal("Animalia", "Chordata", "Mammalia", "Felidae", "genero", "Panthera leo") # ---------- entre parenteses sao os atributos
meu_animal.emitirSom()          # -------------- isso aqui é um METODO!!


