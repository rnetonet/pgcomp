# An Introduction to Statistics with Python

- Por que Estatística ?

    - Serve para esclarecer questões

    - Identificar variáveis e medidas que reponderão os questionamentos propostos

    - Determinar o tamanho da amostra

    - Descrever a variação

    - Emitir declarações quantificadas sobre os parâmetros estimados

    - Fazer predições baseadas nos dados

- Python

    - Pacotes essenciais:

    `jupyter ipython statsmodels seaborn scipy pandas matplotlib numpy scipy`

    - `numpy` é a biblioteca para realizar cálculos e operações numéricas de forma rápida com Python, normalmente importado:

    ```python
    import numpy as np
    ```

    - Por padrão, `numpy` produz vetores. 

    - Comandos mais utilizados para produzir números:

        - Produzir vetores e matrizes de 0:
        
        ```python
        In [2]: # Vetor de zeros                                           
        In [3]: np.zeros(3)                                                
        Out[3]: array([0., 0., 0.])
        In [4]:                                                            
        In [4]: # Matrix de zeros (requer uma tupla)                      
        In [5]: np.zeros( (2, 3) )                                         
        Out[5]: 
        array([[0., 0., 0.],
               [0., 0., 0.]])
        ```
    
        - Produzir vetores e matrizes de 1:

        ```python
        In [6]: np.ones(3)                                                                                     
        Out[6]: array([1., 1., 1.])
        
        In [7]:                                                                                                
        
        In [7]: np.ones( (2, 3) )                                                                              
        Out[7]: 
        array([[1., 1., 1.],
               [1., 1., 1.]])
        ```

        - Para gerar uma distribuição normal randômica (média = 0, sd = 1):

        ```python
        In [5]: np.random.randn()                                                                              
        Out[5]: 0.22812278352471216
        
        In [6]: np.random.randn(2)                                                                             
        Out[6]: array([ 0.23022709, -1.02568453])
        
        In [7]: np.random.randn(3)                                                                             
        Out[7]: array([ 0.29143315, -0.48103053, -0.86537214])
        ```

        - Gerar sequência de números (`range` normal do Python)

        ```python
        In [9]: np.arange(0, 10, 2) # init, non_inclusive end, step                                            
        Out[9]: array([0, 2, 4, 6, 8])
        ```

        - Gerar uma sequência de números separadas linearmente (n números, dentro do intervalo, com a mesma distância entre eles):

        ```python
        In [20]: np.linspace(0, 10, 3) # start, end, samples                                                   
        Out[20]: array([ 0.,  5., 10.])
        
        In [21]: np.linspace(0, 10, 4) # start, end, samples                                                   
        Out[21]: array([ 0.        ,  3.33333333,  6.66666667, 10.        ])
        ```

        - Para produzir vetores a partir de listas, `np.array`:

        ```python
        In [22]: np.array( [1, 2, 3] )                                                                         
        Out[22]: array([1, 2, 3])
        
        In [23]: np.array( (10, 20, 30) )                                                                      
        Out[23]: array([10, 20, 30])
        ```

        - Matrizes são listas de listas:

        ```python
        In [25]: np.array([ 
            ...:     [1, 2, 3], 
            ...:     [10, 20, 30] 
            ...: ])                                                                                            
        Out[25]: 
        array([[ 1,  2,  3],
               [10, 20, 30]])
        ```

        - Cuidado! Um vetor não é o mesmo que uma matriz unidimensional:

        ```python
        In [26]: x = np.arange(3)                                                                              

        In [27]: x                                                                                             
        Out[27]: array([0, 1, 2])
        
        In [28]:                                                                                               
        
        In [28]: mat = np.array([ [1, 2], [3, 4] ])                                                            
        
        In [29]: mat                                                                                           
        Out[29]: 
        array([[1, 2],
               [3, 4]])
        
        In [30]: x.T                                                                                           
        Out[30]: array([0, 1, 2])
        
        In [31]: x.T == x                                                                                      
        Out[31]: array([ True,  True,  True])
        
        In [32]: mat.T                                                                                         
        Out[32]: 
        array([[1, 3],
               [2, 4]])
        
        In [33]: mat.T == mat                                                                                  
        Out[33]: 
        array([[ True, False],
               [False,  True]])
        
        In [34]: 
        ```

- Pandas

    - Normalmente importado como:

    ```python
    import pandas as pd
    ```

    - O objeto mais importante do Pandas é o `DataFrame`. Pense nele como uma tabela de banco de dados: colunas nomeadas e linhas com valores.

    ```python
    In [42]: import numpy as np                                                                            
    In [43]: import pandas as pd                                                                           
    In [44]: t = np.arange(0, 10, 0.1)                                                                     
    In [45]: x = np.sin(t)                                                                                 
    In [46]: y = np.cos(t)         
    In [48]: df = pd.DataFrame({'Time': t, 'x': x, 'y': y})
    ```

    - Colunas são referenciadas por nome:

    ```python
    In [49]: df.x # or df['x']                                                                                        
    Out[49]: 
    0     0.000000
    1     0.099833
    2     0.198669
    3     0.295520
    4     0.389418
    5     0.479426
    6     0.564642
    7     0.644218
    8     0.717356
    9     0.783327
    10    0.841471
    11    0.891207
    12    0.932039
    13    0.963558
    14    0.985450
    15    0.997495
    16    0.999574
    17    0.991665
    18    0.973848
    19    0.946300
    20    0.909297
    21    0.863209
    22    0.808496
    23    0.745705
    24    0.675463
    25    0.598472
    26    0.515501
    27    0.427380
    28    0.334988
    29    0.239249
            ...   
    ```

    - Para extrair mais de uma coluna por vez, passe uma lista:

    ```python
    In [50]: df[['x', 'y']]                                                                                
    Out[50]: 
               x         y
    0   0.000000  1.000000
    1   0.099833  0.995004
    2   0.198669  0.980067
    3   0.295520  0.955336
    4   0.389418  0.921061
    5   0.479426  0.877583
    6   0.564642  0.825336
    7   0.644218  0.764842
    8   0.717356  0.696707
    9   0.783327  0.621610
    10  0.841471  0.540302
    11  0.891207  0.453596
    12  0.932039  0.362358
    13  0.963558  0.267499
    14  0.985450  0.169967
    15  0.997495  0.070737
    16  0.999574 -0.029200
    17  0.991665 -0.128844
    18  0.973848 -0.227202
    19  0.946300 -0.323290
    20  0.909297 -0.416147
    21  0.863209 -0.504846
    22  0.808496 -0.588501
    23  0.745705 -0.666276
    24  0.675463 -0.737394
    25  0.598472 -0.801144
    26  0.515501 -0.856889
    27  0.427380 -0.904072
    28  0.334988 -0.942222
    29  0.239249 -0.970958
    ..       ...       ...
    ```

    - Para extrair os primeiros registros, use `.head()`. Os últimos, `.tail()`:
    
    ```python
    In [51]: df.head()                                                                                     
    Out[51]: 
       Time         x         y
    0   0.0  0.000000  1.000000
    1   0.1  0.099833  0.995004
    2   0.2  0.198669  0.980067
    3   0.3  0.295520  0.955336
    4   0.4  0.389418  0.921061
    
    In [52]: df.tail()                                                                                     
    Out[52]: 
        Time         x         y
    95   9.5 -0.075151 -0.997172
    96   9.6 -0.174327 -0.984688
    97   9.7 -0.271761 -0.962365
    98   9.8 -0.366479 -0.930426
    99   9.9 -0.457536 -0.889191
    ```

    - DataFrames também suportam slices:

    ```python
    In [54]: df[8:11]                                                                                      
    Out[54]: 
        Time         x         y
    8    0.8  0.717356  0.696707
    9    0.9  0.783327  0.621610
    10   1.0  0.841471  0.540302
    ```

    - Você pode extrair colunas e linhas ao mesmo tempo:

    ```python
    In [55]: df[['x', 'y']][3:6]                                                                           
    Out[55]: 
              x         y
    3  0.295520  0.955336
    4  0.389418  0.921061
    5  0.479426  0.877583
    ```

    - Também é possível usar `iloc` para usar a sintaxe: nlinha, ncoluna:

    > Parâmetros numéricos!

    ```python
    In [59]: df.iloc[3:6, [1, 2]]                                                                          
    Out[59]: 
              x         y
    3  0.295520  0.955336
    4  0.389418  0.921061
    5  0.479426  0.877583
    ```

    - E se quiser acesso direto aos valores, `.values`:

    ```python
    In [61]: df.values                                                                                     
    Out[61]: 
    array([[ 0.        ,  0.        ,  1.        ],
           [ 0.1       ,  0.09983342,  0.99500417],
           [ 0.2       ,  0.19866933,  0.98006658],
           [ 0.3       ,  0.29552021,  0.95533649],
           [ 0.4       ,  0.38941834,  0.92106099],
           [ 0.5       ,  0.47942554,  0.87758256],
           [ 0.6       ,  0.56464247,  0.82533561],
           [ 0.7       ,  0.64421769,  0.76484219],
           [ 0.8       ,  0.71735609,  0.69670671],
           [ 0.9       ,  0.78332691,  0.62160997],
           [ 1.        ,  0.84147098,  0.54030231],
           [ 1.1       ,  0.89120736,  0.45359612],
           [ 1.2       ,  0.93203909,  0.36235775],
           [ 1.3       ,  0.96355819,  0.26749883],
           [ 1.4       ,  0.98544973,  0.16996714],
           [ 1.5       ,  0.99749499,  0.0707372 ],
           [ 1.6       ,  0.9995736 , -0.02919952],
           [ 1.7       ,  0.99166481, -0.12884449],
           [ 1.8       ,  0.97384763, -0.22720209],
           [ 1.9       ,  0.94630009, -0.32328957],
           [ 2.        ,  0.90929743, -0.41614684],
           [ 2.1       ,  0.86320937, -0.5048461 ],
           [ 2.2       ,  0.8084964 , -0.58850112],
           [ 2.3       ,  0.74570521, -0.66627602],
           [ 2.4       ,  0.67546318, -0.73739372],
           [ 2.5       ,  0.59847214, -0.80114362],
           [ 2.6       ,  0.51550137, -0.85688875],
           [ 2.7       ,  0.42737988, -0.90407214],
           [ 2.8       ,  0.33498815, -0.94222234],
           [ 2.9       ,  0.23924933, -0.97095817],
           [ 3.        ,  0.14112001, -0.9899925 ],
           [ 3.1       ,  0.04158066, -0.99913515],
           [ 3.2       , -0.05837414, -0.99829478],
           [ 3.3       , -0.15774569, -0.98747977],
           [ 3.4       , -0.2555411 , -0.96679819],
           [ 3.5       , -0.35078323, -0.93645669],
           [ 3.6       , -0.44252044, -0.89675842],
           [ 3.7       , -0.52983614, -0.84810003],
           [ 3.8       , -0.61185789, -0.79096771],
           [ 3.9       , -0.68776616, -0.7259323 ],
           [ 4.        , -0.7568025 , -0.65364362],
           [ 4.1       , -0.81827711, -0.57482395],
           [ 4.2       , -0.87157577, -0.49026082],
           [ 4.3       , -0.91616594, -0.40079917],
           [ 4.4       , -0.95160207, -0.30733287],
           [ 4.5       , -0.97753012, -0.2107958 ],
           [ 4.6       , -0.993691  , -0.11215253],
           [ 4.7       , -0.99992326, -0.01238866],
    ```

- A grande diferença entre o `numpy` e o `pandas`

    - `numpy` lida primeiramente com linhas, `data[0]` retorna a primeira **linha**

    - `pandas` lida primeiramente com colunas, `data['x'][0]` retorna a primeira linha da coluna **x**

- `loc`, `iloc`

    - Só use `.loc` se suas **linhas** forem nomeadas

    - `iloc` serve para referenciar linhas por números e colunas também:

    ```python
    In [70]: df.iloc[0] # first row                                                                        
    Out[70]: 
    Time    0.0
    x       0.0
    y       1.0
    Name: 0, dtype: float64
    
    In [71]: df.iloc[0, 0:1] # first row, first two columns 0 and 1                                                                  
    Out[71]: 
    Time    0.0
    Name: 0, dtype: float64
    
    In [72]: df.iloc[0, 0:2] # first row, first three columns                                         
    Out[72]: 
    Time    0.0
    x       0.0
    Name: 0, dtype: float64

    In [74]: df.iloc[0:5, 0:3] # first 5 rows, with first 3 columns
    Out[74]: 
       Time         x         y
    0   0.0  0.000000  1.000000
    1   0.1  0.099833  0.995004
    2   0.2  0.198669  0.980067
    3   0.3  0.295520  0.955336
    4   0.4  0.389418  0.921061
    ```

- Agrupamento com `pandas`

