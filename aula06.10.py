# AULA SOBRE CLASSES

#class Usuario:
    #def __init__ (self, nome, email, senha):
        #self.nome = nome
        #self._email = email
        #self._senha = senha
        
        

# 1 passo - criar a CLASSE

class Usuario:             
    def __init__ (self, nome, email, senha):
        self._nome = nome  #    coloquei o _ pra tornar "privado"
        self._email = email
        self._senha = senha
        
# passo 2 - PROFESSOR QUER 1 METODO PRA LOGAR

    def logar (self, email, senha):
       if email == self._email and senha == self._senha:
           print ("Acesso Liberado")
       else: 
           print ("Acesso Negado")
       
    


# passo 3 - PROFESSOR QUER 1 METODO PRA ALTERAR SENHA

    def alterarsenha (self, senha_atual, nova_senha):
        if senha_atual != self._senha:
            print ("SENHA ERRADA!")
        if nova_senha == self._senha:
            print ("SENHA IGUAL A ANTERIOR")
        else:
            self._senha = nova_senha 
            print ("SENHA ALTERADA COM SUCESSO!")




# PROFESSOR QUER 1 METODO PRA EXIBIR NOME