/*
Funções agregadas são funções que realizam algum tipo de pre-processamento ou cálculo nas colunas retornando algum valor
    - COUNT: Contas os número de registros
    - SUM: Soma os valores de uma coluna numérica
    - AVG: Calcula a média dos valores de uma coluna numérica
    - MIN: Retorna o valor mínimo de uma coluna
    - MAX: Retorna o valor máximo de uma coluna

Agrupamento de resultados é usado para dividir os dados em grupos de acordo com algum tipo de critério
    - SELECT
    - FROM
    - GROUP BY

Ordenação de Resultado - ordena os dados por algum critério por exemplo ordernar por ordem alfabética, idade...
    - SELECT
    - FROM
    - ORDER BY


*/
-- Contar todos usuarios cadastrados
SELECT COUNT(*) as total_usuarios FROM usuarios;

-- contas apenas usuarios com reserva
SELECT COUNT(*) as total_usuarios FROM usuarios us
INNER JOIN reservas rs ON us.id = rs.id_usuario

-- usario com maioridade
SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS maior_idade FROM usuarios;

-- dedmonstrar quantidade de reservas para cada destino
SELECT COUNT (*), id_destino FROM reservas
GROUP BY id_destino;

-- ordernar o destino que mais tem reservas
SELECT COUNT (*) AS qtd_reservas, id_destino FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas DESC;
