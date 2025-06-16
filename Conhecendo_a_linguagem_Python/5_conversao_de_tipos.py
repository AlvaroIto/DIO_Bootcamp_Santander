"""
Convertando tipos

Em alguns momentos será necessário converter o tipo de uma variável para manipular de forma diferente.Por exemplo:
Variáveis do tipo string, que armazenam textos, podem ser convertidas para números inteiros ou de ponto flutuante para realizar cálculos matemáticos.


#Inteiro para float
preco = 10
print(preco)

preco = float(preco)
print(preco)


#Float para inteiro
preco = 10.30
print(preco)

preco = int(preco)
print(preco)


#Numérico para string
preco = 10.30
idade = 28

preco = str(preco)
idade = str(idade)

texto = f"O preço é {preco} e a idade é {idade}"
print(texto)


#String para numérico
preco = "10.30"
idade = "28"
print(float(preco))
print(int(idade))

"""