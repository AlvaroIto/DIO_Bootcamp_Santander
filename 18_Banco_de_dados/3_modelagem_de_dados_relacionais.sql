/*
Tabelas
Ela é usada para armazenar dados de forma organizada. Cada tabela em um banco de dados relacional tem um nome único e é dividida em colunas e linhas

Colunas
Uma coluna é uma estrutura de uma tabela que representa um atributo específico doos dados armazenados. Cada colunas tem um nome único e um tipo de dados associado que define o tipo de informação que pode ser armazenado nela, como números, texto, datas, etc.

Registros
Um registro, també conhecido como linha ou tupla, é uma instância individual de dados de uma tabela

Tipos de dados:
Os dados podem varia muito entre os diversos SGBD, os mais comuns são:
    - Inteiro (Integer)
    - Decimal/Numérico (Decimal/Numeric)
    - Caractere/Varchar (Character/Varchar)
    - Data/Hora (Date/Time)
    - Booleano (Boolean)
    - Texto longo (Text)

Comandos:
    - CREATE TABLE
        CREATE TABLE {{nome}}
            ({{coluna}} {{tipo}} {{opções}} COMMENT {{'COMENTARIO'}})

    - INSERT
        INSERT INTO
        {nome-tabela}
        ([coluna1, coluna2,...]) *** você pode ocultar as colunas
        VALUES
        ([valor-coluna1, valor-coluna2,...])
    
    - SELECT
        SELECT {{lista_colunas}}
        FROM tabela; 
    Onde * retorna todas as colunas
    Comandos: SELECT operadores:
        = igualdade
        <> ou != (desigualdade)
        > (maior que)
        < (menor que)
        >= (maior ou igual que)
        <= (menor ou igual que)
        LIKE (comparação de padrões)
        IN (pertence a uma lista de valores)
        BETWEEN (dentro ded um intervalo)
        AND (e lógico)
        OR (ou lógico)

    - UPDATE
        UPDATE {{ tabela }}
        SET
        {{ coluna_1 }} = {{ novo_valor_1 }},
        {{ coluna_2 }} = {{ novo_valor_2 }}
        WHERE
        {{ condicao }};

    - DELETE
        DELETE FROM
        {{ tabela }}
        WHERE
        {{ condicao}};


Opções:
Restrição de valor:
    - NOT NULL
    - UNIQUE
    - DEFAULT
Chaves primárias e estrangeiras
Auto Incrementoo
*/

-- Criação da tabela usuários
CREATE TABLE usuarios (
    id INT, 
    nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
    email VARCHAR(100) NOT NULL UNIQUE COMMENT 'Email do usuário',
    endereco VARCHAR(50) NOT NULL COMMENT 'Endereço do usuário',
    data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário'
); 

-- Criação da tabela destinos
CREATE TABLE viagens.destinos (
    id INT,
    nome VARCHAR(255) NOT NULL UNIQUE COMMENT 'Nome do destino',
    descricao VARCHAR(255) NOT NULL COMMENT 'Descrição do destino'
);

-- Criação da tabela reservas
CREATE TABLE viagens.reservas (
    id INT COMMENT 'Identificador único da reserva',
    id_usuario INT COMMENT 'Referência ao ID do usuário que fez a reserva'
    id_destino INT COMMENT 'Referência ao ID do destino da reserva',
    data DATE COMMENT 'Data da reserva',
    status VARCHAR(255) DEFAULT 'pendente' COMMENT 'Status da reserva (confirmada, pendente, cancelada, etc)'
);

-- INSERT E SELECT
-- Inserir dados tabela usuarios
INSERT INTO usuarios (
    id,
    nome,
    email,
    data_nascimento,
    endereco
) VALUES (
    1, 
    "Fulano da Silva", 
    "fulano@email.com", 
    "1992-19-05", 
    "Av Brasil, 1 - Bairro Brasil/SP"
);
 
-- Inserir dados tabela destino
INSERT INTO destino (
    id,
    nome, 
    descricao
) VALUES (
    1, 'Praia do Brasil', 'Praia'
);

-- Inserir dados tabela reservas
INSERT INTO reserva (
    id,
    id_usuario,
    id_destino,
    status,
    data
) VALUES (
    1, 
    1, 
    1,
    'pendente',
    '2025-11-11'
);

-- SELECT
SELECT * FROM usuarios;  -- mostra todas os usuários do banco
SELECT * FROM destinos;  -- mostra todas os destinos do banco
SELECT * FROM reserva;  -- mostra todas os reservas do banco

SELECT * FROM usuarios
WHERE id = 1; -- mostra todos os usuários com ID 1

SELECT * FROM usuarios
WHERE id = 1 AND nome LIKE "%Fulano%"; -- mostra todos os usuários com ID 1 e nome Fulano

SELECT * FROM usuarios
WHERE id = 1 OR nome LIKE "%Ciclano%"; -- mostra todos os usuários com ID 1 ou nome Ciclano

-- atualziar campo
UPDATE usuarios
SET id = 4
WHERE email = 'teste@email.com';

-- excluir dado
DELETE FROM destino
WHERE nome = 'Praia do Brasil';



