# Scaffold: LLM-Powered Log Summarizer + Alert Classifier

## Folder Structure
```
llm_log_summarizer/
├── data/
│   └── sample_logs/
├── logs/
├── src/
│   ├── preprocess.py
│   ├── summarizer.py
│   └── classifier.py
├── ui/
│   └── app.py  # Streamlit or FastAPI
├── tests/
├── requirements.txt
└── README.md
```

## Quick Start
- Set up a virtual environment
- Add sample logs in `data/sample_logs/`
- Run `preprocess.py` to clean and format logs
- Call `summarizer.py` or `classifier.py` via `app.py`
---