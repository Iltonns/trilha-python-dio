# Importando as classes necessárias do módulo datetime
# - date: para trabalhar apenas com datas (ano, mês, dia)
# - datetime: para trabalhar com data e hora completa
# - timedelta: para realizar operações de soma e subtração com datas
from datetime import date, datetime, timedelta

# Definindo o tipo de carro para calcular o tempo de serviço
# P = Pequeno, M = Médio, G = Grande
tipo_carro = "M"  # P, M, G

# Definindo os tempos de serviço em dias para cada tipo de carro
tempo_pequeno = 30    # Carros pequenos levam 30 dias
tempo_medio = 45      # Carros médios levam 45 dias
tempo_grande = 60     # Carros grandes levam 60 dias

# Obtendo a data e hora atual do sistema
data_atual = datetime.now()

# Estrutura condicional para calcular a data estimada de entrega
# baseada no tipo de carro
if tipo_carro == "P":
    # Para carros pequenos: soma 30 minutos da data atual
    # timedelta(minutes=30) cria um intervalo de 30 minutos
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    # Para carros médios: soma 45 minutos da data atual
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    # Para carros grandes: soma 60 minutos da data atual
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


# Exemplo 1: Calculando a data de ontem
# date.today() retorna apenas a data atual (sem hora)
# timedelta(days=1) cria um intervalo de 1 dia
# A subtração retorna a data de ontem
print(date.today() - timedelta(days=1))

# Exemplo 2: Calculando uma hora antes de um horário específico
# datetime(2023, 7, 25, 10, 19, 20) cria uma data/hora específica
# timedelta(hours=1) cria um intervalo de 1 hora
# A subtração retorna o horário de 1 hora antes
# .time() extrai apenas a parte do horário (HH:MM:SS)
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

# Exemplo 3: Obtendo apenas a data atual (sem hora)
# datetime.now() retorna data e hora atual
# .date() extrai apenas a parte da data (ano-mês-dia)
print(datetime.now().date())
