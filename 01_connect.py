import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

Key = os.getenv("AZURE_KEY")
Endpoint = os.getenv("AZURE_ENDPOINT")
client = TextAnalyticsClient(endpoint=Endpoint, credential=AzureKeyCredential(Key))
print("client created successfully")
