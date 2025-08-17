# Entity Extraction with LangExtract

This project demonstrates how to use [LangExtract](https://pypi.org/project/langextract/) with OpenAI models to extract structured information such as **person names**, **countries**, and **skill sets** from unstructured text.


## How It Works
1. Define extraction examples (`EXAMPLES`) and a prompt (`PROMPT`) for guidance.
2. Pass input text to the `extract_result` function.
3. Extracted entities (person_name, country, skill-set) are returned with attributes and character intervals.

## Sample Output
```otpt
person_name Amir {'country': 'Egypt'}
country Cairo {'person_name': 'Amir'}
skill-set sketching intricate blueprints {'person_name': 'Amir'}
```

## Installation
```bash
pip install -r requirements.txt
```

## Requirements
- Python 3.8+
- LangExtract
- OpenAI API key set as environment variable:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

