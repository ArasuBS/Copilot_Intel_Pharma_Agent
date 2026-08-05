import json

print("Report generator started")

with open("data/classified_records.json", "r", encoding="utf-8") as f:
    records = json.load(f)

print(f"Classified records: {len(records)}")

for record in records[:5]:
    print(record["topics"], "-", record["title"])
