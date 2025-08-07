def exibir_mensagem(): # Função sem parâmetros
    print("Olá mundo!")


def exibir_mensagem_2(nome): # Função com parâmetro
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"): # Função com parâmetro opcional
    print(f"Seja bem vindo {nome}!")


exibir_mensagem() # Chamada da função sem parâmetros
exibir_mensagem_2(nome="Eleilton") # Chamada da função com parâmetro
exibir_mensagem_3() # Chamada da função com parâmetro opcional
exibir_mensagem_3(nome="Chappie") # Chamada da função com parâmetro opcional
