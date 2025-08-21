# Importando a classe datetime do módulo datetime
# Esta classe nos permite trabalhar com datas e horas
from datetime import datetime

# Obtendo a data e hora atual do sistema
# datetime.now() retorna um objeto datetime com a data/hora atual
data_hora_atual = datetime.now()

# Definindo uma string que representa uma data e hora específica
# Esta string está no formato ISO (YYYY-MM-DD HH:MM)
data_hora_str = "2023-10-20 10:20"

# Definindo máscaras de formatação para diferentes idiomas/formato
# %d = dia do mês (01-31)
# %m = mês (01-12) 
# %Y = ano com 4 dígitos
# %a = nome abreviado do dia da semana
mascara_ptbr = "%d/%m/%Y %a"

# Máscara para formato em inglês/ISO
# %Y = ano com 4 dígitos
# %m = mês (01-12)
# %d = dia do mês (01-31)
# %H = hora em formato 24h (00-23)
# %M = minuto (00-59)
mascara_en = "%Y-%m-%d %H:%M"

# Usando strftime para formatar a data/hora atual
# strftime = "string format time" - converte datetime para string formatada
# Aplica a máscara brasileira: dia/mês/ano + dia da semana abreviado
print(data_hora_atual.strftime(mascara_ptbr))

# Usando strptime para converter string em objeto datetime
# strptime = "string parse time" - converte string formatada para datetime
# Primeiro parâmetro: string com a data/hora
# Segundo parâmetro: máscara que define o formato da string
data_convertida = datetime.strptime(data_hora_str, mascara_en)

# Exibindo o objeto datetime convertido
print(data_convertida)

# Verificando o tipo do objeto retornado
# Deve ser <class 'datetime.datetime'>
print(type(data_convertida))
