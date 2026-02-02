import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#COLUNAS PARA ANALISE
colunas_selecionadas = [
    'NU_INSCRICAO', 
    'Q006',             
    'TP_ESCOLA',        
    'NU_NOTA_CN',       
    'NU_NOTA_CH',       
    'NU_NOTA_LC',       
    'NU_NOTA_MT',       
    'NU_NOTA_REDACAO'   
]

# Dicionário de Renda (Estimativa baseada no Salário Mínimo 2021 ~ R$ 1.100)
dict_renda = {
    'A': 0,          
    'B': 550,        
    'C': 1375,      
    'D': 1925,      
    'E': 2475,    
    'F': 3025,    
    'G': 3850,      
    'H': 4950,      
    'I': 6050,       
    'J': 7150,       
    'K': 8250,     
    'L': 9350,      
    'M': 10450,      
    'N': 12100,      
    'O': 14850,     
    'P': 19250,      
    'Q': 25000       
}

print("Carregando dataset (pode demorar um pouco)...")
df = pd.read_csv('dados/MICRODADOS_ENEM_2021.csv', sep=';', encoding='latin-1', usecols=colunas_selecionadas)

# Limpeza Inicial: Removemos alunos que faltaram em alguma prova
df.dropna(subset=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO'], inplace=True)

# Criar Nota Média Geral
df['NOTA_FINAL'] = (df['NU_NOTA_CN'] + df['NU_NOTA_CH'] + df['NU_NOTA_LC'] + df['NU_NOTA_MT'] + df['NU_NOTA_REDACAO']) / 5

# Converter Renda
df['RENDA_NUMERICA'] = df['Q006'].map(dict_renda)

print(f"Dados prontos. Total de alunos válidos para análise: {len(df)}")
print(df[['Q006', 'RENDA_NUMERICA', 'NOTA_FINAL']].head())

df.to_csv('dados/enem_2021_limpo.csv', index=False)