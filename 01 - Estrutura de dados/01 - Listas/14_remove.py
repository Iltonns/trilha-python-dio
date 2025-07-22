linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]


"""O método .remove() em listas Python é usado para remover a primeira ocorrência de um valor específico. Ele recebe como argumento o elemento que você deseja remover da lista. Se o elemento não existir, ocorre um erro ValueError.

Apenas a primeira ocorrência do valor é removida.
Se o valor não estiver na lista, ocorre um erro.
Não retorna nada (None)."""