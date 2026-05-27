import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

Key = os.getenv("AZURE_KEY")
Endpoint = os.getenv("AZURE_ENDPOINT")
client = TextAnalyticsClient(endpoint=Endpoint, credential=AzureKeyCredential(Key))
print("client created successfully")

documents = [
    "I had the best day of my life. I wish you were there with me."]
result = client.analyze_sentiment(documents=documents)
for doc in result:
    print("Document Sentiment: {}".format(doc.sentiment))
    print("Overall scores: positive={}; neutral={}; negative={} \n".format(
        doc.confidence_scores.positive,
        doc.confidence_scores.neutral,
        doc.confidence_scores.negative,
    ))
