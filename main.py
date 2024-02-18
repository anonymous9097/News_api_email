import requests
from send_email import send_email

api = "8588afec044e47d59e67401c98431ecd"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-01-18&"
       "sortBy=publishedAt"
       "&apiKey=8588afec044e47d59e67401c98431ecd")

# Make Requests
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + str(article["title"]) + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

