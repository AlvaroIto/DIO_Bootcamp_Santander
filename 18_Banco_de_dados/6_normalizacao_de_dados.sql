/*
Problema:
Desenvolver uma feature na qual sugerimos destino com base na cidaded do usário. Na criação da tabela usuário, o campo endereço está configurado de forma livre.
Ex:
    ID: 1 Nome: João Endereço: Rua A, 123, Cidade X, Estado Y
    ID: 2 Nome: Maria Endereço: Rua B, 345, Cidade Y, Estado Z
    ID: 3 Nome: Pedro Endereço: Rua C, 456, Cidade Z, Estado Y

Para evitar o tipo de dado inconsistente existe a normalização de dados

A normalização de dados é um processo no qual se organiza e estrutura um banco de dados relacional de forma a eliminar redundâncias e anomalias, garantindo a consistência e integridade dos dados.

Formas Normais
1FN: Atomicidade de dados
    A 1FN estabelece que cada valor em uma tabela deve ser atômico, ou seja, indivisível. Nenhum campo deve conter múltiplos valores ou lsitas. No seu caso, o campo "endereço" contém múltiplos valores, com rua, número, cidade e estado. Para atingir a 1FN, precisamos dividir o campo "endereço" em colunas separadas

Usuário
    id
    nome
    email
    senha
    data_nascimento
    rua
    numero 
    cidade
    estado
    pais

2FN
    A 2FN estabelece que uma tabela deve estar na 1FN
    Todos os atributos não chave devem depender totalemten da chave primária
    *Dica se sua tabela tem uma chave primária siples não existe a possibilidade de termos dependência parcial e por tanto ela já se econtra na 2FN

3FN
    Uma tabela deve estar na 2FN
    Nenhuma coluna não-chave depender de outra coluna não-chave
    Nosso exemplo: Relação Estado -> Cidade

*/

-- EXEMPLO NF1
-- Adicionar novas colunas (rua, numero, cidade estado), fazer a migração de dados para os campos corretos e por fim será removido a coluna endereço
-- criação das novas colunas na tabela usuario
ALTER TABLE usuarios
ADD rua VARCHAR(100), 
ADD numero VARCHAR(10),
ADD cidade VARCHAR(50),
ADD estado VARCHAR(20);

-- efetuar a divisão do endereço com substrings index
UPDATE usuarios
SET rua = SUBSTRINGS_INDEX(SUBSTRINGS_INDEX(endereco, ',', 1), ',', -1),
    numero = SUBSTRINGS_INDEX(SUBSTRINGS_INDEX(endereco, ',', 2), ',', -1),
    cidade = SUBSTRINGS_INDEX(SUBSTRINGS_INDEX(endereco, ',', 3), ',', -1),
    estaddo = SUBSTRINGS_INDEX(endereco, ',', -1),

-- remover coluna endereço
ALTER TABLE usuários
DROP COLUMN endereco;


