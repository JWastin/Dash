
import dash
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html


app = Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/JWastin/Dash/main/Title_1')

fig = px.scatter(df, x="X", y="Y")

app.layout = html.Div([
    dcc.Graph(
        id='cells position',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

