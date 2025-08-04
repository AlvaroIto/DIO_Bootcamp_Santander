'''
Aprender a importância dos arquivos, como abrir, ler, escrever e gerenciar arquivos em Python. Utilizaremos os formatos txt e csv

Os arquivos são essenciais para qualquer tipo de programação, pois fornecem um meio de armazenar e recuperar dados. Através da manipulação de arquivos, podemos persistir oos dados além da vida útil de um programa específico.

Um arquivo é um container no computador onde as informações são armazenadas em formato digital. Existem ddois tipos de arquivos que podemos manipular em Python: arquivoos dde texto e arquivos binários.


Abrindo e fechando arquivos
Para manipular arquivos em Python, primeiro precisamos abri-los. Usamos a função 'open()' para isso. Quano terminamos de trabalhar com o arquivo, usamos a função 'close()' para liberar recursos

Exemplo:
file = open('example.txt', 'r')
# ... fazemos algo com o arquivo ...
file.close()

Existem diferentes modos para abrir um arquivo, como somente leitura ('r'), gravação('w') e anexar('a'). O modo de abertura deve ser escolhido de acordo com a operação que iremos realizar.

# para ler um arquivo
file = open('example.txt', 'r')
# para escrever em um arquivo
file = open('example.txt', 'w')
# para anexar conteúdo a um arquivo existente
file = open('example.txt', 'a')


Lendo um arquivo
Python fornece várias maneiras de ler um arquivo. Podemos usar 'read()', 'realine()' ou 'readlines()' dependendo de nosssas necessidades

# ler todo o conteúdo do arquivo de uma vez
file = open('example.txt', 'r')
print(file.read())
file.close()

O método 'readline()' lê uma linha por vez, enquanto o 'readlines()' retorna uma lista onde cada elemento é uma linha do arquivo.


Escrevendo em um arquivo
Podemos usar 'write()' ou 'writelines()' para escrever em um arquivo. Lembre-se, no entanto ded abrir o arquivo no modo correto.
Exemplo
file = open('example.txt', 'w')
file.write('olá, mundo!')
file.close()


Gerenciando arquivos e diretórios
Python também oferece funções para gerenciar arquivos de diretórios. Podemos criar, renomear e excluir arquivos e diretórios usando os módulos 'os' e 'shutil'.

import os
import shutil

#criar um diretório
os.mkdir('exemplo')
#renomear um arquivo
os.rename('old.txt', 'new.txt')
#remover um arquivo
os.remove('unwanted.txt')
#mover um arquivo
shutil.move('sourve.txt', 'destination.txt')


'''