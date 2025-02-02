import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load sample data
df = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Sales': [100, 150, 200, 130, 180, 160, 170, 250, 300, 310]
})

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Line Chart', 'value': 'line'},
            {'label': 'Bar Chart', 'value': 'bar'}
        ],
        value='line',
        clearable=False
    ),
    dcc.Graph(id='graph'),
])

# Update graph based on dropdown selection
@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(chart_type):
    if chart_type == 'line':
        fig = px.line(df, x='Date', y='Sales', title="Sales Over Time")
    else:
        fig = px.bar(df, x='Date', y='Sales', title="Sales Over Time")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
