'''
Em Python, um iterador é um oobjeto que contém um número contável de valores que podem ser iterados, o que significa que você pode percorrer todos os valores. O protocolo do iterador é uma maneira do Python fazer a iteração de um objeto, que consiste em dois métodos especiais "__iter__()" e "__next__()"

Utilizamos para:
- Ler arquivos grandes.
    Economiza memória evitando carregar todas as linhas do arquivo. 
    Iterar linha a linha do arquivo.

Exemplo

'''
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'large_file.txt')

class FileIterator:
    def __init__(self, filename):
        self.file = open(filename)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.file.readline()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration



for line in FileIterator(file_path):
    print(line)