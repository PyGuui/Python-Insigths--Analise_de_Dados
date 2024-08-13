import pandas as pd

import plotly.express as px


tabela = pd.read_csv("cancelamentos.csv")

tabela = tabela.drop(columns="CustomerID")

#print(tabela.info())

tabela = tabela.dropna()

#print(tabela.info())


print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna,color="cancelou")

    grafico.show()


#Tratando Dados para baixa nos cancelamentos
filtro = tabela["ligacoes_callcenter"]<=4
tabela = tabela[filtro]


filtro = tabela["dias_atraso"]<=20
tabela = tabela[filtro]


filtro = tabela["duracao_contrato"]!="Monthly"
tabela = tabela[filtro]


print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))