# Análise Exploratória de Dados (EDA) - Base Varejo

Este projeto realiza um processo completo de Extração, Transformação e Análise de Dados (ETL/EDA) sobre uma base de registros de compras de um supermercado. O objetivo é demonstrar a preparação e limpeza de dados brutos para extração de métricas de Business Intelligence.

## Tecnologias Utilizadas
- **Python 3.x**
- **Pandas e NumPy:** Manipulação e limpeza de dados.
- **Matplotlib e Seaborn:** Visualização gráfica.
- **OS:** Gerenciamento multiplataforma de caminhos de arquivos.

## Como Executar o Projeto
O script foi construído com caminhos relativos multiplataforma, rodando perfeitamente tanto no Windows (VsCode) quanto no Android/Linux (Termux).

1. Clone o repositório ou baixe a pasta.
2. Certifique-se de ter as bibliotecas instaladas (`pip install pandas numpy matplotlib seaborn`).
3. Execute o comando no terminal do seu ambiente:
   python script.py
4. O relatório será impresso no terminal, o gráfico (grafico_vendas_genero), será salvo na pasta dados/graficos/ e a base limpa (df_limpo.csv), será salva na pasta dados/processados/.

## Reflexão Teórica: Importância do ETL e Qualidade de Dados

​A etapa de ETL (Extract, Transform, Load) é a espinha dorsal de qualquer projeto de Business Intelligence. Dados do mundo real chegam sujos, com registros faltantes, formatos incorretos (como datas lidas como texto) e categorias inconsistentes.

​Neste projeto, a garantia da qualidade dos dados ocorreu ao removermos colunas fantasmas geradas por delimitadores vazios, convertermos a tipagem das datas para datetime e tratarmos os valores nulos e duplicados. Garantir a integridade dessa base é o que impede que um modelo de Machine Learning falhe ou que um painel de Power BI apresente faturamentos incorretos aos tomadores de decisão.

## Principais Conclusões e Insights

​A partir da base saneada, os seguintes agrupamentos e estatísticas nos trouxeram visão de negócio:

**​Estabilização da Base**: A remoção de delimitadores vazios e o preenchimento/remoção de nulos salvaram a análise de distorções no perfil de clientes.

**​Leitura Categórica**: A tradução dos códigos numéricos (1, 2, 3) para o Estado Civil real das pessoas viabilizou a leitura humana dos dados agrupados.

**​Perfil Familiar**: Através da estatística descritiva (Média e Moda), traçamos o núcleo familiar predominante, informação vital para campanhas de produtos em grandes volumes.

**​Volume por Gênero**: O agrupamento de compras indicou com clareza o gênero responsável pela maior movimentação da loja, o que direciona orçamentos de marketing.

**​Campeões de Vendas**: A listagem dos "Top 10" produtos mais vendidos serve como guia para gestão de estoque e posicionamento físico nas prateleiras.

**​Problema Remanescente na Base**: A ausência de uma coluna com o "Valor Unitário (R$)" por produto limita a análise financeira; sabemos quanto saiu, mas não qual o lucro real gerado no período.