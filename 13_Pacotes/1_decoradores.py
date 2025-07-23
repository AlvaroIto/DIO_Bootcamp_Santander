'''
#########################################################################
Funções em Python são objetos dde primeira classe. Isso significa que as funções podem ser passadas e usadas como argumentos.

def dizer_oi(nome):
    return f'Oi {nome}'

def incentivar_aprender(nome):
    return f'Oi {nome}, vamos aprender Python juntos!'

def mensagem_para_fulano(funcao_mensagem):
    return funcao_mensagem('Fulano')

mensagem_para_fulano(dizer_oi)
mensagem_para_fulano(incentivar_aprender)

#########################################################################
Inner functions - É possível definir funções dentro de outras funções. Tais funções são chamadas de funções internas.

def pai():
    print('Escrevendo da função pai()')

    def filho1():
        print('Escrevendo da função filho1()')

    def filho2():
        print('Escrevendo da função filho2()')

    filho2
    filho1

pai()

#########################################################################
Python também permite que você use funções como valores de retorno

def calcular(operacao):
    def somar(a, b):
        return a + b
    
    def subrtrair(a, b):
        return a - b
    
    if operacao == '+':
        return somar
    else:
        return subrtrair
    
resultado = calcular('+')(1, 3)
print(resultado)

#########################################################################
Decoradores simples

def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar a função')
        funcao()
        print('Faz algo depois de executar a função')
    
    return envelope

def ola_mundo():
    print('Olá mundo!')

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

#########################################################################
Açúcar Sintático
O Python permite que você use decoradores de maneira mais simples com o símbolo @

def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar a função')
        funcao()
        print('Faz algo depois de executar a função')
    
    return envelope

@meu_decorador
def ola_mundo():
    print('Olá mundo!')

ola_mundo()

#########################################################################
Funções de decoração com argumentos

Podemos usar *args e **kwargs na função interna, com isso ela aceitará um número arbitrário de argumentos posicionais e de palavras-chave.

def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return envelope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')

aprender('Python')

#########################################################################
Retornando valores de funções decoradas

O decorador pode decidir se retorna o valor da função decorada ou não. Para que o valor seja retornado a função de envelope deve retornar o valor da função decorada.

def duplicar(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado

    return envelope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')
    return tecnologia.upper()

resultado = aprender('Python')
print(resultado)

#########################################################################
Introspecção
Introspecção é a capacidade de um objeto saber sobre seus próprios atributos em tempo de execução

import functools

def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado

    return envelope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')
    return tecnologia.upper()

resultado = aprender('Python')
print(resultado)
print(duplicar.__name__)

'''

