import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# 📥 Load dataset
df = pd.read_csv('data.csv')  # Replace with your actual file

# 🧹 Clean and filter data
df = df.dropna()
df = df[df['trip_distance'] > 0]  # Optional filter to remove noise

# 🖥️ Create Dash app
app = dash.Dash(__name__)
app.title = "NYC Taxi Dashboard"

# 🧱 Layout
app.layout = html.Div([
    html.H1("NYC Taxi Data Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Payment Type:"),
        dcc.Dropdown(
            id='payment-filter',
            options=[{'label': str(i), 'value': i} for i in sorted(df['payment_type'].unique())],
            value=df['payment_type'].unique()[0]
        )
    ], style={'width': '30%', 'padding': '10px'}),

    dcc.Graph(id='fare-distribution'),
    dcc.Graph(id='trip-distance-vs-fare')
])

# 🔁 Callbacks to update graphs
@app.callback(
    [Output('fare-distribution', 'figure'),
     Output('trip-distance-vs-fare', 'figure')],
    [Input('payment-filter', 'value')]
)
def update_graphs(payment_type):
    filtered_df = df[df['payment_type'] == payment_type]

    # Histogram of fare amounts
    fig1 = px.histogram(
        filtered_df,
        x='fare_amount',
        nbins=50,
        title=f'Fare Distribution for Payment Type {payment_type}',
        color_discrete_sequence=['#636EFA']
    )

    # Scatter plot: Trip distance vs fare
    fig2 = px.scatter(
        filtered_df,
        x='trip_distance',
        y='fare_amount',
        title=f'Trip Distance vs Fare for Payment Type {payment_type}',
        opacity=0.6,
        color_discrete_sequence=['#EF553B']
    )

    return fig1, fig2

# ▶️ Run app (fixed for latest Dash versions)
if __name__ == '__main__':
    app.run(debug=True)
