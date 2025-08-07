/*
Problema em uma tabela:
Usuários com endereços longos não estão conseguindo realizar cadastro no sistema
Opções:
    - Recriar a tabela, migrar os dados e excluir a tabela anterior
    - Alterar estrutura da tabela

Drop table
O comando DROP TABLE é usado no SQL - para remover uma tabela existente de um banco de dados relacional
Ele exclui permanentemente a tabela
DROP TABLE {{ tabela }}

Alter Table
A cláusula ALTER TABLE é usada no SQL para modificar a estrutura de uma tabela existente em um banco de dados relacional.
Ela permite:
    - Adicionar, alterar ou excluir colunas
    - Modificar as restrições, índices
    - Renomear a tabela entre outras alterações
*/

-- Alterar restrição da coluna endereço para mais caracteres FORMA 1
CREATE TABLE novos_usuarios (
    id INT, 
    nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
    email VARCHAR(100) NOT NULL UNIQUE COMMENT 'Email do usuário',
    endereco VARCHAR(100) NOT NULL COMMENT 'Endereço do usuário',
    data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário'
);

-- migrar dados de uma tabela para outra
INSERT INTO novos_usuarios (
    id, 
    nome,
    email,
    endereco,
    data_nascimento
) 
SELECT id, nome, email, endereco, data_nascimento
FROM usuarios;

-- excluiir tabela antiga
DROP TABLE usuarios;

-- alterar nome da tabela
ALTER TABLE novos_usuarios RENAME usuarios;


-- Alterar restrição da coluna endereço para mais caracteres FORMA 2
ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR(150);
