'''
O que são operadores aritméticos?
Os operadores aritméticos executam operaçãoes matemáticas, como adição, subtração com operandos

# adição
print(1 + 1)  # Saída: 2

# subtração
print(2 - 1)  # Saída: 1

# multiplicação
print(2 * 3)  # Saída: 6

# divisão
print(6 / 3)  # Saída: 2.0

# divisão inteira
print(7 // 3)  # Saída: 2

# módulo (resto da divisão)
print(7 % 3)  # Saída: 1

# exponenciação
print(2 ** 3)  # Saída: 8


Na matemática existe uma regra que indica quais operações devem ser executadas primeiro. Isso é útil pois ao analisar uma expressão, a dependert da ordem das operações o valor pode ser diferente:

x = 10 - 5 * 2
x é igual a 10 ou 0? = 0

A defininão indica a seguinte ordem como a correta:
1. Parênteses
2. Exponenciação
3. Multiplicação e Divisão (da esquerda para a direita)
4. Adição e Subtração (da esquerda para a direita)

Exemplo:
print(10 - 5 * 2)  # Saída: 0
print((10 - 5) * 2)  # Saída: 10
print(10 ** 2 * 2)  # Saída: 200
print(10 ** (2 * 2))  # Saída: 10000
print(10 / 2 * 4)  # Saída: 20.0

'''

produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = 10 + 5 * 4
y = (10 / 2) + (25 * 2) - (2  ** 2)
print(x)
print(y)


