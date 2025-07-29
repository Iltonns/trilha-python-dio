contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

#Acessando um valor inesistente no dicionário
resultado = contatos.get("chave")  # None
print(resultado)

#Acesssando um valor no dicionário e devolvendo um segundo argumento
resultado = contatos.get("chave", {})  # {}
print(resultado)

#Acesssando um valor no dicionário e devolvendo um segundo argumento
resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
