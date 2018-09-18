---
theme: "white"
transition: "fadeIn"
highlightTheme: "tomorrow"
center: false
controls: false
---

### Stream Mining & MOA
---

---

### Stream Mining


* Olhe ao redor: quase tudo produz dados
* Em alta frequência
* Continuamente
* E que pode mudar com o tempo

---

### Exemplos

* LHC (Large Hadron Collider)
* Compras online
* UTI´s

---

### Identificações necessárias

* Mudanças
* Padrões, regularidades...

---

### Ferramentas

* MOA
* SAMOA (Versão distribuída do MOA)
* streamDM (MOA em C++)
* spark.apache.org/streaming
* R `stream` (apenas *clustering*)
* R `streaMOA` (conector com o MOA)

---

### O que é Stream Mining

Intersecção entre: 

* Aprendizagem de Máquina
* *Online Learning*
* Séries Temporais
* Bases de Dados

---

### Desafios Stream Mining

* Análise Incremental
* Limitação de memória e tempo
* Sempre pronto para `predict(data)`
* Ser adaptável a mudanças, entrada é não-estacionária
* Lidar com *feedback* limitado/atrasado

---

### Diferença *Machine Learning* clássico ?

* Entrada e saída **não** são independentes e identicamente distribuídos

---

### Como lidar com mudança ?

* Retreinos
    * Periódicos ?
    * Provocados por uma queda na precisão ?
    * **Ineficiente!**

---

### Alternativas - Stream Mining

---

### Utilização de *batch-incremental*

* Permite a utilização de qualquer algoritmo clássico de *Machine Learning*

* *Batchs* de dados são utilizados

* Novo modelo a cada *batch*

---

### Dois níveis

* Sumarização no nível 1 (online)
* Análise mais aprofundade no nível 2 (offline)
* *Pode usar janelas, etc*

---

### Realmente incremental
* Adaptação de algoritmo clássico
* Novo algoritmo

---

### Lembre-se

Com *streams*, sempre é uma aproximação

**Não há resultado 100%**

---


 