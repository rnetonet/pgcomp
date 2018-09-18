---
theme: "white"
customTheme: "notes"
transition: "fadeIn"
highlightTheme: "tomorrow"
center: false
controls: true
---

# MOA

---

Algoritmos - Drift Detection

```bash
moa/classifiers/core/driftdetection/
├── AbstractChangeDetector.java
├── ADWINChangeDetector.java
├── ADWIN.java
├── ChangeDetector.java
├── CusumDM.java
├── DDM.java
├── EDDM.java
├── EnsembleDriftDetectionMethods.java
├── EWMAChartDM.java
├── GeometricMovingAverageDM.java
├── HDDM_A_Test.java
├── HDDM_W_Test.java
├── PageHinkleyDM.java
├── RDDM.java
├── SEEDChangeDetector.java
├── SeqDrift1ChangeDetector.java
├── SeqDrift2ChangeDetector.java
└── STEPD.java
```

---

Todos algoritmos estendem a interface `AbstractChangeDetector`:

```java
void resetLearning()          // Recomeça do zero o detector de novidades
void input(double inputValue) // Adiciona um valor númerico ao detector de novidades
boolean getChange()           // Houve mudança ?
boolean getWarningZone()      // Está na zona de perigo ? (Entre um aviso e o alerta de mudança propriamente dito)
double getEstimation()        // Predição do próximo valor
double getDelay()             // Tamanho do "delay" na mudança identificada
double[] getOutput()          // [nMudanças, nAvisos, delay, estimativa]
```

---

`ADWINChangeDetector.java`

- Baseado em `ADaptive sliding WINdow (ADWIN)`

- Mantém uma janela de tamanho variável de dados recentes

- Janela sempre tem o maior tamanho possível (*length*) que mantenha a média entre os elementos do recorte

```java
// ADWIN.java
public double getEstimation() {
    return TOTAL / WIDTH;
}

// ADWINChangeDetector.java
double ErrEstim = this.adwin.getEstimation();
if(adwin.setInput(inputValue)) {
        if (this.adwin.getEstimation() > ErrEstim) {
        this.isChangeDetected = true;
    }
}
```

---

`CusumDM.java`

- Baseado na soma cumulativa (E. S. Page)

- Baseado em um número de qualidade (θ). A média da distribuição, por exemplo

- Permite detectar mudanças abruptas em séries temporais

```java
public void input(double x) {
    // ...

    // m_n = n instancias
    x_mean = x_mean + (x - x_mean) / (double) m_n;
    m_n++;

    // calcula a soma cumulativa
    sum = Math.max(0, sum + x - x_mean - this.delta);

    // se não alcançou o número mínimo de instâncias para analizar, continua
    if (m_n < this.minNumInstancesOption.getValue()) {
        return;
    }

    // se a soma é maior que o threshold, indica mudança
    if (sum > this.lambda) {
        this.isChangeDetected = true;
    } 
```

---

`DDM.java`

- Criado pelo João Gama. Baseia-se em controle de taxa de erro

- Utiliza a ideia de "contextos", sequências de dados em que a distribuição é estacionária

- Modelo é treinado (Perceptron, Rede Neural, Árvore de Decisão). Novo dado recebido é classificado com esse modelo

    -  Se estiver dentro do contexto, a taxa de erro decrescerá
    
    -  Se a distribuição mudar, a taxa de erro crescerá

- Quando a taxa de erro atinge determinado limite, um novo contexto é concebido e novo modelo treinado

---

`DDM.java`

```java
public void input(double prediction) {
    // prediction = 1 ou 0
    m_p = m_p + (prediction - m_p) / (double) m_n;
    m_s = Math.sqrt(m_p * (1 - m_p) / (double) m_n);

    m_n++;

    // respeita um n mínimo de instâncias
    if (m_n < minNumInstances) {
        return;
    }

    // ?
    // atualiza a mínima
    if (m_p + m_s <= m_psmin) {
        m_pmin = m_p;
        m_smin = m_s;
        m_psmin = m_p + m_s;
    }

    if (m_n > minNumInstances && m_p + m_s > m_pmin + outcontrolLevel * m_smin) {
        this.isChangeDetected = true;
    } else if (m_p + m_s > m_pmin + warningLevel * m_smin) {
        this.isWarningZone = true;
    } else {
        this.isWarningZone = false;
    }
}
```

---

`EDDM.java`

- Similar ao `EDM`, mas baseia-se na distribuição estimada das distâncias entre as taxas de erro de classificação

- Pode encapsular qualquer algoritmo de aprendizagem

---

`EDDM.java`

```java
public void input(double prediction) {
    // prediction = 0 ou 1
    
    m_n++;

    if (prediction == 1.0) {
        this.isWarningZone = false;
        this.delay = 0;
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
            if (m_n > FDDM_MINNUMINSTANCES && m_numErrors > m_minNumErrors
                    && p < FDDM_OUTCONTROL) {
                this.isChangeDetected = true;
            } else if (m_n > FDDM_MINNUMINSTANCES
                    && m_numErrors > m_minNumErrors && p < FDDM_WARNING) {
                this.isWarningZone = true;
            } else {
                this.isWarningZone = false;
            }
        }
    }
}
```

---

`EnsembleDriftDetectionMethods.java`

- Utiliza um conjunto de `ChangeDetector`´s

- Detecta mudança quando uma condição é atendida

    - Condição Max: todos detectores apontam mudança

    - Condição Min: pelo menos um detector aponta mudança
    
    - Condição Avg: a maioria dos detectores aponta mudança

---

`EnsembleDriftDetectionMethods.java`

```java
public void input(double prediction) {
    for (int i = 0; i < cds.length; i++) {
        cds[i].input(prediction);
        if (cds[i].getChange()) {
            preds[i] = true;
        }
    }

    int typePrediction = this.predictionOption.getChosenIndex();

    int numberDetections = 0;
    for (int i = 0; i < cds.length; i++) {
        if (preds[i] == true) {
            numberDetections++;
        }
    }

    if (typePrediction == 0) { 
        // Choose Max
        this.isChangeDetected = (numberDetections == cds.length);
    } else if (typePrediction == 1) {
        // Choose Min
        this.isChangeDetected = (numberDetections > 0);
    } else if (typePrediction == 2) {
        // Choose Avg
        this.isChangeDetected = (numberDetections > cds.length/2) ;
    }
    if (this.isChangeDetected == true) {
        this.resetLearning();
    }
}
```

---

`EWMAChartDM.java`

- *EWMA (Exponentially Weighted Moving Average Charts for Detecting
Concept Drift)*

- Similar ao `EDM` e `EDDM` também baseia-se nas taxas de erro de um classificador encapsulado

- O(1)

- Completamente online, não armazena dados em memória

- Detecta um incremento na média das entradas recebidas

---

`EWMAChartDM.java`

```python
public void input(double prediction) {
    // prediction = 0 ou 1

    m_sum += prediction;
    m_p = m_sum/m_n; // m_p + (prediction - m_p) / (double) (m_n+1);
    m_s = Math.sqrt(  m_p * (1.0 - m_p)* lambda * (1.0 - Math.pow(1.0 - lambda, 2.0 * m_n)) / (2.0 - lambda));

    m_n++;

    z_t += lambda * (prediction - z_t);

    
    double L_t = 3.97 - 6.56 * m_p + 48.73 * Math.pow(m_p, 3) - 330.13 * Math.pow(m_p, 5) + 848.18 * Math.pow(m_p, 7); //%1 FP
    
    this.estimation = m_p;
    this.isChangeDetected = false;
    this.isWarningZone = false;
    this.delay = 0;

    if (m_n < this.minNumInstancesOption.getValue()) {
        return;
    }
        
    if (m_n > this.minNumInstancesOption.getValue() && z_t > m_p + L_t * m_s) {
        this.isChangeDetected = true;
    } else if (z_t > m_p + 0.5 *  L_t * m_s) {
        this.isWarningZone = true;
    } else {
        this.isWarningZone = false;
    }
}
```

---

`GeometricMovingAverageDM.java`

- Similar a `EWMAChartDM`, só que usa média geométrica dos erros

- Usa classificador encapsulado

---

`HDDM_A_Test.java`

- Utiliza teoria da probabilidade, limites de Hoeffding

- Define um limite superior para a probabilidade de variação de um conjunto de variáveis limitadas em relação aos seus valores esperados

- Variação `A` usa a média como estimador

- Status possíveis: *STABLE, WARNING e DRIFT*

---

`HDDM_W_Test.java`

# TODO

---

`PageHinkleyDM.java`

# TODO

---

`RDDM.java`

# TODO

---

`SEEDChangeDetector.java`

# TODO

---

`SeqDrift1ChangeDetector.java`

# TODO

---

`SeqDrift2ChangeDetector.java`

# TODO

---

`STEPD.java`

# TODO