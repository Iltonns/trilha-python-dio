lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]



"""
O fatiamento (ou slicing) em Python é uma técnica para acessar partes de sequências, como listas, strings ou tuplas, usando a notação [início:fim:passo].

início: índice onde começa o fatiamento (inclusivo).
fim: índice onde termina (exclusivo).
passo: de quantos em quantos elementos pula.

"""