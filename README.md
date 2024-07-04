# Projeto NoSQL

## Visão Geral

Este projeto é uma aplicação que armazena informações de clientes, gerencia metadados de certificados e gera certificados em formato PNG. Utiliza tecnologias como Docker, Python (Flask), PostgreSQL, WSL, SSH e VirtualBox para criar uma infraestrutura robusta e escalável.

A ideia desse projeto foi melhorar um anterior que tinha feito. (https://github.com/Jtavora/Projeto_NoSql.git)
Acredito que tenha conseguido atigingir meu objetivo!
De melhorias temos:
-Utilizacao FastAPI
-Autenticacao na API
-Diversas rotas funcionais

## Como Executar

Para testar o projeto localmente, siga os passos abaixo:

```sh
# Clone o repositório
git clone https://github.com/Jtavora/Projeto_IHC-Requisitos.git

# Acesse o diretório do projeto
cd Projeto_IHC-Requisitos

# Execute o comando para iniciar os containers
sudo docker-compose up -d


# Acesse a URL localhost:5001/Inicio
# Cadastre alguns clientes. (Se tentar acessar "Clientes" sem cadastrar nenhum, pode ocorrer um problema)
# Teste o sistema
```

#Detalhe
Ao executar pode dar erro ai baixar o pillow.
Entre no log do container e veja.
Caso tenha dado, basta entrar no bash do container e dar "pip install pillow"
