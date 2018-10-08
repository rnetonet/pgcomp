# DetectA: abrupt concept drift detection in non-stationary environments

```
@article{ESCOVEDO2018119,
title = "DetectA: abrupt concept drift detection in non-stationary environments",
journal = "Applied Soft Computing",
volume = "62",
pages = "119 - 133",
year = "2018",
issn = "1568-4946",
doi = "https://doi.org/10.1016/j.asoc.2017.10.031",
url = "http://www.sciencedirect.com/science/article/pii/S1568494617306361",
author = "Tatiana Escovedo and Adriano Koshiyama and Andre Abs da Cruz and Marley Vellasco",
keywords = "Concept drift, Drift detection, Proactive approach"
}
```

## Observações

- Overview do paper sobre Concept Drift:

    - Relevante. Maioria dos problemas do mundo real têm que lidar com Concept Drift
    
    - Originado por ambientes não-estacionários

    -  A atualização frequente do modelo mitiga o Concept Drift, mas é custoso

    - Tipos de Concept Drift:

        - Abrupt / Sudden: B substitui A imediatamente
        
        - Gradual: B, pouco a pouco, se torna prevalente em relação a A
    
    - Formas de lidar:

        - Passive / Reactive: Monitora a taxa de erro do modelo, quando sobe, trata o drift. *Precisa errar para detectar*

        - Proactive: Monitora os padrões e antes de inferir erroneamente detecta o drift, atualiza o modelo. *Não precisa errar para detectar*

- Paper é uma continuação do trabalho em **A2D2: A pre-event abrupt drift detection**

```
@article{Escovedo2015A2D2AP,
  title={A2D2: A pre-event abrupt drift detection},
  author={Tatiana Escovedo and Adriano Soares Koshiyama and Marley M. B. R. Vellasco and Rubens Nascimento Melo and Andr{\'e} Vargas Abs da Cruz},
  journal={2015 International Joint Conference on Neural Networks (IJCNN)},
  year={2015},
  pages={1-8}
}
```

- *Concept Drift* == *Change Detection*

- Paper lida com Concept Drift em Aprendizagem de Máquina - Classificação, mas CD pode ocorrer com Regressão Linear, Séries Temporais, etc

- Trabalhos Relacionados (métodos para detecção Concept Drift de forma pró-ativa):

    - *PCA Feature Extraction for Change Detection in Multidimensional Unlabeled Data*:

        - Extrai componentes usando PCA
        - Componentes com maior variância são acompanhados, por serem mais sensíveis às mudanças
        - Usando *log-likelihood* e o monitoramento da variância e média desses componentes, permite indicar CD
        
        ```
        @ARTICLE{PCAFeatureExtractionChangeDetection, 
        author={L. I. Kuncheva and W. J. Faithfull}, 
        journal={IEEE Transactions on Neural Networks and Learning Systems}, 
        title={PCA Feature Extraction for Change Detection in Multidimensional Unlabeled Data}, 
        year={2014}, 
        volume={25}, 
        number={1}, 
        pages={69-80}, 
        keywords={feature extraction;image classification;image segmentation;principal component analysis;video signal processing;PCA feature extraction;adaptive classification;classification error monitoring;multidimensional unlabeled data;principal component analysis;semiparametric log-likelihood change detection criterion;multidimensional distribution;video segmentation;Feature extraction;Covariance matrix;Principal component analysis;Gaussian distribution;Hidden Markov models;Monitoring;Standards;Change detection;feature extraction;log-likelihood detector;pattern recognition}, 
        doi={10.1109/TNNLS.2013.2248094}, 
        ISSN={2162-237X}, 
        month={Jan},}
        ```

    - *Proactive drift detection: Predicting concept drifts in data streams using probabilistic networks*

        - Usa redes de probabilidades para os próximos pontos de drift

        - Baseia-se no histórico de taxas de mudança

        - Menos falsos positivos

        ```
        @INPROCEEDINGS{ProactiveDriftDetectionProbabilistic, 
        author={K. Chen and Y. S. Koh and P. Riddle}, 
        booktitle={2016 International Joint Conference on Neural Networks (IJCNN)}, 
        title={Proactive drift detection: Predicting concept drifts in data streams using probabilistic networks}, 
        year={2016}, 
        volume={}, 
        number={}, 
        pages={780-787}, 
        keywords={data handling;estimation theory;learning (artificial intelligence);probability;proactive drift detection;concept drifts prediction;data streams;probabilistic networks;future drift points location prediction;reoccurring stream volatility patterns;drift estimation;ProSeed drift detector;Market research;Detectors;Probabilistic logic;Reservoirs;Prediction algorithms;Error analysis;Computer science}, 
        doi={10.1109/IJCNN.2016.7727279}, 
        ISSN={2161-4407}, 
        month={July},}
        ```

- Metodologia **DetectA**
- Reativo ou Pró-ativo:
    - **Reativo:** Instantes $t$ e $t + 1$ devem ter labels. 
    Verifica a diferenças entre informações estatísticas (média, variância) dos dois instantes.

    - **Pró-ativo:** No instante $t + 1$ não existem labels.
    Comparação é feita através da execução de um algoritmo não-supervisionado aglomerativo (*k-means*) para $t$ e $t + 1$, as informações estatísitas derivadas das formações são comparadas.
    Observações:

        - Números de grupos a serem formados é conhecido (número de classes)

        - Centróide inicial é a média condicional do vetor de cada classe

        - Mais eficiente que métodos divisivos

## Conclusões

- Detector é eficiente. Lida bem com datasets de grande dimensionalidade, blocos de tamanho médio, qualquer proporção de drift e ou balanceamento das classes

- O trabalho também detalha um procedimento para produção de streams com drifts abruptos

## Trabalhos Futuros

- Metodologia para substituir a escolha ad-hoc do algoritmo de clusterização (testes com outros algoritmos, análise da silhueta)

- Usar método de classificação mais complexo, ex: ensembles de redes neurais ou abordagens neuro evolutivas

- Abordagem híbrida, combinando abordagem pró-ativa e reativa.
Ao receber dados, verificar pró-ativamente. Se não houver indício, realiza a classificação. Se ocorrer erro, adota a abordagem reativa.

