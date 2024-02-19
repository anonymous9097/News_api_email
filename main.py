import requests
from send_email import send_email

topic = "tesla"
api = "8588afec044e47d59e67401c98431ecd"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-01-18&"
       "sortBy=publishedAt&"
       "apiKey=8588afec044e47d59e67401c98431ecd&"
       "language=en")

# Make Requests
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Daily News!\n\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = (body + str(article["title"]) + "\n"
                + str(article["description"]) + "\n"
                + str(article["url"]) + 2 * "\n")

body = body.encode("utf-8")
send_email(body)
