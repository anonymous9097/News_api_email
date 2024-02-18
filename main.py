import requests

api = "8588afec044e47d59e67401c98431ecd"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-01-18&"
       "sortBy=publishedAt"
       "&apiKey=8588afec044e47d59e67401c98431ecd")

# Make Requests
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
