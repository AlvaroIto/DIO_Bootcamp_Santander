'''
Conhecer métodos uteis para manipular objetos do tipo sting, como interpolar valores de variáveis e entender como funciona o fatiamento.

A classe string do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples

curso = 'pYtHon'

print(curso.upper())
>>> PYTHON

print(curso.lower())
>>> python

print(curso.title())
>>> Pytthon

# Espaços em branco
curso = '     Python  '

print(curso.strip())
>>> 'Python'

print(curso.lstrip())
>>> 'Python  '

print(curso.rstrip())
>>> '    Python'

# Junções e centralização
curso = 'Python'

print(curso.center(10, '#'))
>>> '##Python##'

print('.'.join(curso))
>>> 'P.y.t.h.o.n'

'''

menu = 'Python'

print('####' + menu + '####')
print(menu.center(14))
print(menu.center(14, '#'))
print('-'.join(menu))

