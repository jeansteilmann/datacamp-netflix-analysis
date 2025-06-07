# Projeto: Análise de Dados da Netflix (Netflix Data Analysis)

## Visão Geral do Projeto

Este é um projeto de análise de dados exploratória (EDA) que investiga um subconjunto específico do catálogo da Netflix. O foco principal é a identificação e contagem de filmes que atendem a critérios específicos de lançamento, gênero e duração. Desenvolvido como parte do aprendizado em ciência de dados com Python.

## Conjunto de Dados

O conjunto de dados utilizado é `netflix_data.csv`, contendo informações detalhadas sobre filmes e séries disponíveis na plataforma Netflix.

| Coluna         | Descrição                                   |
| :------------- | :------------------------------------------ |
| `show_id`      | O ID do show                                |
| `type`         | Tipo de show (Filme ou Série)               |
| `title`        | Título do show                              |
| `director`     | Diretor do show                             |
| `cast`         | Elenco do show                              |
| `country`      | País de origem                              |
| `date_added`   | Data de adição à Netflix                    |
| `release_year` | Ano de lançamento original                  |
| `duration`     | Duração do show em minutos (para filmes)    |
| `description`  | Descrição do show                           |
| `genre`        | Gênero do show                              |

## Funcionalidade do Script

O script `netflix_analysis.py` realiza as seguintes operações:

1.  **Carregamento de Dados:** Carrega o dataset `netflix_data.csv` para um DataFrame Pandas.
2.  **Filtragem de Tipo:** Exclui séries, focando a análise exclusivamente em filmes.
3.  **Tratamento de Dados Ausentes:** Lida com valores ausentes na coluna 'duration' (ex: removendo ou imputando).
4.  **Filtragem por Década:** Filtra os filmes para incluir apenas aqueles lançados na década de 1990 (entre 1990 e 1999, inclusive).
5.  **Análise Específica:** Identifica e conta os filmes da década de 90 que são do gênero 'Action' e possuem uma duração menor que 90 minutos.
6.  **Saída:** Imprime a contagem final dos filmes que atendem a todos os critérios.

## Como Executar o Projeto

Para executar o script e replicar a análise, siga os passos abaixo:

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/SeuUsuario/datacamp-netflix-analysis.git](https://github.com/SeuUsuario/datacamp-netflix-analysis.git)
    cd datacamp-netflix-analysis
    ```
2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```
3.  **Instale as Dependências:**
    O projeto requer a biblioteca `pandas`.
    ```bash
    pip install pandas numpy
    ```
4.  **Execute o Script Python:**
    ```bash
    python netflix_analysis.py
    ```
    O script processará os dados e exibirá a contagem de filmes no console.

## Ferramentas e Bibliotecas

* Python 3.x
* Pandas 
* NumPy 
