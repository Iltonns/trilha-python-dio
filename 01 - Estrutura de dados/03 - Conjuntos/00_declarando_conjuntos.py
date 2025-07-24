numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}


"""O método set() em Python é uma função embutida que cria um conjunto (set) a partir de um iterável (como listas, tuplas ou strings). Conjuntos são coleções não ordenadas de elementos únicos, ou seja, não permitem elementos duplicados.

Principais características do set:

Remove duplicatas automaticamente.
Não garante ordem dos elementos.
Permite operações matemáticas como união, interseção e diferença.

Uso comum:

Remover duplicatas de uma lista.
Testar rapidamente se um elemento está presente (busca rápida).
Realizar operações de conjuntos (união, interseção, etc"""