import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

Key = os.getenv("AZURE_KEY")
Endpoint = os.getenv("AZURE_ENDPOINT")
client = TextAnalyticsClient(endpoint=Endpoint, credential=AzureKeyCredential(Key))
print("client created successfully")

documents = ["My credit card number is 1234-5678-9012-3456 and my adhaar number is 123-45-6789."]
result = client.recognize_pii_entities(documents=documents)
for doc in result:
    print("PII Entities:")
    for entity in doc.entities:
        print("\t", entity.text, "-", entity.category, "-")
