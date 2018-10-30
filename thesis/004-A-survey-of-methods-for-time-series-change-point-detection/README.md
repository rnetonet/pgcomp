# A survey of methods for time series change point detection

- *Change points* - variações abruptas em séries temporais. Podem representar mudanças de estado. 

- Detecção de change point é útil para modelagem e predição de séries temporais

- Existem métodos supervisionados e não-supervisionados

- Conceitos similares, com técnicas muito próximas: *segmentation*, *edge detection*, *event detection*, *anomaly detection*

- *Change point detection* é próximo aos problemas de: *change point estimation*, *change point estimation* e *change point mining*

- Mas *change point estimation* foca em modelar e interpretar as mudanças em uma série temporal, ao invés de apenas detectar a mudança.
Foco de estimar é descrever a natureza e o grau da mudança identificada.

- Alguns exemplos motivacionais:

    - Monitoramento de condições médicas

    - Detecção de mudanças climáticas

    - Detecção de limites (entre palavras, sentenças, silêncios e ruído) - reconhecimento de fala

    - Análise de imagens ou vídeos

    - Detectar alterações na atividade humana (interrupções/notificações mais suaves, mudanças de saúde)

- Definições

    - Série Temporal é uma sequência infinita de vetores ou unidades de dados recebidos a cada intante de tempo

    - Série Temporal estacionária: série temporal cujas propriedades estatísticas (média, por exemplo) se mantêm constantes

    - Um caso especial de Série Temporal estacionária é IID, Independente e Igualmente Distribuída, são independentes e 
apresentam a mesma probabilidade de distribuição

    - Dada uma série temporal de tamanho T (um recorte de uma série infinita até o instante t), é possível gerar uma matrix 
todas subsequências possíveis de tamanho k, movendo uma janela deslizante de tamanho k através de T

    - **Change point** representa uma transição de estado para o processo produtor da série temporal

    - Detecção de Change Point -> Teste de hipótese -> Hipótese null: não há mudança / Hipótese alternativa: há mudança

- Critérios dos algoritmos de CPD

    - Online x Offline

        - Offline: Analisa um batch de dados já produzido e identifica todos change points
    
        - Online: Avalia enquanto o processo corre. Recebe cada dado e analisa se é um change point, idealmente antes do próximo dado
            - Contudo, nenhum algoritmo na prática opera em tempo real, pois precisa comparar os dados recebidos com novos dados, o que varia é a quantidade necessária de novos dados
            (`e-real-time` algorithm: algoritmo que requer `e` novos dados para conseguir detectar change points)
    
    - Escalabilidade
        
        - Algoritmos de detecção de CP devem ser eficientes, pois as séries temporais de interesse normalmente são grandes em número de pontos e dimensões
    
            - As técnicas não paramétricas são mais eficientes (dados não possuem estruturas ou características comuns sabidas)
    
            - Paramétricos usam um modelo, treinam e discartam os dados de treinamento
    
            - Não-paramétricos retem tudo para realizar a inferência
    
            - Boas alternativas para o trade-off entre boa predição e performance são:
            
                - Algoritmos anytime: podem ser interrompidos e retornam o melhor valor obtido até aquele momento
    
                - Algoritmos com contrato SLA: algoritmos com timeout
    
                - Todo algoritmo anytime pode se tornar um algoritmo com SLA, o inverso nem sempre

    - Restrições dos Algoritmos

        - Restrições impostas aos dados ou ao próprio algoritmo

        - Quanto aos dados, alguns algoritmos podem requerer: número de change points nos dados, número de estados, features dos estados

        - Em métodos paramétricos, é importante saber o quanto o algoritmo é sensível a escolha inicial dos dados

- Avaliação de performance

    - Se considerarmos apenas output, existem três tipos de algoritmos de detecção de change point:
    
        1. Houve Change Point - Sim/Não (Classificador Binário)
        
        1. Níveis variados de precisão - CP ocorre dentro de de X unidades de tempo (Classificador multiclasse ou algoritmos não supervisionados)

        1. Tempo da próxima mudança ou o tempo de todas mudanças
    
    - Para os dois primeiros tipos, podemos usar as métricas normais de algoritmos de classificação. Começando com uma matrix de confusão.

    - As métricas a seguir também são aplicadas, apesar de serem naturais de classificadores binários. Mas podem ser definidas para cada uma das classes:

        - Acurácia: acertos / total

        - Taxa de erro: 1 - acurácia

        - ***Acurácia e Taxa de Erro* não são bons indicadores para variação de distribuição. Qualquer erro de classificação é tratado igual. Prefira Sensibilidade e média G.**

        - Sensibilidade = *Recall* = *TP (True Positive) Rate*: "Percentual de pessoas doentes que de fato foram classificadas como doentes": `TruePositive / Positive` ou `TruePositive / TruePositive / FalseNegative`

        - Especifidade = *TN (True Negative) Rate*: "Percentual de pessoas saudáveis que de fato **não** foram classificadas como doentes": `TN/N` ou `TN / (FP + TN)`

        - G-mean ou Média - G: As classes detectadas são desbalanceadas, assim o G-mean é um bom indicador da performance do algoritmo de detecção de CP. $\sqrt{Sensibilidade x Especifidade}$

        - Precisão: Percentual de Change Points detectados corretamente em relação a todos change points detectados: $\frac{TP}{TP + FP}$

        - F-measure ou F-score: Razão com pesos entre Precisão e Recall (Sensibilidade).

        - Curvas ROC (Gráfico da relação TP (y)) x FP (x)): Melhor algoritmo se o ponto estiver mais próximo a (0, 1).
        Para ver a performance média de um algoritmo, podemos calcular a área embaixo da curva (AUC). Quanto mais próximo de 1, melhor.

        - Curva Precisão / Recall: Similar à curva ROC, mas plota a Precisão em relação à Especifidade. 
        O bom algoritmo tem seu ponto plotado, nesse gráfico, mais próximo ao topo direito (1, 1).
        Também permite o cálculo da AUC, sendo bastante informativo quando a distribuição de classes é muito enviesada.

    - Agora, se a distância entre o CP predizido e o CP de fato é uma medida de performance, as métricas acima não servem.
    Outras podem ser aplicadas:

        - MAE (Mean Absolute Error - Média de Erro Absoluto):
        Média dos somatórios das distâncias absolutas entre os CPs preditos e os CPs de fato: 

        $MAE = \frac{\sum_{i=1}^{\#CP}|PredictedCP - ActualCP|}{\#CP}$

        - MSE (Mean Squared Error - Média de Erro Elevada): Similar ao MAE, mas por elevar o somatório, evidencia outliers: 
        
        $MSE = \frac{\sum_{i=1}^{\#CP}|PredictedCP - ActualCP|^2}{\#CP}$

        - MSD (Mean Signed Difference - Média de Erro considerando o sinal): Similar ao MAE, mas não faz o módulo, passando a levar em conta a direção do erro. 
        
        $MSD = \frac{\sum_{i=1}^{\#CP}PredictedCP - ActualCP}{\#CP}$

        - RMSE (Root Mean Squared Error - Erro médio elevado e raíz):
        
        $RMSE = \sqrt{\frac{\sum_{i=1}^{\#CP}|PredictedCP - ActualCP|^2}{\#CP}}$

        - NRMSE (Normalized Root Mean Squared Error - Erro médio elevado raíz normalizado): É o RMSE normalizado, permitindo comparar entre datasets diferentes, pois a escala de valores dos CPs é desprezada.

        $NRMSE1 = \frac{RMSE}{MaxLength(ActualCP) - MinLength(ActualCP)}$

        $NRMSE2 = \frac{RMSE}{Mean(ActualCP)}$

- Métodos de Aprendizagem de Máquina aplicados a CPD:

    - Supervisionados

        - Binários ou multi-classe

        - Multi-classe: Se número de estados for conhecido, o algoritmo perpassa os dados usando uma janela deslizantes, comparando os datapoints para encontrar os limites entre estados. Algoritmos: Decision Tree, Nearest Neighbor, SVM, Naive Bayes, Baysian Net, HMM (Markov), Conditional Random Field (CRF), Gaussian Mixture Model (GMM).

        - Binário: Apenas duas classes, normal e em mudança (CP). Apesar de menos classes, é um problema de aprendizado mais complexo, pois podem ter diferentes formas de estado de "mudança". 
        
            Se for utilizado um algoritmo que produza resultados interpretáveis (Decision Tree, por exemplo), também será possível entender a natureza da mudança, além do CP.

            Classificadores binários tendem a sofrer com o desbalanceamento de classes, pois haverão mais "estados normais" do que estados de "mudança".

        - Um outro método é a utilização de um Classificador Virtual (VC). Duas janelas, labels +1 na primeira, labels -1 na segunda.
        Treina-se um classificador virtual com essas duas janelas. Se há um change point, ambas janelas devem ser devidamente classificadas 
        com uma acurácia maior que 0.5

        - Métodos não supervisionados para detecção de change point:
            
            - Likelihood: 
                - Probability Density: CUSUM, Change Finder
                - Direct Ratio: KLIEP, uLSIF, RuLSIF, SPLL
            
            - Subspace Model: SI, SST

            - Probabilistic Methods: Gausiann Process, Bayesian

            - Kernel Based Method

            - Graph Based Methods

            - Clustering: SWAB, MDL, Shapelet, Model Fitting

- Métodos não supervisionados

    - Usados em dados sem labels

    - Segmenta séries temporais, permitindo encontrar change points com base 
    nas diferenças estatísticas entre os segmentos

    - Likelihood ratio: 

        - Analisa a probabilidade da distribuição de uma janela antes e outra depois de um possível change point. Monitora o logaritmo do "likelihood ra
        ratio" desses dois intervalos, se diferirem acima de um limite, 
        indica um change point

        - Principais: CUSUM e Change Finder. Contudo, ambos são paramétricos.

        - Novos métodos têm usado "direct density ratio" para permitir dados não paramétricos

        - SPLL é mais recente e é semi paramétrico

    - Subspace model methods

        - Aplica técnicas de identificação de sistemas, teoria do controle
    
    - Probabilistc Methods

        - Bayesian era aplicado inicialmente de modo offline, usando segmentação retrospectiva

        - BCPD, Bayesin online, surge assumindo que uma série temporal pode ser dividida em partições estados 
        não sobrepostas e que os dados em uma partição são i.i.d a uma probabilidade de distribuição.
        A utilização da variável run length permite utilizar todos intervalos anteriores para predizer a distribuição 
        do próximo intervalo. Se o cálculo de probabilidade do novo intervalo for o maior, change point.

        - Gaussian: Usa predição gaussian com noise para predizer distribuição em t, usandos dados até t - 1.
        Se a diferença entre a predição e a distribuição de fato, assum change point.

        Por considerar todos dados até t-1 é mais complexo e preciso que o BCPD.

    - Kernel-based methods

        - Normalmente aplicados ao aprendizado supervisionado, algumas técnicas utilizam para cálculo a homogeneidade dos 
        dados na janela anterior e na atual (RKHS), usando o teste de Fisher.

        - Sofrem pois são muito dependentes da escolha do Kernel e seus parâmetros. É ainda mais problemático para problemas 
        com moderada ou alta dimensionalidade

    - Graph based methods

        - Séries temporais podem ser tratadas como grafos

        - Observações como nós e arestas conectandos-os, denotando a distância entre eles

        - Não paramétrico

        - Grafo pode ser definido usando minimum spanning tree, minimum distance pairing, nearest neighbor graph ou visibility graph

        - Constrói o grafo. Cada nó considerado um potencial change point, divide o grafo em dois, A e B.

        - O número de arestas é levado em conta na detecção de change point. Arestas menores, portanto, favorecem a identificação

        - Se ultrapassar determinado limite (threshold), indica change point

        - Muito útil para dados com alta dimensionalidade e poucas informações sobre os parâmetros, apesar de usar pouco 
        as informações da série temporal em si, fiando-se na construção do grafo

    - Métodos Clustering (não supervisionado)

        - Podemos considerar o problema de change point como um problema de clusterização com o número de clusters conhecidos ou não

        - Se uma observação está em um cluster em t e em outro em t + 1, change point

        - SWAB, MDL (Minimum Description Length), u-Shapelet (distância de S para parte da série temporal é muito menor que para todo o resto da série temporal), Model fitting (nova observação não se enquadra me nenhum dos clusters existentes)

- Discussões e comparações

    - Online vs Offline

        - Métodos Supervisionados: n-real time. Precisam apenas das n instâncias de treinamento.

        - Likelihood ratio: Comparam duas janelas. Precisam da anterior e da atual. n + k realtime.

        - Subspace model: Similares a likelihood ratio. n + k realtime.

        - Probabilistic: Precisam de apenas uma janela. n realtime.

        - Kernel based: Também usam janelas deslizantes. Mas precisam de retrospectiva. n + k realtime.

        - Clustering:

            - SWAB: w (tamanho do buffer) realtime

            - MDL e Shapelet: offline (precisam de toda série temporal)

            - Model fitting: n-realtime (precisa de apenas uma janela)

        - Graph based: n-realtime, usa apenas uma janela.

    - Ordenamento de Offline para Online:

        - Shapelet + MDL -> SWAB -> Likelihood + Subspace + Kernel -> Supervised + Probabilistic + Model Fitting + Graph
    
    - Escalabilidade

        - Não paramétricos melhores que paramétricos

        - Algoritmos supervisionados são difíceis de mensurar

        - **Não há nenhum algoritmo com contrato de tempo SLA ou que seja interruptível. Espaço para pesquisa.**

        - Quando lidamos com séries temporais multi dimensionais, o custo computacional aumenta

        - O único algoritmo que requer valores discretos é o MDL, todos outros aceitam discretos e contínuos

        - Métodos supervisionados tendem a ter melhores resultados, mas dependem de bons dados para treinamento e 
        saber sobre todos possíveis estados da série temporal

        - Métodos não supervisionados se fiam na mudança de distribuição dos dados antes e depois do change point

        - Maioria dos algoritmos não supervisionados de CPD tem alguma limitação quanto ao tipo de dado da série.
        Por vezes dependendo de um sistema de forgetting para lidar com observações antigas.

    - Performance

        - Comparar performance entre algoritmos testados com diferentes datasets é complicado

        - **A maioria dos estudos não traz comparações ou informações sobre a performance do algoritmo. Espaço para pesquisa.**

        - Datasets utilizados:

            - Speech recognition This is the IPSJ SIG-SLP Corpora and Environments for Noisy Speech Recognition (CENSREC) dataset provided by the National Institute of Informatics (NII)

            - ECG This is a respiration dataset found in the UCR Time Series Data Mining Archive. This dataset records patients’ respiration measured by thorax extension as they wake up. The series is manually segmented by a medical expert.
        
            - Speech recognition This dataset represents soundtracks from popular French 1980s entertainment TV shows (“Le Grand ’Echiquier”). The dataset comprises roughly three hours of sound track data.

            -   Brain–Computer Interface Data Signals acquired during these brain–
            computer interface (BCI) trial experiments naturally exhibit temporal structure. The
            corresponding dataset formed the basis of the BCI competition III. Data are acquired
            during four non-feedback sessions on three normal subjects where each subject was
            asked to perform different tasks, where time when the subject switches from one task to
            another are random.
            

            - Iowa Crop Biomass NDVI Data The NDVI time series data was available as
            a data product for years 2001–2006. In this dataset, observations were made for every
            sixteen days.
            
            - Smart Home Data These data represent sensor readings collected in a smart
            apartment located on the on WSU campus. The apartment is equipped with infrared
            motion/ambient light sensors, door/ambient temperature sensors, light switch sensors,
            and power usage sensors. The data are labeled with corresponding human activities and
            changes naturally occur between the activities.
            
            - Human activity dataset. This is a subset of the Human Activity Sensing
            Consortium challenge 2011, which provides human activity information collected by
            portable three-axis accelerometers. The task of change point detection is to segment the
            time series data according to the six behaviors: “stay”, “walk”, “jog”, “skip”, “stair up”,
            and “stair down”.
        
        - Em resumo:

            - Métodos supervisionados tendem a ser melhores, se houver bastante dado de treinamento e a série for estacionária

            - Senão, não supervisionados são melhores

            - **Não há uma análise rigorosa de performance entre os métodos não supervisionados. Espaço para pesquisa.**

            - Para séries com alta dimensão, opte por Graph ou Probabilistícos.

- Conclusões, desafios e trabalhos futuros

    - **Problemas em aberto:**
        
        - Algoritmos mais online:
            
            - Menor janela
            
            - Algoritmos anytime ?

        - Análise da robustez dos algoritmos

        - Além de saber que houve uma mudança, é necessário entender a natureza da mudança. 
        Calcular índices de dissimilaridade quando do change point pode ser uma solução.

       - Desenvolver método para o cálculo automático de threshold para indicar CP

       - Lidar com séries não estacionárias (trends), concept drift. 
       A mistura de métodos de CPD com Concept Drift é desafiador mas importante, pois muitos problemas do mundo real dependem disso.

       