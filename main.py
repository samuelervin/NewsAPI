import requests
import json
import os
import send_email as sendmail

topic = "tesla"
api_key = "a31b1041f492426ea5093016caeed677"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&from=2024-06-10" \
      "&sortBy=publishedAt" \
      f"&apiKey={api_key}" \
      "&language=en" 

request = requests.get(url)

content = request.json()
message = ""
if content['status'] == 'ok':
    for article in content['articles'][:20]:
        if article['source']['name'] is not None:
            message += article['source']['name'] + "\n"
        if article['publishedAt'] is not None:
            message += article['publishedAt'] + "\n"
        if article['author'] is not None:
            message += article['author'] + "\n"
        if article['title'] is not None:
            message += article['title'] + article['url'] + "\n"
        if article['description'] is not None:
            message += article['description'] + "\n"
        message += "-----------------------------------\n"
        
message.encode('utf-8')

sendmail.send_mail("News", "Here is the latest news", message)
print("Email sent")
