# Análise Socioeconômica do ENEM

Este projeto investiga o impacto de fatores socioeconômicos (Renda Familiar e Tipo de Escola) no desempenho dos candidatos do ENEM 2021. Utilizando Python e Estatística, quantificamos a desigualdade educacional no Brasil.

## Objetivo
Responder à pergunta: **"Quanto a condição financeira e a escolha da escola influenciam a nota final do aluno?"**

## Tecnologias Utilizadas
* **Python 3.9**
* **Pandas:** Manipulação de grandes volumes de dados (ETL).
* **Matplotlib & Seaborn:** Visualização de dados.
* **Scikit-Learn:** Criação de modelos de Machine Learning (Regressão Linear Múltipla).
* **Estatística:** Correlação, Regressão Linear e Teste de Hipóteses.

## Estrutura do Projeto
O projeto foi dividido em etapas de pipeline de dados:
1.  **Ingestão:** Leitura otimizada dos microdados (arquivo original > 2GB).
2.  **Limpeza:** Tratamento de valores nulos (NaN) e filtragem de colunas irrelevantes.
3.  **Feature Engineering:** Conversão da renda (Letras) em valores numéricos e criação de variáveis binárias (Dummy) para escolas privadas.
4.  **Modelagem:** Treinamento de algoritmo de Regressão Linear.

## Principais Resultados

### 1. A Desigualdade Visualizada
A análise exploratória revelou uma correlação clara: conforme a renda sobe, a mediana das notas aumenta consistentemente.

![Regressão Escolas](resultados\grafico_regressao_escolas.png)
*O gráfico acima mostra duas tendências paralelas: alunos de escola privada (vermelho) partem de uma nota base superior aos da pública (azul), mesmo com a mesma renda.*

### 2. O Modelo Matemático (Machine Learning)
Treinamos um modelo de Regressão Linear Múltipla que atingiu um **R² de 24%** (0.2402). Os coeficientes descobertos foram:

| Fator | Impacto na Nota (Estimado) |
| :--- | :--- |
| **Nota Base (Intercepto)** | 496.46 pontos |
| **Renda Familiar** | +5.7 pontos a cada R$ 1.000,00 extras |
| **Bônus Escola Privada** | **+55.47 pontos** (apenas por estudar em particular) |

### Conclusão
O estudo estatístico aponta que a desigualdade no ENEM é estrutural.
* Um aluno de escola **Pública** com renda de R$ 3.000 tem nota estimada de **513.7**.
* Um aluno de escola **Privada** com a mesma renda (R$ 3.000) tem nota estimada de **569.1**.

Essa diferença de **~55 pontos** muitas vezes define a aprovação em cursos concorridos no Sisu.

---
**João Otávio Gurgel de Oliveira**
*Projeto desenvolvido para fins de estudo em Ciência de Dados.*