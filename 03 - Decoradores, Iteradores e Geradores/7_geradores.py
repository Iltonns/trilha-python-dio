# ==========================================
# GERADORES EM PYTHON
# ==========================================
# 
# Geradores são funções especiais que retornam um iterador
# Eles usam a palavra-chave 'yield' em vez de 'return'
# 
# VANTAGENS DOS GERADORES:
# - Economia de memória (não carregam todos os dados na memória de uma vez)
# - Lazy evaluation (avaliação preguiçosa - só processa quando necessário)
# - Útil para grandes volumes de dados
# - Permitem iteração infinita

def meu_gerador(numeros: list[int]):
    """
    Função geradora que multiplica cada número por 2
    
    Args:
        numeros: Lista de números inteiros
        
    Yields:
        Cada número multiplicado por 2, um por vez
    """
    # Loop através de cada número na lista
    for numero in numeros:
        # 'yield' pausa a execução e retorna o valor
        # Quando a função é chamada novamente, continua de onde parou
        yield numero * 2


# EXEMPLO DE USO DO GERADOR
# O gerador é iterável, então podemos usar em um loop for
print("Resultados do gerador:")
for i in meu_gerador(numeros=[1, 2, 3]):
    print(f"Valor gerado: {i}")

# ==========================================
# COMPARAÇÃO: FUNÇÃO NORMAL vs GERADOR
# ==========================================

def funcao_normal(numeros: list[int]):
    """Função normal que retorna uma lista completa"""
    resultado = []
    for numero in numeros:
        resultado.append(numero * 2)
    return resultado

# Função normal: cria lista completa na memória
print("\nFunção normal (lista completa):")
resultado_lista = funcao_normal([1, 2, 3])
print(f"Lista completa: {resultado_lista}")

# Gerador: processa um item por vez
print("\nGerador (processamento lazy):")
gerador = meu_gerador([1, 2, 3])
print(f"Primeiro valor: {next(gerador)}")
print(f"Segundo valor: {next(gerador)}")
print(f"Terceiro valor: {next(gerador)}")

# ==========================================
# EXEMPLO PRÁTICO: GERADOR INFINITO
# ==========================================

def contador_infinito(inicio: int = 0):
    """
    Gerador que conta infinitamente a partir de um número
    
    Args:
        inicio: Número inicial para começar a contagem
        
    Yields:
        Números sequenciais infinitos
    """
    numero = inicio
    while True:  # Loop infinito
        yield numero
        numero += 1

# Demonstração do gerador infinito (limitado a 5 iterações)
print("\nGerador infinito (primeiros 5 valores):")
contador = contador_infinito(10)
for _ in range(5):
    print(f"Contador: {next(contador)}")

# ==========================================
# EXEMPLO: GERADOR PARA LER ARQUIVOS GRANDES
# ==========================================

def ler_arquivo_por_linha(nome_arquivo: str):
    """
    Gerador para ler arquivo linha por linha
    Útil para arquivos muito grandes
    
    Args:
        nome_arquivo: Caminho para o arquivo
        
    Yields:
        Cada linha do arquivo, uma por vez
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                # Remove espaços em branco e retorna a linha
                yield linha.strip()
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado!")

# Exemplo de uso (comentado para não dar erro se arquivo não existir)
# print("\nLendo arquivo linha por linha:")
# for linha in ler_arquivo_por_linha("exemplo.txt"):
#     print(f"Linha: {linha}")
