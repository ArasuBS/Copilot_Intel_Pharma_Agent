import json
from html import unescape
import re
import feedparser

def save_results(articles):

    with open("data/rss_results.json", "w", encoding="utf-8") as f:
        json.dump(
            articles,
            f,
            indent=2,
            ensure_ascii=False
        )

RSS_URL = "https://www.fiercepharma.com/rss/xml"

print("RSS script started")

feed = feedparser.parse(RSS_URL)

print(f"Found {len(feed.entries)} articles")

articles = []

for article in feed.entries[:5]:
    articles.append({
        "title": re.sub('<.*?>', '', unescape(article.title)),
        "link": article.link,
        "date": article.get("published", ""),
        "source": "Fierce Pharma"
    })

save_results(articles)

print("Saved results to data/rss_results.json")

for article in articles:
    print("-" * 80)
    print(f"SOURCE: {article['source']}")
    print(f"TITLE: {article['title']}")
    print(f"LINK: {article['link']}")
    print(flink": {article['date']}")
