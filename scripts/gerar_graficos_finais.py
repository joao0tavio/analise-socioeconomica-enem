import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar e Preparar
df = pd.read_csv('dados/enem_2021_limpo.csv')
df.dropna(subset=['RENDA_NUMERICA', 'TP_ESCOLA'], inplace=True)
df = df[df['TP_ESCOLA'].isin([2, 3])].copy()

df['Tipo_Escola'] = df['TP_ESCOLA'].map({2: 'Pública', 3: 'Privada'})

# Configuração de Estilo
sns.set_theme(style="whitegrid")

# GRÁFICO 1: A Regressão Dupla
plt.figure(figsize=(10, 6))

sns.regplot(x='RENDA_NUMERICA', y='NOTA_FINAL', data=df[df['TP_ESCOLA']==2], 
            scatter=False, color='blue', label='Escola Pública')
sns.regplot(x='RENDA_NUMERICA', y='NOTA_FINAL', data=df[df['TP_ESCOLA']==3], 
            scatter=False, color='red', label='Escola Privada')

amostra = df.sample(5000)
sns.scatterplot(x='RENDA_NUMERICA', y='NOTA_FINAL', hue='Tipo_Escola', 
                data=amostra, alpha=0.1, palette={'Pública':'blue', 'Privada':'red'})

plt.title('Impacto da Renda na Nota: Pública vs Privada')
plt.xlabel('Renda Familiar (R$)')
plt.ylabel('Nota Final Média')
plt.legend()
plt.ylim(0, 1000)
plt.xlim(0, 20000)

plt.savefig('grafico_regressao_escolas.png', dpi=300)

# GRÁFICO 2: Comparação Direta (Boxplot)
plt.figure(figsize=(8, 6))
sns.boxplot(x='Tipo_Escola', y='NOTA_FINAL', data=df, palette="Set2")
plt.title('Distribuição de Notas por Tipo de Escola')
plt.xlabel('')
plt.ylabel('Nota Final')
plt.savefig('grafico_boxplot_escolas.png', dpi=300)
