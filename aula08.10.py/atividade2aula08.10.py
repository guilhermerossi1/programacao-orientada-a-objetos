# Situação-problema

# Uma empresa de mobilidade urbana trabalha com diferentes meios de transporte. Todos possuem identificação e podem se locomover, mas cada transporte funciona de maneira diferente.

# Sua missão: modelar os veículos da empresa.

# Requisitos:

# Crie uma classe chamada Veiculo.

# Defina os atributos modelo e velocidade.

# Encapsule o atributo velocidade, impedindo valores negativos.

# Crie as subclasses Carro e Bicicleta.

# Implemente o método mover() de forma diferente em cada subclasse.

# Crie uma lista contendo veículos de tipos diferentes e execute o método mover() para todos.

# Desafio extra: crie uma classe Moto com seu próprio comportamento.

class Veiculo:
    def __init__ (self, modelo, velocidade):
        self.modelo = modelo
        if velocidade >= 0:
          self._velocidade = velocidade
        else:
            print("Valor inválido");
    def mover (self):
        print ("Movimento Aleatório")
            
class Carro (Veiculo):
    def mover (self):
        print ("Movimento de Carro")

class Bicicleta (Veiculo):
    def mover (self):
        print ("Movimento de Bicicleta")  
        
class Moto (Veiculo):
    def mover (self):
        print ("Movimento de Moto")
    
lista_veiculos = [Carro("Gol",120), Bicicleta("Monark",40), Moto("Biz", 80)]

for item in lista_veiculos:
    item.mover ()        