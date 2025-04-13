# Project: LLM-Powered Log Summarizer + Alert Classifier

## Objective
Build a tool that ingests logs (e.g., JSON, Zeek, syslog), classifies or summarizes alerts using a fine-tuned or pre-trained LLM.

## MVP Timeline: 7–10 days
### Fastest MVP Path

## Phases
### Phase 1: Data Collection and Exploration (1–2 days)
- Use open syslog or Zeek logs
- Optionally, generate synthetic logs

### Phase 2: Preprocessing (1 day)
- Clean and chunk logs
- Format for prompt input

### Phase 3: LLM Integration (2–3 days)
- Use OpenAI API or Hugging Face model
- Test summarization and classification
- Prompt tuning

### Phase 4: Interface (2 days)
- Build a CLI or Streamlit UI for upload + display
- Optional: deploy with FastAPI

### Phase 5: Output formatting + Export (1–2 days)
- Save to JSON/CSV or send via email

## Tools
- LangChain, Hugging Face Transformers
- Streamlit or FastAPI
- JSON/CSV, syslog, Zeek log samples

---