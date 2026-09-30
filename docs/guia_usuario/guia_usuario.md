# Guia do Usuário — MEICash

## 1. Apresentação

O MEICash é um sistema web desenvolvido para auxiliar Microempreendedores
Individuais (MEIs) no controle de suas movimentações financeiras.

O sistema permite registrar receitas e despesas, consultar e filtrar
movimentações, acompanhar um resumo financeiro e gerar relatórios.

---

## 2. Acesso ao sistema

O MEICash está disponível pela internet no endereço:

https://meicash.onrender.com

Para utilizar as funcionalidades do sistema, o usuário deve possuir uma conta
cadastrada e realizar o login.

> Observação: por utilizar uma instância gratuita de hospedagem, o primeiro
> acesso após um período de inatividade pode levar alguns segundos para carregar.

---

## 3. Cadastro de usuário

Caso ainda não possua uma conta:

1. Acesse a página inicial do MEICash.
2. Selecione a opção de cadastro.
3. Preencha os dados solicitados.
4. Informe uma senha.
5. Confirme o cadastro.

Após a conclusão, o usuário poderá acessar o sistema utilizando o e-mail e a
senha cadastrados.

---

## 4. Login

Para entrar no MEICash:

1. Acesse https://meicash.onrender.com.
2. Informe o e-mail cadastrado.
3. Informe a senha.
4. Clique em **Entrar**.

Após a autenticação, o usuário será direcionado para a página principal do
sistema.

---

## 5. Resumo financeiro

Na página principal, o MEICash apresenta um resumo da situação financeira do
usuário.

São exibidas informações relacionadas às receitas, despesas e saldo das
movimentações cadastradas.

O saldo é calculado considerando:

**Saldo = Total de Receitas - Total de Despesas**

As informações são atualizadas de acordo com as movimentações registradas pelo
usuário.

---

## 6. Cadastro de receita

Para registrar uma entrada financeira:

1. Acesse a opção **Cadastrar Receita**.
2. Informe a descrição da receita.
3. Informe o valor.
4. Selecione ou informe a data.
5. Informe a categoria.
6. Preencha as demais informações disponíveis, quando necessário.
7. Confirme o cadastro.

Após o registro, a receita será armazenada no banco de dados e passará a
compor o resumo financeiro do usuário.

---

## 7. Cadastro de despesa

Para registrar uma saída financeira:

1. Acesse a opção **Cadastrar Despesa**.
2. Informe a descrição da despesa.
3. Informe o valor.
4. Selecione ou informe a data.
5. Informe a categoria.
6. Preencha as demais informações disponíveis, quando necessário.
7. Confirme o cadastro.

Após o registro, a despesa será armazenada no banco de dados e considerada no
cálculo do resumo financeiro.

---

## 8. Consulta de movimentações

A opção de movimentações permite visualizar os lançamentos financeiros
cadastrados pelo usuário.

Nessa tela é possível consultar receitas e despesas e visualizar informações
como:

- descrição;
- valor;
- data;
- categoria;
- tipo da movimentação.

Os registros apresentados pertencem ao usuário autenticado no sistema.

---

## 9. Filtro de movimentações

Na tela de movimentações, o usuário pode aplicar filtros para facilitar a
localização de determinados registros.

Os filtros permitem restringir os resultados exibidos conforme os critérios
disponíveis no sistema.

Após informar os critérios desejados, o usuário deve executar a filtragem para
visualizar apenas as movimentações correspondentes.

---

## 10. Edição de movimentação

Para alterar uma movimentação existente:

1. Acesse a lista de movimentações.
2. Localize o registro desejado.
3. Selecione a opção de edição.
4. Altere os campos necessários.
5. Salve as alterações.

Após a confirmação, os novos dados serão armazenados no banco de dados e
refletidos nas demais telas do sistema.

---

## 11. Exclusão de movimentação

Para remover uma receita ou despesa:

1. Acesse a lista de movimentações.
2. Localize o registro desejado.
3. Selecione a opção de exclusão.
4. Confirme a operação.

Após a exclusão, a movimentação deixa de fazer parte dos cálculos financeiros
do usuário.

---

## 12. Relatório financeiro

O MEICash permite consultar um relatório das movimentações financeiras.

Para utilizar essa funcionalidade:

1. Acesse a opção **Relatório**.
2. Informe o período desejado, quando aplicável.
3. Gere ou consulte o relatório.
4. Verifique as receitas, despesas e demais informações apresentadas.

Caso seja necessário gerar um arquivo, utilize a opção de impressão do
navegador.

Na janela de impressão, selecione:

**Salvar como PDF**

e escolha o local onde o arquivo será armazenado.

---

## 13. Encerramento da sessão

Ao finalizar o uso do sistema, utilize a opção **Sair** para encerrar a sessão.

Isso impede que outra pessoa utilizando o mesmo navegador tenha acesso direto
às informações financeiras do usuário.

---

## 14. Persistência dos dados

Os dados cadastrados no MEICash são armazenados em um banco de dados
PostgreSQL hospedado na plataforma Neon.

A aplicação web está hospedada na plataforma Render e realiza a comunicação
com o banco de dados para cadastrar, consultar, editar e excluir as
informações financeiras.

---

## 15. Considerações finais

O MEICash foi desenvolvido com o objetivo de fornecer ao Microempreendedor
Individual uma forma simples de registrar e acompanhar receitas e despesas.

Nesta primeira iteração da fase de construção, foram disponibilizadas as
principais funcionalidades relacionadas ao cadastro de usuário, autenticação,
controle de movimentações, resumo financeiro e emissão de relatório.