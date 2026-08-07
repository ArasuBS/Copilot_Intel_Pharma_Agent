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
adc_targets = adc_topic["targets"]
adc_products = adc_topic["products"]
adc_payloads = adc_topic["payloads"]
adc_technologies = adc_topic["technologies"]

adc_terms = (
    adc_keywords
    + adc_targets
    + adc_products
    + adc_payloads
    + adc_technologies
)

print(f"ADC keywords loaded: {len(adc_keywords)}")
print(f"ADC classification terms: {len(adc_terms)}")

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

cld_topic = next(
    topic for topic in topics["topics"]
    if topic["name"] == "Cell Line Development"
)

cld_keywords = cld_topic["keywords"]

print(f"CLD keywords loaded: {len(cld_keywords)}")

print(f"Bispecifics keywords loaded: {len(bispecifics_keywords)}")

print(f"NAMS keywords loaded: {len(nams_keywords)}")

with open("data/pubmed_results.json", "r", encoding="utf-8") as f:
    pubmed_records = json.load(f)

with open("data/rss_results.json", "r", encoding="utf-8") as f:
    rss_records = json.load(f)

print(f"PubMed records: {len(pubmed_records)}")
print(f"RSS records: {len(rss_records)}")

all_records = pubmed_records + rss_records

print()
print("=" * 60)
print("PHARMA INTELLIGENCE CLASSIFIER")
print("=" * 60)
print()

print("INPUT SUMMARY")
print("-" * 60)
print(f"PubMed Records : {len(pubmed_records)}")
print(f"RSS Records    : {len(rss_records)}")
print(f"Total Records  : {len(all_records)}")
print()

sources = {}

for record in all_records:
    source = record["source"]
    sources[source] = sources.get(source, 0) + 1

print("Source breakdown:")
print(sources)

adc_records = []

for record in all_records:
    title = record["title"]

    for keyword in adc_terms:
        if keyword.lower() in title.lower():
            adc_records.append(record)
            break
print()
print("=" * 60)
print("ADC")
print("=" * 60)
print(f"Records Identified : {len(adc_records)}")

for record in adc_records:
    record["topics"] = ["ADC"]

classified_records = []

for record in adc_records:
    classified_records.append(record)

nams_records = []

for record in all_records:
    title = record["title"]

    for keyword in nams_keywords:
        if keyword.lower() in title.lower():
            nams_records.append(record)
            break
print()
print("=" * 60)
print("NAMS")
print("=" * 60)
print(f"Records Identified : {len(nams_records)}")

bispecific_records = []

for record in all_records:
    title = record["title"]

    for keyword in bispecifics_keywords:
        if keyword.lower() in title.lower():
            bispecific_records.append(record)
            break

print()
print("=" * 60)
print("BISPECIFICS")
print("=" * 60)
print(f"Records Identified : {len(bispecific_records)}")

cld_records = []

for record in all_records:
    title = record["title"]

    for keyword in cld_keywords:
        if keyword.lower() in title.lower():
            cld_records.append(record)
            break

print()
print("=" * 60)
print("CELL LINE DEVELOPMENT")
print("=" * 60)
print(f"Records Identified : {len(cld_records)}")

for record in cld_records:
    record["topics"] = ["Cell Line Development"]

for record in bispecific_records:
    record["topics"] = ["Bispecifics"]

for record in nams_records:
    record["topics"] = ["NAMS"]

for record in nams_records:
    classified_records.append(record)
    
for record in bispecific_records:
    classified_records.append(record)

for record in cld_records:
    classified_records.append(record)

print(f"Total classified records: {len(classified_records)}")

topic_counts = {}

for record in classified_records:
    for topic in record["topics"]:
        topic_counts[topic] = topic_counts.get(topic, 0) + 1

print()
print("=" * 60)
print("CLASSIFICATION SUMMARY")
print("=" * 60)

for topic, count in topic_counts.items():
    print(f"{topic:<25} {count}")

print()
print(f"Total Classified : {len(classified_records)}")
print(f"Total Records    : {len(all_records)}")

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
