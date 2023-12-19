from class_item_pedido import ItemPedido
# definição da classe
class Pedido:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor
    def __init__(self, codido_pedido):
        self.__codigo_pedido = codido_pedido
        self.__status = 0  # 0 = aberto, 1 = finalizado/pago
        # criando uma estrutura map em python para armzenar itens do pedido
        self.__itens_pedidos = []
        self.__cliente = None
        self.__funcionario = None

    def adicionar_produto(self, produto, quantidade):
        item_pedido = ItemPedido(produto, quantidade)
        self.__itens_pedidos.append(item_pedido)
    
    @property
    def _status(self):
        return self.__status

    @_status.setter
    def _status(self, value):
        self.__status = value

    @property
    def _codigo_pedido(self):
        return self.__codigo_pedido

    @_codigo_pedido.setter
    def _codigo_pedido(self, value):
        self.__codigo_pedido = value

    @property
    def _endereco_entrega(self):
        return self.__endereco_entrega

    @_endereco_entrega.setter
    def _endereco_entrega(self, value):
        self.__endereco_entrega = value

    @property
    def _itens_pedidos(self):
        return self.__itens_pedidos

    @_itens_pedidos.setter
    def _itens_pedidos(self, value):
        self.__itens_pedidos = value
    
    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario
        
    def adicionar_item_ao_pedido(self, itempedido):
        self.__itens_pedidos.append(itempedido)

    def remover_item_pedido(self, codigo_item):
        if 0 <= codigo_item < len(self._itens_pedidos):
            self._itens_pedidos.pop(codigo_item)
        else:
            print("Item não encontrado.")

    def concluir_pedido(self):
        self._status = 1

    def quantidade_itens_pedido(self):
        return int(len(self.__itens_pedidos))
        # return self.__itens_pedidos.__sizeof__
    
    def calcular_preco_total(self):
        total = 0
        for item in self.__itens_pedidos:
            total += item._preco_item
        return total

    def toString(self):
        str_line = "** INÍCIO DAS INFORMAÇÕES DO PEDIDO **"
        print(str_line, end='\n')
        str_line = "CÓDIGO DO PEDIDO:" + str(self._codigo_pedido)
        print(str_line, end='\t')
        str_line = "STATUS DO PEDIDO:" + \
            str(self._status)  # (0-aberto | 1-finalizado)
        print(str_line, end='\n')
        str_line = "CEP ENDEREÇO PARA ENTREGA:" + \
            str(self._endereco_entrega._cep)
        print(str_line, end='\t')
        str_line = "RUA:" + str(self._endereco_entrega._rua)
        print(str_line, end='\t')
        str_line = "BAIRRO/CIDADE PARA ENTREGA:" + \
            str(self._endereco_entrega._bairro) + "/" + \
            str(self._endereco_entrega._cidade)
        print(str_line, end='\n')
        str_line = "QUANTIDADE DE ITENS DO PEDIDO:" + \
            str(self.quantidade_itens_pedido())
        print(str_line, end='\n')
        dbl_preco_total = 0.0
        for i, item in enumerate(self._itens_pedidos):
            str_line = "\t #ITEM:" + str(i)
            print(str_line, end='\t')
            str_line = "PRODUTO:" + str(item._produto._descricao)
            print(str_line, end='\t')
            str_line = "QTD (#):" + str(item._quantidade)
            print(str_line, end='\t')
            str_line = "SUBTOTAL (R$):" + str(item._preco_item)
            dbl_preco_total += item._preco_item
            print(str_line, end='\n')
        str_line = "PREÇO TOTAL DO PEDIDO:" + str(dbl_preco_total)
        print(str_line, end='\n')
        
         # Adicionar informações do cliente e do funcionário
        if self.__cliente is not None:
            str_line += f"\nCLIENTE: {self.__cliente._nome}"  # Use o atributo correto do cliente
        if self.__funcionario is not None:
            str_line += f"\nFUNCIONÁRIO: {self.__funcionario._nome}"  # Use o atributo correto do funcionário

        str_line += "\n** FIM DAS INFORMAÇÕES DO PEDIDO **"
        return str_line
