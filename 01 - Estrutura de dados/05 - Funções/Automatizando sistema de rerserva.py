def processar_reservas():
    # Recebe a lista de quartos disponíveis como entrada do usuário, separando por espaço e convertendo para inteiro.
    # Usa set para facilitar a remoção e busca dos quartos.
    quartos_disponiveis = set(map(int, input().split()))
    
    # Recebe a lista de reservas solicitadas como entrada do usuário, separando por espaço e convertendo para inteiro.
    reservas_solicitadas = list(map(int, input().split()))

    # Inicializa listas para armazenar reservas confirmadas e recusadas.
    confirmadas = []
    recusadas = []

    # Para cada reserva solicitada, verifica se o quarto está disponível.
    for reserva in reservas_solicitadas:
        if reserva in quartos_disponiveis:
            # Se disponível, adiciona à lista de confirmadas e remove dos disponíveis.
            confirmadas.append(reserva)
            quartos_disponiveis.remove(reserva)
        else:
            # Se não disponível, adiciona à lista de recusadas.
            recusadas.append(reserva)

    # Exibe as reservas confirmadas e recusadas, separando os números por espaço.
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chama a função principal para executar o processamento de reservas
processar_reservas()