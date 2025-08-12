# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
# Para cada paciente, lê os dados (nome, idade, status) separados por vírgula e espaço
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)  # Converte a idade para inteiro
    pacientes.append((nome, idade, status))  # Adiciona uma tupla com os dados na lista de pacientes

# Ordenação por prioridade
# Cria uma lista apenas com pacientes urgentes
urgentes = [p for p in pacientes if p[2] == "urgente"]
# Ordena os pacientes urgentes pela idade (do maior para o menor)
urgentes.sort(key=lambda x: x[1], reverse=True)
# Extrai apenas os nomes dos pacientes urgentes
urgentes = [p[0] for p in urgentes]
# Cria uma lista com nomes de pacientes normais que são idosos (idade >= 60)
idosos = [p[0] for p in pacientes if p[2] == "normal" and p[1] >= 60]
# Cria uma lista com nomes de pacientes normais que não são idosos (idade < 60)
normais = [p[0] for p in pacientes if p[2] == "normal" and p[1] < 60]

# Combina as listas na ordem de prioridade: urgentes, idosos, normais
ordem = urgentes + idosos + normais

# Exibe a ordem de atendimento dos pacientes
print("Ordem de Atendimento:", ", ".join(ordem))

