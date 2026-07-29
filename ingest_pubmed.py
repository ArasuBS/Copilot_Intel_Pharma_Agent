import requests

SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


def search_pubmed(term="antibody drug conjugate"):
    params = {
        "db": "pubmed",
        "term": term,
        "retmax": 10,
        "retmode": "json"
    }

    response = requests.get(SEARCH_URL, params=params)
    response.raise_for_status()

    return response.json()["esearchresult"]["idlist"]


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
            "pubdate": record.get("pubdate")
        })

    return papers


if __name__ == "__main__":

    ids = search_pubmed()

    papers = fetch_summaries(ids)

    print(f"Found {len(papers)} papers\n")

    for paper in papers:
        print("-" * 80)
        print(f"PMID: {paper['pubmed_id']}")
        print(f"DATE: {paper['pubdate']}")
        print(f"TITLE: {paper['title']}")
