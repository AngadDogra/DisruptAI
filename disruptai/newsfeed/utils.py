import requests

NEWS_API_KEY = 'b77712965ffe47bfa4c36fa27d05524d'  # Replace this

def fetch_news():
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=5&apiKey={NEWS_API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        return [(a['title'], a.get('description', 'No description available')) for a in articles]
        # return [a['title'] for a in articles]

    else:
        return []
