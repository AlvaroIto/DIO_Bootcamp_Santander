"""
Função input

A função builtin input é utlizada quando queremos ler dados da entrada padrão (teclado). ela retorna uma string, mesmo que o usuário digite um número. Para converter o valor lido para outro tipo, é necessário utilizar as funções de conversão de tipos.
Exemplo:
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

Função print
A função builtin print é utilizada para exibir dados na saída padrão (tela). Ela recebe um ou mais argumentos e os exibe na tela, separados por espaços. É possível formatar a saída utilizando f-strings ou o método format.
Exemplo:
nome = "João"
sobrenome = "Silva"
print(nome, sobrenome)  # Exibe: João Silva
print(nome, sobrenome, end="...\n")  # Exibe: João Silva...
print(nome, sobrenome, sep="-")  # Exibe: João-Silva

"""