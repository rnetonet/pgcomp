# Análise e Propostas de Evolução - MATE84

### Situação

Durante a coleta dos dados e códigos-fonte realizados pela turma anterior, contataram-se as seguintes situações:

* Dispositivos e sensores ainda não foram disponibilizados. 

    * *Sendo verificado se estão "prontos" para uso, para 
evitarmos a necessidade de refazê-los*;

* **Base de dados** não está devidamente estruturada, requerendo nova modelagem;

* **Aprendizagem de Máquina**, possíveis aprimoramentos:
     
    * Tratamento dos dados;
    
    * Modelo estático. Modelo deve ser adaptar conforme novos dados são obtidos;
    
    * Utilização de outros algoritmos de classificação;
    
    * Utilização de algoritmos não-supervisionados;

* **Integração dos sistemas**:

    * Ciclo `coleta -> bd -> tratamento de dados -> módulo aprendizagem` está manual;

### Propostas

1. Remodelagem do BD; 
1. Tentar coletar dados em novos ambientes, adequando código de coleta à nova base;
1. Automatizar integração com o módulo de aprendizagem;
1. Aprimoramentos de integração (`coleta -> bd -> tratamento -> ML`);
1. Adequar o módulo de visualização à nova estrutura de base de dados;
1. Aprimoramento nos algoritmos de ML: novos algoritmos supervisionados, atualização do modelo de forma adaptativa e explorar algoritmos não-supervisionados.