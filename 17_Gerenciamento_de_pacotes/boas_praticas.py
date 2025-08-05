'''
Python tem uma série de  convenções e melhores práticas codificadas em PEPs (Proposta de Melhoria do Python). A mais cnohecida destas é provavelmente a PEP 8, que cobre o estilo de codificação.

PEP 8 é o guia de estilo para codificação em Python. Ele inclui convenções sobre nomes de variáveis, uso ded espaços em branco, comprimento da linha e muitas outras coisas que ajudam a manter o código Python consistente e legível

Algumas das principais recomendações da PEP 8 incluem usar 4 espaços para identação, limitar as linhas a 79 caracteres, usar nomes de variáveis em snake_case para funções e variáveis, e CamelCase para classes

Exemplo
def somar(argumento_1, argumento_2):
    pass
    
class ContBancaria:
    pass
    
Para nos ajudar a seguir as recomendações da PEP8, podemos usar ferramentas de checagem de estilo como flake8. Essas ferramentas verificam nosso código e nos informam onde estamos desviando do guia de estilo

pip install flake8
flake8 meu_script.py

Black é uma ferramenta de formatação de código Python que segue a filosofia 'formato único'. Black reformata todo o seu arquivo em um estilo consistente, simplicando a tarefa de manter o código em conformiddade com a PEP 8.

pip install black
black meu_script.py

Isort é uma ferramente Python para classificar importações alfaveticamente e separá-las automaticamente em seções. Ele proporciona uma maneira rápida e fácil de ordenar e categorizar suas importações.

pip install isort
isort meu_script.py


'''