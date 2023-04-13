# Repositório do projeto Inventory Reports 📊

## Módulo: CIÊNCIA DA COMPUTAÇÃO

 Repositório possuí projeto desenvolvido no período que estive na **Trybe**, abordando conceitos de `Python`, `POO` e `Padrões de projetos`.

## Informações de aprendizados

- Este é um projeto desenvolvido para praticar `Python`;
- Segundo projeto utilizando `Python`;
- Utilizei o `Pytest` para fazer meus testes.

## Linguagens e ferramentas usadas

[![Git][Git-logo]][Git-url]
[![Python][Python-logo]][Python-url]
[![Pytest][Pytest-logo]][Pytest-url]

## O que foi desenvolvido

Neste projeto, implementei um gerador de relatórios, utilizando a Programação Orientada a Objetos e Design patterns, que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

Esses dados de estoque poderão ser obtidos de diversas fontes:

- Através da importação de um arquivo CSV;
- Através da importação de um arquivo JSON;
- Através da importação de um arquivo XML.

Além disso, o relatório final possuirá duas versões: `simples` e `completa`.

## Habilidades trabalhadas

- Aplicar conceitos de Orientação a Objetos em Python;
- Aplicar padrões de projeto;
- Leitura e escrita de arquivos (XML, CSV, JSON).

## Instruções para instalar e rodar

1. Clone o repo:

    ```bash
    git clone git@github.com:Ludson96/project-inventory-report.git
    ```

1. Entre na pasta do repositório que você acabou de clonar:

    ```bash
    cd project-inventory-report
    ```

1. Caso não tenha instalado o python, pode usar o docker:

    ```bash
    docker-compose up
    ```

1. Crie e ative o ambiente virtual:

    ```bash-shell
    python3 -m venv .venv && source .venv/bin/activate
    ```

1. Instale as dependências no ambiente virtual:

    ```bash
    python3 -m pip install -r dev-requirements.txt
    ```

1. Para rodar todos os testes utilize o comando:

    ```bash
    python3 -m pytest
    ```

1. Para rodar apenas em um arquivo:

    ```bash-shell
    python3 -m pytest <path do arquivo>
    ```

1. Para executar a classe principal execute o comando abaixo:

     ```bash-shell
    inventory_report <caminho do arquivo> <tipo do relatório>

    Ex.: inventory_report inventory_report/data/inventory.csv simples

    #caso não funcione, execute o comando: 
    
    pip install .
    ```

## Tipos de relatórios

Abaixo um exemplo da diferença entre os relatórios.

<details>

  <summary><strong>Simples</strong></summary>

```bash-shell
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
```

</details>

<details>

  <summary><strong>Completo</strong></summary>

```bash-shell
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE
```

</details>

> `docker-compose.yml` fornecido pela trybe.

[Git-logo]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com
[Python-logo]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
[Pytest-logo]: https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white
[Pytest-url]: https://docs.pytest.org/en/7.2.x/
