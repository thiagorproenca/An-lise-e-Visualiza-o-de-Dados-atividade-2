import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dados fictícios para vendas, número de clientes e lucro
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
vendas = [200, 220, 250, 300, 400, 450, 500]
clientes = [50, 60, 70, 80, 90, 100, 110]
lucro = [1000, 1200, 1500, 1800, 2000, 2200, 2500]

df_vendas = pd.DataFrame({
    'Dia': dias,
    'Vendas': vendas,
    'Clientes': clientes,
    'Lucro': lucro
})

# Gráfico de Barras: Total de Vendas por Dia
plt.figure(figsize=(10, 6))
sns.barplot(x='Dia', y='Vendas', data=df_vendas, palette='viridis')
plt.title('Total de Vendas por Dia')
plt.xlabel('Dia da Semana')
plt.ylabel('Vendas (R$)')
plt.show()

# Gráfico de Dispersão: Relação entre Número de Clientes e Total de Vendas
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Clientes', y='Vendas', data=df_vendas, s=100, color='blue')
plt.title('Relação entre Número de Clientes e Total de Vendas')
plt.xlabel('Número de Clientes')
plt.ylabel('Vendas (R$)')
plt.grid(True)
plt.show()

# Heatmap: Correlação entre Vendas, Número de Clientes e Lucro
correlacao = df_vendas[['Vendas', 'Clientes', 'Lucro']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação entre Vendas, Número de Clientes e Lucro')
plt.show()