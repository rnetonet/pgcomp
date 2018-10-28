# On learning guarantees to unsupervised concept drift detection on data streams

- Intro
    
    - Utilizando o framework de Estabilidade de Algoritmo, para provar limites de aprendizagem nas técnicas não
    supervisionadas aplicados a detecção de concept drift em streams de dados
    
    - Também implementa o algoritmo Plover, que permite a detecção de concept drift usando as funções de 
    Momentos Estatísticos ou Power Spectrum. Permitindo adaptar a função de medida mais adequada à natureza 
    dos dados.
    
    - STL (Statistical Learning Theory) permite garantir e identificar o melhor algoritmo para aprendizagem supervisionada
    
    - Algoritmos não supervisionados não dispõem de tal arcabouço. Valendo-se de índices internos e externos.
    Contudo, os índices externos utilizam a correta definição dos clusters (labels), o que não é justo.
    Logo, algoritmos não supervisionados, não têm esse aracabouço estatístico.
    
    - Apesar dessas limitações, algoritmos não supervisionados têm sido utilizados na detecção de concept drift em stream de dados.
    
    - Data streams são sequências abertas de dados uni ou multidimensionais, gerados a partir de algum processo.
    
    - Esses processos podem ser afetados ao longo do tempo, alterando o comportamento dos dados gerados: concept drift
    
    - Apesar dos resultados considerados bons, algoritmos não supervisionados usados em CPD não apresentam garantias de aprendizagem
    
    - O paper usa a Estabilidade Algoritimica para quantificar divergências relevantes ao longo do stream, baseando-se 
    que a mudança de conceito ocorre quando o algoritmo corrente deixa de satisfazer a propriedade de Estabilidade Uniforme (Concentration Inequalities)
    
    - O algoritmo proposto permite a mudança da função de medida a depender da natureza dos dados analisados. 
    
    - Existem outros trabalhos que permitem variabilidade na função de medida.
    A grande diferença é que o arcabouço proposto suporta diversas funções, por basear-se na estabilidade algoritmica.
    
    - O algoritmo Plover é apenas um testcase para o framework de garantia de aprendizado apresentado
    
    - O Plover foi testado com: mean, variance, kurtosis. **Um extensão possível é a aplicação de outras funções de medida.**
    
- Trabalhos Relacionados

    - Aprendizado não supervisionado = implícito

    - Os algoritmos totalmente implícitos tendem a detectar drift mesmo se o modelo atual ainda for útil, pois 
    baseiam-se apenas na distribuição dos dados

- Concentration Inequalities

    - Métodos para prover limites sobre como uma variável randômica desvia de algum valor (normalmente seu valor esperado)

- Estabilidade Uniforme

    - Considerando um data strem com perturbações, mas oriundas de uma mesma probabilidade de distribuição

    - Aplica uma função de loss ao longo do stream comparando duas janelas, provando que o modelo se mantém 
    suficiente para classificação dos dados

    - A função de loss pode ser completamente independente dos dados, sem causar o risco de virar um classificador de memória. 
    Lembre-se: algoritmo não supervisionado. Não há labels.

    - Requer que os dados sejam i.i.d (independentes e identicamente distribuídos)

    - A exigência de um stream i.i.d traz desafios, tendo em vista que muitos streams apresentam dependência entre seus valores.
    Contudo, a reconstrução de streams em phase-spaces sana parte deles.

- Plover

    - Algoritmo para detecção de concept drift baseado na uniformidade-estável

    - Requisitos:
        
        - Função loss (`l()`), deve ser independente dos dados

        - Stream deve ser i.i.d

    - Algoritmo:

        ```
        # parameters
        stream
        loss_function()
        max_window_length 
        probability
        threshold

        # algorithm
        queue = []
        while stream:
            observation = next(stream)
            queue.append(observation)

            if len(queue) == max_window_size:
                current_measure = compute_measure(loss_function, queue)
                divergence = calculate_divergence(previous_measure, current_measure)
                divergence_term = calculate_divergence_term()
            
                if divergence_term > threshold:
                    raise DriftDetection()
        ```
    
    - 4 principais parâmetros:

        - probability = ex: 0.05 (classificador é bom 95%)

        - threshold (baseado em divergências anteriores)
        
        - função de loss(). o paper usa um momento estatístico:
            
            - mean: comportamento médio é mantido
            
            - variance: amplitude entre divergências
            
            - skewness: medida de assimetria sobre a média, positivo, negativo ou indefinida. 
            Permite identificar tendências.

            - kurtosis: Permite descrever o formato da probabilidade de distribuição dos dados.
            Útil para identificar outliers.

        - tamanho da janela

            - alguns autores julgam problemático

            - mas se a frequência for conhecida, pode-se usar o teorema de Nyquist-Shannon: 
            para analisar e tirar conclusões, precisa-se do dobro de dados de um ciclo.

            Ex: 125 dados a cada ciclo. o mínimo para poder analisar será 250.

            - Usando técnicas de Power Spectrum (oriundas do processamento de sinais), 
            permite reduzir a janela até quando as magnitudes da janela de tamanho `p` 
            são muito próximas ou iguais as magnitudes janela com `2p`

            - Implementa um algoritmo para cálculo do tamanho da janela:

                - Realiza uma transformação de Fourier, obtendo um matriz associando frequências e amplitudes aos dados.
                Compara duas janelas diferentes: uma com `w` e outra com `w + 1`, para verificar a divergência com o aumento da janela.

                - Usa DTW para encontrar o melhor match entre as séries temporais

                - Com o resultado da DTW, é possível plotar o tamanho da janela X divergência, inferindo o tamanho da janela 
                quando as divergências diminuem e ficam muito pequenas.

- Experimentos e resultados

    - 4 sintéticos. 3 oriundos de uma distribuição normal e 1 de um stream sinusiodal (testando o power spectrum)

    - 2 real-world: música de Beethoven (Fur Elise) que tem mudanças de harmonia e o índice S&P 500, para detectar 
    o momento de reflexão da crise americana de 2008.

    - O algoritmo depende fortemente da escolha correta da função adequada à natureza dos dados

    - A análise de Power Spectrum é mais versátil, por verificar amplitude e frequência

    - Forams feitos testes com dados do mundo real não supervisionados:

        - Preço do bitcoin

        - Vôos atrasados no aeroporto LAX
    
- Discussão

    - **Oportunidade de pesquisa: adicionar as garantias de aprendizagem, como feito neste trabalho, aos algoritmos de rede neural, Self-Organizing Novelty Detection (SONDE) e Grow When Required (GWR). ** 

- Sobre o arcabouço de garantia de aprendizagem:

    - Utiliza o conceito de Estabilidade Algoritmica de Bousque e Elisseef, que provê condições para convergência 
    entra uma função e a o seu valor estipulado. No caso, alguma função de divergência, permitindo verificar a 
    estabilidade do algoritmo. O conceito baseia-se na teoria de *Concentration Inequality*, que estabelece limites 
    de como e quanto uma variável randômica se afasta de um valor (normalmente do seu valor esperado).

    - Somatório dos casos de sucesso, mostrando que o modelo ainda representa o stream.