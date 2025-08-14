# ========================================
# EXEMPLO DE HERANÇA SIMPLES EM PYTHON
# ========================================
# 
# Herança é um conceito fundamental da Programação Orientada a Objetos (POO)
# que permite que uma classe "herde" características (atributos e métodos) 
# de outra classe, chamada de "classe pai" ou "superclasse".
#
# Neste exemplo, vamos criar uma hierarquia de veículos onde diferentes
# tipos de veículos herdam características básicas de uma classe base.

# ========================================
# CLASSE BASE (SUPERCLASSE) - VEICULO
# ========================================
# Esta é a classe "pai" que contém características comuns a todos os veículos
class Veiculo: 
    # CONSTRUTOR (método especial que é executado quando criamos um objeto)
    # O parâmetro 'self' representa a instância do objeto sendo criado
    def __init__(self, cor, placa, numero_rodas):
        # Atributos da classe - características que todo veículo tem
        self.cor = cor          # Cor do veículo
        self.placa = placa      # Placa de identificação
        self.numero_rodas = numero_rodas  # Quantidade de rodas
    
    # MÉTODO - ação que todo veículo pode realizar
    def ligar_motor(self):
        print("Ligando o motor")
    
    # MÉTODO ESPECIAL __str__ - define como o objeto será exibido quando
    # usarmos print() ou str() nele
    def __str__(self):
        # Retorna uma string formatada com o nome da classe e todos os atributos
        # __class__.__name__ pega o nome da classe atual
        # __dict__ contém todos os atributos do objeto
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# ========================================
# SUBCLASSES (CLASSES FILHAS)
# ========================================
# Estas classes herdam TUDO da classe Veiculo usando (Veiculo)
# Elas automaticamente têm todos os atributos e métodos da classe pai

class Motocicleta(Veiculo):
    # A palavra 'pass' significa "não fazer nada"
    # Como não definimos nada novo, a moto herda tudo do veículo
    # Mas com 2 rodas por padrão
    pass


class Carro(Veiculo):
    # O carro também herda tudo do veículo
    # Mas com 4 rodas por padrão
    pass


# ========================================
# SUBCLASSE COM COMPORTAMENTO ESPECÍFICO
# ========================================
class Caminhao(Veiculo):
    # Este construtor sobrescreve o construtor da classe pai
    # Adiciona um novo parâmetro: carregado
    def __init__(self, cor, placa, numero_rodas, carregado):
        # super() chama o construtor da classe pai (Veiculo)
        # Isso garante que os atributos básicos sejam configurados
        super().__init__(cor, placa, numero_rodas)
        # Adiciona o novo atributo específico do caminhão
        self.carregado = carregado
    
    # MÉTODO ESPECÍFICO - só o caminhão tem este método
    def esta_carregado(self):
        # Usa operador ternário para verificar se está carregado
        # Se self.carregado for True, imprime "Sim", senão "Não"
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


# ========================================
# CRIANDO OBJETOS (INSTANCIANDO CLASSES)
# ========================================
# Agora vamos criar objetos reais das nossas classes

# Cria uma moto: cor preta, placa abc-1234, 2 rodas
moto = Motocicleta("preta", "abc-1234", 2)

# Cria um carro: cor branco, placa xde-0098, 4 rodas  
carro = Carro("branco", "xde-0098", 4)

# Cria um caminhão: cor roxo, placa gfd-8712, 8 rodas, carregado=True
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

# ========================================
# TESTANDO OS OBJETOS
# ========================================
# Vamos ver como cada objeto se comporta

# Exibe informações da moto (usa o método __str__ herdado)
print(moto)

# Exibe informações do carro (usa o método __str__ herdado)
print(carro)

# Exibe informações do caminhão (usa o método __str__ herdado)
print(caminhao)

# ========================================
# RESULTADO ESPERADO:
# ========================================
# Motocicleta: cor=preta, placa=abc-1234, numero_rodas=2
# Carro: cor=branco, placa=xde-0098, numero_rodas=4  
# Caminhao: cor=roxo, placa=gfd-8712, numero_rodas=8, carregado=True
#
# Observe que:
# - Moto e Carro herdam tudo de Veiculo
# - Caminhão herda tudo de Veiculo + tem atributo extra (carregado)
# - Todos usam o mesmo método __str__ para exibição
# - Todos podem usar o método ligar_motor() herdado
