# MATE10 - Sistemas Fuzzy

# 21/08/2018

## Organização do Curso

* Livro: Fuzzy Sets and Fuzzy Logic - Theory and Applications, Klir e Yuan, 1995

* Artigos: L.A Zadeh (Criador da Lógica Fuzzy)

* Ferramentas:
    * R
        * frbs
    * Keel - Uni. Granada

## O que é

* Quantifica a incerteza (não determinismo, visão de parte do todo)

* "Estado de crença": em modelos não-Fuzzy, os agentes devem saber tudo 
sobre o mundo que serão inseridos

* A qualidade do sistema é dada pela "Medida de Desempenho". 
Busca-se maximizar esse indicador.

* Teoria da probabilidade: determina o grau de crença. 
    * Baseada em eventos
    * Mais informação, mais certeza na crença
    * O resultado da análise muda conforme a quantidade de dados
    * A função densidade (quantos sucessos no conjunto A) determina o resultado
    * Conhecimento parcial

* Na Lógica Fuzzy - determina o grau de verdade:
    * Baseada em fatos
    * Permanece mesmo com o aumento da quantidade de dados
    * A ideia de "falso" reside no grau de incerteza da afirmação
    * Valor é determinado pela função de pertinência
    * É baseado numa análise crítica, lastreada em eventos anteriores
    * A probabilidade dá espaço à sorte. Fuzzy, não.
    * Verdade Parcial

* Artigos:

https://ieeexplore.ieee.org/document/327367/?reload=true
https://ieeexplore.ieee.org/document/7337858/

---

# 28/08/2018

## Teoria de Conjuntos Fuzzy

* Conceito:

    * Falta de limites precisos de uma coleção de objetos.
      Não existem limites *crisp*

    * A imprecisão é conceitual (diferente do conceito de probabilidade)

* Interpretação

    * Não é generalidade

    * Não é ambiguidade

    * **Os elementos são atribuído às classes através de uma escala numérica**

* Função de pertinência (Interpretação)

    * Similaridade

        * Grau de compatibilidade com a classificação do especialista

        * Muito utilizado em análise de dados

        * *Fit* das características com os parâmetros dos especialistas

    * Incerteza (possibilidade)

        * *Crispiniza* o Fuzzy

        * A escala se dará em possível ou impossível (1, 0)

        * **Contudo, por vezes a possibilidade permite uma escala mais granular. Nesse caso, a pertinência perpassa a escala toda**

    * Preferência (grau de satisfação)

        * Grau de preferência


> Aprimorar as interpretações com base nos slides

* Função de pertinência

    $$A: X -> [0, 1]$$

    * Triangular

    * Trapezoidal

    * Gaussiana

    * Representação Tabular

* **AlphaCut** - Filtra e retorna somente as pertinências acima de um *sarrafo*

    * $>=$

* **Strong-AlphaCut** - **AlphaCut**

    * $>$

* Suporte de um conjunto Fuzzy
    
    * Conjunto dos elementos que não foram *"cutted"*


* Core de um conjunto Fuzzy

    * Conjunto de elementos com grau de pertinência $== 1$

* Altura (hgt(A))

    * Maior grau de pertinência

    * Apelido: *supremum(sup)*

    * **Normal**, $hgt(A) == 1$

    * **Sub-normal**, $htg(A) <> 1$

* Cardinalidade:

    * Somatório dos graus de pertinência por conjunto

    * Associado à granularidade da informação

    * Maior valor, maior nível de abstração (generalização)

        * Grupão, engloba muitos elementos

    * Menor valor, menor granularidade (especifidade)

        * Grupinho, engloba poucos elementos

* Operações

    * Normalização

        * $Norm_A(X) = A(X) / h(A)$

        * Põe os valores dentro dos limites nas escalas

    * Concentração

        * $Con_A(x) = A^2(x)$

        * Minora os valores de pertinência

    * Dilatação

        * $Dil_A(x) = A^0.5(x)$

        * Majora os valores de pertinêcia

* Relações

    * Igualdade

        * $A == B, A(x) == B(x)$

        * Pertinência de cada elemento de um grupo A, é a mesma pertinência do mesmo elemento no grupo B

    * Inclusão

        * $A c B, A(x) <= B(x)$

        * Pertinência do elemento em A é menor do que a pertinência em B

* Exercícios - Moodle:

    * 1:

    ```python
    
    ```