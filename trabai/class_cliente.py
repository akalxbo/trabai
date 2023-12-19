from class_pessoa import Pessoa

class Cliente(Pessoa):
    
    def __init__(self, nome, cpf, telefone, endereco_entrega, email, data_nascimento, senha):
        super().__init__(nome, cpf, telefone, endereco_entrega, email, data_nascimento)
        self.__senha =senha
    
    @property
    def _senha(self):
        return self.__senha
    
    @_senha.setter 
    def _senha(self,value):
        self.__senha = value
    

    def listagem(self):
        print(f"Cliente:{self._nome}, CPF:{self._cpf}, Tel:{self._telefone}, Email:{self._email}, Nascimento:{self._data_nascimento}, Senha:{self._senha}")
    