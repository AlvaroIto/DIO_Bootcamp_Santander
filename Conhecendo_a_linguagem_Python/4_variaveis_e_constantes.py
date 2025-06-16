"""
Variáveis
Em linguagens de programação, podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores são chamados de variáveis, pois eles nascem com um valor e não necessariamente permanecem com esse valor durante todo o tempo de execução do programa.

Alterando os valores
Perceba que não precisamos definir o tipo de dados da variável, o Python faz isso automaticamente. Podemos alterar o valor da variável a qualquer momento, e o Python irá entender que o tipo de dado também mudou.

Constantes
Assim como as variáveis, constantes são utilizadadas parar armazenar valores, mas diferentemente das variáveis, as constantes não podem ser alteradas durante a execução do programa.

Python não tem constantes
Não existe uma palavra reservada para informar  ao interpretador que o valor é constante. Em algumas linguagens de programação, como Java, C e C++, existem palavras reservadas para definir constantes. Em Python usamos a convenção de nomear constantes com letras maiúsculas, mas isso não impede que o valor seja alterado.

Boas praticas
- O padrão de nomes deve ser em snake_case, ou seja, palavras separadas por underline. Por exemplo: nome_completo, idade_usuario, valor_total.
- Escolher nomes sugestivos e descritivos para as variáveis, que indiquem claramente o que elas representam. Por exemplo: preco_produto, quantidade_estoque, nome_cliente.
- Nome de constantes todo em maissculas, por exemplo: TAXA_JUROS, LIMITE_SALARIO, NUMERO_MAXIMO.

"""
nome = "Fulano"
idade = 30

print(nome, idade)

limite_saque_diario = 1000.00

BRAZILIAN_STATES = ["SP", "RJ", "MG", "RS", "BA"]