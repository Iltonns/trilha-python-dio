# =============================================================================
# EXEMPLO DE DECORADOR COM ARGUMENTOS
# =============================================================================
# Este código demonstra como criar e usar decoradores em Python
# Um decorador é uma função que modifica o comportamento de outra função

def meu_decorador(funcao):
    """
    Decorador que executa código antes e depois da função decorada.
    
    Args:
        funcao: A função que será decorada
    
    Returns:
        envelope: Uma nova função que envolve a função original
    """
    
    def envelope(*args, **kwargs):
        """
        Função interna que envolve a função original.
        Esta função será executada no lugar da função decorada.
        
        Args:
            *args: Argumentos posicionais passados para a função
            **kwargs: Argumentos nomeados passados para a função
        
        Returns:
            O resultado da função original
        """
        # Executa código ANTES da função original
        print("faz algo antes de executar")
        
        # Chama a função original com todos os argumentos recebidos
        resultado = funcao(*args, **kwargs)
        
        # Executa código DEPOIS da função original
        print("faz algo depois de executar")
        
        # Retorna o resultado da função original
        return resultado

    # Retorna a função envelope (que substituirá a função original)
    return envelope


# =============================================================================
# USANDO O DECORADOR
# =============================================================================
# A sintaxe @meu_decorador é equivalente a:
# ola_mundo = meu_decorador(ola_mundo)

@meu_decorador
def ola_mundo(nome, outro_argumento):
    """
    Função simples que será decorada pelo meu_decorador.
    
    Args:
        nome: Nome para cumprimentar
        outro_argumento: Argumento adicional (não usado neste exemplo)
    
    Returns:
        O nome em maiúsculas
    """
    print(f"Olá mundo {nome}!")
    return nome.upper()


# =============================================================================
# TESTANDO O DECORADOR
# =============================================================================

# Chama a função decorada
# O decorador executará o código antes e depois da função
resultado = ola_mundo("João", 1000)
print(f"Resultado retornado: {resultado}")

# Mostra que a função foi substituída pela função envelope
# Isso demonstra que o decorador realmente modificou a função original
print(f"Tipo da função após decorar: {ola_mundo}")
print(f"Nome da função: {ola_mundo.__name__}")

# =============================================================================
# SAÍDA ESPERADA:
# =============================================================================
# faz algo antes de executar
# Olá mundo João!
# faz algo depois de executar
# Resultado retornado: JOÃO
# Tipo da função após decorar: <function meu_decorador.<locals>.envelope at 0x...>
# Nome da função: envelope
