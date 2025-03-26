# %%
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Carregando o arquivo
brasil = gpd.read_file("Brasil.shp")

# Plotando o mapa
brasil.plot()
plt.show()

# %%
import pandas as pd
import plotly.express as px

data = {
    "Categorias": ["A", "B", "C", "D"],
    "Valores": [50, 120, 80, 200]
}
df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Categorias",
    y="Valores",
    title="Gráfico Interativo",
    color="Categorias",
    text="Valores"
)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.show()

# %%
