# ========================================
# EXEMPLO DE CONSTRUTORES E DESTRUTORES EM PYTHON
# ========================================
# Este código demonstra como funcionam os métodos especiais __init__ e __del__
# em classes Python, que são fundamentais para entender Programação Orientada a Objetos

# Definindo uma classe chamada Cachorro
# Uma classe é como um "molde" ou "planta" para criar objetos
class Cachorro:
    # ========================================
    # CONSTRUTOR (__init__)
    # ========================================
    # O método __init__ é chamado AUTOMATICAMENTE quando criamos um novo objeto
    # É como se fosse a "receita" para criar um cachorro
    # self = representa o próprio objeto que está sendo criado
    # nome, cor, acordado = são os parâmetros que passamos ao criar o objeto
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")  # Mensagem para mostrar quando o construtor é executado
        
        # Atribuindo valores aos atributos do objeto
        # self.nome = nome significa: "o nome deste cachorro será o nome que foi passado"
        self.nome = nome      # Guarda o nome do cachorro
        self.cor = cor        # Guarda a cor do cachorro
        self.acordado = acordado  # Guarda se o cachorro está acordado (padrão é True)

    # ========================================
    # DESTRUTOR (__del__)
    # ========================================
    # O método __del__ é chamado AUTOMATICAMENTE quando o objeto é destruído
    # É como uma "limpeza final" antes do objeto desaparecer da memória
    def __del__(self):
        print("Removendo a instância da classe.")  # Mensagem para mostrar quando o destrutor é executado

    # ========================================
    # MÉTODO COMUM
    # ========================================
    # Este é um método normal da classe (não é especial como __init__ ou __del__)
    def falar(self):
        print("auau")  # Faz o cachorro "latir" imprimindo "auau"

# ========================================
# FUNÇÃO PARA DEMONSTRAR ESCOPO LOCAL
# ========================================
# Esta função mostra como objetos criados dentro de uma função
# são automaticamente destruídos quando a função termina
def criar_cachorro():
    # Criando um cachorro dentro da função
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)  # Imprime o nome do cachorro
    # Quando a função termina, o cachorro 'c' é automaticamente destruído
    # e o destrutor __del__ é chamado

# ========================================
# CÓDIGO PRINCIPAL - EXECUTANDO O EXEMPLO
# ========================================

# Criando um objeto cachorro chamado "Chappie"
# O construtor __init__ será chamado automaticamente
c = Cachorro("Chappie", "amarelo")

# Chamando o método falar() do cachorro
c.falar()  # Isso vai imprimir "auau"

print("Ola mundo")  # Mensagem de teste

# ========================================
# DESTRUINDO O OBJETO MANUALMENTE
# ========================================
# O comando 'del' remove o objeto da memória
# Isso vai chamar automaticamente o destrutor __del__
del c

# ========================================
# TESTE PARA VERIFICAR O COMPORTAMENTO
# ========================================
# Estas mensagens são impressas DEPOIS do objeto ser destruído
# para mostrar que o destrutor foi executado antes
print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# ========================================
# FUNÇÃO COMENTADA
# ========================================
# Esta linha está comentada (não será executada)
# Se descomentarmos, veremos o destrutor sendo chamado automaticamente
# quando a função criar_cachorro() terminar
# criar_cachorro()
