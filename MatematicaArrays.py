import numpy as np
import matplotlib.pyplot as plt
monthly_sales = np.load('monthly_sales.npy')

# o array monthly_sales contem informações de vendas mês a mês de três indústrias diferentes 
# a primeira coluna refere-se a lojas de licores, a segunda restaurantes e a terceira lojas de departamento
"""
# criando um array 2D que cotenha uma coluna com o total mensal de vendas de cada indústria
# axis = 1, soma ao longo das colunas, dimensão 2
# keepdims = True - gera um array 2D, permitindo concatenar ao array monthly_sales, que é 2D

monthly_industry_sales = monthly_sales.sum(axis = 1, keepdims = True)

# adicionando a coluna soma a última coluna de monthly_sales
monthly_industry_sales_total = np.concatenate((monthly_sales, monthly_industry_sales), axis=1)
print(monthly_industry_sales_total)
# análisando as vendas de lojas de departamento em relação à média dos três setores
# criando um array 1D de média mensal de vendas dos três setores
avg_monthly_sales = monthly_sales.mean(axis=1)
print(avg_monthly_sales)

# plotando a venda média por mês dos três setores
plt.plot(np.arange(1,13), avg_monthly_sales, label = "Average sales across industries")

# plotando venda mensal de lojas de departamento
plt.plot(np.arange(1,13), monthly_sales[:,2], label = "Department store sales")
plt.legend()
plt.show()

# conclui-se que as vendas de loja de departamento sâo maiores que a média dos três setores
# em época de fim de ano

# uma métrica para avaliar se um crescimento é estável ao longo de um período é a soma cumulativa
# calculando a média cumulativa de cada um dos três setores
cumulative_monthly_industry = monthly_sales.cumsum(axis=0)
print(cumulative_monthly_industry)

# plotando o gráfico da soma cumulativo para cada setor
plt.plot(np.arange(1, 13), monthly_sales[:,0].cumsum(axis=0), label = "Liquor Stores")
plt.plot(np.arange(1, 13), monthly_sales[:,1].cumsum(axis=0), label = "Restaurants")
plt.plot(np.arange(1, 13), monthly_sales[:,2].cumsum(axis=0), label = "Department stores")
plt.legend()
plt.show()

# pelo gráfico pode-se concluir que o crescimento de vendas de restaurantes e lojas de licor é estável
# ao longo do ano, diferente da venda de lojas de departamento, que tem grande aumento no fim do ano

# criando um array de imposto sobre vendas em cada setor ( assumindo imposto de 5% )
tax_collected = monthly_sales * 0.05
print(tax_collected)

# criando um array com o valor de venda somado ao imposto coletado em cada setor
total_tax_and_revenue = monthly_sales + tax_collected
print(total_tax_and_revenue)
"""
# projetando vendas para o próximo ano do setor lojas de licor
# array 2D com dados coletados de multiplicadores mensais de cada setor 
monthly_industry_multipliers = np.array([[0.98, 1.02, 1. ],
                                        [1.00, 1.01, 0.97],
                                        [1.06, 1.03, 0.98],
                                        [1.08, 1.01, 0.98],
                                        [1.08, 0.98, 0.98],
                                        [1.1 , 0.99, 0.99],
                                        [1.12, 1.01, 1.  ],
                                        [1.1 , 1.02, 1.  ],
                                        [1.11, 1.01, 1.01],
                                        [1.08, 0.99, 0.97],
                                        [1.09, 1.  , 1.02],
                                        [1.13, 1.03, 1.02]])

"""
# criando um array de vendas mensais projetadas para cada setor
projected_monthly_sales = monthly_sales * monthly_industry_multipliers
print(projected_monthly_sales)

# Graph current liquor store sales and projected liquor store sales by month
# criando um gráfico com vendas de lojas de licores 
plt.plot(np.arange(1,13), monthly_sales[:, 0], label="Current liquor store sales")
plt.plot(np.arange(1,13), projected_monthly_sales[:, 0], label="Projected liquor store sales")
plt.legend()
plt.show()
# podemos vetorizar funções do Python para aplicar em array NumPy 
# array contendo strings 
names = np.array([["Izzy", "Monica", "Marvin"],
                  ["Weber", "Patel", "Hernandez"]])

# Vectorizando o método de string .upper(). Lembrando que o método é str.upper()
vectorized_upper = np.vectorize(str.upper)

# Aplicando vectorized_upper ao array name
uppercase_names = vectorized_upper(names)
print(uppercase_names)
"""

# trabalhando com Broadcasting
# encontrando o multiplicador de vendas médio para cada setor 
mean_multipliers = monthly_industry_multipliers.mean(axis=0)
print(mean_multipliers)

# imprimindo os formatos dos arrays mean_multipliers e monthly_sales
print(mean_multipliers.shape, monthly_sales.shape)

# multiplicando cada valor pelo multiplicador daquele setor
projected_sales = monthly_sales * mean_multipliers
print(projected_sales)