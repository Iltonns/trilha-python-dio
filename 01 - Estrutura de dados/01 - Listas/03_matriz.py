matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"


"""Matrizes são estruturas de dados bidimensionais, ou seja, tabelas compostas por linhas e colunas. Em Python, uma matriz pode ser representada como uma lista de listas, onde cada elemento da lista principal é outra lista (cada uma representando uma linha da matriz).

Principais características:

Acesso aos elementos: Use dois índices: matriz[linha][coluna].
Iteração: Pode-se usar loops aninhados para percorrer todos os elementos.
Aplicações: Matrizes são usadas em matemática, processamento de imagens, jogos, entre o"""