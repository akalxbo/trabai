from class_pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, id, email, telefone, data_nascimento, endereco_entrega):
        super().__init__(nome, cpf, email,  telefone, data_nascimento, endereco_entrega)
        self.__id = id
        
    @property
    def _senha(self):
        return self.__senha

    @_senha.setter
    def _senha(self, value):
        self.__senha = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value  
    
    @property
    def _endereco_entrega(self):
        return self.__endereco_entrega

    @_endereco_entrega.setter
    def _endereco_entrega(self, value):
        self.__endereco_entrega = value
        
    def dadosfuncio(self):
        print(f"Funcionario: {self._nome}, Id: {self._id}, CPF:{self._cpf}, Email:{self._email}, Tel: {self._telefone}, Data de nascimento:{self._data_nascimento}, Senha:{self._senha}")