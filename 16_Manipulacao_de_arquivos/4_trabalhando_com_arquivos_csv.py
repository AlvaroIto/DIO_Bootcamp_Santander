'''
Arquivos CSV é um formato de arquivo amplamente utilizado para armazenar dados tabulares. CSV é a sigla para 'Comma Separated Values'

O Python fornece um módulo chamado 'csv' para lidar facilmente com arquivos csv

Exemplo:
import csv
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

Escrevendo em arquivos csv
from pathlib import Path
import csv

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / 'example.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['nome', 'idade'])
    writer.writerow(['João', '30'])
    writer.writerow(['Maria', '25'])

    
Práticas recomendadas
    Usar csv.reader e csv.writer para manipular arquivos CSV
    Fazer o tratamento correto das exceções
    Ao gravar arquivos CSV definir o argumento newline='' no método 'open'


'''
from pathlib import Path
import csv

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / 'example.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['nome', 'idade'])
    writer.writerow(['João', '30'])
    writer.writerow(['Maria', '25'])
    

