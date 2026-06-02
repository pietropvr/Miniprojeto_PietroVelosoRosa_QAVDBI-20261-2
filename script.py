import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as datetime
import os

# 1. DEFINIÇÃO DO CAMINHO (Cross-Platform Windows/Android)
caminho_arquivo = os.path.join('dados', 'nao_processados', 'base_varejo.csv')

# 2. CARREGAMENTO DOS DADOS
df = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8')

# 3. CORREÇÃO IMEDIATA DE SUJEIRA DO ARQUIVO
df = df.iloc[:, :10]

# 4. INSPEÇÃO INICIAL
print("=== CABEÇALHO DA BASE DE DADOS ===")
print(df.head())

print("\n=== INFORMAÇÕES GERAIS ===")
print(f"Total de linhas e colunas: {df.shape}")
print(df.info())

# ==============================================================
# PASSO 2: LIMPEZA E TRANSFORMAÇÃO DE DADOS
# ==============================================================

# 5. REMOÇÃO DE DUPLICADOS
print("\n=== VERIFICAÇÃO DE DUPLICADOS ===")
print(f"Linhas duplicadas encontradas: {df.duplicated().sum()}")

df = df.drop_duplicates()

# 6. CONVERSÃO DE DATAS
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')

# 7. MAPEAMENTO DO ESTADO CIVIL (CL_EC)

mapa_estado_civil = {
    1: 'Casado',
    2: 'Divorciado',
    3: 'Separado',
    4: 'Solteiro',
    5: 'Viúvo'
}

df['CL_EC'] = df['CL_EC'].map(mapa_estado_civil)

# ==============================================================
# PASSO 3: TRATAMENTO DE VALORES NULOS (ANTES E DEPOIS)
# ==============================================================

# 1. CONTAGEM DE NULOS ANTES DA LIMPEZA 
print("\n=== VALORES NULOS (ANTES DA LIMPEZA) ===")
nulos_antes = df.isnull().sum()
print(nulos_antes)

# Preenchendo categorias vazias conforme regra de negócio
df['PR_CAT'] = df['PR_CAT'].fillna('Sem Categoria')

# 2. A LIMPEZA
df = df.dropna()
print("Justificação: Optou-se por usar o dropna() para remover as linhas nulas, garantindo que clientes incompletos não distorcem a análise estatística de perfil do consumidor.")

# 3. CONTAGEM DE NULOS DEPOIS DA LIMPEZA
print("\n=== VALORES NULOS (DEPOIS DA LIMPEZA) ===")
nulos_depois = df.isnull().sum()
print(nulos_depois)

# Mostrar quantas linhas perdemos no total
linhas_restantes = len(df)
print(f"\nLinhas limpas e prontas para análise: {linhas_restantes}")

# ==============================================================
# PASSO 4: ANÁLISE EXPLORATÓRIA BÁSICA (EDA)
# ==============================================================

print("\n=== TOP 5 CATEGORIAS DE PRODUTOS MAIS VENDIDAS ===")

top_categorias = df['PR_CAT'].value_counts().head(5)
print(top_categorias)

print("\n=== PERFIL DE CLIENTES: COMPRAS POR GÉNERO ===")

compras_por_genero = df['CL_GENERO'].value_counts(normalize=True) * 100
print(compras_por_genero.round(2).astype(str) + ' %')

print("\n=== PERFIL DE CLIENTES: CLASSE SOCIAL (SEGMENTAÇÃO) ===")
segmentacao = df['CL_SEG'].value_counts()
print(segmentacao)

# ==============================================================
# PASSO 5: ESTATÍSTICAS DESCRITIVAS E AGRUPAMENTOS (ETAPAS 4 E 5)
# ==============================================================

print("\n=== ESTATÍSTICAS DESCRITIVAS: NÚMERO DE FILHOS (CL_FHL) ===")
# Calculando cada métrica exigida individualmente
media = df['CL_FHL'].mean()
mediana = df['CL_FHL'].median()
desvio_padrao = df['CL_FHL'].std()
moda = df['CL_FHL'].mode()[0] # [0] pega o primeiro resultado caso haja empate
maximo = df['CL_FHL'].max()
minimo = df['CL_FHL'].min()
contagem = df['CL_FHL'].count()

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Moda: {moda}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Contagem total válida: {contagem}")

print("\n=== AGRUPAMENTO 1: VOLUME DE COMPRAS POR GÊNERO ===")
# groupby: Agrupa pelo gênero e conta quantos IDs de compra (CO_ID) existem para cada um
compras_por_genero = df.groupby('CL_GENERO')['CO_ID'].count()
print(compras_por_genero)

print("\n=== AGRUPAMENTO 2: MÉDIA DE FILHOS POR CLASSE SOCIAL ===")
# groupby: Agrupa pela segmentação (A, B, C) e tira a média de filhos
filhos_por_classe = df.groupby('CL_SEG')['CL_FHL'].mean()
print(filhos_por_classe.round(2))

print("\n=== AGRUPAMENTO 3: TOP 10 PRODUTOS MAIS VENDIDOS ===")
# groupby: Agrupa pelo nome do produto e conta as ocorrências
# sort_values(ascending=False): Organiza os números do maior para o menor
# head(10): Mostra apenas os 10 primeiros da lista para não poluir o ecrã
produtos_mais_vendidos = df.groupby('PR_NOME')['CO_ID'].count().sort_values(ascending=False).head(10)
print(produtos_mais_vendidos)


# ==============================================================
# PASSO 7: VISUALIZAÇÃO DE DADOS E EXPORTAÇÃO INTELIGENTE
# ==============================================================

# 1. Configurando o gráfico
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))

compras_por_genero = df['CL_GENERO'].value_counts()
sns.barplot(x=compras_por_genero.index, y=compras_por_genero.values, palette="Blues_d")

plt.title('Volume Total de Compras por Gênero do Cliente', fontsize=14, fontweight='bold')
plt.xlabel('Gênero Biológico', fontsize=12)
plt.ylabel('Quantidade de Compras Registradas', fontsize=12)

# 2. Salvando a imagem (Funciona em todos os sistemas)
caminho_grafico = os.path.join('dados', 'graficos', 'grafico_vendas_genero.png')
plt.savefig(caminho_grafico, bbox_inches='tight', dpi=300)
print(f"Gráfico salvo com sucesso em: {caminho_grafico}")

# 3. AUTOMAÇÃO DE TELA (CROSS-PLATFORM)
if os.name == 'nt':
    # 'nt' é a sigla interna do Python para Windows
    print(" Windows detectado: Abrindo o gráfico na tela...")
    plt.show()
else:
    # Se não for Windows, é Linux/Android 
    print("Ambiente mobile detectado: Gráfico salvo. Abra o arquivo .png na sua pasta 'dados' para visualizar.")

# 4. EXPORTAÇÃO DA BASE LIMPA
caminho_csv = os.path.join('dados', 'processados', 'df_limpo.csv')
df.to_csv(caminho_csv, index=False, sep=';', encoding='utf-8')
print(f"Base limpa salva em CSV: {caminho_csv}")

print("\n=== CONCLUSÕES DO PROJETO (INSIGHTS) ===")
conclusoes = """
1. A base possuía colunas fantasmas geradas por delimitadores vazios, que foram removidos para estabilizar os dados.
2. A conversão dos códigos numéricos de Estado Civil para texto permitiu uma leitura clara para as análises agrupadas.
3. Analisando as estatísticas descritivas, notamos o perfil familiar médio dos clientes (com a moda a indicar o número mais comum de filhos).
4. O agrupamento por género ajudou a identificar qual fatia do público é responsável pelo maior volume de compras no supermercado.
5. PROBLEMA REMANESCENTE: A base foca no volume de produtos, mas a ausência de uma coluna com o "Valor Unitário" impossibilita a análise de faturação real da empresa.
6. O agrupamento de produtos revelou quais são os itens 'campeões de vendas', uma informação estratégica para o posicionamento de produtos nas prateleiras ou para campanhas de marketing."
"""
print(conclusoes)

