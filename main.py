import requests
from send_email import send_email
import os
from dotenv import load_dotenv

topic = "tesla"
api = os.getenv('NEWS_API')
url = ("https://newsapi.org/v2/everything?domains=wsj.com"
       f"&apiKey={api}")

# Make Requests
request = requests.get(url)

# Get a dictionary with data
content = request.json()
print(content)

# Access the article titles and description
body = "Subject: Daily News!\n\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = (body + str(article["title"]) + "\n"
                + str(article["description"]) + "\n"
                + str(article["url"]) + 2 * "\n")

body = body.encode("utf-8")
send_email(body)
