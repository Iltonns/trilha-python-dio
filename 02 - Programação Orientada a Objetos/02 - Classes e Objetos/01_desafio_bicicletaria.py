# ========================================
# DESAFIO: SISTEMA DE BICICLETARIA EM PYTHON
# ========================================
# Este código demonstra como criar uma classe para representar bicicletas
# e como trabalhar com objetos em Programação Orientada a Objetos

# ========================================
# DEFINIÇÃO DA CLASSE BICICLETA
# ========================================
# Uma classe é como um "plano" ou "receita" para criar objetos
# Neste caso, vamos criar um plano para fazer bicicletas
class Bicicleta:
    # ========================================
    # CONSTRUTOR (__init__)
    # ========================================
    # Este método é chamado AUTOMATICAMENTE quando criamos uma nova bicicleta
    # É como a "receita" para montar uma bicicleta com suas características
    # self = representa a própria bicicleta que está sendo criada
    # cor, modelo, ano, valor = são as características que definem a bicicleta
    def __init__(self, cor, modelo, ano, valor):
        # Atribuindo valores aos atributos da bicicleta
        # self.cor = cor significa: "a cor desta bicicleta será a cor que foi passada"
        self.cor = cor          # Guarda a cor da bicicleta (ex: vermelha, azul)
        self.modelo = modelo    # Guarda o modelo da bicicleta (ex: caloi, monark)
        self.ano = ano          # Guarda o ano de fabricação (ex: 2022, 2000)
        self.valor = valor      # Guarda o preço da bicicleta (ex: 600, 189)

    # ========================================
    # MÉTODOS DA CLASSE (COMPORTAMENTOS)
    # ========================================
    # Estes métodos definem o que uma bicicleta pode FAZER
    
    # Método para simular o som da buzina da bicicleta
    def buzinar(self):
        print("Plim plim...")  # Imprime o som da buzina

    # Método para simular a parada da bicicleta
    def parar(self):
        print("Parando bicicleta...")  # Primeira mensagem
        print("Bicicleta parada!")     # Segunda mensagem

    # Método para simular a bicicleta correndo
    def correr(self):
        print("Vrummmmm...")  # Imprime o som da bicicleta em movimento

    # ========================================
    # MÉTODO ESPECIAL __str__
    # ========================================
    # Este método é chamado AUTOMATICAMENTE quando usamos print() no objeto
    # É como uma "carteira de identidade" da bicicleta
    def __str__(self):
        # Retorna uma string com o nome da classe e todos os atributos
        # self.__class__.__name__ = pega o nome da classe (Bicicleta)
        # self.__dict__.items() = pega todos os atributos e valores
        # f'{chave}={valor}' = formata cada atributo como "cor=vermelha"
        # ', '.join() = junta tudo com vírgulas
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# ========================================
# CRIANDO OBJETOS (INSTÂNCIAS) DA CLASSE
# ========================================
# Agora vamos usar nossa "receita" para criar bicicletas reais!

# Criando a primeira bicicleta (b1)
# O construtor __init__ será chamado automaticamente
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

# ========================================
# TESTANDO OS MÉTODOS DA PRIMEIRA BICICLETA
# ========================================
b1.buzinar()  # Chama o método buzinar() - vai imprimir "Plim plim..."
b1.correr()   # Chama o método correr() - vai imprimir "Vrummmmm..."
b1.parar()    # Chama o método parar() - vai imprimir as mensagens de parada

# Exibindo os atributos da primeira bicicleta individualmente
# b1.cor = acessa a cor da bicicleta b1
print(b1.cor, b1.modelo, b1.ano, b1.valor)  # Vai imprimir: vermelha caloi 2022 600

# ========================================
# CRIANDO UMA SEGUNDA BICICLETA
# ========================================
# Cada bicicleta é um objeto INDEPENDENTE com suas próprias características
b2 = Bicicleta("verde", "monark", 2000, 189)

# ========================================
# TESTANDO A SEGUNDA BICICLETA
# ========================================
# Usando print(b2) - isso chama automaticamente o método __str__
# Vai imprimir algo como: "Bicicleta: cor=verde, modelo=monark, ano=2000, valor=189"
print(b2)

# Testando o método correr da segunda bicicleta
b2.correr()   # Vai imprimir "Vrummmmm..."

# ========================================
# RESUMO DO QUE APRENDEMOS:
# ========================================
# 1. Como criar uma classe com atributos e métodos
# 2. Como o construtor __init__ funciona automaticamente
# 3. Como criar objetos (instâncias) da classe
# 4. Como chamar métodos dos objetos
# 5. Como acessar atributos dos objetos
# 6. Como o método __str__ funciona automaticamente
# 7. Como cada objeto é independente e tem suas próprias características
