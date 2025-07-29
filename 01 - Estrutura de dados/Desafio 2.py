"""Crie um sistema de carrinho de compra que permita adicionar produtos e calcular o valor total da compra.

# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# Exibe os itens do carrinho
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")

# Exibe o total da compra
print(f"Total: R${total:.2f}")"""




# Melhorias sugeridas:
# 1. Validar a entrada do usuário para evitar erros em caso de dados inválidos.
# 2. Permitir remover itens do carrinho, se desejado.
# 3. Utilizar funções para modularizar o código.
# 4. Adicionar tratamento de exceções para conversão de preço.
# 5. Permitir adicionar quantidades para cada produto.
# 6. Exibir uma mensagem amigável caso o carrinho esteja vazio.


# Define uma função para adicionar um item ao carrinho
def adicionar_item(carrinho):
    """
    Adiciona um item ao carrinho, validando a entrada e tratando exceções.
    """
    while True:
        try:
            # Solicita ao usuário os dados do produto
            linha = input("Digite o produto, preço e quantidade (ex: 'Arroz 10.50 2'): ").strip()
            if not linha:
                print("Entrada vazia. Tente novamente.")
                continue

            # Separa a string nas 3 últimas partes: nome, preço e quantidade
            partes = linha.rsplit(" ", 2)
            if len(partes) != 3:
                print("Formato inválido. Use: nome preço quantidade")
                continue

            nome, preco_str, qtd_str = partes
            # Converte o preço para float, tratando vírgulas como pontos
            preco = float(preco_str.replace(",", "."))
            # Converte a quantidade para inteiro
            quantidade = int(qtd_str)

            # Valida se os valores são positivos
            if preco < 0 or quantidade <= 0:
                print("Preço deve ser positivo e quantidade maior que zero.")
                continue

            # Adiciona o produto ao carrinho como dicionário
            carrinho.append({"nome": nome, "preco": preco, "quantidade": quantidade})
            print(f"Produto '{nome}' adicionado com sucesso!")
            break
        except ValueError:
            # Trata erros de conversão para float/int
            print("Preço ou quantidade inválidos. Tente novamente.")

# Define uma função para remover itens do carrinho
def remover_item(carrinho):
    """
    Permite remover um item do carrinho pelo nome.
    """
    if not carrinho:
        print("Carrinho vazio. Nada para remover.")
        return

    nome = input("Digite o nome do produto a remover: ").strip()
    for i, item in enumerate(carrinho):
        if item["nome"].lower() == nome.lower():
            carrinho.pop(i)
            print(f"Produto '{nome}' removido do carrinho.")
            return
    print(f"Produto '{nome}' não encontrado no carrinho.")

# Define uma função para exibir o conteúdo do carrinho
def exibir_carrinho(carrinho):
    """
    Exibe os itens do carrinho e o total da compra.
    """
    if not carrinho:
        print("Seu carrinho está vazio!")
        return

    total = 0.0
    print("\nItens no carrinho:")
    for item in carrinho:
        subtotal = item["preco"] * item["quantidade"]
        print(f"{item['nome']}: R${item['preco']:.2f} x {item['quantidade']} = R${subtotal:.2f}")
        total += subtotal
    print(f"Total: R${total:.2f}\n")

# Função principal do sistema de carrinho
def main():
    carrinho = []  # Lista que armazenará os produtos adicionados
    while True:
        # Exibe o menu de opções
        print("\nMenu:")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Exibir carrinho")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ").strip()

        # Direciona o fluxo com base na escolha do usuário
        if escolha == "1":
            adicionar_item(carrinho)
        elif escolha == "2":
            remover_item(carrinho)
        elif escolha == "3":
            exibir_carrinho(carrinho)
        elif escolha == "4":
            print("Saindo do sistema. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa somente se ele for chamado diretamente
if __name__ == "__main__":
    main()
