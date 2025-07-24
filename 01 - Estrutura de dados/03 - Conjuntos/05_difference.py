conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)


"""O método .difference() em Python é utilizado com conjuntos (tipo set) para retornar um novo conjunto contendo os elementos que estão presentes no conjunto original, mas não estão presentes no(s) conjunto(s) passado(s) como argumento.

.difference(outro_conjunto) retorna os elementos exclusivos do conjunto original.
Não altera o conjunto original, apenas retorna um novo conjunto.
É equivalente ao operador de subtração de conjuntos: conjunto_a - conjunto_b."""