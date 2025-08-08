def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def teste(a, b):
    return a * b + b * 3

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair)  # O resultado da operação 10 - 10 = 0
exibir_resultado(10, 10, teste)  # O resultado da operação 10 * 10 + 10 * 3 = 130