import json
from datetime import datetime

with open("data/classified_records.json", "r", encoding="utf-8") as f:
    records = json.load(f)

with open("data/classification_summary.json", "r", encoding="utf-8") as f:
    summary = json.load(f)

report_lines = []

report_lines.append("# Pharma Intelligence Report\n")
report_lines.append(
    f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n"
)

report_lines.append("## Executive Summary\n")

report_lines.append(
    f"Total Records Reviewed: {summary['total_records']}\n"
)

report_lines.append(
    f"Classified Records: {summary['classified_records']}\n"
)

report_lines.append("")

for topic, count in summary["topic_counts"].items():
    report_lines.append(f"- {topic}: {count}")

report_lines.append("\n---\n")

topic_groups = {}

for record in records:
    for topic in record["topics"]:
        topic_groups.setdefault(topic, []).append(record)

for topic, topic_records in topic_groups.items():

    report_lines.append(
        f"## {topic} ({len(topic_records)})\n"
    )

    for record in topic_records:
        report_lines.append(
            f"- {record['title']}"
        )

    report_lines.append("")

with open("data/report.md", "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print("Generated report.md")
