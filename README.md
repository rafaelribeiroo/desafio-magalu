# API PRODUTOS FAVORITOS

A API acima visa colaborar com a equipe de marketing, para que identifiquem os produtos favoritos de cada cliente para que realizem seus trabalhos.

## Iniciando

As instruções a seguir ajuda a baixar e ter uma cópia do projeto em sua máquina local para prosseguir com o desenvolvimento e efetuar testes.

### Pré-requisitos

Algumas tecnologias que você vai precisar ter instaladas previamente são:

```
Python 3.3+
Build-essential (biblioteca PY que contém make, encurtador de comandos)
PIP (qualquer versão)
PostgreSQL 9.x+
```

Vamos acessar o console do Postgres para criar nosso banco de dados.

```
sudo -u postgres psql
postgres=# CREATE DATABASE desafiomagalu;
postgres=# GRANT ALL PRIVILEGES ON DATABASE desafiomagalu TO <seu_usuario>;
```

### Instalação

A seguir, passo-a-passo de como baixar, instalar e executá-lo.

```
$ git clone git@github.com:rafaelribeiroo/desafio-magalu.git ~/Downloads
$ cd ~/Downloads/desafio-magalu
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ make ti
$ make te
```

### Variáveis de Ambiente

Vá na raíz do projeto e execute o arquivo secret_key.py

```
$ python secret_key.py
```

Crie o seguinte arquivo: ".env" na raíz e atribua as chaves/valores abaixo:

```
SECRET_KEY=<resultado_do_secret_key>
DEBUG=TRUE
DB_NAME=desafiomagalu
DB_USER=<seu_usuario>
DB_PASSWORD=<sua_senha>
```

### Tudo Pronto!

```
$ make run
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details


