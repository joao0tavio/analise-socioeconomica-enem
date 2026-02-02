from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd
import numpy as np

# Carregamento dos dados
df = pd.read_csv('dados/enem_2021_limpo.csv')

# Limpeza dos dados
df.dropna(subset=['RENDA_NUMERICA', 'TP_ESCOLA'], inplace=True)
df = df[df['TP_ESCOLA'].isin([2, 3])].copy()

# Engenharia de Atributos
# Se TP_ESCOLA for 3, vira 1. Se for 2, vira 0.
df['ESCOLA_PRIVADA'] = df['TP_ESCOLA'].apply(lambda x: 1 if x == 3 else 0)

# Definindo as Variáveis
X = df[['RENDA_NUMERICA', 'ESCOLA_PRIVADA']]
Y = df['NOTA_FINAL']

# Divisão Treino/Teste
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Treino
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Avaliação
y_pred = modelo.predict(X_test)

print("Resultados da Regressão Múltipla:")
print(f"Intercepto (Nota base Escola Pública + Sem Renda): {modelo.intercept_:.2f}")
print(f"Peso da Renda (a cada R$ 1,00): {modelo.coef_[0]:.4f}")
print(f"Bônus Escola Privada (Pontos extras só por ser privada): {modelo.coef_[1]:.2f}")
print(f"\nR²: {r2_score(y_test, y_pred):.4f}")

# SIMULAÇÃO COMPARATIVA
# Vamos comparar dois alunos com a mesma renda (R$ 3.000), mas escolas diferentes
renda_simulada = 3000
aluno_publica = modelo.predict([[renda_simulada, 0]])[0]
aluno_privada = modelo.predict([[renda_simulada, 1]])[0]

print(f"\n--- Simulação (Renda R$ 3.000) ---")
print(f"Nota na Escola Pública: {aluno_publica:.1f}")
print(f"Nota na Escola Privada: {aluno_privada:.1f}")
print(f"Diferença: {aluno_privada - aluno_publica:.1f} pontos")