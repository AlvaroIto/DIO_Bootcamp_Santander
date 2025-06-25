'''
São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo:
op_compracao + op_logico + op_comparacao...N...

Exemplo
saldo = 1000
saque = 200
limite = 100


#Operador E
saldo >= saque and saque <= limite. # False


#Operador OU
saldo >= saque or saque <= limite # True


#Operador Negação
not 1000 > 1500 # True

contatos_emergencia = []
not contatos_emergencia # True, se contatos_emergencia for uma lista vazia

not "saque 1500;" # False

not"" # True

#Parênteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque # True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # True


'''
# AND = para ser True tudo tem que ser True
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# OR = para ser True só precisa de um True
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

saldo = 1000
saque = 250
limite = 200
conta_especial = True

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite 
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
exp = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp)  # True