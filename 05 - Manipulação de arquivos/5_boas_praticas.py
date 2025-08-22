# =============================================================================
# EXEMPLO DE BOAS PRÁTICAS PARA MANIPULAÇÃO DE ARQUIVOS EM PYTHON
# =============================================================================
# Este arquivo demonstra as melhores práticas para trabalhar com arquivos
# incluindo tratamento de erros, uso de context managers e encoding adequado

# Importando a biblioteca pathlib para manipulação de caminhos de forma moderna
# Path é mais robusto e cross-platform que os.path
from pathlib import Path

# Definindo o caminho raiz do diretório onde este script está localizado
# __file__ é uma variável especial que contém o caminho do arquivo atual
# .parent retorna o diretório pai (um nível acima)
ROOT_PATH = Path(__file__).parent

# =============================================================================
# EXEMPLO 1: LEITURA DE ARQUIVO COM TRATAMENTO DE ERRO BÁSICO
# =============================================================================
try:
    # Usando context manager (with) para garantir que o arquivo seja fechado automaticamente
    # ROOT_PATH / "1lorem.txt" concatena o caminho raiz com o nome do arquivo
    # "r" indica modo de leitura (read)
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        # Lendo todo o conteúdo do arquivo e exibindo na tela
        print(arquivo.read())
except IOError as exc:
    # Capturando erros de entrada/saída (arquivo não encontrado, sem permissão, etc.)
    # exc contém informações detalhadas sobre o erro
    print(f"Erro ao abrir o arquivo {exc}")

# =============================================================================
# EXEMPLO 2: ESCRITA DE ARQUIVO COM ENCODING UTF-8 (COMENTADO)
# =============================================================================
# Este exemplo está comentado para demonstração
# try:
#     # "w" indica modo de escrita (write) - sobrescreve o arquivo se existir
#     # encoding="utf-8" garante que caracteres especiais sejam salvos corretamente
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")

# =============================================================================
# EXEMPLO 3: LEITURA DE ARQUIVO COM ENCODING ESPECÍFICO E TRATAMENTO DUPLO
# =============================================================================
try:
    # Lendo arquivo especificando encoding UTF-8 para evitar problemas com caracteres especiais
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    # Tratando erros de entrada/saída (arquivo não encontrado, sem permissão)
    print(f"Erro ao abrir o arquivo {exc}")
except UnicodeDecodeError as exc:
    # Tratando erros específicos de decodificação de caracteres
    # Isso acontece quando o encoding especificado não consegue decodificar o conteúdo
    print(exc)

# =============================================================================
# RESUMO DAS BOAS PRÁTICAS IMPLEMENTADAS:
# =============================================================================
# 1. Uso de pathlib.Path para manipulação de caminhos (mais moderno e seguro)
# 2. Context managers (with) para garantir fechamento automático de arquivos
# 3. Tratamento específico de exceções (IOError, UnicodeDecodeError)
# 4. Especificação explícita de encoding para evitar problemas com caracteres
# 5. Uso de variáveis para caminhos, facilitando manutenção
# 6. Comentários explicativos para documentar o código
