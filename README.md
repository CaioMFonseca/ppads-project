# MEICash

Sistema de Controle Financeiro para Microempreendedores Individuais.

Projeto desenvolvido na disciplina de Práticas Profissionais em Análise e Desenvolvimento de Sistemas, do curso de Análise e Desenvolvimento de Sistemas.

## Funcionalidades

O MEICash permite:

- cadastro e autenticação de usuários;
- cadastro de receitas;
- cadastro de despesas;
- edição de movimentações;
- exclusão de movimentações;
- consulta de movimentações;
- filtros por tipo, categoria e período;
- consulta do resumo financeiro;
- geração de relatório financeiro por período;
- análise das despesas por categoria;
- exportação do relatório em CSV;
- impressão ou salvamento do relatório em PDF pelo navegador.

## Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLAlchemy
- PostgreSQL em produção
- SQLite para desenvolvimento local
- HTML
- CSS
- Jinja2
- Gunicorn

## Repositório

https://github.com/CaioMFonseca/ppads-project

## Aplicação publicada

https://meicash.onrender.com

---

# Executando o projeto localmente

## 1. Pré-requisitos

Antes de iniciar, é necessário possuir:

- Git instalado;
- Python instalado;
- acesso a um terminal, PowerShell ou Prompt de Comando.

O projeto possui o arquivo `.python-version` com a versão de Python utilizada no desenvolvimento.

## 2. Clonar o repositório

Abra um terminal e execute:

```bash
git clone https://github.com/CaioMFonseca/ppads-project.git
```

Entre na pasta do projeto:

```bash
cd ppads-project
```

Para executar exatamente a versão correspondente à Iteração 2, após a publicação da versão `v2`, utilize:

```bash
git checkout v2
```

## 3. Criar o ambiente virtual

### Windows — PowerShell

```powershell
python -m venv .venv
```

Ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux ou macOS

```bash
python3 -m venv .venv
```

Ative o ambiente:

```bash
source .venv/bin/activate
```

## 4. Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install -r requirements.txt
```

## 5. Configuração das variáveis de ambiente

O projeto aceita as seguintes variáveis de ambiente:

- `SECRET_KEY`: chave utilizada pela aplicação Flask;
- `DATABASE_URL`: endereço de conexão com o banco de dados.

Para desenvolvimento local, não é obrigatório definir `DATABASE_URL`.

Quando essa variável não é informada, o sistema utiliza automaticamente um banco SQLite local:

```text
sqlite:///meicash.db
```

Opcionalmente, pode ser criado um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=uma-chave-local-de-desenvolvimento
```

O arquivo `.env` não deve ser enviado ao repositório.

## 6. Criar as tabelas do banco local

Na primeira execução local, é necessário criar as tabelas do banco SQLite.

Com o ambiente virtual ativado e estando na pasta do projeto, execute:

```bash
python -c "from app import app; from extensions import db; ctx=app.app_context(); ctx.push(); db.create_all(); print('Tabelas criadas com sucesso.'); ctx.pop()"
```

Ao final, deverá ser exibida a mensagem:

```text
Tabelas criadas com sucesso.
```

O banco SQLite será criado localmente na pasta `instance`.

## 7. Executar a aplicação

Execute:

```bash
python app.py
```

A aplicação será iniciada no servidor de desenvolvimento do Flask.

Acesse pelo navegador:

```text
http://127.0.0.1:5000
```

## 8. Primeiro acesso

Como o banco SQLite local começa vazio, é necessário:

1. acessar a opção de cadastro;
2. criar um usuário;
3. realizar o login;
4. cadastrar receitas e despesas;
5. utilizar o dashboard, movimentações e relatórios.

Os dados cadastrados localmente são independentes dos dados da aplicação publicada.

## 9. Relatórios

Na área de relatórios é possível selecionar um período e visualizar:

- total de receitas;
- total de despesas;
- saldo;
- quantidade de movimentações;
- despesas agrupadas por categoria;
- percentual das despesas por categoria;
- movimentações do período.

Também é possível:

- imprimir ou salvar o relatório em PDF;
- exportar as movimentações do período em formato CSV.

O arquivo CSV pode ser aberto em programas como Microsoft Excel e LibreOffice Calc.

## Estrutura do projeto

```text
ppads-project/
│
├── models/
├── repositories/
├── routes/
├── services/
├── static/
├── templates/
├── docs/
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── .python-version
└── README.md
```

A aplicação utiliza uma organização em camadas:

- `models`: entidades e modelos persistidos no banco de dados;
- `repositories`: operações de acesso aos dados;
- `services`: regras de negócio e validações;
- `routes`: rotas e integração entre requisições HTTP e serviços;
- `templates`: páginas HTML renderizadas pelo Flask;
- `static`: arquivos estáticos, incluindo CSS;
- `docs`: documentação complementar do projeto.

## Banco de dados em produção

A versão publicada do MEICash utiliza PostgreSQL hospedado no Neon.

A aplicação é executada no Render utilizando Gunicorn.

As credenciais e strings de conexão de produção não são armazenadas no repositório e devem ser configuradas por meio de variáveis de ambiente.

## Controle de versão

A versão correspondente à primeira iteração da construção está identificada pela tag:

```text
v1
```

A versão correspondente à segunda iteração será identificada pela tag:

```text
v2
```

## Grupo

Grupo 15

### Projeto acadêmico

MEICash — Sistema de Controle Financeiro para Microempreendedores Individuais.