/*
Junções: JOINs
São usadas no SQL para combinar dados de duas ou mais tabelas relacionadas em uma única consulta
Tipo:
    - INNER JOIN
    - LEFT JOIN ou LEFT OUTER JOIN
    - RIGHT JOIN ou RIGHT OUTER JOIN
    - FULL JOIN ou FULL OUTER JOIN

Inner Join
Retorna apenas as linhas que têm correspondência em ambas as tabelas envolvidas na junção. A junção é feita com base em uma condição de igualdade especificada na cláusula ON.

SELECT *
FROM tabela1
INNER JOIN tabe2 on tabela1.coluna = tabela2.coluna;

Left join
Retorna todas as linhas da tabela à esquerda da junção e as linhas correspondente da tabela à direita. Se não houver correspondência, os valores da tabela à direita serão NULL.

SELECT *
FROM tabela1
LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

Right join
Retorna todas as linhas da tabela à direita da junção e as linhas correspondente da tabela à esquerda. Se não houver correspondência, os valores da tabela à direita serão NULL.

Full join
Retorna todas as linhas de ambas as tabelas envolvidas na junção, combinando-as com base em uma condição de igualdade. Se não hoouver correspondência, os valores ausentes serão preenchidos com NULL

SELECT *
FROM tabela1
FULL JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

Sub Consultas
Elas permitem realizar consultas mais complexas permitindo que você use o resultado de uma consulta como entrada para outra consulta

mostrar destinos que não possuem reservas
SELECT * FROM destinos
WHERE id NOT IN (SELECT destino id_destino FROM reservas);

mostrar usuario que não possui reservas
SELECT * FROM usuarios
WHERE id NOT IN (SELECT destino id_usuario FROM reservas);

mostrar a quantidade de reservas de um usuario
SELECT nome, (SELECT COUNT(*) FROM reservas WHERE id_usuario = usuarios.id) AS total_reservas FROM usuarios;

*/

-- Exemplo inner Join - Verificar informação da reserva e informaçãoes de destino
SELECT * FROM usuarios us
INNER JOIN reserva rs ON us.id = rs.id_usuario
INNER JOIN destino ds ON rs.id_destino = ds.id;


-- 