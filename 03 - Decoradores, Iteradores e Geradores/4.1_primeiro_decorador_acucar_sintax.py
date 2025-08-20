# ==========================================
# DECORADORES EM PYTHON - SINTAXE AÇÚCAR
# ==========================================
# Este arquivo demonstra como criar e usar decoradores
# usando a sintaxe açúcar (@decorador) do Python

def meu_decorador(funcao):
    """
    Função decoradora que recebe uma função como parâmetro
    e retorna uma nova função (envelope) que adiciona funcionalidade
    antes e depois da execução da função original
    """
    def envelope():
        """
        Função interna (envelope) que:
        1. Executa código antes da função original
        2. Chama a função original
        3. Executa código depois da função original
        """
        print("faz algo antes de executar")  # Código executado ANTES
        funcao()                             # Executa a função original
        print("faz algo depois de executar") # Código executado DEPOIS

    return envelope  # Retorna a função envelope (não a executa)


# ==========================================
# SINTAXE AÇÚCAR (@decorador)
# ==========================================
# A linha abaixo é equivalente a:
# ola_mundo = meu_decorador(ola_mundo)
# 
# O @meu_decorador aplica automaticamente o decorador
# à função ola_mundo, criando uma versão decorada
@meu_decorador
def ola_mundo():
    """
    Função simples que será decorada pelo meu_decorador
    """
    print("Olá mundo!")


# ==========================================
# EXECUÇÃO
# ==========================================
# Quando chamamos ola_mundo(), na verdade estamos chamando
# a função envelope retornada pelo decorador, que:
# 1. Imprime "faz algo antes de executar"
# 2. Executa a função ola_mundo original
# 3. Imprime "faz algo depois de executar"
ola_mundo()

# ==========================================
# SAÍDA ESPERADA:
# ==========================================
# faz algo antes de executar
# Olá mundo!
# faz algo depois de executar
