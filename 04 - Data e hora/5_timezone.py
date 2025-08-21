# Importando as classes necessárias do módulo datetime
# - datetime: para trabalhar com datas e horas
# - timedelta: para representar diferenças de tempo
# - timezone: para trabalhar com fusos horários
from datetime import datetime, timedelta, timezone

# Criando um objeto datetime com fuso horário de Oslo (UTC+2)
# timedelta(hours=2) representa 2 horas à frente do UTC
# timezone() converte essa diferença em um objeto timezone
# datetime.now() obtém a data/hora atual no fuso especificado
data_oslo = datetime.now(timezone(timedelta(hours=2)))

# Criando um objeto datetime com fuso horário de São Paulo (UTC-3)
# timedelta(hours=-3) representa 3 horas atrás do UTC
# timezone() converte essa diferença em um objeto timezone
# datetime.now() obtém a data/hora atual no fuso especificado
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

# Exibindo as datas e horas nos diferentes fusos horários
print(data_oslo)      # Data/hora atual em Oslo (UTC+2)
print(data_sao_paulo) # Data/hora atual em São Paulo (UTC-3)
