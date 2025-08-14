# ========================================
# EXEMPLO DE HERANÇA MÚLTIPLA EM PYTHON
# ========================================
# 
# Herança múltipla é um conceito avançado da POO que permite que uma classe
# herde características de MUITAS classes ao mesmo tempo.
#
# Neste exemplo, vamos criar uma hierarquia de animais onde:
# - Alguns animais herdam de uma só classe (herança simples)
# - Outros herdam de múltiplas classes (herança múltipla)
# - Vamos usar **kwargs para flexibilidade nos parâmetros

# ========================================
# CLASSE BASE (SUPERCLASSE) - ANIMAL
# ========================================
# Esta é a classe "pai" que contém características básicas de todos os animais
class Animal:
    # CONSTRUTOR - define características básicas de um animal
    def __init__(self, nro_patas):
        # Atributo comum a todos os animais
        self.nro_patas = nro_patas
    
    # MÉTODO ESPECIAL __str__ - define como o objeto será exibido
    def __str__(self):
        # Retorna uma string formatada com o nome da classe e todos os atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# ========================================
# SUBCLASSES INTERMEDIÁRIAS
# ========================================
# Estas classes herdam de Animal e adicionam características específicas

class Mamifero(Animal):
    # CONSTRUTOR com **kwargs - permite receber qualquer parâmetro nomeado
    # **kw significa "aceite qualquer parâmetro extra e coloque em kw"
    def __init__(self, cor_pelo, **kw):
        # Atributo específico dos mamíferos
        self.cor_pelo = cor_pelo
        # super() chama o construtor da classe pai (Animal)
        # **kw passa todos os parâmetros extras para a classe pai
        super().__init__(**kw)


class Ave(Animal):
    # CONSTRUTOR com **kwargs - similar ao Mamifero
    def __init__(self, cor_bico, **kw):
        # Atributo específico das aves
        self.cor_bico = cor_bico
        # super() chama o construtor da classe pai (Animal)
        # **kw passa todos os parâmetros extras para a classe pai
        super().__init__(**kw)


# ========================================
# SUBCLASSE COM HERANÇA SIMPLES
# ========================================
class Gato(Mamifero):
    # Gato herda APENAS de Mamifero (que por sua vez herda de Animal)
    # Como não definimos nada novo, herda tudo automaticamente
    pass


# ========================================
# SUBCLASSE COM HERANÇA MÚLTIPLA
# ========================================
# Ornitorrinco herda de MAMIFERO E AVE ao mesmo tempo!
# Isso é possível porque Python suporta herança múltipla
class Ornitorrinco(Mamifero, Ave):
    # CONSTRUTOR que precisa lidar com herança múltipla
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # IMPORTANTE: Em herança múltipla, super() chama o PRIMEIRO pai listado
        # Neste caso, super().__init__() chama Mamifero.__init__()
        # O Ornitorrinco herda características de Mamifero E Ave
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)
        
        # ATENÇÃO: Como Ave.__init__() não foi chamado explicitamente,
        # o atributo cor_bico não será definido automaticamente
        # Precisamos definir manualmente:
        self.cor_bico = cor_bico


# ========================================
# CRIANDO OBJETOS (INSTANCIANDO CLASSES)
# ========================================
# Vamos criar objetos para testar nossa hierarquia de herança

# Cria um gato: 4 patas, pelo preto
# Observe que usamos parâmetros nomeados para clareza
gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

# Cria um ornitorrinco: 2 patas, pelo vermelho, bico laranja
# O ornitorrinco é um animal especial que tem características de mamífero E ave
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)

# ========================================
# RESULTADO ESPERADO:
# ========================================
# Gato: cor_pelo=Preto, nro_patas=4
# Ornitorrinco: cor_pelo=vermelho, nro_patas=2, cor_bico=laranja
#
# Observe que:
# - Gato herda de Mamifero (que herda de Animal)
# - Ornitorrinco herda de Mamifero E Ave (que herdam de Animal)
# - Todos têm o atributo nro_patas (herdado de Animal)
# - Gato tem cor_pelo (herdado de Mamifero)
# - Ornitorrinco tem cor_pelo (herdado de Mamifero) E cor_bico (definido manualmente)

# ========================================
# CONCEITOS IMPORTANTES:
# ========================================
# 1. **kwargs: Permite receber parâmetros extras de forma flexível
# 2. Herança múltipla: Uma classe pode herdar de várias classes
# 3. super(): Chama métodos da classe pai (ou primeira classe pai em herança múltipla)
# 4. Ordem de herança: A primeira classe listada tem prioridade
# 5. **kw: Passa parâmetros extras para a classe pai
