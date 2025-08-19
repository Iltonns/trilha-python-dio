class Pessoa:
    """Representa uma pessoa com nome e idade.

    Demonstra o uso de métodos de classe (classmethod) como construtores
    alternativos e métodos estáticos (staticmethod) para utilidades
    que não dependem do estado da instância ou da classe.
    """

    def __init__(self, nome, idade):
        """Inicializa a pessoa com `nome` e `idade`."""
        self.nome = nome
        self.idade = idade

    # Método de classe: recebe `cls` e pode atuar como construtor alternativo.
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        """Cria uma pessoa a partir da data de nascimento.

        Observação: cálculo simplificado usando apenas o ano.
        """
        idade = 2022 - ano
        return cls(nome, idade)

    # Método estático: função utilitária relacionada à classe,
    # mas que não usa `self` nem `cls`.
    @staticmethod
    def e_maior_idade(idade):
        """Retorna True se a idade for >= 18 anos."""
        return idade >= 18


# Exemplo de uso do método de classe como construtor alternativo
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)  # imprime o nome e a idade calculada

# Exemplos de uso do método estático para checar maioridade
print(Pessoa.e_maior_idade(18))  # True
print(Pessoa.e_maior_idade(8))   # False
