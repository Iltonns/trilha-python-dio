def salvar_carro(marca, modelo, ano, placa): # Função com parâmetros posicionais
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # Chamada da função com parâmetros posicionais
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # Chamada da função com parâmetros nomeados
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # Chamada da função com parâmetros nomeados
