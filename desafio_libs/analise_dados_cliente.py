import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração para gráficos em português
plt.style.use("default")
sns.set_palette("husl")

print("=" * 60)
print("ANÁLISE DE DADOS DE CLIENTES")
print("=" * 60)

# 1. COLETA/GERAÇÃO DE DADOS SIMULADOS
print("\n1. GERANDO DADOS SIMULADOS DE CLIENTES...")

# Definindo parâmetros para dados realistas
np.random.seed(42)  # Para reproduzibilidade
n_clientes = 500

# Gerando dados demográficos
nomes = [f"Cliente_{i+1}" for i in range(n_clientes)]
idades = np.random.normal(35, 12, n_clientes).astype(int)
idades = np.clip(idades, 18, 80)  # Limitando entre 18 e 80 anos

generos = np.random.choice(["M", "F"], n_clientes, p=[0.45, 0.55])
cidades = np.random.choice(
    [
        "São Paulo",
        "Rio de Janeiro",
        "Belo Horizonte",
        "Porto Alegre",
        "Curitiba",
        "Salvador",
    ],
    n_clientes,
)

# Gerando dados de compras
num_compras = np.random.poisson(8, n_clientes)  # Média de 8 compras por cliente
num_compras = np.clip(num_compras, 1, 50)  # Mínimo 1, máximo 50

# Valor médio por compra (varia por cliente)
valor_medio_compra = np.random.gamma(2, 50, n_clientes)
valor_medio_compra = np.clip(valor_medio_compra, 20, 500)

# Calculando valor total gasto
valor_total_gasto = num_compras * valor_medio_compra

# Criando DataFrame principal
df_clientes = pd.DataFrame(
    {
        "nome": nomes,
        "idade": idades,
        "genero": generos,
        "cidade": cidades,
        "num_compras": num_compras,
        "valor_medio_compra": valor_medio_compra.round(2),
        "valor_total_gasto": valor_total_gasto.round(2),
    }
)

print(f"✓ Dados gerados para {n_clientes} clientes")
print("✓ Primeiras 5 linhas dos dados:")
print(df_clientes.head())

# 2. ANÁLISE DE DADOS
print("\n" + "=" * 60)
print("2. ANÁLISE DOS DADOS")
print("=" * 60)

# 2.1 Identificação dos clientes mais valiosos
print("\n2.1 CLIENTES MAIS VALIOSOS (Top 10)")
print("-" * 40)
top_clientes = df_clientes.nlargest(10, "valor_total_gasto")
print(top_clientes[["nome", "valor_total_gasto", "num_compras", "valor_medio_compra"]])

# 2.2 Análise da frequência de compra e valor médio
print("\n2.2 ANÁLISE DE FREQUÊNCIA E VALORES")
print("-" * 40)
estatisticas = {
    "Frequência de Compra": {
        "Média": df_clientes["num_compras"].mean(),
        "Mediana": df_clientes["num_compras"].median(),
        "Desvio Padrão": df_clientes["num_compras"].std(),
        "Mínimo": df_clientes["num_compras"].min(),
        "Máximo": df_clientes["num_compras"].max(),
    },
    "Valor Médio por Compra": {
        "Média": df_clientes["valor_medio_compra"].mean(),
        "Mediana": df_clientes["valor_medio_compra"].median(),
        "Desvio Padrão": df_clientes["valor_medio_compra"].std(),
        "Mínimo": df_clientes["valor_medio_compra"].min(),
        "Máximo": df_clientes["valor_medio_compra"].max(),
    },
    "Valor Total Gasto": {
        "Média": df_clientes["valor_total_gasto"].mean(),
        "Mediana": df_clientes["valor_total_gasto"].median(),
        "Desvio Padrão": df_clientes["valor_total_gasto"].std(),
        "Mínimo": df_clientes["valor_total_gasto"].min(),
        "Máximo": df_clientes["valor_total_gasto"].max(),
    },
}

for categoria, stats in estatisticas.items():
    print(f"\n{categoria}:")
    for stat, valor in stats.items():
        print(
            f"  {stat}: R$ {valor:.2f}"
            if "Valor" in categoria
            else f"  {stat}: {valor:.2f}"
        )

# 2.3 Segmentação de clientes por valor
print("\n2.3 SEGMENTAÇÃO DE CLIENTES")
print("-" * 40)

# Criando segmentos baseados no valor total gasto
df_clientes["segmento"] = pd.cut(
    df_clientes["valor_total_gasto"],
    bins=[0, 200, 500, 1000, float("inf")],
    labels=["Bronze", "Prata", "Ouro", "Platina"],
)

segmentos = df_clientes["segmento"].value_counts()
print("Distribuição por segmento:")
for seg, count in segmentos.items():
    percentual = (count / len(df_clientes)) * 100
    print(f"  {seg}: {count} clientes ({percentual:.1f}%)")

# 2.4 Análise por demografia
print("\n2.4 ANÁLISE DEMOGRÁFICA")
print("-" * 40)

# Por gênero
print("Gastos por Gênero:")
genero_stats = df_clientes.groupby("genero")["valor_total_gasto"].agg(
    ["mean", "median", "count"]
)
print(genero_stats)

# Por cidade
print("\nTop 3 Cidades por Valor Médio Gasto:")
cidade_stats = (
    df_clientes.groupby("cidade")["valor_total_gasto"]
    .agg(["mean", "count"])
    .sort_values("mean", ascending=False)
)
print(cidade_stats.head(3))

# 2.5 Identificação de padrões de comportamento
print("\n2.5 PADRÕES DE COMPORTAMENTO")
print("-" * 40)

# Correlação entre variáveis
print("Correlações importantes:")
correlacoes = df_clientes[
    ["idade", "num_compras", "valor_medio_compra", "valor_total_gasto"]
].corr()
print(f"Idade vs Valor Total: {correlacoes.loc['idade', 'valor_total_gasto']:.3f}")
print(
    f"Num Compras vs Valor Total: {correlacoes.loc['num_compras', 'valor_total_gasto']:.3f}"
)
print(
    f"Valor Médio vs Valor Total: {correlacoes.loc['valor_medio_compra', 'valor_total_gasto']:.3f}"
)

# Clientes de alto valor mas baixa frequência (oportunidade de retenção)
alto_valor_baixa_freq = df_clientes[
    (df_clientes["valor_total_gasto"] > df_clientes["valor_total_gasto"].quantile(0.75))
    & (df_clientes["num_compras"] < df_clientes["num_compras"].quantile(0.25))
]

print(f"\nClientes de alto valor mas baixa frequência: {len(alto_valor_baixa_freq)}")
print("(Oportunidade para programas de fidelidade)")

# 3. VISUALIZAÇÕES
print("\n" + "=" * 60)
print("3. GERANDO VISUALIZAÇÕES")
print("=" * 60)

# Configurando o layout dos gráficos
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle("Análise de Dados de Clientes", fontsize=16, fontweight="bold")

# Gráfico 1: Distribuição do valor total gasto
axes[0, 0].hist(
    df_clientes["valor_total_gasto"],
    bins=30,
    alpha=0.7,
    color="skyblue",
    edgecolor="black",
)
axes[0, 0].set_title("Distribuição do Valor Total Gasto")
axes[0, 0].set_xlabel("Valor Total Gasto (R$)")
axes[0, 0].set_ylabel("Frequência")
axes[0, 0].grid(True, alpha=0.3)

# Gráfico 2: Segmentação de clientes
segmentos.plot(
    kind="bar", ax=axes[0, 1], color=["#FFD700", "#C0C0C0", "#CD7F32", "#E5E4E2"]
)
axes[0, 1].set_title("Distribuição por Segmento")
axes[0, 1].set_xlabel("Segmento")
axes[0, 1].set_ylabel("Número de Clientes")
axes[0, 1].tick_params(axis="x", rotation=45)

# Gráfico 3: Relação entre número de compras e valor total
axes[1, 0].scatter(
    df_clientes["num_compras"],
    df_clientes["valor_total_gasto"],
    alpha=0.6,
    color="coral",
)
axes[1, 0].set_title("Relação: Número de Compras vs Valor Total")
axes[1, 0].set_xlabel("Número de Compras")
axes[1, 0].set_ylabel("Valor Total Gasto (R$)")
axes[1, 0].grid(True, alpha=0.3)

# Gráfico 4: Gastos por gênero
genero_gastos = df_clientes.groupby("genero")["valor_total_gasto"].mean()
axes[1, 1].bar(
    genero_gastos.index, genero_gastos.values, color=["lightblue", "lightpink"]
)
axes[1, 1].set_title("Valor Médio Gasto por Gênero")
axes[1, 1].set_xlabel("Gênero")
axes[1, 1].set_ylabel("Valor Médio Gasto (R$)")

plt.tight_layout()
plt.show()

# 4. RESUMO EXECUTIVO E RECOMENDAÇÕES
print("\n" + "=" * 60)
print("4. RESUMO EXECUTIVO E RECOMENDAÇÕES")
print("=" * 60)

print("\n📊 PRINCIPAIS INSIGHTS:")
print(
    f"• Valor médio gasto por cliente: R$ {df_clientes['valor_total_gasto'].mean():.2f}"
)
print(f"• Número médio de compras por cliente: {df_clientes['num_compras'].mean():.1f}")
print(f"• Ticket médio: R$ {df_clientes['valor_medio_compra'].mean():.2f}")
print(
    f"• {len(df_clientes[df_clientes['segmento'] == 'Platina'])} clientes no segmento Platina (mais valiosos)"
)

print("\n🎯 OPORTUNIDADES IDENTIFICADAS:")
print(f"• {len(alto_valor_baixa_freq)} clientes de alto valor com baixa frequência")
print("• Potencial para programas de fidelidade e retenção")
print("• Segmentação clara permite estratégias personalizadas")

print("\n💡 RECOMENDAÇÕES:")
print("1. Implementar programa VIP para clientes Platina")
print("2. Campanhas de reativação para clientes de baixa frequência")
print("3. Análise mais detalhada dos padrões sazonais")
print("4. Personalização de ofertas por segmento")

print("\n" + "=" * 60)
print("ANÁLISE CONCLUÍDA COM SUCESSO!")
print("=" * 60)
