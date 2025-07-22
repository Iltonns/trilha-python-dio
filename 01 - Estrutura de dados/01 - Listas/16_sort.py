linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)


"""O método .sort() em Python é usado para ordenar listas no local (ou seja, modifica a lista original). Ele possui alguns parâmetros úteis:

reverse: Se True, ordena em ordem decrescente. Padrão é False.
key: Recebe uma função que retorna um valor para ser usado como critério de ordenação (por exemplo, key=len ordena pelo tamanho dos itens).

.sort() altera a lista original e retorna None.
Para criar uma nova lista ordenada sem modificar a original, use a função sorted()."""