# Scaffold: Financial Transaction Classification System

## Folder Structure
```
transaction_classifier/
├── data/
│   └── transactions.csv
├── models/
│   └── tree_model.pkl
│   └── nn_model.h5
├── notebooks/
│   └── EDA_and_Feature_Engineering.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── evaluate.py
├── api/
│   └── main.py  # FastAPI app
├── dashboard/
│   └── app.py  # Streamlit dashboard
├── config/
│   └── model_config.yaml
├── requirements.txt
├── Dockerfile
└── README.md
```

## Quick Start
1. Place your transaction CSV in the `data/` folder.
2. Run `train.py` to build models.
3. Launch the API with `uvicorn api.main:app --reload`.
4. Run the dashboard via `streamlit run dashboard/app.py`.

## Optional Extensions
- Add authentication to the API.
- Store user labels for feedback learning.