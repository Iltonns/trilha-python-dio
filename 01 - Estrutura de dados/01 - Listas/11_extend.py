linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]


"""O método extend() em Python é usado para adicionar todos os elementos de uma lista (ou outro iterável) ao final de outra lista. Ele modifica a lista original, aumentando seu tamanho com os novos elementos

extend() recebe um iterável (como lista, tupla, etc.).
Adiciona cada elemento desse iterável à lista original.
Diferente de append(), que adiciona o objeto inteiro como um único elemento."""