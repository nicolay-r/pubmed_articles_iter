# pubmed_articles_iter

Non-official JSON-based articles extractor gz snapshot of articles with schema parser for 2025

# Motivation

Mostly driven by limitations of the existing approaches.

⚠️ **Limitations:**
1. [`ncbi/pubmed` on Huggingface](https://huggingface.co/datasets/ncbi/pubmed) -- The existing **dropped the support for 2025** year with related schema
  * The [`pubmed.py`](https://huggingface.co/datasets/ncbi/pubmed/blob/main/pubmed.py) is based on `datasets` data fetcher. 
  * This implementation requires to **contruct train split** which is time consumptive for an instant start
  * The parser finds me [no longer compatible](https://huggingface.co/datasets/ncbi/pubmed/blob/main/pubmed.py#L40) with the `25` year and dump
2. [`pubmeb_parser` on Gihub](https://github.com/titipata/pubmed_parser) -- is not compatible for processing extrated `xml` for paper skimming

## Solution

No-API based implementation for:
1. Downloading `pubmed` resources 
2. `XML` to `JSONL` conversion for `articles`


# AI Disclaimer

The AI has been applied in implementation for: (i) `xml.gz` content downloader and (ii) XLM parsers.

For several fields we adopt advances and techniques previously [exploied in `pubmed.py`](https://huggingface.co/datasets/ncbi/pubmed/blob/main/pubmed.py). 
