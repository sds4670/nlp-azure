import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

Key = os.getenv("AZURE_KEY")
Endpoint = os.getenv("AZURE_ENDPOINT")
client = TextAnalyticsClient(endpoint=Endpoint, credential=AzureKeyCredential(Key))
print("client created successfully")

documents = ["ai is the best thing that happened to humanity. It has made our lives easier and more efficient. I love ai!"]
result = client.recognize_entities(documents=documents)
for doc in result:
    print("Named Entities:")
    for entity in doc.entities:
        print("\t", entity.text, "-", entity.category, "-", entity.subcategory, "-", entity.confidence_score)
