# ==========================================
# OPERAÇÕES DE LEITURA DE ARQUIVOS EM PYTHON
# ==========================================
# Este código demonstra diferentes formas de ler um arquivo de texto
# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

# ==========================================
# MÉTODO 1: read() - Lê todo o arquivo de uma vez
# ==========================================
print("=== MÉTODO 1: read() ===")
print("Lê todo o conteúdo do arquivo como uma única string:")
arquivo = open(
    "05 - Manipulação de arquivos\lorem.txt", "r"  # "r" = modo de leitura (read)
)
print(arquivo.read())  # read() retorna todo o conteúdo como uma string
arquivo.close()  # Sempre feche o arquivo após o uso

# ==========================================
# MÉTODO 2: readline() - Lê apenas a primeira linha
# ==========================================
print("\n=== MÉTODO 2: readline() ===")
print("Lê apenas a primeira linha do arquivo:")
arquivo = open(
    "05 - Manipulação de arquivos\lorem.txt", "r"
)
print(arquivo.readline())  # readline() retorna apenas a primeira linha
arquivo.close()

# ==========================================
# MÉTODO 3: readlines() - Lê todas as linhas em uma lista
# ==========================================
print("\n=== MÉTODO 3: readlines() ===")
print("Lê todas as linhas e retorna uma lista:")
arquivo = open(
    "05 - Manipulação de arquivos\lorem.txt", "r"
)
print(arquivo.readlines())  # readlines() retorna uma lista onde cada elemento é uma linha
arquivo.close()

# ==========================================
# MÉTODO 4: readline() em loop - Lê linha por linha
# ==========================================
print("\n=== MÉTODO 4: readline() em loop ===")
print("Lê o arquivo linha por linha usando um loop:")
arquivo = open(
    "05 - Manipulação de arquivos\lorem.txt", "r"
)
# DICA: Usando o operador walrus (:=) para ler linha por linha
# O loop continua enquanto houver linhas para ler
# Quando readline() retorna uma string vazia (""), o loop para
while len(linha := arquivo.readline()):
    print(linha, end="")  # end="" evita linhas em branco extras

arquivo.close()

# ==========================================
# OBSERVAÇÕES IMPORTANTES:
# ==========================================
# 1. Sempre feche o arquivo após o uso com .close()
# 2. O modo "r" é para leitura (read)
# 3. read() é bom para arquivos pequenos
# 4. readlines() é útil quando você precisa trabalhar com as linhas individualmente
# 5. readline() em loop é eficiente para arquivos grandes
# 6. O operador walrus (:=) é uma funcionalidade do Python 3.8+
