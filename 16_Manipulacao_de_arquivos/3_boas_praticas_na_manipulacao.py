'''
Bloco with
Use o gerenciamento de contexto (context manager) com a declaração 'with'. O gerenciamento de contexto permite trabalhar com arquivos de forma segura, garantinddo que eles sejam fechados corretamente, mesmo em caso de exceções.

Exemplo:
from pathlib import Path
ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / 'lorem.txt', 'r') as arquivo:
    # operações dde leitura/gravação no arquivo
    1/0

print(arquivo.read())

Verifique se o arquivo foi aberto com sucesso
É recomendado verificar se o arquivo foi aberto corretamente antes de executar operações ded leitura ou gravação nele

Exemplo:
from pathlib import Path
ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'nao_existe_lorem.txt', 'r') as arquivo:
        # operações dde leitura/gravação no arquivo
        print(arquivo.read())
except IOError as exc:
    print(f'Erro ao abrir o arquivo {exc}')


Use a codificação correta
Certifique-se dde usar a codificação correta ao ler ou gravar arquivos de texto. O argumento 'encoding' da função 'open()'
permite especificar a codificação.

Exemplo:
with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:

'''

