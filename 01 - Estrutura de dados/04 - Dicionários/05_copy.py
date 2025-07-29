contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

#Cria uma cópia do dicionário sem afetar o valor original
print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

#Cria uma cópia do dicionário sobscrevendo o valor desejado
print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}
