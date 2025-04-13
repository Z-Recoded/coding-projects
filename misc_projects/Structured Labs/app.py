import dash
from dash import html,dcc
import pandas as pd
import plotly.express as px

# Specify the path to your CSV file
file_name = 'misc_projects\Structured Labs\Data\quantum_tomography_dataset.csv'

# Load CSV file (make sure the path is correct)
df = pd.read_csv(file_name, header=None)

# Rename columns by index for easier reference
df.columns = ['fidelity', 'trace_distance', 'purity_original', 'purity_reconstructed']

# Preview first few rows
print(df.head())

# Create scatter plot
fig = px.scatter(
    df,
    x='fidelity',
    y='purity_reconstructed',
    color='trace_distance',
    title='Fidelity vs Purity (Reconstructed)',
    labels={
        'fidelity': 'Fidelity',
        'purity_reconstructed': 'Purity (Reconstructed)',
        'trace_distance': 'Trace Distance'
    },
    color_continuous_scale='Viridis'
)

#Build Dash app
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Quantum Tomography Dataset', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig),
])

if __name__ == '__main__':
    app.run(debug=True)