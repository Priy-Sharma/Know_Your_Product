# Know Your Product

AI-powered app that reads a photo of a product label (face wash, shampoo,
detergent, milk packet, etc.), extracts the ingredient list with OCR, and
uses an LLM to explain what's actually in the product.

This first milestone covers: the landing page UI, image upload, OCR text
extraction, and an LLM call that filters the raw OCR text down to just the
ingredients (shown as bullet points). The agentic retrieval/verification
workflow (LangGraph) and Snowflake storage are separate, later milestones —
`src/ingredients/parser.py` is where that logic will eventually plug in.

## Repo structure

```
know_your_product/
├── app.py                     # Streamlit entry point — landing page + upload + results
├── config.py                  # env/config loading (API keys, OCR settings)
├── requirements.txt
├── .env.example                # copy to .env and fill in your key
├── assets/                    # logo / static images used by the UI
└── src/
    ├── ocr/
    │   └── extractor.py       # image -> raw text (pytesseract)
    ├── ingredients/
    │   └── parser.py          # raw text -> clean ingredient list (LLM call)
    └── ui/
        ├── styles.py          # CSS to match the landing-page mock
        └── landing.py         # hero section, category cards, steps strip
```

## Setup

1. Install Tesseract OCR on your machine (not a Python package):
   - macOS: `brew install tesseract`
   - Ubuntu/Debian: `sudo apt-get install tesseract-ocr`
   - Windows: install from https://github.com/UB-Mannheim/tesseract/wiki and
     add it to PATH.
2. `pip install -r requirements.txt`
3. `cp .env.example .env` and add your API key (Anthropic, by default —
   swap in `src/ingredients/parser.py` if you want to use a different
   provider).
4. `streamlit run app.py`

## Next milestones (not in this pass)

- LangGraph agentic workflow: source retrieval, evidence verification,
  unknown-ingredient handling.
- Snowflake schema + writes for structured product/ingredient data.
- Chatbot follow-up Q&A on a scanned product.
