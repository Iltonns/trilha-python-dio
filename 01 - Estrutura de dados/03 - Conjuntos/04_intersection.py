conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)


"""O método .intersection() em Python é utilizado para encontrar a interseção entre dois ou mais conjuntos (sets). Ele retorna um novo conjunto contendo apenas os elementos que estão presentes em todos os conjuntos envolvidos.
Resumindo: .intersection() é útil para encontrar elementos compartilhados entre conjuntos.
"""
# Você também pode usar o operador & para obter o mesmo resultado:
resultado = conjunto_a & conjunto_b
print(resultado)


# O método .intersection() pode receber múltiplos conjuntos como argumento:
conjunto_c = {3, 4, 5}
resultado = conjunto_a.intersection(conjunto_b, conjunto_c)  # Saída: {3}