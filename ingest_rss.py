from html import unescape
import re
import feedparser

RSS_URL = "https://www.fiercepharma.com/rss/xml"

print("RSS script started")

feed = feedparser.parse(RSS_URL)

print(f"Found {len(feed.entries)} articles")

articles = []

for article in feed.entries[:5]:
    articles.append({
        "title": re.sub('<.*?>', '', unescape(article.title)),
        "link": article.link,
        "source": "Fierce Pharma"
    })

for article in articles:
    print("-" * 80)
    print(f"SOURCE: {article['source']}")
    print(f"TITLE: {article['title']}")
    print(f"LINK: {article['link']}")
