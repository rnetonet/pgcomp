# Pettitt - A Non-Parametric Approach to the Change-Point Problem

```
@article{Pettitt,
	author = {Pettitt, Anthony},
	year = {1979},
	month = {01},
	pages = {},
	title = {A Non-Parametric Approach to the Change-Point Problem},
	volume = {28},
	booktitle = {Journal of the Royal Statistical Society. Series C. Applied Statistics}
}
```

## Observações

- Não-paramétrico: não requer distribuição normal dos dados. 
Analisa números ordinais, que representam posições de um *rank*

- Hipótese **null**: Não houveram mudanças

- Não requer conhecer a distribuição inicial

- Datasets utilizados:

    -  Page (PAGE, 1954)
        - Dados Contínuos (-1.05 a 3.29)
        - Observações de Bernoulli (0, se <= 0 / 1, se > 0)
        - Testes exatos e conservadores
        ```bash
        @article{Page,
        author = {PAGE, E. S.},
        title = {CONTINUOUS INSPECTION SCHEMES},
        journal = {Biometrika},
        volume = {41},
        number = {1-2},
        pages = {100-115},
        year = {1954},
        doi = {10.1093/biomet/41.1-2.100},
        URL = {http://dx.doi.org/10.1093/biomet/41.1-2.100},
        eprint = {/oup/backfile/content_public/journal/biomet/41/1-2/10.1093/biomet/41.1-2.100/2/41-1-2-100.pdf}
        }
        ```

    - *The Lindisfarn Scribes*
        - Binomial (quantidade palavras terminadas em *-s* e *-a*)
        - Autores diferentes, aplicavam terminações diferentes
        - Testes exatos e conservadores
    
    - Dados industriais
        - Percentual de um material na composição de um produto em 27 amostras
        - Testes aproximados 

- Outras técnicas:
    - PAGE - CUSUM
    ```
    @article{Page,
    author = {PAGE, E. S.},
    title = {CONTINUOUS INSPECTION SCHEMES},
    journal = {Biometrika},
    volume = {41},
    number = {1-2},
    pages = {100-115},
    year = {1954},
    doi = {10.1093/biomet/41.1-2.100},
    URL = {http://dx.doi.org/10.1093/biomet/41.1-2.100},
    eprint = {/oup/backfile/content_public/journal/biomet/41/1-2/10.1093/biomet/41.1-2.100/2/41-1-2-100.pdf}
    }
    ``` 

    - Sen and Srivastava - Testes no nível de média para um modelo normal
    ```
    @article{Sen_and_Srivastava,
    author = {Sen, Ashish and Srivastava, M},
    year = {1975},
    month = {01},
    pages = {},
    title = {On Tests for Detecting Change in Mean},
    volume = {3},
    booktitle = {Ann. Stat.}
    }
    ```

    - Hinkley - Probabilidade entre o valor especificado de T e o valor estimado de T
    ```
    @article{Hinkley,
    author = {Hinkley, D},
    year = {1970},
    month = {04},
    pages = {},
    title = {Inference About the Change-Point in a Sequence of Random Variables},
    volume = {57},
    booktitle = {Biometrika}
    }
    ```

    - Smith - Uma abordagem Bayesiana para inferir *change-point*
    ```
    @article{Smith,
    author = {SMITH, A. F. M.},
    title = {A Bayesian approach to inference about a change-point in a sequence of random variables},
    journal = {Biometrika},
    volume = {62},
    number = {2},
    pages = {407-416},
    year = {1975},
    doi = {10.1093/biomet/62.2.407},
    URL = {http://dx.doi.org/10.1093/biomet/62.2.407},
    eprint = {/oup/backfile/content_public/journal/biomet/62/2/10.1093/biomet/62.2.407/2/62-2-407.pdf}
    }
    ```

    - McGilchrist e Woodyer
    ```
    @article{McGilchrist_and_Woodyer,
    author = {A. McGilchrist, C and D. Woodyer, K},
    year = {1975},
    month = {08},
    pages = {321-325},
    title = {Note on a distribution-free CUSUM technique},
    volume = {17},
    booktitle = {Technometrics}
    }
    ```

- O método de Pettitt não requer conhecimento sobre a distribuição inicial. Diferentemente dos outros métodos mencionados acima, que requerem

## Observações sobre a implementação / MOA

- Detecta mesmo quando não há drift
- Muito sensível
- Possivelmente requererá um modelo de janelas