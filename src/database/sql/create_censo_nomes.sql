CREATE TABLE censo_nomes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    decada VARCHAR(20) NOT NULL,
    frequencia INTEGER NOT NULL,
    sexo CHAR(1) NULL
);