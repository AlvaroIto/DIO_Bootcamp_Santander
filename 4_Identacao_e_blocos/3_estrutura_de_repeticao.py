'''
São estruturas utilizadas para repetir um trecho de código um dedterminado número de vezes. Esse número pode ser conhecido previamente ou determinado através ded uma expressão lógica

Exemplo sem repetição
# Receba um número do teclado e exiba os 2 números seguintes

a = int(input('Informe um número inteiro: '))
print(a)

a += 1

a += 1
print(a)

Exemplo com repetição
a = int(input('Informe um número inteiro: '))
print(a)

repita 2 vezes:
    a += 1
    print(a)

Comando for
O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes qque nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

texto = input('informe um texto:')
vogais = 'AEIOU'

for letra in texto:
if letra.upper() in vogais:
print(letra, end='')

Função range
Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um inicio (inclusivo) para um fim (exclusivo). Se  usarmos range(i, j) será produzido: i, i+1, i+2,..., j-1
Ela recebe 3 argumentos: stop(obrigatório), start(opcional) e step(opcional)

list(range(4)) #saida: [0, 1, 2, 3]

Utilizanddo range com for
for numero in range(0, 11):
    print(numero, end='')
#saida: 0 1 2 3 4 5 6 7 8 9 10


While
O comando while é usadod para repetir um bloco ded código várias vezes. Faz sentido usar while quando não sabemos o número exato9 de vezes que nosso bloco de código deve ser executado

opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n:'))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibinddo extrato')
    else:
        print('Saindo')



'''
