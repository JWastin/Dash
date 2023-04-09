
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv('/home/edmon/Documents/Labo/Physio_Ca/Rutter Lab Analysis/1. Calcuim Immaging plots/Table_1')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

