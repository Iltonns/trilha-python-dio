# ==========================================
# EXEMPLO: PASSAGEM DE FUNÇÕES COMO PARÂMETROS
# ==========================================
# Este código demonstra como funções podem ser passadas como argumentos
# para outras funções, um conceito fundamental para decoradores

def mensagem(nome):
    """
    Função simples que retorna uma mensagem de saudação básica.
    
    Args:
        nome (str): Nome da pessoa a ser cumprimentada
    
    Returns:
        str: Mensagem de saudação formatada
    """
    print("executando mensagem")
    return f"Oi {nome}"


def mensagem_longa(nome):
    """
    Função que retorna uma mensagem de saudação mais elaborada.
    
    Args:
        nome (str): Nome da pessoa a ser cumprimentada
    
    Returns:
        str: Mensagem de saudação longa formatada
    """
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"


def executar(funcao, nome):
    """
    Função que recebe uma função como parâmetro e a executa.
    Esta é a base para entender decoradores - funções que recebem
    outras funções como argumentos.
    
    Args:
        funcao (function): Função que será executada
        nome (str): Nome que será passado para a função
    
    Returns:
        str: Resultado da execução da função passada como parâmetro
    """
    print("executando executar")
    return funcao(nome)


# ==========================================
# TESTANDO A PASSAGEM DE FUNÇÕES
# ==========================================

# Chamando executar() passando a função 'mensagem' como primeiro argumento
# Isso demonstra que funções são objetos de primeira classe em Python
print(executar(mensagem, "Eleilton"))

# Chamando executar() passando a função 'mensagem_longa' como primeiro argumento
# A função executar() não sabe qual função recebeu, apenas a executa
print(executar(mensagem_longa, "Eleilton"))

# ==========================================
# CONCEITO IMPORTANTE:
# ==========================================
# Em Python, funções são objetos de primeira classe, o que significa que:
# 1. Podem ser atribuídas a variáveis
# 2. Podem ser passadas como argumentos para outras funções
# 3. Podem ser retornadas por outras funções
# 4. Podem ser armazenadas em estruturas de dados
#
# Este conceito é fundamental para entender decoradores, que são
# funções que modificam o comportamento de outras funções.
