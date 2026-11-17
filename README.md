# Structured JSON Output Generator Using LLMs

## Project Overview
This project converts unstructured product descriptions into structured JSON using a Large Language Model (LLM).

The application uses Python, Ollama, Qwen 3.5, Pydantic, and Streamlit.

## Technologies Used
- Python
- Ollama
- Qwen 3.5 (2B)
- Pydantic
- Streamlit

## Project Structure
```text
structured-json-generator/
│
├── app.py
├── extractor.py
├── schemas.py
├── test_validation.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Features
- Extracts product details from natural language.
- Generates structured JSON output.
- Validates output using Pydantic.
- Handles missing and ambiguous information.
- Detects invalid data such as negative prices.
- Allows users to download generated JSON.

## How to Run

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Make sure Ollama is installed and the model is available:

```bash
ollama pull qwen3.5:2b
```

3. Start the application:

```bash
streamlit run app.py
```

## Validation
Pydantic checks the generated product data against the defined schema. The validation test rejects negative prices.

## Screenshots
Add your application screenshots in the `screenshots/` folder.

## Conclusion
This project demonstrates how LLMs can transform unstructured text into consistent structured JSON. Combining an LLM with Pydantic validation improves the reliability of AI-powered data extraction.