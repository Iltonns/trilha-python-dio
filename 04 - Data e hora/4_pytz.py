# Importando a classe datetime do módulo datetime para trabalhar com datas e horas
from datetime import datetime

# Importando a biblioteca pytz para trabalhar com fusos horários (timezones)
# pytz é uma biblioteca que fornece informações precisas sobre fusos horários
import pytz

# Criando um objeto datetime com o fuso horário de Oslo, Noruega
# pytz.timezone("Europe/Oslo") retorna um objeto timezone que representa o fuso horário de Oslo
# datetime.now() com um timezone retorna a data e hora atual naquele fuso horário específico
data = datetime.now(pytz.timezone("Europe/Oslo"))

# Criando um objeto datetime com o fuso horário de São Paulo, Brasil
# pytz.timezone("America/Sao_Paulo") retorna um objeto timezone que representa o fuso horário de São Paulo
# datetime.now() com um timezone retorna a data e hora atual naquele fuso horário específico
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

# Exibindo a data e hora atual no fuso horário de Oslo
print(data)

# Exibindo a data e hora atual no fuso horário de São Paulo
print(data2)
