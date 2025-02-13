'''
import pandas as pd
import openpyxl


dados = pd.read_excel('..\\Importar\cidades\Cidades.xlsx')
print(dados.head())


dados = pd.read_excel ('..\\Importar\cidades\Cidades.xlsx')


df=dados.rename(columns={
         'IDVendas' : 'mama',
         'NomeCidades':'Cidade',
         'Qtde':'QtdeVendas'
         }, inplace = False)

print(dados.head())
print(df.head())
'''
'''

import pandas as pd
import openpyxl
import matplotlib as plt
import numpy as np

dados = pd.read_excel('..\\Importar\cidades\GraficoCidade.xlsx')


df=dados.rename(columns={
         'IDVendas' : 'mama',
         'NomeCidades':'Cidade',
         'Qtde':'QtdeVendas'
         }, inplace = False)

#cidade = df['Cidade'],qtde = df['QtdeVendas']

plt.plot(df['Cidade'],'df['QtdeVendas'])
plt.show()
'''
'''
import pandas as pd
import matplotlib.pyplot as plt  # Corrigido: importação correta do matplotlib.pyplot
import numpy as np

# Leitura dos dados do Excel
dados = pd.read_excel('..\\Importar\\cidades\\GraficoCidade.xlsx')  # Corrigido: barra invertida na string de caminho

df=dados.rename(columns={
         'IDVenda' : 'mama',
         'NomeCidade':'Cidade',
         'Qtde':'QtdeVendas'
         })

# Plotando o gráfico de linha
plt.plot(df['Cidade'], df['QtdeVendas'], marker='o')  # Corrigido: sintaxe do plot

plt.xlabel('Cidade')  # Rótulo do eixo X
plt.ylabel('Quantidade de Vendas')  # Rótulo do eixo Y
plt.title('Vendas por Cidade')  # Título do gráfico

# Exibindo o gráfico
plt.show()
'''

import pandas as pd
import matplotlib.pyplot as plt  # Corrigido: importação correta do matplotlib.pyplot
import numpy as np

fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.legend()
# Show the plot
plt.show()
