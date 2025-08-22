# Importando a biblioteca pathlib para manipulação de caminhos de forma mais robusta
from pathlib import Path

# Definindo o caminho raiz do projeto (diretório onde este arquivo está localizado)
ROOT_PATH = Path(__file__).parent

# =============================================================================
# EXEMPLO 1: Tratamento de erros ao abrir um arquivo
# =============================================================================

# Bloco try-except para capturar diferentes tipos de erros que podem ocorrer
# ao tentar abrir um arquivo
try:
    # Tentando abrir um arquivo para leitura ("r" = read)
    # O caminho é construído concatenando ROOT_PATH + "novo-diretorio" + "novo.txt"
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
    
except FileNotFoundError as exc:
    # Este erro ocorre quando o arquivo especificado não existe no caminho
    print("Arquivo não encontrado!")
    print(exc)  # Imprime a mensagem de erro detalhada
    
except IsADirectoryError as exc:
    # Este erro ocorre quando tentamos abrir um diretório como se fosse um arquivo
    print(f"Não foi possível abrir o arquivo: {exc}")
    
except IOError as exc:
    # Este erro captura problemas gerais de entrada/saída (I/O)
    # Por exemplo: permissões insuficientes, disco cheio, etc.
    print(f"Erro ao abrir o arquivo: {exc}")
    
except Exception as exc:
    # Este é um capturador genérico que pega qualquer outro tipo de erro
    # que não foi capturado pelos excepts anteriores
    # É uma boa prática para garantir que nenhum erro passe despercebido
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")

# =============================================================================
# EXEMPLO 2: Código comentado demonstrando outro cenário de erro
# =============================================================================

# Código comentado que demonstra o que aconteceria se tentássemos
# abrir um diretório ao invés de um arquivo
# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")  # Tentando abrir um diretório
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")

# =============================================================================
# OBSERVAÇÕES IMPORTANTES:
# =============================================================================
# 1. A ordem dos excepts é importante: sempre coloque os erros mais específicos primeiro
# 2. Exception deve ser sempre o último, pois captura qualquer erro
# 3. É uma boa prática usar 'as exc' para capturar a mensagem de erro
# 4. Sempre feche os arquivos após o uso (arquivo.close()) ou use 'with' statement
# 5. O Path(__file__).parent retorna o diretório onde este arquivo está localizado
