from goose3 import Goose
import pandas as pd

config = {
    'browser_user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2)',
}
g = Goose(config)
articles = []
urls = []

with open('articles_url.txt', 'r') as f:
    for line in f:
        url = f.readline().strip()
        urls.append(url)
        article = g.extract(url=url)
        articles.append(article)
        print('Article extracted from: {}'.format(url))
print('Total number of articles extracted: {}'.format(len(articles)))

df = pd.DataFrame({'title': [article.title for article in articles],
                    'cleaned_text': [article.cleaned_text for article in articles],
                    'url': [url for url in urls],
                    'domain': [article.domain for article in articles],
                    'publish_date': [article.publish_date for article in articles],
                    'meta_description': [article.meta_description for article in articles],
                    'meta_keywords': [article.meta_keywords for article in articles],
                    'meta_lang': [article.meta_lang for article in articles],
                    'additional_data': [article.additional_data for article in articles],
                    'tags': [article.tags for article in articles]})
df.to_csv('./data/articles.csv', index=False)