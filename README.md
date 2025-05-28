# Relatório Automatizado: Indústria → Varejo

Este projeto realiza uma análise comercial detalhada de um cenário fictício de uma indústria que distribui produtos para supermercados, varejos e redes com apoio de distribuidores. Ele gera visualizações e um relatório PDF automatizado com gráficos, métricas e insights.

## 🔍 Visão Geral

- Dataset com 50.000 registros simulados de vendas, equipes e feedbacks.
- Análises estatísticas, operacionais e comerciais.
- Geração automática de gráficos e relatório PDF final.

## 📊 Análises Realizadas

- Receita e lucro totais
- Top produtos mais vendidos
- Lucro por categoria
- Desempenho médio das equipes de vendas
- Vendas por canal e região metropolitana
- Evolução das vendas no tempo
- Correlação entre volume de vendas e desempenho
- Margem de lucro média por produto
- Problemas operacionais recorrentes
- Feedbacks negativos por categoria

## 📁 Estrutura do Projeto

```
projeto_python/
├── analise_dataset.py
├── envio_email.py
├── gerar_token.py
├── industria_varejo_dataset.csv
├── relatorio_industria_varejo.pdf
├── vendas_por_equipe.png
├── lucro_por_categoria.png
├── vendas_por_canal.png
├── evolucao_vendas.png
├── desempenho_por_equipe.png
├── dispersao_vendas_desempenho.png
├── .gitignore
└── README.md
```

## ▶️ Como Executar

1. Instale as bibliotecas necessárias:

```bash
pip install pandas matplotlib fpdf
```

2. Execute o script principal:

```bash
python analise_dataset.py
```

3. Será gerado o relatório: `relatorio_industria_varejo.pdf`.

## 🚀 Autor

Alex Sandro ([@AlexMell01](https://github.com/AlexMell01))

---

> Projeto desenvolvido como parte do plano intensivo de aprendizado em Análise de Dados e publicação de portfólio no GitHub.
