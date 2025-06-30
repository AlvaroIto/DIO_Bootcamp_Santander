'''
Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizando o método format e a última é utlizando f strings.

A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, por esse motivo iremos focar nas 2 últimas.

Método format
nome = 'Fulano'
idade = 29
profissao = 'Programador'
linguagem = 'Python'

print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))

print('Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.'.format(nome, idade, profissao, linguagem))

print('Olá, me chamo {noome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.'.format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))


Método f string
nome = 'Fulano'
idade = 29
profissao = 'Programador'
linguagem = 'Python'

print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.')

formatar strings com f-string

PI = 3.14159

print(f'Valor de PI: {PI:.2f}')
>>> 'Valor de PI: 3.14

print(f'Valor de PI: {PI:10.2f}')
>>> 'Valor de PI:           3.14'

'''

