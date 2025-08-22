# Importando módulos necessários para manipulação de arquivos e diretórios
import os          # Módulo para operações do sistema operacional
import shutil      # Módulo para operações de alto nível com arquivos
from pathlib import Path  # Classe para manipulação de caminhos de forma orientada a objetos

# Definindo o caminho raiz como o diretório onde este script está localizado
# __file__ é uma variável especial que contém o caminho do arquivo atual
ROOT_PATH = Path(__file__).parent

# ===== OPERAÇÕES COM DIRETÓRIOS =====

# Criando um novo diretório chamado "novo-diretorio" no caminho raiz
# os.mkdir() cria um diretório único (não cria diretórios pai se não existirem)
os.mkdir(ROOT_PATH / "novo-diretorio")

# ===== OPERAÇÕES COM ARQUIVOS =====

# Criando um novo arquivo chamado "novo.txt" no caminho raiz
# O modo "w" (write) cria o arquivo se não existir, ou sobrescreve se existir
arquivo = open(ROOT_PATH / "novo.txt", "w")
# É importante fechar o arquivo após o uso para liberar recursos do sistema
arquivo.close()

# ===== OPERAÇÕES DE RENOMEAR E REMOVER =====

# Renomeando o arquivo "novo.txt" para "alterado.txt"
# os.rename() move/renomeia arquivos ou diretórios
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# Removendo o arquivo "alterado.txt" do sistema de arquivos
# os.remove() deleta permanentemente o arquivo (não vai para a lixeira)
os.remove(ROOT_PATH / "alterado.txt")

# ===== OPERAÇÕES COM SHUTIL =====

# Movendo um arquivo para dentro de um diretório usando shutil.move()
# shutil.move() é mais robusto que os.rename() para operações complexas
# Esta operação move o arquivo "novo.txt" para dentro do diretório "novo-diretorio"
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")

# NOTA: Este código tem um problema lógico - tenta mover "novo.txt" que foi deletado
# Para funcionar corretamente, seria necessário criar o arquivo novamente antes de movê-lo
