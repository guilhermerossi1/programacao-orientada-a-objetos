# ATIVIDADE 08.10 - POO

# Situação-problema

#Um pet shop deseja desenvolver um sistema simples para cadastrar diferentes tipos de animais. Cada animal possui características comuns, mas apresenta comportamentos específicos.
#Sua missão: criar uma representação desses animais utilizando classes em Python.

#Requisitos:

#Crie uma classe geral chamada Animal.
#Defina os atributos nome e idade.
#Proteja o atributo nome contra acesso direto.
#Crie as classes Cachorro e Gato, herdando de Animal.
#Implemente o método emitir_som() com um comportamento diferente para cada animal.
#Crie pelo menos um cachorro e um gato e apresente seus sons.


class Animal:
    def __init__ (self, nome, idade):
        self._nome = nome
        self.idade = idade
    def emitir_som (self):
        print ("som_generico")
        
class Cachorro (Animal):
    def emitir_som (self):
        print ("auau")

class Gato (Animal):
    def emitir_som (self):
        print ("miaumiau")
        
meu_cachorro = Cachorro ("Trovão", "3 anos")

meu_gato = Gato ("Belo", "1 ano")

meu_cachorro.emitir_som ()
meu_gato.emitir_som ()

