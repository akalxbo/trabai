from class_endereco import Endereco
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_produto import Produto
from class_cliente import Cliente
from class_funcionario import Funcionario
from class_nota_fiscal import NotaFiscal
from datetime import datetime

clientes = []
funcionarios = []
pedidos = []
produtos = []
mesas=[]
enderecos=[]

def menu_principal():  # MENU PRINCIPAL
    print('''
        Menu Principal:
        [1] - Cliente
        [2] - Funcionario 
        [3] - Controle de vendas
        [4] - Cadastrar novo produto
        [5] - Remover um produto
        [6] - Pesquisar um produto
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def menu_cliente():
    print('''
        Menu do Cliente:
        [1] - Cadastrar cliente
        [2] - Listar clientes
        [s] - Sair
    ''')
    return str(input('Escolha uma opção:'))

def menu_funcionario():
    print('''
        Menu do Funcionario:
        [1] - Cadastrar Funcionario
        [2] - Visualizar Funcionario
        [s] - Sair  
        ''')
    return str(input('Escolha uma opção: '))
            
def menu_pedido():
    print('''
        MENU Vendas:
        [1] - Abrir novo pedido
        [2] - Adicionar item ao pedido
        [3] - Remover item do pedido
        [4] - Listar itens do pedido em detalhes
        [5] - Finalizar pedido e imprimir
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def cadastrar_cliente():
    nome = input("Nome do Cliente:  ")
    cpf = int(input("Numero do Cpf: "))
    telefone = int(input("Numero de telefone: "))
    email = input("Informe o seu email:  ")
    data_nascimento = input("Informe sua data de nascimento: ")
    senha = str(input("Senha do cliente: "))
    
    endereco_entrega = selecionar_ou_cadastrar_endereco()

    novo_cliente = Cliente(nome, cpf, telefone, email, data_nascimento, senha, endereco_entrega)

    clientes.append(novo_cliente)
    
def listar_clientes():
    if not clientes:
        print("Não existem clientes cadastrados.")
    else:
        print("Lista De Clientes")
        for cliente in clientes:
            cliente.listagem()

def cadastrar_funcionario():
    nome = str(input("Nome do Funcionario:  "))
    id = str(input("Informe seu id: "))
    cpf = str(input("Informe seu cpf: "))
    telefone = str(input("Informe o numero de telefone: "))
    data_nascimento = str(input("Informe sua data de nascimento (formato dd/mm/aaaa): "))
    
    endereco_entrega = selecionar_ou_cadastrar_endereco()


    novo_funcionario = Funcionario(nome,id,cpf,telefone, data_nascimento, endereco_entrega)
    funcionarios.append(novo_funcionario)
    print(f"Funcionario cadastrado com sucesso")

def listar_funcionario():
        if not funcionarios:
            print("Sem Funcionarios.")
        else:
            print("Lista de Funcionarios")
            for funcionario in funcionarios:
                funcionario.dadosfuncio()
                
def cadastrar_pedido():
    codigo_pedido = input("Digite o código do pedido: ")

    if any(pedido._codigo_pedido == codigo_pedido for pedido in pedidos):
        print(f"Já existe um pedido com o código {codigo_pedido}.")
        return

    mesa_numero = input("Digite o número da mesa (deixe em branco para não associar a uma mesa): ")
    mesa = encontrar_mesa_por_numero(mesa_numero)

    novo_pedido = Pedido(codigo_pedido)

    if mesa:
        mesa._pedidos.append(novo_pedido)
        pedidos.append(novo_pedido)
        print(f"Pedido {novo_pedido._codigo_pedido} associado à mesa {mesa._numero_da_mesa}.")
    else:
        pedidos.append(novo_pedido)
        print(f"Pedido {novo_pedido._codigo_pedido} cadastrado com sucesso!")

def pedido_adicionar_item():
    codigo_pedido = input("Digite o código do pedido ao qual deseja adicionar um produto: ")

    # Find the pedido with the given codigo_pedido
    pedido_encontrado = None
    for pedido in pedidos:
        if pedido._codigo_pedido == codigo_pedido:
            pedido_encontrado = pedido
            break

    if pedido_encontrado is None:
        print(f"Pedido {codigo_pedido} não encontrado.")
        return

    # Get the product code and quantity to add to the pedido
    codigo_produto = input("Digite o código do produto a adicionar: ")
    quantidade = int(input("Digite a quantidade desejada: "))

    # Find the product with the given codigo_produto
    produto_encontrado = encontrar_produto_por_codigo(codigo_produto)

    if produto_encontrado is None:
        print(f"Produto {codigo_produto} não encontrado.")
        return

    # Create an ItemPedido and add it to the pedido
    item_pedido = ItemPedido(produto_encontrado, quantidade)
    pedido_encontrado.adicionar_item_ao_pedido(item_pedido)

    print(f"Produto {produto_encontrado._descricao} adicionado ao pedido {pedido_encontrado._codigo_pedido} com sucesso!")
    
def pedido_remover_item():
    int_pedido_selecionado = int(input('Informe o código do pedido para remover um item selecionado: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_item = int(input('Informe o número do item para remover deste pedido ' + str(pedido._codigo_pedido) + ': '))
        # verifica se número intem informado existe: não faz sentido remover item 5 se ele não existe
        #if pedido.quantidade_itens_pedido() <= int_codigo_item:
        pedido.remover_item_pedido(int_codigo_item)
    else:
        print("Pedido inexistente")
        return False
    
def visualizar_pedidos():
    if not pedidos:
        print("Nenhum pedido cadastrado.")
    else:
        print("Pedidos disponíveis:")
        for i, pedido in enumerate(pedidos):
            print(f"{i + 1}: Código do Pedido - {pedido._codigo_pedido}")

        pedido_numero = input("Digite o número do pedido que deseja visualizar: ")

        try:
            pedido_numero = int(pedido_numero)
            if 1 <= pedido_numero <= len(pedidos):
                print(pedidos[pedido_numero - 1])
            else:
                print("Número de pedido inválido.")
        except ValueError:
            print("Número de pedido inválido. Digite um número válido.")
            
def concluir_e_remover_pedido():
    codigo_pedido = input("Digite o código do pedido que deseja concluir: ")

    pedido_encontrado = None
    for pedido in pedidos:
        if pedido._codigo_pedido == codigo_pedido:
            pedido_encontrado = pedido
            pedido.concluir_pedido()

            formas_de_pagamento = escolher_forma_de_pagamento()
            detalhes = input("Informe algum detalhe: ")
            
            nota_fiscal = NotaFiscal(formas_de_pagamento, True, True, detalhes)
            nota_fiscal.display(pedido)

            break

    if pedido_encontrado is None:
        print(f"Pedido {codigo_pedido} não encontrado.")
        return

    pedidos.remove(pedido_encontrado)

    # Check if the order is associated with a table
    for mesa in mesas:
        if pedido_encontrado in mesa._pedidos:
            mesa._pedidos.remove(pedido_encontrado)
            print(f"Pedido {codigo_pedido} concluído e removido da mesa {mesa._numero_da_mesa} com sucesso!")

    print(f"Pedido {codigo_pedido} concluído e removido com sucesso!")
   
def escolher_forma_de_pagamento():
    while True:
        print("Escolha a forma de pagamento:")
        print("1. Pix")
        print("2. Cartão de Crédito")
        print("3. Cartão de Débito")
        print("4. Dinheiro")
        print("0. Voltar")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            return "pix"
        elif opcao == '2':
            return "cartao de credito"
        elif opcao == '3':
            return "debito"
        elif opcao == '4':
            return "dinheiro"
        elif opcao == '0':
            return None
        else:
            print("Opção inválida. Tente novamente.")


def adicionar_cliente_e_funcionario_ao_pedido():
    # Verificar se existem clientes e funcionários cadastrados
    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return
    if not funcionarios:
        print("Nenhum funcionário cadastrado. Cadastre um funcionário primeiro.")
        return

    # Listar clientes disponíveis
    print("Clientes disponíveis:")
    for i, cliente in enumerate(clientes):
        print(f"{i + 1}: {cliente._nome}")  # Corrigindo para usar o atributo correto

    cliente_numero = input("Digite o número do cliente desejado: ")
    try:
        cliente_numero = int(cliente_numero)
        if 1 <= cliente_numero <= len(clientes):
            cliente_selecionado = clientes[cliente_numero - 1]
        else:
            print("Número de cliente inválido.")
            return
    except ValueError:
        print("Número de cliente inválido.")
        return

    # Listar funcionários disponíveis
    print("Funcionários disponíveis:")
    for i, funcionario in enumerate(funcionarios):
        print(f"{i + 1}: {funcionario._nome}")  # Corrigindo para usar o atributo correto

    funcionario_numero = input("Digite o número do funcionário desejado: ")
    try:
        funcionario_numero = int(funcionario_numero)
        if 1 <= funcionario_numero <= len(funcionarios):
            funcionario_selecionado = funcionarios[funcionario_numero - 1]
        else:
            print("Número de funcionário inválido.")
            return
    except ValueError:
        print("Número de funcionário inválido.")
        return
   
def cadastrar_endereco():
    cep = input("Digite o CEP do novo endereço: ")
    rua = input("Digite a rua do novo endereço: ")
    numero = input("Digite o número do novo endereço: ")
    complemento = input("Digite o complemento do novo endereço: ")
    bairro = input("Digite o bairro do novo endereço: ")
    cidade = input("Digite a cidade do novo endereço: ")

    novo_endereco = Endereco(cep, rua, numero, complemento, bairro, cidade)
    enderecos.append(novo_endereco)
    print("Novo endereço cadastrado e selecionado com sucesso.")
    return novo_endereco

def cadastrar_produto():
    codigo_produto = input("Digite o código do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    validade = input("Digite a validade do produto: ")

    novo_produto = Produto(codigo_produto, descricao, preco, validade)
    produtos.append(novo_produto)
    print(f"Produto {novo_produto._codigo_produto} cadastrado com sucesso!")

def remover_produto():
    codigo_produto = input("Digite o código do produto que deseja remover: ")

    for produto in produtos:
        if produto._codigo_produto == codigo_produto:
            produtos.remove(produto)
            print(f"Produto {codigo_produto} removido com sucesso!")
            break
    else:
        print(f"Produto {codigo_produto} não encontrado.")

def pesquisar_produto():
    codigo_produto = input("Digite o código do produto que deseja pesquisar: ")

    for produto in produtos:
        if produto._codigo_produto == codigo_produto:
            print(f"Produto encontrado: {produto._descricao}, Preço: {produto._preco}, Validade: {produto._validade}")
            break
    else:
        print(f"Produto {codigo_produto} não encontrado.")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de Produtos:")
        for produto in produtos:
            print(f"Código: {produto._codigo_produto}, Descrição: {produto._descricao}, Preço: {produto._preco}, Validade: {produto._validade}")

def buscar_pedido_por_codigo(int_codigo_pedido):
    # Verifica se existe produto cadastrado
    for chave in pedidos.keys():
        if chave == int_codigo_pedido:
            return pedidos[int_codigo_pedido]
    return False

def selecionar_ou_cadastrar_endereco():
    endereco_entrega = None
    opcao = input("Deseja selecionar um endereço existente (S) ou cadastrar um novo endereço (N)? ").strip().lower()

    if opcao == 's':
        # Selecionar um endereço existente
        if not enderecos:
            print("Nenhum endereço cadastrado. Por favor, cadastre um novo endereço.")
            endereco_entrega = cadastrar_endereco()
        else:
            print("Endereços cadastrados:")
            for i, endereco in enumerate(enderecos):
                print(f"{i + 1}. CEP: {endereco._cep}, Rua: {endereco._rua}, Bairro: {endereco._bairro}, Cidade: {endereco._cidade}")

            escolha = input("Digite o número do endereço desejado: ")
            try:
                escolha_numero = int(escolha)
                if 1 <= escolha_numero <= len(enderecos):
                    endereco_entrega = enderecos[escolha_numero - 1]
                    print("Endereço selecionado com sucesso.")
                else:
                    print("Opção inválida. Usando o endereço padrão.")
                    endereco_entrega = cadastrar_endereco()
            except ValueError:
                print("Opção inválida. Usando o endereço padrão.")
                endereco_entrega = cadastrar_endereco()
    elif opcao == 'n':
        endereco_entrega = cadastrar_endereco()
    else:
        print("Opção inválida. Usando o endereço padrão.")
        endereco_entrega = cadastrar_endereco()

    return endereco_entrega

def cadastrar_endereco():
    cep = input("Digite o CEP do novo endereço: ")
    rua = input("Digite a rua do novo endereço: ")
    numero = input("Digite o número do novo endereço: ")
    complemento = input("Digite o complemento do novo endereço: ")
    bairro = input("Digite o bairro do novo endereço: ")
    cidade = input("Digite a cidade do novo endereço: ")

    novo_endereco = Endereco(cep, rua, numero, complemento, bairro, cidade)
    enderecos.append(novo_endereco)
    print("Novo endereço cadastrado e selecionado com sucesso.")
    return novo_endereco

def cadastrar_mesa():
    numero_da_mesa = input("Digite o número da mesa: ")

    for mesa in mesas:
        if mesa._numero_da_mesa == numero_da_mesa:
            print("Mesa já cadastrada.")
            return

    nova_mesa = mesa(numero_da_mesa)
    mesas.append(nova_mesa)
    print(f"Mesa {nova_mesa._numero_da_mesa} cadastrada com sucesso!")

def encontrar_mesa_por_numero(numero_mesa):
    for mesa in mesas:
        if mesa._numero_da_mesa == numero_mesa:
            return mesa
    return None

def encontrar_produto_por_codigo(codigo_produto):
    for produto in produtos:
        if produto._codigo_produto == codigo_produto:
            return produto
    return None

def adicionar_cliente_e_funcionario_ao_pedido():
    # Verificar se existem clientes e funcionários cadastrados
    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return
    if not funcionarios:
        print("Nenhum funcionário cadastrado. Cadastre um funcionário primeiro.")
        return

    # Listar clientes disponíveis
    print("Clientes disponíveis:")
    for i, cliente in enumerate(clientes):
        print(f"{i + 1}: {cliente._nome}")  # Corrigindo para usar o atributo correto

    cliente_numero = input("Digite o número do cliente desejado: ")
    try:
        cliente_numero = int(cliente_numero)
        if 1 <= cliente_numero <= len(clientes):
            cliente_selecionado = clientes[cliente_numero - 1]
        else:
            print("Número de cliente inválido.")
            return
    except ValueError:
        print("Número de cliente inválido.")
        return

    # Listar funcionários disponíveis
    print("Funcionários disponíveis:")
    for i, funcionario in enumerate(funcionarios):
        print(f"{i + 1}: {funcionario._nome}")  # Corrigindo para usar o atributo correto

    funcionario_numero = input("Digite o número do funcionário desejado: ")
    try:
        funcionario_numero = int(funcionario_numero)
        if 1 <= funcionario_numero <= len(funcionarios):
            funcionario_selecionado = funcionarios[funcionario_numero - 1]
        else:
            print("Número de funcionário inválido.")
            return
    except ValueError:
        print("Número de funcionário inválido.")
        return

    # Listar pedidos disponíveis
    print("Pedidos disponíveis:")
    for i, pedido in enumerate(pedidos):
        print(f"{i + 1}: Código do Pedido - {pedido._codigo_pedido}")

    pedido_numero = input("Digite o número do pedido ao qual deseja adicionar cliente e funcionário: ")
    try:
        pedido_numero = int(pedido_numero)
        if 1 <= pedido_numero <= len(pedidos):
            pedido_selecionado = pedidos[pedido_numero - 1]
        else:
            print("Número de pedido inválido.")
            return
    except ValueError:
        print("Número de pedido inválido.")
        return

    # Associar cliente e funcionário ao pedido
    pedido_selecionado.cliente = cliente_selecionado
    pedido_selecionado.funcionario = funcionario_selecionado

    print(f"Cliente {cliente_selecionado._nome} e funcionário {funcionario_selecionado._nome} associados ao pedido {pedido_selecionado._codigo_pedido} com sucesso.")



# Aplicação de exemplo disciplina POO - UFRB
# Sistema de controle de pedidos
# Professor Guilherme Braga Araújo
while True:
    # menu_principal
    opcao_escolhida = menu_principal()
    # verificando escolha
    # opc sair
    if (opcao_escolhida == "s"):
        break
    # opc menu cliente - 1
    elif (opcao_escolhida == "1"):
        opcao_cliente = menu_cliente()
        if opcao_cliente == '1':
            cadastrar_cliente()
        elif opcao_cliente == '2':
            listar_clientes()
        elif opcao_cliente == '3':
            print("Saindo do menu de cliente.")
            break
        else:
            print('Opção invalida')
    #opc menu funcionario  - 2       
    elif (opcao_escolhida == "2"):
        opcao_funcionario = menu_funcionario()
        if opcao_funcionario == '1':
            cadastrar_funcionario()
        elif opcao_funcionario == '2':
            listar_funcionario()
        elif opcao_funcionario == '3':
            print("Saindo do menu do funcionario.")
            break
        else:
            print("Opção Invalida")   
    # opc menu vendas - abrir pedido - 3
    elif opcao_escolhida == "3":
        opcao_pedido = menu_pedido()
        if opcao_pedido == "1":
            cadastrar_pedido()
            adicionar_cliente_e_funcionario_ao_pedido()
        elif opcao_pedido == "2":
            pedido_adicionar_item()
        elif opcao_pedido == "3":
            pedido_remover_item()
        elif opcao_pedido == "4":
            visualizar_pedidos()
        elif opcao_pedido == "5":
            concluir_e_remover_pedido()
            pass
        else:
            print("Opção inválida.")
    # opc add produto
    elif opcao_escolhida == "4":
        cadastrar_produto()
    # opc remove
    elif opcao_escolhida == "5":
        remover_produto()
    # opc busca
    elif opcao_escolhida == "6":
        pesquisar_produto()
    #opc lista
    elif opcao_escolhida == "7":
        listar_produtos()
    else:
        print("Opção inválida.")
