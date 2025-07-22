# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0] # Filtra os numeros pares da lista
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros] # Gera uma lista com os quadrados dos numeros
print(quadrado)


"""Compreensão de listas (ou list comprehensions) é uma forma concisa e eficiente de criar listas em Python. Ela permite gerar uma nova lista a partir de uma sequência existente, aplicando filtros e transformações em uma única linha de código."""