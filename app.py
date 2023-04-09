
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)
server = app.server

df = pd.read_csv('https://github.com/JWastin/Dash/blob/main/Title_1')

fig = px.scatter(df, x="X", y="Y")

app.layout = html.Div([
    dcc.Graph(
        id='cells position',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

