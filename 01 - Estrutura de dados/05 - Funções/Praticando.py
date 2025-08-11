# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# Função para definir prioridade
def prioridade(paciente):
    nome, idade, status = paciente
    # Quanto maior o valor, maior a prioridade
    if status.lower() == "urgente":
        return (2, 0)  # Máxima prioridade
    elif idade > 60:
        return (1, 0)  # Prioridade média
    else:
        return (0, 0)  # Prioridade baixa

# Ordenar pacientes (reverse=True porque queremos maior prioridade primeiro)
pacientes_ordenados = sorted(pacientes, key=prioridade, reverse=True)

# Exibir resultado
ordem = [p[0] for p in pacientes_ordenados]
print("Ordem de Atendimento:", ", ".join(ordem))
