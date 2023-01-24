# Oficina Backend Python Flask e FastAPI

<div>
<img src="https://flask.palletsprojects.com/en/2.2.x/_images/flask-logo.png" alt="Flask logo" width="360" align="center"/>
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI logo" width="360" align="center"/>
</div>

## Conteúdo

1. [Introdução](#introducao)
2. [Requisitos](#requisitos)
3. [Preparando o Ambiente Virtual](#ambiente_virtual)
4. [Exemplos](#exemplos)

   1. [ex01 - API Mínima](#ex01)
      1. [flask](#ex01_flask)
      2. [fastapi](#ex01_fastapi)
   2. [ex02 - Configurações](#ex02)
      1. [flask](#ex02_flask)
      2. [fastapi](#ex02_fastapi)
   3. [ex03 - Métodos HTTP](#ex03)
      1. [flask](#ex03_flask)
      2. [fastapi](#ex03_fastapi)
   4. [ex04 - Parâmetros URL](#ex04)
      1. [flask](#ex04_flask)
      2. [fastapi](#ex04_fastapi)
   5. [ex05 - Query URL](#ex05)
      1. [flask](#ex05_flask)
      2. [fastapi](#ex05_fastapi)
   6. [ex06 - Templates](#ex06)
      1. [flask](#ex06_flask)
      2. [fastapi](#ex06_fastapi)
   7. [ex07 - Static](#ex07)
      1. [flask](#ex07_flask)
      2. [fastapi](#ex07_fastapi)
   8. [ex08 - Tarefas Assíncronas](#ex08)
      1. [flask](#ex08_flask)
      2. [fastapi](#ex08_fastapi)
   9. [ex09 - Injeção de Dependências](#ex09)
      1. [flask](#ex09_flask)
      2. [fastapi](#ex09_fastapi)
   10. [ex10 - Validação de dados](#ex10)
       1. [flask](#ex10_flask)
       2. [fastapi](#ex10_fastapi)
   11. [ex11 - Serialização e Desserialização](#ex11)
       1. [flask](#ex11_flask)
       2. [fastapi](#ex11_fastapi)
   12. [ex12 - Middleware](#ex12)
       1. [flask](#ex12_flask)
       2. [fastapi](#ex12_fastapi)
   13. [ex13 - Modularização](#ex13)
       1. [flask](#ex13_flask)
       2. [fastapi](#ex13_fastapi)
   14. [ex14 - Autenticação](#ex14)
       1. [flask](#ex14_flask)
       2. [fastapi](#ex14_fastapi)
   15. [ex15 - CORS](#ex15)
       1. [flask](#ex15_flask)
       2. [fastapi](#ex15_fastapi)
   16. [ex16 - Test Driven Development](#ex16)
       1. [flask](#ex16_flask)
       2. [fastapi](#ex16_fastapi)
   17. [ex17 - Dockerização](#ex17)
       1. [flask](#ex17_flask)
       2. [fastapi](#ex17_fastapi)

5. [Exemplos em construção](#exemplos)

   18. [ex18 - Interagindo com DB SQL](#ex18)
       1. [flask](#ex18_flask)
       2. [fastapi](#ex18_fastapi)
   19. [ex19 - Interagindo com DB NoSQL](#ex19)
       1. [flask](#ex19_flask)
       2. [fastapi](#ex19_fastapi)
   20. [ex20 - Padrão de Serviço](#ex20)
       1. [flask](#ex20_flask)
       2. [fastapi](#ex20_fastapi)

## Introdução <a name="introducao"></a>

Neste repositório são apresentadas aplicação server-side em Python, simples a fim de auxiliar a compreensão sobre os diversos aspectos de uma API contruida com as bibliotecas [FLASK](https://flask.palletsprojects.com/en/2.2.x/) ou [FASTAPI](https://fastapi.tiangolo.com/). Cada exemplo é abordado em FLASK, diretórios "exN_flask" e em FASTAPI, diretórios "exN_fastapi".

## Requisitos <a name="requisitos"></a>

> Python +3.10
> Docker

## Preparando Ambiente Virtual <a name="ambiente_virtual"></a>

> pip3 install --upgrade pip
> pip3 install poetry
> poetry install

## Executando exemplos <a name="executando_exemplos"></a>

> poetry run python3 ex01_fastapi/main.py

## Exemplos <a name="exemplos"></a>

Nesta sessão apresenta-se resumos sobre cada exemplo.

### ex01 - API Mínima <a name="ex01"></a>

API Mínima

#### ex01_flask <a name="ex01_flask"></a>

#### ex01_fastapi <a name="ex01_fastapi"></a>

### ex02 - Configurações <a name="ex02"></a>

Trabalhando com Environment Variables, Config File, Instance Folder, Classes and inheritance

#### ex02_flask <a name="ex02_flask"></a>

#### ex02_fastapi <a name="ex02_fastapi"></a>

### ex03 - Métodos HTTP <a name="ex03"></a>

Utilizando métodos HTTP: get, post, put e delete

#### ex03_flask <a name="ex03_flask"></a>

#### ex03_fastapi <a name="ex03_fastapi"></a>

### ex04 - Parâmetros URL <a name="ex04"></a>

Utilizando Parâmetros passados URL

#### ex04_flask <a name="ex04_flask"></a>

#### ex04_fastapi <a name="ex04_fastapi"></a>

### ex05 - Query URL <a name="ex05"></a>

Utilizando query passada na URL

#### ex05_flask <a name="ex05_flask"></a>

#### ex05_fastapi <a name="ex05_fastapi"></a>

### ex06 - Templates <a name="ex06"></a>

Trabalhando com Templates

#### ex06_flask <a name="ex06_flask"></a>

#### ex06_fastapi <a name="ex06_fastapi"></a>

### ex07 - Static <a name="ex07"></a>

Trabalhando com Static Folder, para arquivos como texto, imagens, css, javascript, etc.

#### ex07_flask <a name="ex07_flask"></a>

#### ex07_fastapi <a name="ex07_fastapi"></a>

### ex08 - Tarefas Assíncronas <a name="ex08"></a>

Trabalhando com tarefas assincronas simples. Entretanto sugere-se o uso da biblioteca Celery para tarefas complexas.

#### ex08_flask <a name="ex08_flask"></a>

#### ex08_fastapi <a name="ex08_fastapi"></a>

### ex09 - Injeção de Dependências <a name="ex09"></a>

A injeção de dependências é uma técnica onde um objeto (ou método estático) fornece as dependências de outro objeto. Uma dependência é um objeto que pode ser usado, ou seja, um serviço.

#### ex09_flask <a name="ex09_flask"></a>

#### ex09_fastapi <a name="ex09_fastapi"></a>

### ex10 - Validação de dados <a name="ex10"></a>

A validação de dados é importante para verificar os dados recebidos numa requisição, e se estes atentem os requisitos especificados nos modelos.

#### ex10_flask <a name="ex10_flask"></a>

#### ex10_fastapi <a name="ex10_fastapi"></a>

### ex11 - Serialização e Desserialização <a name="ex11"></a>

A serialização de dados é o processo de conversão de dados estruturados para um formato que permita o compartilhamento ou armazenamento dos dados de uma forma que permita a recuperação de sua estrutura original. Em alguns casos, a intenção secundária da serialização de dados é minimizar o tamanho dos dados, o que reduz os requisitos de largura de banda. A desserialização converte tipos de dados complexos, como objetos, de e para tipos de dados Python nativos.

#### ex11_flask <a name="ex11_flask"></a>

#### ex11_fastapi <a name="ex11_fastapi"></a>

### ex12 - Middleware <a name="ex12"></a>

Middleware são usados para aplicar uma lógica a cada requisição antes de ser processada pelo View.

#### ex12_flask <a name="ex12_flask"></a>

#### ex12_fastapi <a name="ex12_fastapi"></a>

### ex13 - Modularização <a name="ex13"></a>

Decomposição da aplicação em models, schemas, routers, services, views, templates, etc

#### ex13_flask <a name="ex14_flask"></a>

#### ex13_fastapi <a name="ex14_fastapi"></a>

### ex14 - Autenticação <a name="ex14"></a>

Neste exemplo é abordada a autenticação do tipo HTTP, entretanto existem diversas outras formas de autenticação.
Como JWT, Form, OAuth, etc.

#### ex14_flask <a name="ex14_flask"></a>

#### ex14_fastapi <a name="ex14_fastapi"></a>

### ex15 - CORS <a name="ex15"></a>

O middleware CORS (Cross-Origin Resource Sharing) verifica se as solicitações vêm ou não de origens permitidas.

#### ex15_flask <a name="ex15_flask"></a>

#### ex15_fastapi <a name="ex15_fastapi"></a>

### ex16 - Test Driven Development <a name="ex16"></a>

TDD se baseia em pequenos ciclos de repetições, onde para cada funcionalidade do sistema um teste é criado antes.
Neste exemplo utiliza-se a ferramenta pytest.

#### ex16_flask <a name="ex16_flask"></a>

#### ex16_fastapi <a name="ex16_fastapi"></a>

### ex17 - Dockerização <a name="ex17"></a>

Dockerização é o processo de compactação, implantação e execução de aplicativos usando contêineres do Docker. O Docker é uma ferramenta de código aberto que envia seu aplicativo com todas as funcionalidades necessárias como um pacote.

#### ex17_flask <a name="ex17_flask"></a>

#### ex17_fastapi <a name="ex17_fastapi"></a>

### ex18 - Interagindo com DB SQL <a name="ex18"></a>

Interação com banco de dados relacional PostgreSQL através do SQLAlchemy

#### ex18_flask <a name="ex18_flask"></a>

#### ex18_fastapi <a name="ex18_fastapi"></a>

### ex19 - Interagindo com DB NoSQL <a name="ex19"></a>

Interação com banco de dados não relacional MondoDB através do SQLAlchemy

#### ex19_flask <a name="ex19_flask"></a>

#### ex19_fastapi <a name="ex19_fastapi"></a>

### ex20 - Padrão de Serviço <a name="ex20"></a>

Aplicando o Service Pattern na API.
Exemplo de um aquisição de temperatura corporal.
Onde cada sensor é exclusivo a um voluntário.

Models:
temperatura (MongoDB)
sensor_id: int
voluntario_id: int
timestamp: datetime
n_pacote: int
temperatura: Array(int)
voluntario(postgreSQL)
voluntario_id: int
nome: str
cpf: str
idade: str
email: str
sensor (postgreSQL)
sensor_id: int
nome: str
(FK) voluntario_id: int

#### ex20_flask <a name="ex20_flask"></a>

#### ex20_fastapi <a name="ex20_fastapi"></a>
