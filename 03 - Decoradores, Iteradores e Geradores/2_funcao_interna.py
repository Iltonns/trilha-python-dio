# ==========================================
# FUNÇÕES ANINHADAS (NESTED FUNCTIONS)
# ==========================================
# Este código demonstra como definir funções dentro de outras funções
# em Python, criando um escopo local para essas funções internas

def principal():
    """
    Função principal que contém funções aninhadas.
    Demonstra o conceito de escopo local e funções aninhadas.
    """
    print("executando a funcao principal")

    # ==========================================
    # FUNÇÃO ANINHADA 1
    # ==========================================
    # Esta função só existe dentro do escopo da função 'principal'
    # Não pode ser chamada de fora da função 'principal'
    def funcao_interna():
        print("executando a funcao interna")

    # ==========================================
    # FUNÇÃO ANINHADA 2
    # ==========================================
    # Outra função aninhada que também só existe
    # dentro do escopo da função 'principal'
    def funcao_2():
        print("executando a funcao 2")

    # ==========================================
    # CHAMADAS DAS FUNÇÕES ANINHADAS
    # ==========================================
    # As funções aninhadas são chamadas dentro da função principal
    # Elas só podem ser executadas aqui, dentro do seu escopo
    funcao_interna()
    funcao_2()


# ==========================================
# EXECUÇÃO DO PROGRAMA
# ==========================================
# Chama a função principal, que por sua vez
# executa as funções aninhadas
principal()

# ==========================================
# CONCEITOS IMPORTANTES:
# ==========================================
# 1. FUNÇÕES ANINHADAS: Funções definidas dentro de outras funções
# 2. ESCOPO LOCAL: As funções internas só existem dentro da função externa
# 3. ENCAPSULAMENTO: As funções internas não podem ser acessadas de fora
# 4. ORGANIZAÇÃO: Útil para organizar código relacionado em um só lugar
# 5. CLOSURE: Base para criar closures (funções que "lembram" do escopo)
