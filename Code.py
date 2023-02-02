import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv (r'lifeExp.csv')
print(df.head(3))
df1 = df[['continent', 'year','lifeExp']]
print(df1.head())
heatmap1_data = pd.pivot_table(df1, values='lifeExp',index=['continent'],columns='year')
sns.heatmap(heatmap1_data, cmap="YlGnBu")
plt.show()
df2 = df[['country','continent', 'year','lifeExp']]
heatmap2_data = pd.pivot_table(df2,values='lifeExp', index=['country'], columns='year')
heatmap2_data.head(n=5)
sns.heatmap(heatmap2_data, cmap="BuGn")
plt.show()
df3 = df[['country','continent', 'year','lifeExp']]
heatmap3_data = pd.pivot_table(df3,values='lifeExp', index=['continent','country'], columns='year')
plt.figure(figsize=(8, 12))
sns.heatmap(heatmap3_data, cmap="RdYlBu")
plt.show()
