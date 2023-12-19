class Pessoa:
    def __init__(self, nome, cpf, telefone, email, data_nascimento, endereco_entrega):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__data_nascimento = data_nascimento
        self.__email = email
        self.__endereco_entrega = endereco_entrega

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _data_nascimento(self):
        return self.__data_nascimento

    @_data_nascimento.setter
    def _data_nascimento(self, value):
        self.__data_nascimento = value

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

    @property
    def _endereco_entrega(self):
        return self.__endereco_entrega
    
    @_endereco_entrega.setter
    def _endereco_entrega(self, value):
        self.__endereco_entrega = value
