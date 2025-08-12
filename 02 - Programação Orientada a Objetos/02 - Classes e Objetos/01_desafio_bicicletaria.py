# Definição da classe Bicicleta
class Bicicleta:
    # Método construtor, inicializa os atributos da bicicleta
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor          # Cor da bicicleta
        self.modelo = modelo    # Modelo da bicicleta
        self.ano = ano          # Ano de fabricação
        self.valor = valor      # Valor da bicicleta

    # Método para simular o som da buzina
    def buzinar(self):
        print("Plim plim...")

    # Método para simular a parada da bicicleta
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    # Método para simular a bicicleta correndo
    def correr(self):
        print("Vrummmmm...")

    # Método especial para representar o objeto como string
    def __str__(self):
        # Retorna uma string com o nome da classe e os atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Instanciando objetos da classe Bicicleta
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()  # Chama o método buzinar
b1.correr()   # Chama o método correr
b1.parar()    # Chama o método parar
print(b1.cor, b1.modelo, b1.ano, b1.valor)  # Exibe os atributos individualmente

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)     # Exibe a representação em string do objeto
b2.correr()   # Chama o método correr
