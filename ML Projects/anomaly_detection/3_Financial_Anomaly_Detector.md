# Project: Anomaly Detection for Personal Finances

## Objective
Analyze personal bank or transaction data to detect unusual behavior and unexpected spending using ML.

## MVP Timeline: 10–14 days

## Phases
### Phase 1: Data Aggregation (2–3 days)
- Export CSVs from your bank or connect via Plaid sandbox
- Format for ML input (date, merchant, amount, category)

### Phase 2: Preprocessing (2 days)
- Clean, scale, feature engineer (monthly spend, category drift)

### Phase 3: Model Selection (3–4 days)
- Use Isolation Forest, DBSCAN, or Autoencoders
- Evaluate performance manually or with labels

### Phase 4: Visualization + Alerts (2–3 days)
- Use Streamlit or Jupyter Dash
- Graph spend trends and flag anomalies

### Phase 5: Extend (Optional)
- Budgeting, category grouping, notification system

## Tools
- Scikit-learn, pandas, Streamlit
- Plaid (optional), Seaborn/Plotly
---