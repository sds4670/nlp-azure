import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

Key = os.getenv("AZURE_KEY")
Endpoint = os.getenv("AZURE_ENDPOINT")
client = TextAnalyticsClient(endpoint=Endpoint, credential=AzureKeyCredential(Key))
print("client created successfully")
documents = ["I had the best day of my life. I wish you were there with me.",
             "என் வாழ்க்கையில் நான் அனுபவித்த மிகச் சிறந்த நாள் இது. நீ என்னுடன் இருந்திருந்தால் நன்றாக இருந்திருக்கும்.",
             "我人生中最美好的一天。希望你和我在一起。",
             "Ich hatte den besten Tag meines Lebens. Ich wünschte, du wärst mit mir dort gewesen."]
result = client.detect_language(documents=documents)
for idx, doc in enumerate(result):
    print("Document text: {}".format(documents[idx]))
    print("Language detected: {} (ISO6391 name: {})\n".format(doc.primary_language.name, doc.primary_language.iso6391_name))
