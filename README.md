1° baixar o dataset

acessando o link: https://gist.github.com/rioto9858/ff72b72b3bf5754d29dd1ebf898fc893#file-top50musicfrom2010-2019-csv, baixar o arquivo .zip do repositório e descompactar na pasta do seu projeto.

OBS: para faciliar o desenvolvimento o arquivo foi renomeado para musics.csv

2° Passo criar um arquivo .ipynb (Jupyter notebook) para desenvolver a base do algoritimo

3° Importar as bibliotecas que serão utilizadas no desenvolvimento no arquivo .ipynb.

bibliotecas utilizadas:

import pandas as pd - Para realizar a leitura do dataset e modificações
from sklearn.feature_extraction.text import CountVectorizer - Classe usada para "vetorizar" as informações do dataset
from sklearn.metrics.pairwise import cosine_similarity - Função usada para achar a similiaridade entre os vetores
import pickle - biblioteca usada ao final do algoritimo para guardar variaveis na memória ROM do computador

4° Importar a base de dados realizar a limpeza das informações

Na segunda célula fazemos a importação da base de dados e guardamos na variavel musics, a função read_csv espera uma string
contendo o caminho do arquivo .csv e retorna uma classa DataFrame da biblioteca pandas

A terceira célula a função dropna remove colunas que tenha valores nulos

Na quarta célula os valores das linhas são renomeados para facilitar posteriormente o desenvolvimento

A quinta célula remove os espaços das strings das linhas de "artist" e "genre" para que posteriormente a vetorização ocorra
de maneira correta

Por ultimo nessa etapa utilizamos a função set_value para formatar os valores das colunas ao final todas terão o prefixo com o
nome da sua linha por exemplo:

genre artist year == genre:pop artist:artista year:2020
pop artista 2020 ==

Isso é feito para que a função de similiaridade verifique apenas os valores das próprias colunas como bpm por bpm e artist por artist

Além disso é gerado uma nova linha "tags" contendo a concatenaçao das linhas do array "keys"

5° vetorização e similiaridade

Na 7° célula é criado a variavel data contendo as colunas title artist genre e tags da variavel musics, automaticamente
o valor dessa variável se torna uma class DataFrame da biblioteca pandas

A variavel count_v da oitava celula se trata de uma instancia da classe CountVectorizer que será responsavel por vetorizar nossos
valores com base nas palavras da linha "tags" das musicas, os vetores foram guardados na variavel "vectors"

Na célula 10 temos a variavel similarity que representa uma matriz contendo a similiaridade entre cada vetor do dataset
podemos perceber que quando o valor é 1 se trata de uma comparação com o próprio vetor

1 - [1,...]
2 - [...,1,...]
3 - [...,...,1]

e assim sucessivamente, ou seja o primeiro elemento do segundo vetor da variavel similarity se trata da comparação da segunda entre a primeira música

6° Função de recomendação

A função recommend espera o nome da música e apresenta o nome de 5 musicas recomendadas

Na primeira linha da função procuramos pelo indice da musica com base no nome o atributo .index retorna uma tupla com o primeiro
valor sendo o indice da coluna e o segundo sendo o tipo de dado do indice por isso deve-se usar o [0] para termos somente o indice

Tendo o indice da música podemos acessar o vetor de similiaridade usando a variavel similarity, para facilitar o entendimento
guardamos as musicas com seu indice dentro da variavel musics_with_index.

Por fim criamos a variavel musics_list que ordenara as musicas em ordem decrescente (passando o reverse=True) e usando o segundo
indice dos elementos da variavel music_with_index que sera o valor da similiaridade da música, o [1:6] filtra os valores entre
menor que 1 e maior que 0.6 assim descartamos a similiaridade da propria musica (que seria 1) e removemos as similiaridades baixas

Dentro do for são printados os nomes das musicas recomendadas, rodando a função usando a musica Diamonds (Rihanna) percebemos
que dentro das recomendações temos uma música da mesma cantora (Work)

7° Armazenar as variáveis

Usando a biblioteca pickle armazenaremos as variaveis contendo as musicas e similiaridades para usarmos em um novo código
a função dump cria um arquivo da variavel passada como primeiro parametro e o arquivo passado como segundo parametro usando a
função open nativa do python

8° Front-End

Para criarmos a interface de usuário é necessário criar um arquivo .py no mesmo diretório do projeto para usarmos as variaveis em
memória geradas pelo pickle, após isso importaremos as seguintes bibliotecas

import streamlit as st - Para criar a interface
import pickle - Para ler as variaveis em memória
import pandas as pd - para importar a base de dados

9° Importar base e recriar função de recomendação

Nas linhas 4 a 7 são importados as variaveis em memória dos arquivo .pkl e gerado o classe DataFrame das musicas

Na linha 10 a 20 foi recriado a função de recommend apenas mudando o tipo de retorno para array, sendo possível apresentar
a musica posteriormente ao usuário dentro do front-end

10° Codifiação do front-end

Na linha 23 definimos o titulo da página como "Music Recommender System"
Na linha 24 criamos um select com o placeholder "Select the music" contendo a lista de musicas do dataset

Na linha 29 é criado um botão que ao ser clicado roda a funcão recommend passando o valor da musica selecionada e posteriormente
escrevendo o retorno na tela, assim sendo mais seguro ao usuário que tem os valores corretos dos nomes das musicas

Para rodar o front-end basta digitar no cmd: streamlit run nome-do-arquivo.py
COM A BIBLIOTECA STREAMLIT INSTALADA

-- pip install streamlit

Demonstração:

colocar ultimas imagens
