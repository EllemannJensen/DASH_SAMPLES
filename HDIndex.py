import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://github.com/EllemannJensen/DASH_SAMPLES/blob/main/HDI.csv', error_bad_lines=False, sep=';', decimal= ",", thousands='.')

fig = px.scatter(df, x="Gross national income (GNI) per capita", y="Life expectancy at birth",
                 size="Mean years of schooling", color="HD Categorie", hover_name="Country",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='GNI-vs-LEaB',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
