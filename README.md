# API de Busca de Dados de Processo

Este é o README do projeto que consiste em uma API para buscar dados de um processo em todos os graus dos Tribunais de Justiça de Alagoas (TJAL) e do Ceará (TJCE). O objetivo é coletar informações sobre um processo jurídico a partir do número fornecido e retornar os detalhes do processo em todas as esferas.

# Desafio

O Jusbrasil coleta uma variedade de dados públicos que não são facilmente acessíveis e melhora seu acesso para todos. Um dos tipos de dados coletados são os dados sobre processos. O desafio é fazer uma API que busque dados de um processo em todos os graus dos Tribunais de Justiça de Alagoas (TJAL) e do Ceará (TJCE). Geralmente o processo começa no primeiro grau e pode subir para o segundo. Você deve buscar o processo em todos os graus e retornar suas informações.

## Input

A API foi desenvolvida para receber um JSON contendo o número do processo. Para descobrir o tribunal, você pode pedir essa informação no input ou usar o padrão CNJ de numeração de processos jurídicos disponível em [https://www.cnj.jus.br/programas-e-acoes/numeracao-unica/](https://www.cnj.jus.br/programas-e-acoes/numeracao-unica/).

## Output

O cliente tem a capacidade de pegar os dados quando o processamento termina, portanto, foi criado um mecanismo para permitir isso. A API retorna sempre um JSON contendo as informações dos processos encontrados em todas as esferas.

# Projeto
## Bibliotecas Utilizadas

O projeto utilizou as seguintes bibliotecas:

- re
- requests
- BeautifulSoup
- Selenium
- Flask
- json

## Execução do Projeto

Para executar o projeto, siga as instruções abaixo:

1. Certifique-se de ter todas as bibliotecas mencionadas anteriormente instaladas corretamente em seu ambiente.

2. Navegue até a raiz do projeto.

3. Execute o arquivo `main.py`.

Para utilizar a API e enviar o dicionário JSON contendo o número do processo, você pode utilizar uma ferramenta de testes de API, como o Postman (https://www.postman.com/). 

### Siga as etapas abaixo para fazer a requisição:

1. Certifique-se de ter a API em execução. Por padrão, o endereço da API é o endereço local da sua máquina (por exemplo, http://localhost:5000).

2. Abra o Postman ou outra ferramenta similar.

3. Crie uma nova requisição e defina o método como "POST".

4. Insira o URL da API, por exemplo, `http://localhost:5000/processos`.

5. No corpo da requisição, selecione a opção "raw" e escolha o formato "JSON (application/json)".

6. Cole o dicionário JSON com o número do processo, por exemplo:

``` dicionário em json
{
	"processo": "0710802-55.2018.8.02.0001"
}
```

7. Clique em "Enviar" para enviar a requisição à API.

A API processará a solicitação e retornará um JSON com as informações do processo em todas as esferas propostas no desafio.
