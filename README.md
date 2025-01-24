# CPF Validator

## Motivação do Projeto

Este projeto tem como objetivo criar uma função para validar CPFs brasileiros. A validação de CPF é uma necessidade comum em diversas aplicações, especialmente em sistemas que lidam com dados de usuários no Brasil. A função verifica se o CPF fornecido é válido de acordo com as regras estabelecidas pela Receita Federal do Brasil.

## Descrição

A função é implementada em Python e está configurada para ser executada como uma Azure Function. Ela pode ser acionada via requisições HTTP (GET ou POST) e retorna se o CPF fornecido é válido ou não.

## Estrutura do Projeto

- `__init__.py`: Contém a lógica principal da função, incluindo a validação do CPF.
- `function.json`: Arquivo de configuração da Azure Function, definindo os bindings e métodos HTTP suportados.

## Como Executar a função localmente

1. **Pré-requisitos**:
   - Conta no Azure.
   - Azure Functions Core Tools instalado.
   - Python 3.6 ou superior.

2. **Passos**:
   - Clone o repositório do projeto.
   - Navegue até o diretório do projeto.
   - Instale as dependências necessárias (se houver).
   - Execute o comando abaixo para iniciar a função localmente:

     ```sh
     func start
     ```

   - Functions:
        validator: [GET,POST] http://localhost:7071/api/validator

## Como Fazer Deploy na Azure Function

Para fazer o deploy da função para o Azure, siga os passos abaixo:

1. **Login no Azure**:
   - Execute o comando abaixo para fazer login na sua conta do Azure:

     ```sh
     az login
     ```

2. **Criação do Grupo de Recursos e Função**:
   - Crie um grupo de recursos (se ainda não tiver um):

     ```sh
     az group create --name <nome-do-grupo> --location <localizacao>
     ```

   - Crie uma Function App:

     ```sh
     az functionapp create --resource-group <nome-do-grupo> --consumption-plan-location <localizacao> --runtime python --runtime-version 3.8 --functions-version 3 --name cpfValidator --storage-account <nome-da-conta-de-armazenamento>
     ```

3. **Deploy da Função**:
   - Execute o comando abaixo para fazer o deploy da função:

     ```sh
     func azure functionapp publish cpfValidator
     ```

## Exemplo de Uso

### Requisição GET
```
GET https://localhost:7071/api/validate-cpf?cpf=12345678909
```
ou
```
GET https://<your-function-app>.azurewebsites.net/api/validate-cpf?cpf=12345678909
```

### Requisição GET
```
POST https://localhost:7071/api/validate-cpf
```
ou
```
POST https://<your-function-app>.azurewebsites.net/api/validate-cpf
```
```
body:
{ "cpf": "12345678909" }
```

## Retornos Possíveis

- **200 OK**: O CPF é válido.
- **400 Bad Request**: O CPF é inválido.
- **200 OK**: Mensagem padrão quando nenhum CPF é fornecido.
