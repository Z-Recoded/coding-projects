# Build Plan: Financial Transaction Classification System

## Objective
Develop a machine learning system that classifies personal financial transactions into spending categories using both decision trees and neural networks. Deploy the system as a REST API and integrate with a dashboard.

## MVP Timeline: 10–14 days

## Phases

### Phase 1: Data Collection & Exploration (2–3 days)
- Use Kaggle datasets (e.g., “Bank Transactions Dataset” or simulated Plaid exports)
- Explore transaction structure: date, description, merchant, amount

### Phase 2: Feature Engineering (2 days)
- Extract keywords from transaction descriptions
- Create time-based features (day of week, hour)
- Normalize or bin transaction amounts

### Phase 3: Model Development (3–4 days)
- Train decision tree and simple neural network
- Use ensemble or fallback model logic
- Evaluate with F1-score, accuracy, confusion matrix

### Phase 4: API Deployment (2–3 days)
- Build API with FastAPI or Flask
- Create endpoints: `/predict`, `/health`, `/retrain` (optional)
- Dockerize for local and cloud deployment

### Phase 5: Dashboard Integration (2–3 days)
- Use Streamlit or Dash to display categorized transaction history
- Support manual corrections + feedback loop

### Optional: Active Learning/Feedback System
- Allow users to reclassify incorrect entries
- Use labels to fine-tune models later

## Tools & Frameworks
- Python, Scikit-learn, Keras (TensorFlow backend)
- FastAPI, Docker
- Streamlit, pandas, matplotlib/seaborn

---