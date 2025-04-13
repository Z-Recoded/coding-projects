import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load your CSV
file_path = 'misc_projects/Structured Labs/Data/quantum_tomography_dataset.csv'
# Load and sanitize the CSV
df = pd.read_csv(file_path, header=None)

# Rename columns
df.columns = ['fidelity', 'trace_distance', 'purity_original', 'purity_reconstructed']

# Strip whitespace from every cell
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Convert all columns to float (forcefully)
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop any rows that couldn't convert
df.dropna(inplace=True)

# Now calculate derived value
df['purity_loss'] = df['purity_original'] - df['purity_reconstructed']

# Preview first few rows
print(df.dtypes)

# Build 3D scatter plot
fig_3d = px.scatter_3d(
    df,
    x='fidelity',
    y='trace_distance',
    z='purity_reconstructed',
    color='purity_reconstructed',
    title='3D Scatter: Fidelity vs Trace Distance vs Purity Reconstructed',
    labels={
        'fidelity': 'Fidelity',
        'trace_distance': 'Trace Distance',
        'purity_reconstructed': 'Purity (Reconstructed)'
    },
    color_continuous_scale='Viridis'
)

# Dash App
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H2("Quantum Tomography Data Viewer", style={'textAlign': 'center'}),
    html.P("Explore the reconstructed quantum state metrics in 3D space."),
    dcc.Graph(figure=fig_3d),
])

if __name__ == '__main__':
    app.run(debug=True)