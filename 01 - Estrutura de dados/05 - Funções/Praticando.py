# Função para determinar a prioridade do paciente
def get_priority(paciente):
    _, idade, status = paciente
    if status.lower() == "urgente":
        return 0  # Prioridade máxima
    elif idade > 60:
        return 1  # Prioridade alta
    else:
        return 2  # Prioridade normal

# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for i in range(n):
    entrada = input().strip().split(", ")
    nome = entrada[0]
    idade = int(entrada[1])
    status = entrada[2]
    pacientes.append((nome, idade, status, i))  # Adiciona índice para manter ordem de chegada

# Ordenar os pacientes: primeiro por prioridade, depois por ordem de chegada
pacientes_ordenados = sorted(pacientes, key=lambda x: (get_priority(x), x[3]))

# Extrair apenas os nomes na ordem correta
nomes_ordenados = [paciente[0] for paciente in pacientes_ordenados]

# Formatar a saída
print("Ordem de Atendimento:", ", ".join(nomes_ordenados))
