class Mesa:
    def _init_(self, numero_da_mesa):
        self.__numero_da_mesa = numero_da_mesa
        self.__funcionario = None
        self.__pedidos = []

    @property
    def _numero_da_mesa(self):
        return self.__numero_da_mesa

    @_numero_da_mesa.setter
    def _numero_da_mesa(self, value):
        self.__numero_da_mesa = value

    @property
    def _funcionario(self):
        return self.__funcionario

    @_funcionario.setter
    def _funcionario(self, value):
        self.__funcionario = value

    @property
    def _pedidos(self):
        return self.__pedidos

    @_pedidos.setter
    def _pedidos(self, value):
        self.__pedidos = value

    def calcular_preco_total(self):
        total = 0
        for pedido in self.__pedidos:
            total += pedido.calcular_preco(pedido)
        return total