# Insight API

Essa é a API de uma aplicacao que foi desenvolvida para buscar dados do Censo de nomes do IBGE realizando a manipulação dos dados e persistindo-os.

## Tecnologias Utilizadas

- *Python*: [https://www.python.org/] Python;
- *FastAPI*: [https://fastapi.tiangolo.com/] Framework para criação de servidores simples em Python;
- *Postgres*: [https://fastapi.tiangolo.com/] Banco de dados SQL;
- *SQLAlchemy*: [https://www.sqlalchemy.org/] ORM para conexão com o banco de dados;
- *Docker*: [https://www.docker.com/] Ferramenta para contêinerização;
- *API do IBGE*: [https://servicodados.ibge.gov.br/api/docs/nomes?versao=2#api-Nomes-nomeGet] API do IBGE para busca de dados do Censo de Nomes por década de nascimento.

## A API consiste em dois endpoints:

**POST**
```
http://localhost:3000/censo/nomes
```
- body
```
{
    "nome": "jonathan",
    "sexo": "m"
}
```

**GET**
```
http://localhost:3000/nomes
```
- params
```
?sexo=M
?decada=1970
?nome=jonathan
```

## Para rodar a aplicação:

**Primeiro de tudo precisamos instalar os pacotes do projeto**
```
pip3 install -r requirements.txt
```

**Executar o Docker para subir o contêiner do banco de dados**
```
docker-compose up -d
```

**Assim que a imagem subir vamos executar a API**
```
uvicorn main:app --reload --port 3000
```
