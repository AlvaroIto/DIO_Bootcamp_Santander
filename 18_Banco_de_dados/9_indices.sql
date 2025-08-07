/*
Análise de plano de execução
Ela nos permite examinar as operações realizadas, as tabelas acessadas, os índices utilizados e outras informações importantes par identificar possíveis melhorias de desempenho

Estrutura
EXPLAIN
    SELECT *
    FROM {{tabela}}
...

Tipos de campos:
    - select_type: 'SIMPLE', 'SUBQUERY', 'JOIN'
    - table
    - type: 'ALL', 'INDEX' entre outros
    - possible_keys: Os índices possíveis que podem ser utilizados na operação
    - key: O índice utilizado na operação, se aplicável
    - key_len: O comprimento do índice utilziado
    - ref: As colunas ou constantes usadas para acessar o índice
    - rows


*/

-- pesquisar todos os usuários com nome João Silva
EXPLAIN
    SELECT * FROM usuarios WHERE nome = 'João Silva';

-- adicionar índice na query
CREATE INDEX indx_nome ON usuarios (nome);
EXPLAIN
    SELECT * FROM usuarios WHERE nome = 'João Silva';