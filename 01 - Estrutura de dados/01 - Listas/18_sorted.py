linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]


"""O sorted() é uma função embutida do Python que retorna uma nova lista ordenada a partir de qualquer iterável (como listas, tuplas, dicionários, etc.), sem modificar o original.

Principais parâmetros:

iterable: o objeto que você quer ordenar.
key: uma função que define como os elementos serão comparados (por exemplo, key=len ordena pelo tamanho).
reverse: se True, ordena em ordem decrescente."""