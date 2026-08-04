import requests
import json
import yaml

SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def load_topics():

    with open("topics.yaml", "r", encoding="utf-8") as f:
        topics = yaml.safe_load(f)

    return topics

def search_pubmed(term="antibody drug conjugate"):
    params = {
        "db": "pubmed",
        "term": term,
        "retmax": 30,
        "retmode": "json"
    }

    response = requests.get(SEARCH_URL, params=params)
    response.raise_for_status()

    return response.json()["esearchresult"]["idlist"]
    
    
def save_results(papers):
    with open("data/pubmed_results.json", "w", encoding="utf-8") as f:
        json.dump(
            papers,
            f,
            indent=2,
            ensure_ascii=False
        )

def fetch_summaries(ids):
    if not ids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "json"
    }

    response = requests.get(SUMMARY_URL, params=params)
    response.raise_for_status()

    result = response.json()["result"]

    papers = []

    for pubmed_id in ids:
        record = result.get(pubmed_id)

        if not record:
            continue

        papers.append({
            "pubmed_id": pubmed_id,
            "title": record.get("title"),
            "pubdate": record.get("pubdate"),
            "source": "PubMed"
        })

    return papers
    
def get_topic(topics_data, topic_name):

    for topic in topics_data["topics"]:
        if topic["name"] == topic_name:
            return topic

    return None

if __name__ == "__main__":

    topics = load_topics()
    
    adc = get_topic(topics, "ADC")
    nams = get_topic(topics, "NAMS")
    bispecifics = get_topic(topics, "Bispecifics")
    
    adc_keywords = adc["keywords"][:2]
    nams_keywords = nams["keywords"][:7]
    bispecific_keywords = bispecifics["keywords"][:5]
    
    keywords = adc_keywords + nams_keywords + bispecific_keywords
    
    query = ' OR '.join([f'"{k}"' for k in keywords])
    
    print(f"Using query: {query}")

    print(adc_keywords)
    print(nams_keywords)

    print(f"Keyword count: {len(keywords)}")

    print("ADC keywords:")
    print(adc_keywords)

    print("NAMS keywords:")
    print(nams_keywords)
    
    ids = search_pubmed(query)

    papers = fetch_summaries(ids)

    save_results(papers)

    print("Saved results to data/pubmed_results.json")

    print(f"Found {len(papers)} papers\n")

    for paper in papers:
        print("-" * 80)
        print(f"PMID: {paper['pubmed_id']}")
        print(f"DATE: {paper['pubdate']}")
        print(f"TITLE: {paper['title']}")
