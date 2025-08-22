# ==========================================
# OPERAÇÕES DE ESCRITA EM ARQUIVOS
# ==========================================
# Este código demonstra como escrever dados em arquivos usando Python
# Vamos aprender diferentes métodos de escrita e boas práticas

# ==========================================
# 1. ABRINDO UM ARQUIVO PARA ESCRITA
# ==========================================
# O parâmetro "w" (write) abre o arquivo para escrita
# ⚠️ ATENÇÃO: Se o arquivo já existir, todo o conteúdo será sobrescrito!
# ⚠️ ATENÇÃO: Se o arquivo não existir, ele será criado automaticamente
arquivo = open(
    "C:\Users\eleil\OneDrive\Documents\GitHub\trilha-python-dio\05 - Manipulação de arquivos", "w"
)

# ==========================================
# 2. ESCREVENDO TEXTO SIMPLES
# ==========================================
# O método write() escreve uma string no arquivo
# Não adiciona quebra de linha automaticamente
arquivo.write("Escrevendo dados em um novo arquivo.")

# ==========================================
# 3. ESCREVENDO MÚLTIPLAS LINHAS
# ==========================================
# O método writelines() aceita uma lista de strings
# Cada elemento da lista é escrito sequencialmente
# Usamos "\n" para criar quebras de linha
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])

# ==========================================
# 4. FECHANDO O ARQUIVO
# ==========================================
# SEMPRE feche o arquivo após terminar de usá-lo
# Isso libera recursos do sistema e garante que os dados sejam salvos
arquivo.close()

# ==========================================
# BOAS PRÁTICAS E ALTERNATIVAS
# ==========================================
# 
# RECOMENDADO: Use o contexto 'with' para operações com arquivos
# Exemplo:
# with open("arquivo.txt", "w") as arquivo:
#     arquivo.write("Texto aqui")
#     # O arquivo é fechado automaticamente ao sair do bloco
#
# OUTROS MODOS DE ABERTURA:
# "a" - append (adiciona ao final do arquivo)
# "r+" - leitura e escrita
# "w+" - escrita e leitura (trunca o arquivo)
# "a+" - append e leitura
#
# ==========================================
