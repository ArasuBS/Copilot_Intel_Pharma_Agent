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

bispecifics_topic = next(
    topic for topic in topics["topics"]
    if topic["name"] == "Bispecifics"
)

bispecifics_keywords = bispecifics_topic["keywords"]

print(f"Bispecifics keywords loaded: {len(bispecifics_keywords)}")

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

rss_title = rss_records[0]["title"]

print("Checking first RSS title against NAMS keywords")

for keyword in nams_keywords[:5]:
    print(keyword)

sources = {}

for record in all_records:
    source = record["source"]
    sources[source] = sources.get(source, 0) + 1

print("Source breakdown:")
print(sources)

first_record = all_records[0]

print("First record title:")
print(first_record["title"])

adc_match = False

for keyword in adc_keywords:
    if keyword.lower() in first_record["title"].lower():
        adc_match = True
        break

print(f"ADC match: {adc_match}")

adc_records = []

for record in all_records:
    title = record["title"]

    for keyword in adc_keywords:
        if keyword.lower() in title.lower():
            adc_records.append(record)
            break
print(f"ADC records found: {len(adc_records)}")

for record in adc_records[:5]:
    print(record["title"])

for record in adc_records:
    record["topics"] = ["ADC"]

classified_records = []

for record in adc_records:
    classified_records.append(record)

print("Tagged ADC records:")

for record in adc_records[:3]:
    print(record["topics"], "-", record["title"])

nams_records = []

for record in all_records:
    title = record["title"]

    for keyword in nams_keywords:
        if keyword.lower() in title.lower():
            nams_records.append(record)
            break
print(f"NAMS records found: {len(nams_records)}")

for record in nams_records:
    record["topics"] = ["NAMS"]

for record in nams_records:
    classified_records.append(record)

print(f"Total classified records: {len(classified_records)}")

topic_counts = {}

for record in classified_records:
    for topic in record["topics"]:
        topic_counts[topic] = topic_counts.get(topic, 0) + 1

print("Topic counts:")
print(topic_counts)

with open("data/classified_records.json", "w", encoding="utf-8") as f:
    json.dump(
        classified_records,
        f,
        indent=2,
        ensure_ascii=False
    )

print("Saved results to data/classified_records.json")

summary = {
    "total_records": len(all_records),
    "classified_records": len(classified_records),
    "topic_counts": topic_counts
}

with open("data/classification_summary.json", "w", encoding="utf-8") as f:
    json.dump(
        summary,
        f,
        indent=2,
        ensure_ascii=False
    )

print("Saved results to data/classification_summary.json")

print("Tagged NAMS records:")

for record in nams_records[:3]:
    print(record["topics"], "-", record["title"])

for record in nams_records[:5]:
    print(record["title"])

print(f"Total records: {len(all_records)}")

for keyword in adc_keywords[:5]:
    print(keyword)
print("Sample NAMS keywords:")

for keyword in nams_keywords[:5]:
    print(keyword)
