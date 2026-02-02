from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

df = pd.read_csv('dados/enem_2021_limpo.csv')
df.dropna(subset=['RENDA_NUMERICA'], inplace=True)

X = df[['RENDA_NUMERICA']] 
Y = df['NOTA_FINAL']

# Divisão Treino vs Teste
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Criação e Treino do Modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Avaliação
# Vamos prever as notas dos 20% que o modelo nao viu
y_pred = modelo.predict(X_test)

print("Resultados do Modelo:")
print(f"Intercepto (Nota base se renda for 0): {modelo.intercept_:.2f}")
print(f"Coeficiente Angular (Aumento de nota por R$ de renda): {modelo.coef_[0]:.4f}")
print(f"\nR² (Quanto a renda explica a nota?): {r2_score(y_test, y_pred):.4f}")
print(f"Erro Médio (RMSE): {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")

# Exemplo de previsão
renda_exemplo = 5000 # Renda de 5k
nota_prevista = modelo.predict([[renda_exemplo]])[0]
print(f"\nSimulação: Um aluno com renda familiar de R$ 5.000 teria nota estimada de: {nota_prevista:.1f}")