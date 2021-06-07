from app.news_test import News
from app import app
import urllib.request, json
from .models import news

apiKey = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_TOP_BASE_URL"]

def get_news(category):
    get_news_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(movie_results_list)

    return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        source = news_item.get('source')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        opening_url = news_item.get('url')
        image_url = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        news_object = News(source, author, title, description,opening_url,image_url,publishedAt)
        news_results.append(news_object)

    return  news_results