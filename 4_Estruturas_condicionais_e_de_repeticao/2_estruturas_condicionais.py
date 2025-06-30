'''
A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

If
Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilziar a palavra reservada if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.

Exemplo:
saldo = 1000.0
saque = float(input('Digite o valor do saque: '))

if saldo >= saque:
    print('Saque realizado com sucesso!')
if saldo < saque:
    print('Saldo insuficiente para realizar o saque.')

If / else
Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário, o bloco de código do else será executado.

Exemplo:
saldo = 1000.0
saque = float(input('Digite o valor do saque: '))

if saldo >= saque:
    print('Saque realizado com sucesso!')
else:
    print('Saldo insuficiente para realizar o saque.')

If / elif / else
Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif, o elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas podem dificultar a leitura do código.

Exemplo:
opcao = int(input('Informe a opção: [1] Sacar \n[2] Extrato: '))
if opcao == 1:
    valor = float(input('Digite o valor do saque: '))
    #... # lógica de saque
elif opcao == 2:
    print('Exibindo extrato...')
else:
    print('Opção inválida!')


If aninhado
Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro de outras estruturas if/elif/else.

Exemplo:
if  conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com cheque especial!')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    else:
        print('saldo insuficiente')

If ternário
O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida

Exemplo:
status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} ao realizar o saque')

'''