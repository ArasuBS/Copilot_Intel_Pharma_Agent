import feedparser

RSS_URL = "https://www.fiercepharma.com/rss/xml"

print("RSS script started")

feed = feedparser.parse(RSS_URL)

print(f"Found {len(feed.entries)} articles")

for article in feed.entries[:5]:
    print(article.title)
