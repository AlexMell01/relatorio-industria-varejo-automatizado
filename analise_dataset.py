import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# 🚀 Projeto: relatorio-industria-varejo-automatizado
# Este script realiza análise comercial completa e gera relatório PDF automatizado.

# Caminho do dataset
caminho_dataset = 'industria_varejo_dataset.csv'  # ← (renomeie o CSV para manter coerência)
df = pd.read_csv(caminho_dataset)

# Visualização inicial
print("PRIMEIRAS LINHAS DO DATASET:")
print(df.head())

print("\nINFO DO DATASET:")
print(df.info())

print("\nESTATÍSTICAS DESCRITIVAS:")
print(df.describe(include='all'))

print("\nVALORES NULOS POR COLUNA:")
print(df.isnull().sum())

print("\nTIPOS DE DADOS:")
print(df.dtypes)

print("\nVALORES ÚNICOS POR COLUNA CATEGÓRICA:")
for coluna in df.select_dtypes(include='object').columns:
    print(f"{coluna}: {df[coluna].nunique()} únicos")

# Receita e lucro
print(f"\nRECEITA TOTAL: R$ {df['Receita_Total'].sum():,.2f}")
print(f"LUCRO TOTAL: R$ {df['Lucro'].sum():,.2f}")

# Top produtos
print("\nTOP 10 PRODUTOS MAIS VENDIDOS:")
print(df['Produto'].value_counts().head(10))

# Lucro por categoria
lucro_por_categoria = df.groupby('Categoria')['Lucro'].sum().sort_values(ascending=False)
print("\nLUCRO POR CATEGORIA:")
print(lucro_por_categoria)

# Desempenho das equipes
desempenho_equipes = df.groupby('Equipe_Vendas')['Desempenho_Equipe'].mean().sort_values(ascending=False)
print("\nTOP 5 EQUIPES COM MELHOR DESEMPENHO MÉDIO:")
print(desempenho_equipes.head(5))

# Vendas por região
vendas_por_regiao = df['Regiao_Metropolitana'].value_counts()
print("\nVOLUME DE VENDAS POR REGIÃO METROPOLITANA:")
print(vendas_por_regiao)

# Gráfico: Lucro por categoria
plt.figure(figsize=(8, 6))
ax = lucro_por_categoria.plot(kind='bar')
plt.title('Lucro Total por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Lucro (R$)')
plt.xticks(rotation=45)
for i in ax.containers:
    labels = [f"R$ {v:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') for v in i.datavalues]
    ax.bar_label(i, labels=labels, padding=3)
plt.tight_layout()
plt.savefig('lucro_por_categoria.png', dpi=300)
plt.show()

# Gráfico: Vendas por canal
vendas_por_canal = df['Canal_Venda'].value_counts()
plt.figure(figsize=(6, 6))
vendas_por_canal.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Participação de Vendas por Canal')
plt.ylabel('')
plt.tight_layout()
plt.savefig('vendas_por_canal.png', dpi=300)
plt.show()

# Gráfico: Evolução de vendas
df['Data'] = pd.to_datetime(df['Data'])
vendas_por_mes = df.groupby(df['Data'].dt.to_period('M')).size()
plt.figure(figsize=(10, 5))
ax = vendas_por_mes.plot(kind='line', marker='o')
plt.title('Evolução de Vendas ao Longo do Tempo')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Vendas')
plt.grid(True)
plt.xticks(rotation=45)
for x, y in zip(vendas_por_mes.index.astype(str), vendas_por_mes.values):
    plt.text(x, y, str(y), ha='center', va='bottom')
plt.tight_layout()
plt.savefig('evolucao_vendas.png', dpi=300)
plt.show()

# Gráfico: Vendas por equipe
vendas_por_equipe = df['Equipe_Vendas'].value_counts().sort_index()
plt.figure(figsize=(8, 6))
ax = vendas_por_equipe.plot(kind='bar')
plt.title('Volume de Vendas por Equipe')
plt.xlabel('Equipe')
plt.ylabel('Volume de Vendas')
plt.xticks(rotation=45)
for i in ax.containers:
    ax.bar_label(i, fmt='%d', padding=3)
plt.tight_layout()
plt.savefig('vendas_por_equipe.png', dpi=300)
plt.show()

# Gráfico: Desempenho médio por equipe
desempenho_por_equipe = df.groupby('Equipe_Vendas')['Desempenho_Equipe'].mean().sort_index()
plt.figure(figsize=(8, 6))
ax = desempenho_por_equipe.plot(kind='bar')
plt.title('Desempenho Médio por Equipe')
plt.xlabel('Equipe')
plt.ylabel('Desempenho Médio')
plt.xticks(rotation=45)
for i in ax.containers:
    labels = [f"{v:.2f}" for v in i.datavalues]
    ax.bar_label(i, labels=labels, padding=3)
plt.tight_layout()
plt.savefig('desempenho_por_equipe.png', dpi=300)
plt.show()

# Correlação
vendas_por_equipe = df['Equipe_Vendas'].value_counts()
desempenho_por_equipe = df.groupby('Equipe_Vendas')['Desempenho_Equipe'].mean()
correlacao_df = pd.DataFrame({'Volume_Vendas': vendas_por_equipe, 'Desempenho_Medio': desempenho_por_equipe})
correlacao = correlacao_df['Volume_Vendas'].corr(correlacao_df['Desempenho_Medio'])

print(f"\nCORRELAÇÃO ENTRE VOLUME DE VENDAS E DESEMPENHO MÉDIO DAS EQUIPES:\n{correlacao:.4f}")
print("\nTABELA DE VENDAS E DESEMPENHO POR EQUIPE:")
print(correlacao_df)

# Gráfico: Dispersão
plt.figure(figsize=(8, 6))
plt.scatter(correlacao_df['Volume_Vendas'], correlacao_df['Desempenho_Medio'])
for i, txt in enumerate(correlacao_df.index):
    plt.annotate(txt, (correlacao_df['Volume_Vendas'].iloc[i], correlacao_df['Desempenho_Medio'].iloc[i]),
                 textcoords="offset points", xytext=(5,5), ha='left')
plt.title('Dispersão: Volume de Vendas x Desempenho Médio')
plt.xlabel('Volume de Vendas')
plt.ylabel('Desempenho Médio')
plt.grid(True)
plt.tight_layout()
plt.savefig('dispersao_vendas_desempenho.png', dpi=300)
plt.show()

# Margem de lucro
df['Margem_Lucro_%'] = ((df['Lucro'] / (df['Quantidade'] * df['Custo'])) * 100).round(2)
margem_media_produto = df.groupby('Produto')['Margem_Lucro_%'].mean().sort_values(ascending=False).head(10)
print("\nTOP 10 PRODUTOS COM MAIOR MARGEM DE LUCRO MÉDIA (%):")
print(margem_media_produto)

# Problemas recorrentes
problemas_recorrentes = df['Problema'].value_counts()
print("\nPROBLEMAS MAIS RECORRENTES NAS OPERAÇÕES:")
print(problemas_recorrentes)

# Feedbacks negativos
feedback_negativo = df[df['Feedback_Nota'] <= 2]
feedback_negativo_categoria = feedback_negativo['Categoria'].value_counts()
print("\nFEEDBACKS NEGATIVOS POR CATEGORIA:")
print(feedback_negativo_categoria)

# Gerar PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Relatório Automatizado: Indústria -> Varejo", ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, "Resumo das principais análises realizadas com base no dataset de vendas, equipes e feedbacks de clientes.\n")

graficos = [
    'lucro_por_categoria.png',
    'vendas_por_canal.png',
    'evolucao_vendas.png',
    'vendas_por_equipe.png',
    'desempenho_por_equipe.png',
    'dispersao_vendas_desempenho.png'
]

for grafico in graficos:
    pdf.add_page()
    pdf.image(grafico, x=10, y=30, w=180)
    pdf.ln(85)

pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.multi_cell(0, 10, "Interpretações e Insights")

texto = f"""
- Receita Total: R$ {df['Receita_Total'].sum():,.2f}
- Lucro Total: R$ {df['Lucro'].sum():,.2f}
- Maior volume de vendas: Região {df['Regiao_Metropolitana'].mode()[0]}
- Problema mais recorrente: {df['Problema'].value_counts().idxmax()}
- Correlação entre volume e desempenho: {correlacao:.4f}
- Equipe com maior desempenho: {desempenho_equipes.idxmax()} ({desempenho_equipes.max():.4f})
- Categoria com mais feedbacks negativos: {feedback_negativo_categoria.idxmax()} ({feedback_negativo_categoria.max()} ocorrências)
"""

texto = texto.replace("→", "->")  # Substitui qualquer seta por um caractere ASCII
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, texto.encode('latin-1', 'ignore').decode('latin-1'))


pdf.output("relatorio_industria_varejo.pdf")
print("✅ Relatório PDF gerado com sucesso: relatorio_industria_varejo.pdf")


  