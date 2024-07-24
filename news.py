import requests
from flask import Flask, render_template, send_file
from newspaper import Article  # type: ignore
import nltk  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
import json
from io import BytesIO

# Download NLTK resources if not already downloaded
nltk.download('punkt')

app = Flask(__name__)

def fetch_article_urls():
    base_url = 'https://www.hindustantimes.com/'
    categories = ['technology', 'sports', 'education', 'latest-news']  # Define categories
    all_matching_links = []
    seen_article_ids = set()  # To keep track of unique article IDs

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    for category in categories:
        url = base_url + category
        response = requests.get(url, headers=headers)
        matching_links = []

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            a_tags = soup.find_all('a', href=True)

            for a_tag in a_tags:
                href = a_tag['href']
                if a_tag.has_attr('data-articleid'):
                    article_id = a_tag['data-articleid']
                    if article_id not in seen_article_ids:
                        seen_article_ids.add(article_id)
                        full_url = base_url + href if href.startswith('/') else href
                        matching_links.append({'article_id': article_id, 'url': full_url})
        else:
            print(f'Failed to retrieve the page for {category}. Status code:', response.status_code)

        if matching_links:
            all_matching_links.append({'category': category, 'links': matching_links})

    return all_matching_links

def scrape_articles():
    all_urls = fetch_article_urls()
    articles = {}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    for category in all_urls:
        for article in category['links']:
            article_id = article['article_id']
            url = article['url']
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                article_data = Article(url)
                article_data.download()
                article_data.parse()
                article_data.nlp()

                title = article_data.title
                summary = article_data.summary
                publish_date = str(article_data.publish_date) if article_data.publish_date else 'N/A'
                image_url = article_data.top_image

                articles[article_id] = {
                    'category': category['category'],
                    'url': url,
                    'title': title,
                    'summary': summary,
                    'publish_date': publish_date,
                    'image_url': image_url
                }
            else:
                print(f'Failed to retrieve article from {url}. Status code:', response.status_code)

    return articles

@app.route('/')
def index():
    articles = scrape_articles()
    return render_template('news.html', articles=articles)

@app.route('/download')
def download():
    articles = scrape_articles()
    json_data = json.dumps(articles, indent=4)

    json_file = BytesIO()
    json_file.write(json_data.encode('utf-8'))
    json_file.seek(0)

    return send_file(json_file, as_attachment=True, download_name='articles.json', mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
