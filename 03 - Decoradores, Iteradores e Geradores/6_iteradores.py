# =============================================================================
# IMPLEMENTAÇÃO DE UM ITERADOR PERSONALIZADO EM PYTHON
# =============================================================================
# Este código demonstra como criar uma classe iterável personalizada
# que implementa o protocolo de iteração do Python

class MeuIterador:
    """
    Classe que implementa um iterador personalizado.
    Um iterador é um objeto que permite percorrer uma sequência de dados
    elemento por elemento, um de cada vez.
    """
    
    def __init__(self, numeros: list[int]):
        """
        Construtor da classe.
        
        Args:
            numeros (list[int]): Lista de números inteiros que será iterada
        """
        self.numeros = numeros      # Armazena a lista de números
        self.contador = 0           # Controla a posição atual na iteração

    def __iter__(self):
        """
        Método obrigatório para tornar a classe iterável.
        Retorna o próprio objeto, pois esta classe já é um iterador.
        
        Returns:
            self: O próprio objeto iterador
        """
        return self

    def __next__(self):
        """
        Método obrigatório para implementar o protocolo de iteração.
        Retorna o próximo elemento da sequência ou levanta StopIteration
        quando não há mais elementos.
        
        Returns:
            int: O próximo número multiplicado por 2
            
        Raises:
            StopIteration: Quando não há mais elementos para iterar
        """
        try:
            # Obtém o número na posição atual
            numero = self.numeros[self.contador]
            # Avança para a próxima posição
            self.contador += 1
            # Retorna o número multiplicado por 2 (transformação personalizada)
            return numero * 2
        except IndexError:
            # Quando o índice está fora dos limites da lista,
            # significa que chegamos ao fim da iteração
            raise StopIteration


# =============================================================================
# TESTE DO ITERADOR PERSONALIZADO
# =============================================================================
# Demonstra como usar a classe MeuIterador em um loop for

print("Iterando sobre a lista [38, 13, 11] com multiplicação por 2:")
for i in MeuIterador(numeros=[38, 13, 11]):
    print(f"  {i}")

# =============================================================================
# EXPLICAÇÃO DO FUNCIONAMENTO:
# =============================================================================
# 1. O loop for chama iter() na classe MeuIterador
# 2. iter() retorna o próprio objeto (que já é um iterador)
# 3. O loop chama next() repetidamente até receber StopIteration
# 4. Cada chamada de next() retorna o próximo número * 2
# 5. Quando não há mais números, StopIteration é levantado e o loop para
#
# Resultado esperado:
#   76  (38 * 2)
#   26  (13 * 2)
#   22  (11 * 2)
