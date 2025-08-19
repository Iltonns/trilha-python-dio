"""
Exemplo didático de uso de classes abstratas com o módulo abc (Abstract Base Classes).

- Uma classe abstrata (subclasse de ABC) define uma interface que as subclasses
  concretas devem implementar.
- @abstractmethod marca métodos que precisam ser implementados nas subclasses.
- @property junto a @abstractproperty indica que a propriedade deve ser exposta
  pelas subclasses (nota: abstractproperty é considerado legado; o padrão
  moderno é usar @property junto com @abstractmethod no getter). 
"""

from abc import ABC, abstractmethod, abstractproperty


# Classe base abstrata que define a interface mínima de um controle remoto
class ControleRemoto(ABC):
    # Método abstrato: toda subclasse deve implementar como ligar o aparelho
    @abstractmethod
    def ligar(self):
        pass

    # Método abstrato: toda subclasse deve implementar como desligar o aparelho
    @abstractmethod
    def desligar(self):
        pass

    # Propriedade abstrata que expõe a marca do dispositivo controlado
    @property
    @abstractproperty
    def marca(self):
        pass


# Implementação concreta de um controle remoto específico para TV
class ControleTV(ControleRemoto):
    def ligar(self):
        # Passos específicos para ligar a TV
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        # Passos específicos para desligar a TV
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


# Implementação concreta de um controle remoto para Ar Condicionado
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        # Passos específicos para ligar o ar condicionado
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        # Passos específicos para desligar o ar condicionado
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


# Demonstração de uso: instanciando um controle de TV e utilizando seus métodos
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


# Demonstração de uso: instanciando um controle de Ar Condicionado e utilizando seus métodos
controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
