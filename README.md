# Sistema Academico

## Execução

```bash
docker-compose up --build -d
```
acessar o site: `http://localhost:5000/`

## Testes

```bash
docker exec -it gestor-de-usuarios pytest --cov -vv
```
