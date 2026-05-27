# NLP Azure Project

A comprehensive NLP project using Azure Text Analytics to perform various Natural Language Processing tasks.

## Features

- **Sentiment Analysis** - Analyze emotional tone of text
- **Language Detection** - Identify the language of text content
- **Named Entity Recognition (NER)** - Extract named entities (persons, organizations, locations, etc.)
- **Key Phrase Extraction** - Extract important phrases from text
- **PII Detection** - Identify Personally Identifiable Information in text
- **Book Analysis** - Extract insights from large HTML documents

## Prerequisites

- Python 3.x
- Azure Cognitive Services account
- Azure Text Analytics API credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sds4670/nlp-azure.git
cd nlp-azure
```

2. Create and activate a virtual environment:
```bash
python -m venv env
.\env\Scripts\activate  # Windows
source env/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your Azure credentials by creating a `.env` file:
```bash
cp .env.example .env
```

Edit `.env` and add your Azure credentials:
```
AZURE_KEY=your_azure_key_here
AZURE_ENDPOINT=https://your-service.cognitiveservices.azure.com/
```

## Usage

Run any of the analysis scripts:

```bash
python sentiment.py
python language_detection.py
python named_enitity.py
python key_phrase.py
python pii_detection.py
python book.py
```

## Files

- `01_connect.py` - Basic Azure connection test
- `sentiment.py` - Sentiment analysis example
- `language_detection.py` - Language detection example
- `named_enitity.py` - Named entity recognition example
- `key_phrase.py` - Key phrase extraction example
- `pii_detection.py` - PII detection example
- `book.py` - Book/document analysis combining multiple features
- `requirements.txt` - Python dependencies

## License

MIT
