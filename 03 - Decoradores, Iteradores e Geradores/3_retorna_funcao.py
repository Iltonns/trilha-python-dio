# ==========================================
# FUNÇÕES QUE RETORNAM OUTRAS FUNÇÕES
# ==========================================
# Este exemplo demonstra o conceito de "closure" e funções de ordem superior
# onde uma função retorna outra função como resultado

def calculadora(operacao):
    """
    Função que retorna uma função específica baseada na operação fornecida.
    Esta é uma implementação de "factory function" - uma função que cria outras funções.
    
    Args:
        operacao (str): String representando a operação matemática ("+", "-", "*", "/")
    
    Returns:
        function: Uma função que executa a operação matemática especificada
    """
    
    # Funções internas (nested functions) que realizam as operações matemáticas
    def soma(a, b):
        """Função interna para adição"""
        return a + b

    def sub(a, b):
        """Função interna para subtração"""
        return a - b

    def mul(a, b):
        """Função interna para multiplicação"""
        return a * b

    def div(a, b):
        """Função interna para divisão"""
        return a / b

    # Usando match/case (Python 3.10+) para retornar a função apropriada
    # baseada na operação solicitada
    match operacao:
        case "+":
            return soma      # Retorna a função soma (sem executá-la)
        case "-":
            return sub       # Retorna a função sub (sem executá-la)
        case "*":
            return mul       # Retorna a função mul (sem executá-la)
        case "/":
            return div       # Retorna a função div (sem executá-la)


# ==========================================
# EXEMPLOS DE USO
# ==========================================

# Obtém a função de soma da calculadora
op = calculadora("+")
print(f"A Soma é: {op(2, 2)}")  # Executa a função retornada com os argumentos 2 e 2

# Obtém a função de subtração da calculadora
op = calculadora("-")
print(f"A Subtração é: {op(2, 2)}")  # Executa a função retornada com os argumentos 2 e 2

# Obtém a função de multiplicação da calculadora
op = calculadora("*")
print(f"A Multiplicação é: {op(2, 2)}")  # Executa a função retornada com os argumentos 2 e 2

# Obtém a função de divisão da calculadora
op = calculadora("/")
print(f"A Divisão é: {op(2, 2)}")  # Executa a função retornada com os argumentos 2 e 2

# ==========================================
# CONCEITOS IMPORTANTES
# ==========================================
# 1. Closure: As funções internas têm acesso ao escopo da função externa
# 2. Factory Function: calculadora() é uma função que "fabrica" outras funções
# 3. Função de Ordem Superior: calculadora() recebe uma string e retorna uma função
# 4. Lazy Evaluation: As operações não são executadas até que a função retornada seja chamada
