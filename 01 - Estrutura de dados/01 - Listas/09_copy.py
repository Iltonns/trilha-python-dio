lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]


"""O método copy() em Python cria uma cópia superficial (shallow copy) da lista original. Isso significa que ele retorna uma nova lista com os mesmos elementos, mas referências para objetos mutáveis (como listas internas) ainda apontam para os mesmos objetos.

Alterações em objetos mutáveis dentro da lista original ou da cópia afetam ambas. Para cópias profundas (deep copy), use o módulo copy com copy.deepcopy()."""