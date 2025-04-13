import pandas as pd
import plotly.express as px

# Load CSV file (make sure the path is correct)
df = pd.read_csv('data/quantum_tomography_dataset.csv', header=None)

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

# Show plot in browser
fig.show()
