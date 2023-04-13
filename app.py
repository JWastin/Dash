
import dash
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html


app = dash.Dash(__name__)
server = app.server

#df = [[1,2],[3,4]]
#fig = px.scatter(df)
df= pd.read_csv("https://raw.githubusercontent.com/JWastin/Dash/main/Title_1")
fig = px.scatter(df,x="X",y="Y")


app.layout = html.Div([
    html.Header("Position of cells center",style = {"fontsize" : 40,
                                                    "textAlign" : "center"}),
    
    dcc.Graph(
        id='cells position',
        figure=fig
    )
    
])

if __name__ == '__main__':
    app.server.run(debug=True) 
    

