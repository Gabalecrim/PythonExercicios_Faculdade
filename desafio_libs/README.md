# 📊 Projeto de Análise de Dados de Clientes

Este projeto realiza uma análise exploratória sobre dados simulados de clientes, utilizando as bibliotecas **Pandas**, **NumPy**, **Matplotlib** e **Seaborn**. O objetivo é identificar padrões de comportamento, segmentar clientes por valor e propor ações estratégicas com base nos insights extraídos.

---

## 🧠 Objetivo

Simular um conjunto de dados de clientes e realizar uma **análise exploratória completa**, desde a geração dos dados até a visualização e recomendações práticas.

---

## 📁 Estrutura do Código

O script está dividido nas seguintes etapas:

### 1. Geração de Dados

- Criação de 500 clientes fictícios com:
  - Nome, idade, gênero, cidade
  - Número de compras, valor médio por compra, valor total gasto

### 2. Análise Exploratória

- Identificação dos **clientes mais valiosos**
- Estatísticas de frequência de compra, valores médios e totais
- Segmentação em 4 categorias: **Bronze**, **Prata**, **Ouro** e **Platina**
- Análises por **gênero** e **cidade**
- Verificação de **correlações** entre variáveis
- Identificação de **clientes de alto valor com baixa frequência**

### 3. Visualizações

Gráficos gerados com `Matplotlib` e `Seaborn`:

- Histograma do valor total gasto
- Gráfico de barras com a distribuição por segmento
- Dispersão entre número de compras e valor gasto
- Comparação de gasto médio por gênero

### 4. Resumo Executivo

Apresentação de:

- Insights numéricos
- Oportunidades encontradas
- Recomendações estratégicas

---

## ▶️ Como Executar

### Pré-requisitos

Certifique-se de ter o Python 3.7+ instalado e as bibliotecas abaixo:

```bash
pip install pandas numpy matplotlib seaborn
```

### Execução

1. Salve o código em um arquivo chamado `analise_clientes.py`.
2. No terminal, execute:

```bash
python analise_clientes.py
```

3. Os resultados serão exibidos no console e as visualizações abrirão automaticamente em uma janela separada.

---
