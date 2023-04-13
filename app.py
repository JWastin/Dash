
import dash
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html


app = dash.Dash(__name__)
server = app.server

df = [["X","Y"],[1,2],[3,4]]

fig = px.scatter(df, x="X", y="Y")

app.layout = html.Div([
    dcc.Graph(
        id='cells position',
        figure=fig
    )
])

if __name__ == '__main__':
    app.server.run(debug=True) 
    

