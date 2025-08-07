/*
Chaves primárias
    - identifica exclusivamente
    - não pode conter valores nulos (NULL)
    - uma tabela pode ter apenas uma chave primária

Estrutura:
CREATE TABLE {{ tabela }}(
    id PRIMARY KEY AUTOINCREMENT,
    ...,
);

Caso a tabela esteja criada
ALTER TABLE {{ tabela }}
MODIFY COLUMN ID INT PRIMARY KEY;

Chaves estrangeiras
Ela é usada para estabelecer e manter a integridade dos ddados entre as tabela relacionadas
    - Pode ser nula (NOT NULL); ** registro órfão
    - É possível ter mais de uma (ou nenhuma) em uma tabela

Estrutura:
CREATE TABLE {{ tabela }}(
    id PRIMARY KEY AUTOINCREMENT,
    chave_estrangeira INT,
    FOREING KEY (chave_estrangeira) REFERENCES {{outra_tabela}} (id)
);

Caso a tabela esteja criada
ALTER TABLE {{ tabela }}
ADD CONSTRAINT {{ nome_constraint }}
FOREING KEY (ID_)
REFERENCES {{outra_tabela}} (ID)

Restrições:
    - ON DELETE especifica o que acontece com os registros dependentes quando um registro pai é excluído.
    - ON UPDATE define o comportamento dos registros dependentes quando um registro pai é utilizadoo
    - CASCADE, SET NULL, SET DEFAULT e RESTRICT
*/
-- criar chave primaria no id e auto incremento
ALTER Table usuarios
MODIFY COLUMN id INT AUTOINCREMENT,
ADD PRIMARY KEY (id);

-- inserir primary key na tabela reservas
ALTER TABLE reservas
MODIFY COLUMN id INT AUTOINCREMENT,
ADD PRIMARY KEY (id);

--  inserir foreing key na tabela reservas
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREING KEY(id_usuario) REFERENCES usuarios (id);

--  inserir foreing key na tabela destinos
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_destinos
FOREING KEY(id_destino) REFERENCES destinos (id);

-- inserindo dados na tabela reserva
INSERT INTO reserva(id_usuario, id_destino, data) VALUES (1, 1, '2043-11-11')

-- atualizando coluna com cascade delete
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREING KEY (id_usuario) REFERENCES usuarios (id)
ON DELETE CASCADE;

