import json

print("Classifier started")

with open("data/pubmed_results.json", "r", encoding="utf-8") as f:
    pubmed_records = json.load(f)

with open("data/rss_results.json", "r", encoding="utf-8") as f:
    rss_records = json.load(f)

print(f"PubMed records: {len(pubmed_records)}")
print(f"RSS records: {len(rss_records)}")
