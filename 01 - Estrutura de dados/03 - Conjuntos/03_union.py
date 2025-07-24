conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)


"""O método .union() em Python é usado com conjuntos (tipo set) para unir dois ou mais conjuntos, retornando um novo conjunto que contém todos os elementos distintos presentes em qualquer um dos conjuntos envolvidos.

Não altera os conjuntos originais.
Aceita múltiplos argumentos: a.union(b, c, d, ...)
Elementos duplicados são removidos automaticamente, pois conjuntos não permitem duplicatas."""