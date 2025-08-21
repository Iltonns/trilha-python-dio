# Importando as classes principais do módulo datetime
# - date: para trabalhar apenas com datas (ano, mês, dia)
# - datetime: para trabalhar com data e hora completa
# - time: para trabalhar apenas com horários (hora, minuto, segundo)
from datetime import date, datetime, time

# ===== TRABALHANDO COM DATAS (date) =====

# Criando uma data específica: ano=2023, mês=7 (julho), dia=10
# O mês deve ser um número de 1 a 12
data = date(2023, 7, 10)
print(f"Data criada: {data}")  # Exibe: 2023-07-10

# Obtendo a data atual do sistema
data_atual = date.today()
print(f"Data atual: {data_atual}")  # Exibe a data de hoje no formato YYYY-MM-DD

print()  # Linha em branco para separar as seções

# ===== TRABALHANDO COM DATA E HORA (datetime) =====

# Criando um datetime com data específica (sem especificar hora)
# Por padrão, a hora será 00:00:00 (meia-noite)
data_hora = datetime(2023, 7, 10)
print(f"Data e hora criada: {data_hora}")  # Exibe: 2023-07-10 00:00:00

# Obtendo a data e hora atual do sistema
data_hora_atual = datetime.today()
print(f"Data e hora atual: {data_hora_atual}")  # Exibe data e hora atual completa

print()  # Linha em branco para separar as seções

# ===== TRABALHANDO COM HORÁRIOS (time) =====

# Criando um horário específico: hora=17, minuto=23, segundo=0
# A hora deve ser de 0 a 23 (formato 24h)
# O minuto deve ser de 0 a 59
# O segundo deve ser de 0 a 59
hora = time(17, 23, 0)
print(f"Horário criado: {hora}")  # Exibe: 17:23:00

# ===== EXEMPLOS ADICIONAIS DE USO =====

# Criando datetime com data e hora específicas
data_hora_completa = datetime(2023, 7, 10, 14, 30, 45)
print(f"Data e hora completa: {data_hora_completa}")  # Exibe: 2023-07-10 14:30:45

# Criando time com microssegundos
hora_precisa = time(12, 15, 30, 500000)  # 500000 microssegundos = 0.5 segundos
print(f"Horário com microssegundos: {hora_precisa}")  # Exibe: 12:15:30.500000
