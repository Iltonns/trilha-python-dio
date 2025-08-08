# ============================================================
# Sistema Bancário Simples em Python
#
# Este projeto simula um sistema bancário básico, permitindo:
# - Cadastro de usuários (identificados por CPF)
# - Criação de contas bancárias para cada usuário
# - Depósitos, saques e extratos por conta
# - Listar contas
# - Transferências entre contas
# - Controle de limite de saques diários
#
# O objetivo é praticar lógica de programação, manipulação de listas
# e funções em Python, simulando operações comuns de um banco.
# ============================================================

# Menu de opções apresentado ao usuário
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[t] Transferir
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair

=> """

# Lista para armazenar os usuários cadastrados
usuarios = []
# Lista para armazenar as contas criadas
contas = []
# Limite de saques diários por conta
LIMITE_SAQUES = 3

# Função para encontrar um usuário pelo CPF
def encontrar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# Função para criar um novo usuário
def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if encontrar_usuario(cpf):
        print("Já existe um usuário com este CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Adiciona o novo usuário à lista de usuários
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")

# Função para criar uma nova conta bancária para um usuário existente
def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = encontrar_usuario(cpf)
    if not usuario:
        print("Usuário não encontrado, cadastre primeiro!")
        return
    numero_conta = len(contas) + 1

    # Adiciona a nova conta à lista de contas
    contas.append({
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0,
        "limite": 500
    })
    print(f"Conta criada com sucesso! Agência: 0001 Conta: {numero_conta}")

# Função para encontrar uma conta pelo número
def encontrar_conta(numero_conta):
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            return conta
    return None

# Função para realizar depósito em uma conta
def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para realizar saque em uma conta
def sacar(conta):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["numero_saques"] >= LIMITE_SAQUES

    # Verifica as condições para saque
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para exibir o extrato de uma conta
def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    print(conta["extrato"] if conta["extrato"] else "Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

# Função para transferir valores entre contas
def transferir():
    origem_num = int(input("Informe o número da conta de origem: "))
    destino_num = int(input("Informe o número da conta de destino: "))
    valor = float(input("Informe o valor da transferência: "))
    origem = encontrar_conta(origem_num)
    destino = encontrar_conta(destino_num)

    # Verifica se as contas existem e se o valor é válido
    if not origem or not destino:
        print("Conta de origem ou destino não encontrada.")
        return
    if valor <= 0 or valor > origem["saldo"]:
        print("Transferência inválida! Verifique o saldo e o valor.")
        return
    
    # Realiza a transferência
    origem["saldo"] -= valor
    origem["extrato"] += f"Transferência enviada: R$ {valor:.2f} para conta {destino_num}\n"
    destino["saldo"] += valor
    destino["extrato"] += f"Transferência recebida: R$ {valor:.2f} da conta {origem_num}\n"
    print("Transferência realizada com sucesso!")

# Função para listar todas as contas cadastradas
def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada no sistema.")
        return
    
    print("\n================ LISTA DE CONTAS ================")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
        print(f"CPF: {conta['usuario']['cpf']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")
        print("-" * 45)
    print("================================================")

# Loop principal do sistema bancário
while True:
    opcao = input(menu)

    # Cadastro de novo usuário
    if opcao == "nu":
        criar_usuario()

    # Cadastro de nova conta
    elif opcao == "nc":
        criar_conta()

    # Operações de depósito, saque e extrato
    elif opcao in ["d", "s", "e"]:
        numero_conta = int(input("Informe o número da conta: "))
        conta = encontrar_conta(numero_conta)
        if not conta:
            print("Conta não encontrada!")
            continue
        if opcao == "d":
            depositar(conta)
        elif opcao == "s":
            sacar(conta)
        elif opcao == "e":
            exibir_extrato(conta)

    # Transferência entre contas
    elif opcao == "t":
        transferir()

    # Listar contas
    elif opcao == "lc":
        listar_contas()

    # Sair do sistema
    elif opcao == "q":
        break
    
    # Opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")




        