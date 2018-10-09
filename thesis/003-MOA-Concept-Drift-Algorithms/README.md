# MOA - Concept Drift Algorithms

## Interfaces e classes abstratas

- Interface `ChangeDetector`

```java
// Reseta o detector
public void resetLearning();

// Adiciona um valor numérico para o detector
public void input(double inputValue);

// Houve mudança ? true ou false
public boolean getChange();

// Está na "warning zore" ? Isto é, entre um alerta e a detecção de fato de um drift
public boolean getWarningZone();

// Predição do próximo valor
public double getEstimation();

// Tamanho do delay na detecção da mudança
public double getDelay();

// Array:
// número de detecções, número de alertas, delay e predição do próximo valor
public double[] getOutput();

// String com representação do modelo
public void getDescription(StringBuilder sb, int indent);

// Retorna uma cópia _deste_ detector
public ChangeDetector copy();
```

- Classe Abstrata - `AbstractChangeDetector`

```java
// Atributos
protected boolean isChangeDetected;
protected boolean isWarningZone;
protected double estimation;
protected double delay;
protected boolean isInitialized;

// Reinicia o detector
public void resetLearning() {
    this.isChangeDetected = false;
    this.isWarningZone = false;
    this.estimation = 0.0;
    this.delay = 0.0;
    this.isInitialized = false;
}

// Output
public double[] getOutput() {
    double[] res = {this.isChangeDetected ? 1 : 0, this.isWarningZone ? 1 : 0, this.delay, this.estimation};
    return res;
}

// Cópia do detector
public ChangeDetector copy() {
    return (ChangeDetector) super.copy();
}
```

## ADWIN - Learning from Time-Changing Data with Adaptive Windowing

```
@INPROCEEDINGS{Bifet07learningfrom,
    author = {Albert Bifet and Ricard Gavaldà},
    title = {Learning from time-changing data with adaptive windowing},
    booktitle = {In SIAM International Conference on Data Mining},
    year = {2007}
}
```

- Observações:
    
    - Utiliza janelas de tamanho variável, que são recomputadas online, 
de acordo com a taxa de mudança observada nos dados dessas janelas

    - O algoritmo aumenta dinamicamente a janela (W) enquanto não há mudanças no contexto e diminui quando uma mudança é detectada. 

    - O algoritmo tenta encontrar duas "subjanelas" dentro de W que apresentem médias divergentes

    - Se encontrar, a subjanela mais antiga é descartada, ensejando a detecção de um drift

    - O tamanho máximo da janela (W) é estatisticamente consistente com a hipótese que não houve mudança no valor médio da janela

    - O algoritmo também apresente garantias rigorosas a cerca da performance, com limites para o número de falso positivos e falso negativos

    - Não detecta drift quando não há

## CusumDM

```
@article{citeulike:3720621,
    author = {Page, E. S.},
    citeulike-article-id = {3720621},
    citeulike-linkout-0 = {http://dx.doi.org/10.2307/2333009},
    citeulike-linkout-1 = {http://www.jstor.org/stable/2333009},
    doi = {10.2307/2333009},
    issn = {00063444},
    journal = {Biometrika},
    keywords = {changepoint, classic},
    number = {1/2},
    pages = {100--115},
    posted-at = {2008-12-03 00:32:25},
    priority = {2},
    publisher = {Biometrika Trust},
    title = {{Continuous Inspection Schemes}},
    url = {http://dx.doi.org/10.2307/2333009},
    volume = {41},
    year = {1954}
}
```

- Observações:

    - Não detecta drift quando não há

    - [Link explicação Wikipedia](https://en.wikipedia.org/wiki/CUSUM)

- Parâmetros:

```java
// Número mínimos de instâncias antes de verificar por mudanças
// Padrão: 30
public IntOption minNumInstancesOption = new IntOption(
            "minNumInstances",
            'n',
            "The minimum number of instances before permitting detecting change.",
            30, 0, Integer.MAX_VALUE);

// "delta" - fator de "tolerância" do teste
public FloatOption deltaOption = new FloatOption("delta", 'd',
        "Delta parameter of the Cusum Test", 0.005, 0.0, 1.0);

// "lambda" - limite do teste
public FloatOption lambdaOption = new FloatOption("lambda", 'l',
        "Threshold parameter of the Cusum Test", 50, 0.0, Float.MAX_VALUE);
```

- Atributos:

```java
// Atributos e valores de inicialização

// número de instâncias
private int m_n = 1;

// soma
private double sum = 0.0;

// média
private double x_mean = 0.0;

// Valor da configuração
private double delta = this.deltaOption.getValue();
private double lambda = this.lambdaOption.getValue();
```

- Funcionamento Java:

```java
input(x):
    // média_x = media_x + ((x - media_x) / num_instancias)
    // nova média é a média anterior + a diferença do valor atual // para com a média anterior, dividido pelo número de instâncias
    x_mean = x_mean + (x - x_mean) / (double) m_n

    // soma = max(0, soma + x - media_x - delta)
    // soma é no mínimo zero, ou a soma anterior + a instância atual - a média - delta
    sum = Math.max(0, sum + x - x_mean - delta);

    // num_instancias++
    m_n++;

    // media_x é a estimativa
    this.estimation = x_mean;
    
    // não calcula delay, pois detecta na chegada da instância
    this.isChangeDetected = false;
    this.isWarningZone = false;
    this.delay = 0;

    // se a soma > lambda (limite no teste)
    if (sum > lambda) {
        isChangeDetected = true;
    }
}
```

- Implementação Python:

[cusumdm.py](cusumdm.py)

## Learning with Drift Detection - DDM

```
@InProceedings{10.1007/978-3-540-28645-5_29,
author="Gama, Jo{\~a}o
and Medas, Pedro
and Castillo, Gladys
and Rodrigues, Pedro",
editor="Bazzan, Ana L. C.
and Labidi, Sofiane",
title="Learning with Drift Detection",
booktitle="Advances in Artificial Intelligence -- SBIA 2004",
year="2004",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="286--295"
}
```

- Observações:

    - Não detecta drift quando não há

- Parâmetros

```java
public IntOption minNumInstancesOption = new IntOption(
        "minNumInstances",
        'n',
        "The minimum number of instances before permitting detecting change.",
        30, 0, Integer.MAX_VALUE);

public FloatOption warningLevelOption = new FloatOption(
        "warningLevel", 'w', "Warning Level.",
        2.0, 1.0, 4.0);
    
public FloatOption outcontrolLevelOption = new FloatOption(
        "outcontrolLevel", 'o', "Outcontrol Level.",
        3.0, 1.0, 5.0);
```

- Atributos

```java
m_n = 1;
m_p = 1;
m_s = 0;
m_psmin = Double.MAX_VALUE;
m_pmin = Double.MAX_VALUE;
m_smin = Double.MAX_VALUE;
minNumInstances = this.minNumInstancesOption.getValue();
warningLevel = this.warningLevelOption.getValue();
outcontrolLevel = this.outcontrolLevelOption.getValue();
```

- Funcionamento Java

```python
public void input(double prediction) {
    // prediction must be 1 or 0
    // It monitors the error rate
    if (this.isChangeDetected == true || this.isInitialized == false) {
        resetLearning();
        this.isInitialized = true;
    }
    m_p = m_p + (prediction - m_p) / (double) m_n;
    m_s = Math.sqrt(m_p * (1 - m_p) / (double) m_n);

    m_n++;

    // System.out.print(prediction + " " + m_n + " " + (m_p+m_s) + " ");
    this.estimation = m_p;
    this.isChangeDetected = false;
    this.isWarningZone = false;
    this.delay = 0;

    if (m_n < minNumInstances) {
        return;
    }

    if (m_p + m_s <= m_psmin) {
        m_pmin = m_p;
        m_smin = m_s;
        m_psmin = m_p + m_s;
    }

    if (m_n > minNumInstances && m_p + m_s > m_pmin + outcontrolLevel * m_smin) {
        //System.out.println(m_p + ",D");
        this.isChangeDetected = true;
        //resetLearning();
    } else if (m_p + m_s > m_pmin + warningLevel * m_smin) {
        //System.out.println(m_p + ",W");
        this.isWarningZone = true;
    } else {
        this.isWarningZone = false;
        //System.out.println(m_p + ",N");
    }
}
```

- Implementação Python

[ddm.py](ddm.py)

## Early Drift Detection Method - EDDM

```
@inproceedings{EDDM,
    author = {Baena-Garc{\'{\i}}a, Manuel and del Campo-{\'{A}}vila, Jos{\'{e}} and Fidalgo, Ra{\'{u}}l and Bifet, Albert and Gavald{\'{a}}, Ricard and Morales-Bueno, Rafael},
    booktitle = {In Fourth International Workshop on Knowledge Discovery from Data Streams},
    citeulike-article-id = {7359988},
    keywords = {concept, data, drift, learning, machine, mining},
    posted-at = {2010-06-26 09:39:10},
    priority = {0},
    title = {{Early drift detection method}},
    year = {2006}
}
```

- Observações:

    - Detecta mesmo quando não há

- Parâmetros

    - Não parametrizável

- Atributos

```java
FDDM_OUTCONTROL = 0.9;
FDDM_WARNING = 0.95;
FDDM_MINNUMINSTANCES = 30;

m_n = 1;
m_numErrors = 0;
m_minNumErrors = 30;
m_d = 0;
m_lastd = 0;
m_mean = 0.0;
m_stdTemp = 0.0;
m_m2smax = 0.0;
estimation = 0.0;
```

- Funcionamento Java

```java
m_n++;

if (prediction == 1.0) {
    m_numErrors += 1;
    m_lastd = m_d;
    m_d = m_n - 1;
    int distance = m_d - m_lastd;
    double oldmean = m_mean;
    m_mean = m_mean + ((double) distance - m_mean) / m_numErrors;
    this.estimation = m_mean;
    m_stdTemp = m_stdTemp + (distance - m_mean) * (distance - oldmean);
    double std = Math.sqrt(m_stdTemp / m_numErrors);
    double m2s = m_mean + 2 * std;

    if (m2s > m_m2smax) {
        if (m_n > FDDM_MINNUMINSTANCES) {
            m_m2smax = m2s;
        }
    } else {
        double p = m2s / m_m2smax;
        if (m_n > FDDM_MINNUMINSTANCES && m_numErrors > m_minNumErrors && p < FDDM_OUTCONTROL) {
            this.isChangeDetected = true;
        }
    }
```

- Implementação Python

