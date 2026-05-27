# NLP Azure Project

A comprehensive Natural Language Processing project leveraging Azure Text Analytics API to analyze text data. This project demonstrates multiple NLP tasks performed on different text sources, from simple sentences to large document files.

## 🎯 Implemented Features

### ✅ Core NLP Tasks

1. **Language Detection** (`language_detection.py`)
   - Automatically detect the language of input text
   - Supports multilingual content (English, Tamil, Chinese, German, etc.)
   - Returns ISO 6391 language codes

2. **Key Phrase Extraction** (`key_phrase.py`)
   - Extract important keywords and phrases from text
   - Useful for summarization and content analysis
   - Works across multiple languages

3. **PII Detection** (`pii_detection.py`)
   - Identify and detect Personally Identifiable Information
   - Recognizes credit card numbers, ID numbers, and sensitive data
   - Critical for data privacy and security applications

4. **Book/Document Analysis** (`book.py`)
   - Comprehensive analysis of large HTML documents
   - Combines language detection, key phrase extraction, and PII detection
   - Processes large documents by splitting them into Azure-compliant chunks
   - Extracts text from HTML files using BeautifulSoup

## 📋 Prerequisites

- Python 3.x
- Azure Cognitive Services account with Text Analytics API
- Azure credentials (API Key and Endpoint)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/sds4670/nlp-azure.git
cd nlp-azure
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv env
.\env\Scripts\activate

# macOS/Linux
python -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Azure Credentials
```bash
cp .env.example .env
```

Edit `.env` and add your Azure credentials:
```
AZURE_KEY=your_azure_api_key_here
AZURE_ENDPOINT=https://your-service.cognitiveservices.azure.com/
```

## 💻 Usage Examples

### Language Detection
```bash
python language_detection.py
```
Detects language from multiple sample texts in English, Tamil, Chinese, and German.

**Output:**
```
Language detected: English (ISO6391 name: en)
Language detected: Tamil (ISO6391 name: ta)
Language detected: Chinese_Simplified (ISO6391 name: zh_Hans)
Language detected: German (ISO6391 name: de)
```

### Key Phrase Extraction
```bash
python key_phrase.py
```
Extracts key phrases from AI-related text content.

**Output:**
```
Key Phrases:
 ai
 thing
 lives
 humanity
```

### PII Detection
```bash
python pii_detection.py
```
Identifies sensitive information like credit card numbers and ID numbers.

**Output:**
```
PII Entities:
  1234-5678-9012-3456 - CreditCardNumber -
  123-45-6789 - AdhaarNumber -
```

### Book Analysis (Comprehensive)
```bash
python book.py
```
Analyzes large HTML documents by:
1. Reading HTML file using BeautifulSoup
2. Extracting plain text
3. Detecting language
4. Extracting key phrases
5. Identifying PII entities

**Features:**
- Handles large documents by chunking text (5000 char limit per Azure request)
- Processes HTML content efficiently
- Combines multiple NLP tasks in a single workflow

## 📁 Project Structure

```
nlp-azure/
├── language_detection.py    # Language detection from multilingual text
├── key_phrase.py           # Key phrase extraction
├── pii_detection.py        # Personally Identifiable Information detection
├── book.py                 # Comprehensive document analysis
├── 01_connect.py           # Azure connection test
├── sentiment.py            # Sentiment analysis (basic setup)
├── named_enitity.py        # Named Entity Recognition (NER)
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🔑 Key Files Documentation

| File | Purpose | Status |
|------|---------|--------|
| `language_detection.py` | Multilingual language detection | ✅ Implemented |
| `key_phrase.py` | Extract important phrases | ✅ Implemented |
| `pii_detection.py` | Detect sensitive data | ✅ Implemented |
| `book.py` | Combined analysis on large documents | ✅ Implemented |
| `sentiment.py` | Sentiment analysis setup | ⏳ Available |
| `named_enitity.py` | Named entity recognition | ⏳ Available |

## ⚙️ Dependencies

- `azure-ai-textanalytics` - Azure Text Analytics client
- `azure-core` - Azure core utilities
- `beautifulsoup4` - HTML parsing for document analysis

## 🔐 Security Notes

- ⚠️ Never commit `.env` files with credentials
- ✅ Use `.env.example` as template for credentials
- ✅ API keys and endpoints are loaded from environment variables
- ✅ `.gitignore` protects sensitive files from being pushed

## 📊 Workflow: Processing a Book

The `book.py` script demonstrates the complete workflow:

```
HTML Document
    ↓
BeautifulSoup Parsing
    ↓
Text Extraction
    ↓
Text Chunking (5000 chars)
    ↓
Azure Text Analytics Processing
    ├── Language Detection
    ├── Key Phrase Extraction
    └── PII Detection
    ↓
Results Display
```

## 🎓 Learning Outcomes

This project demonstrates:
- Integration with Azure Cognitive Services
- Multilingual NLP processing
- Document parsing and text extraction
- Data privacy and PII detection
- Large document handling with chunking
- Environment-based configuration management

## 📝 Example Output

```
Client created successfully
Text extracted successfully

Key Phrases:
- best day
- life
- wishes
- humanity

Language detected: English (ISO6391 name: en)

PII Entities:
  (none detected in sample)
```

## 🚀 Future Enhancements

- Sentiment analysis on book excerpts
- Named entity extraction from documents
- Batch processing of multiple documents
- Results export to JSON/CSV
- Web interface for document analysis

## 📄 License

MIT

## 👤 Author

Created as an NLP exploration project using Azure Cognitive Services
