import json
import yaml

print("Classifier started")

with open("topics.yaml", "r", encoding="utf-8") as f:
    topics = yaml.safe_load(f)

print(f"Topics loaded: {len(topics['topics'])}")

topic_names = [topic["name"] for topic in topics["topics"]]

print(f"Available topics: {', '.join(topic_names)}")

adc_topic = next(
    topic for topic in topics["topics"]
    if topic["name"] == "ADC"
)

adc_keywords = adc_topic["keywords"]

print(f"ADC keywords loaded: {len(adc_keywords)}")

nams_topic = next(
    topic for topic in topics["topics"]
    if topic["name"] == "NAMS"
)

nams_keywords = nams_topic["keywords"]

print(f"NAMS keywords loaded: {len(nams_keywords)}")

with open("data/pubmed_results.json", "r", encoding="utf-8") as f:
    pubmed_records = json.load(f)

with open("data/rss_results.json", "r", encoding="utf-8") as f:
    rss_records = json.load(f)

print(f"PubMed records: {len(pubmed_records)}")
print(f"RSS records: {len(rss_records)}")

all_records = pubmed_records + rss_records

for topic in topics["topics"]:
    print(f"Topic: {topic['name']}")

for topic in topics["topics"]:
    print(f"{topic['name']} keywords: {len(topic['keywords'])}")

print("Sample PubMed title:")
print(pubmed_records[0]["title"])

print("Sample RSS title:")
print(rss_records[0]["title"])

sources = {}

for record in all_records:
    source = record["source"]
    sources[source] = sources.get(source, 0) + 1

print("Source breakdown:")
print(sources)

print(f"Total records: {len(all_records)}")

for keyword in adc_keywords[:5]:
    print(keyword)
print("Sample NAMS keywords:")

for keyword in nams_keywords[:5]:
    print(keyword)
