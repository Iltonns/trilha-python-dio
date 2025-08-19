# Exemplo prático de atributos de classe versus atributos de instância
# Demonstra como a alteração de um atributo de classe reflete em todas as instâncias

class Estudante:
    # Atributo de classe: compartilhado por TODAS as instâncias da classe
    escola = "DIO"

    def __init__(self, nome, matricula):
        # Atributos de instância: pertencem a cada objeto criado
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        # Retorna uma representação amigável ao imprimir o objeto
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    # Recebe quaisquer objetos e imprime sua representação
    for obj in objs:
        print(obj)


# Criação de duas instâncias; ambas começam com a escola definida no atributo de classe ("DIO")
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

# Alteração do atributo de classe. Essa mudança impacta todas as instâncias
# que não tenham um atributo de instância com o mesmo nome.
Estudante.escola = "Python"
# Nova instância já nasce com a nova escola; as anteriores também passam a exibir a mudança
aluno_3 = Estudante("Chappie", 3)
# Reimprime para evidenciar que o atributo de classe mudou para todas as instâncias
mostrar_valores(aluno_1, aluno_2, aluno_3)
