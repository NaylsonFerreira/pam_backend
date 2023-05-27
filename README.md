# Projeto Escola

## SO dependências

Python versão 3.7

## instalando dependências

```sh
pip install -r requirements.txt
```

## Rodando migrations

```sh
python manage.py migrate
```

## Carrengando fixtures

```sh
python manage.py loaddata escola_app/fixtures/*
```

## Rodando projeto localmente

```sh
python manage.py runserver 0.0.0.0:8000
```

username: admin
password: admin