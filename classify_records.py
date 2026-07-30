import json
import yaml

print("Classifier started")

with open("topics.yaml", "r", encoding="utf-8") as f:
    topics = yaml.safe_load(f)

print(f"Topics loaded: {len(topics['topics'])}")

topic_names = [topic["name"] for topic in topics["topics"]]

print(f"Available topics: {', '.join(topic_names)}")

with open("data/pubmed_results.json", "r", encoding="utf-8") as f:
    pubmed_records = json.load(f)

with open("data/rss_results.json", "r", encoding="utf-8") as f:
    rss_records = json.load(f)

print(f"PubMed records: {len(pubmed_records)}")
print(f"RSS records: {len(rss_records)}")
