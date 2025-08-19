# Exemplo de encapsulamento: classe que modela uma conta bancária simples.
class Conta:
    def __init__(self, nro_agencia, saldo=0):
        # Saldo inicial da conta. Por convenção, o prefixo "_" indica que o atributo
        # é tratado como "protegido" (evitar acesso direto externo e preferir métodos).
        self._saldo = saldo
        # Número da agência é um atributo público (sem prefixo "_")
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # Deposita um valor na conta, somando ao saldo atual.
        # Observação: não há validação aqui (ex.: impedir valores negativos).
        self._saldo += valor

    def sacar(self, valor):
        # Realiza um saque, subtraindo o valor do saldo.
        # Observação: neste exemplo, o saldo pode ficar negativo, pois não há validação.
        self._saldo -= valor

    def mostrar_saldo(self):
        # Retorna o saldo atual da conta.
        # Este método é a forma recomendada de acessar o saldo (em vez de acessar _saldo diretamente).
        return self._saldo


# Exemplo de uso da classe:
# Cria uma conta na agência "0001" com saldo inicial de 100
conta = Conta("0001", 100)
# Deposita 100; saldo passa a 200
conta.depositar(100)
# Exibe o número da agência (atributo público)
print(conta.nro_agencia)
# Exibe o saldo atual usando o método público
print(conta.mostrar_saldo())
