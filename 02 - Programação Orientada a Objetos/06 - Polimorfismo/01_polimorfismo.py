# Exemplo simples de polimorfismo em Python
# Ideia: objetos diferentes respondem à mesma mensagem (método) de formas distintas.
# Aqui usamos "duck typing": qualquer objeto que tenha o método voar() pode ser usado no plano_voo().

class Passaro:
    # Classe base que define a interface/contrato: todo "Passaro" deve saber "voar"
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    # Sobrescreve o método voar com um comportamento específico
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    # Avestruz também é um Passaro, mas não voa; ainda assim cumpre a interface
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
# Apesar de "funcionar" por duck typing, semanticamente um Avião não é um Pássaro.
# Herança deve modelar uma relação "é-um"; aqui quebramos essa ideia (má prática de design).
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj):
    # Função polimórfica: recebe QUALQUER objeto com método voar.
    # Não importa o tipo exato; importa apenas a existência do método (duck typing).
    obj.voar()


# Cada chamada abaixo demonstra um comportamento diferente para a "mesma" operação voar()
plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
