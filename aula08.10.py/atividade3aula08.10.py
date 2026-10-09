# Situação-problema

# Uma empresa possui diferentes categorias de funcionários.
# Todos recebem salário, porém a forma de calcular a remuneração mensal varia conforme o cargo.
# Sua missão: representar a estrutura de funcionários de uma empresa por meio de classes.

# Requisitos:

# Crie uma classe geral chamada Funcionario.
# Defina os atributos nome e salario_base.
# Encapsule o salário, impedindo valores negativos.
# Crie duas subclasses: Gerente e Vendedor.
# O gerente recebe o salário-base mais um bônus fixo.
# O vendedor recebe o salário-base mais uma comissão.
# Implemente o método calcular_salario() de maneira diferente em cada classe.
# Crie uma lista de funcionários e mostre o salário final de cada um.

class Funcionario:
    def __init__ (self, nome, salario_base):
        self.nome = nome
        if salario_base >= 0:
            self._salario_base = salario_base
        else: 
            print ("Ação Inválida")
            
class Gerente (Funcionario):
    def __init__ (self, nome, salario_base):
        super().__init__(nome, salario_base)
        self.bonus_fixo = 1000


    def calcular_salario (self):
        print(self._salario_base + self.bonus_fixo)


class Vendedor (Funcionario):
    def __init__ (self, nome, salario_base):
        super ().__init__ (nome, salario_base)
        self.comissao = 0
        
    def adicionar_comissao (self, comissao):
        self.comissao += comissao
        
    def calcular_salario (self):
        print (self._salario_base + self.comissao)
        
lista_funcionarios = [Gerente ("João", 3000), Vendedor ("Pedro", 2000)]

lista_funcionarios[1].adicionar_comissao(3000)

for objetoaleatorio in lista_funcionarios:
    objetoaleatorio.calcular_salario ()        
    