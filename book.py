import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from bs4 import BeautifulSoup

# Azure Credentials
KEY = os.getenv("AZURE_KEY")
ENDPOINT = os.getenv("AZURE_ENDPOINT")

# Create client
client = TextAnalyticsClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(KEY)
)

print("Client created successfully")


# Read HTML File
file_path = r"C:\Users\HP\Downloads\pg2701-h\pg2701-images.html"

with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()


# Parse HTML and extract text
soup = BeautifulSoup(html_content, "html.parser")

text = soup.get_text(separator=" ", strip=True)

print("Text extracted successfully")


# Azure Text Analytics accepts list of documents
# Large books should be sliced because Azure has limits

documents = [text[:5000]]


# Extract Key Phrases
result = client.extract_key_phrases(documents=documents)


# Print Results
for doc in result:

    if not doc.is_error:

        print("\nKey Phrases:\n")

        for phrase in doc.key_phrases:
            print("-", phrase)

    else:
        print("Error:", doc.error)


result = client.detect_language(documents=documents)
for idx, doc in enumerate(result):
    print("Document text: {}".format(documents[idx]))
    print("Language detected: {} (ISO6391 name: {})\n".format(doc.primary_language.name, doc.primary_language.iso6391_name))
 
result = client.recognize_pii_entities(documents=documents)
for doc in result:
    print("PII Entities:")
    for entity in doc.entities:
        print("\t", entity.text, "-", entity.category, "-")
