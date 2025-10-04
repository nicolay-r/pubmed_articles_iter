# pubmed_articles_iter

Non-official JSON-based articles extractor for [PubMed Open-Access (OA) subset](https://pmc.ncbi.nlm.nih.gov/tools/ftp/) 
of articles with schema parser for 2025.

# Motivation

Mostly driven by limitations of the existing approaches.

⚠️ **Limitations:**
1. [`ncbi/pubmed` on Huggingface](https://huggingface.co/datasets/ncbi/pubmed) -- The existing **dropped the support for 2025**
    * The [`pubmed.py`](https://huggingface.co/datasets/ncbi/pubmed/blob/main/pubmed.py) is based on `datasets` data fetcher. 
    * This implementation requires to **construct train split** to skim through the whole data before start using it.
2. [`pubmeb_parser` on GitHub](https://github.com/titipata/pubmed_parser) -- is not compatible for processing extracted `xml` for paper skimming
    * [`pp.parse_pubmed_references`](https://github.com/titipata/pubmed_parser?tab=readme-ov-file#parse-pubmed-oa-citation-references) returns `None` for unzipped `xml`.

## Solution

No-API based implementation for:
1. Downloading `pubmed` resources 
2. `XML` to `JSONL` conversion for `articles`


# AI Disclaimer

The AI has been applied in implementation for: 
* (i) `xml.gz` content downloader,
* (ii) XLM parsers.

For several fields we adopt advances and techniques previously [exploited in `pubmed.py`](https://huggingface.co/datasets/ncbi/pubmed/blob/main/pubmed.py). 
