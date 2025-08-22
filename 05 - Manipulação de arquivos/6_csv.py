# =============================================================================
# MANIPULAÇÃO DE ARQUIVOS CSV EM PYTHON
# =============================================================================
# Este script demonstra três formas diferentes de trabalhar com arquivos CSV:
# 1. Criação e escrita de um arquivo CSV
# 2. Leitura de um arquivo CSV usando índices de coluna
# 3. Leitura de um arquivo CSV usando nomes de coluna (DictReader)
# =============================================================================

# Importa o módulo csv para manipulação de arquivos CSV
import csv
# Importa Path para manipulação de caminhos de arquivo de forma segura
from pathlib import Path

# Define o caminho raiz como o diretório onde este script está localizado
ROOT_PATH = Path(__file__).parent

# Define constantes para os índices das colunas (para facilitar manutenção)
COLUNA_ID = 0      # Primeira coluna (índice 0)
COLUNA_NOME = 1    # Segunda coluna (índice 1)

# =============================================================================
# SEÇÃO 1: CRIANDO E ESCREVENDO UM ARQUIVO CSV
# =============================================================================
print("=== CRIANDO ARQUIVO CSV ===")

try:
    # Abre o arquivo 'usuarios.csv' para escrita ('w')
    # newline="" evita linhas em branco extras no Windows
    # encoding="utf-8" garante suporte a caracteres especiais
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        # Cria um objeto escritor CSV
        escritor = csv.writer(arquivo)
        
        # Escreve o cabeçalho (nomes das colunas)
        escritor.writerow(["id", "nome"])
        
        # Escreve as linhas de dados
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
        
    print("✓ Arquivo CSV criado com sucesso!")
    
except IOError as exc:
    # Trata erros de entrada/saída (ex: permissões, disco cheio)
    print(f"❌ Erro ao criar o arquivo: {exc}")

# =============================================================================
# SEÇÃO 2: LENDO UM ARQUIVO CSV USANDO ÍNDICES DE COLUNA
# =============================================================================
print("\n=== LENDO CSV COM ÍNDICES DE COLUNA ===")

try:
    # Abre o arquivo 'usuarios.csv' para leitura ('r')
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        # Cria um objeto leitor CSV
        leitor = csv.reader(arquivo)
        
        # Itera sobre cada linha do arquivo
        for idx, row in enumerate(leitor):
            # Pula o cabeçalho (primeira linha, índice 0)
            if idx == 0:
                continue
            
            # Acessa as colunas usando índices numéricos
            print(f"ID: {row[COLUNA_ID]}")      # row[0] - primeira coluna
            print(f"Nome: {row[COLUNA_NOME]}")   # row[1] - segunda coluna
            print("-" * 20)
            
except IOError as exc:
    # Trata erros de entrada/saída
    print(f"❌ Erro ao ler o arquivo: {exc}")

# =============================================================================
# SEÇÃO 3: LENDO UM ARQUIVO CSV USANDO NOMES DE COLUNA (DictReader)
# =============================================================================
print("\n=== LENDO CSV COM NOMES DE COLUNA (DictReader) ===")

try:
    # Abre o arquivo 'usuarios.csv' para leitura
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        # Cria um leitor CSV que usa nomes de coluna como chaves
        # DictReader automaticamente usa a primeira linha como cabeçalho
        reader = csv.DictReader(csvfile)
        
        # Itera sobre cada linha do arquivo
        for row in reader:
            # Acessa as colunas usando nomes (mais legível e menos propenso a erros)
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
            print("-" * 20)
            
except IOError as exc:
    # Trata erros de entrada/saída
    print(f"❌ Erro ao ler o arquivo: {exc}")

print("\n=== PROGRAMA FINALIZADO ===")
