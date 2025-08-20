"""Sistema bancário orientado a objetos.

Este módulo implementa um pequeno domínio bancário para estudo de POO,
incluindo clientes, contas, histórico de transações e os tipos de transação
depósito e saque. Há também um menu interativo simples via terminal.

Conceitos de POO utilizados:
- Classes e objetos
- Herança
- Encapsulamento (atributos com prefixo _ e propriedades somente leitura)
- Polimorfismo (sobrescrita de método `sacar` em `ContaCorrente`)
- Classes e métodos abstratos (interface de `Transacao`)
"""

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    """Representa um cliente do banco.

    Um cliente pode possuir um endereço e uma ou mais contas bancárias.
    """
    def __init__(self, endereco):
        """Inicializa o cliente com endereço e lista vazia de contas."""
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        """Delegar a execução de uma transação para a conta informada."""
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """Associa uma conta ao cliente."""
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """Especialização de `Cliente` para pessoa física."""
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    """Modelo genérico de conta bancária.

    Esta classe define operações básicas como depósito e saque e mantém um
    histórico de transações associadas à conta.
    """
    def __init__(self, numero, cliente):
        """Cria uma conta com saldo zero e associa a um cliente.

        Parâmetros:
        - numero: identificador numérico da conta
        - cliente: instância de `Cliente` (ou subclasses)
        """
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        """Fábrica de contas para facilitar a criação sem conhecer o construtor."""
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        """Realiza um saque, validando saldo e valor positivo.

        Retorna True em caso de sucesso; caso contrário, False.
        """
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        """Realiza um depósito, aceitando apenas valores positivos.

        Retorna True em caso de sucesso; caso contrário, False.
        """
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    """Conta corrente com limites de valor e quantidade de saques."""
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        """Saque que respeita `limite` e `limite_saques` além das regras da conta."""
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        """Representação amigável para impressão de dados da conta."""
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    """Armazena o histórico de transações de uma conta."""
    def __init__(self):
        """Inicializa a lista interna de transações como vazia."""
        self._transacoes = []

    @property
    def transacoes(self):
        """Lista de dicionários com registros de transações realizadas."""
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """Adiciona um registro de transação ao histórico com tipo, valor e data."""
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    """Interface para operações financeiras que afetam uma `Conta`.

    Implementações concretas devem definir `valor` e o método `registrar`.
    """
    @property
    @abstractproperty
    def valor(self):
        """Valor monetário da transação."""
        pass

    @abstractclassmethod
    def registrar(self, conta):
        """Aplica a transação sobre a `conta` informada e registra no histórico."""
        pass


class Saque(Transacao):
    """Transação de saque de valores de uma conta."""
    def __init__(self, valor):
        """Cria um saque com o `valor` informado."""
        self._valor = valor

    @property
    def valor(self):
        """Retorna o valor do saque."""
        return self._valor

    def registrar(self, conta):
        """Tenta sacar da conta e, em caso de sucesso, registra no histórico."""
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """Transação de depósito de valores em uma conta."""
    def __init__(self, valor):
        """Cria um depósito com o `valor` informado."""
        self._valor = valor

    @property
    def valor(self):
        """Retorna o valor do depósito."""
        return self._valor

    def registrar(self, conta):
        """Tenta depositar na conta e, em caso de sucesso, registra no histórico."""
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
