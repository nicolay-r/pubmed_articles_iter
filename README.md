# pubmed_articles_iter

A [PubMed Open-Access (OA) subset](https://pmc.ncbi.nlm.nih.gov/tools/ftp/) XML to JSON converter for articles. 

This repo represent an [iter-based implementation](https://github.com/nicolay-r/pubmed_articles_iter/blob/1dc021dbef965ad858b53b1a31eeb5237970d804/core/pubmed_parser.py#L6-L20) for the downloaded PubMed subset.

# Motivation

Mostly driven by limitations of the existing approaches.

⚠️ **Limitations:**
1. [`ncbi/pubmed` on Huggingface](https://huggingface.co/datasets/ncbi/pubmed) -- The existing **dropped the support for 2025**
    * The [`pubmed.py`](https://huggingface.co/datasets/ncbi/pubmed/blob/main/pubmed.py) is based on `datasets` data fetcher. 
    * This implementation requires to **construct train split** to skim through the whole data before start using it.
2. [`pubmeb_parser` on GitHub](https://github.com/titipata/pubmed_parser) -- is not compatible for processing extracted `xml` for paper skimming
    * [`pp.parse_pubmed_references`](https://github.com/titipata/pubmed_parser?tab=readme-ov-file#parse-pubmed-oa-citation-references) returns `None` for unzipped `xml`.

# Usage

Launch the following scripts:
1. `pubmed_1_download.py` -- downloading `pubmed` resources;
2. `pubmed_2_articles_xml_to_jsonl.py` -- `XML` to `JSONL` conversion for `articles`;
   * It exploits the

# AI Disclaimer

The AI has been applied in implementation for: 
* (i) `xml.gz` content downloader,
* (ii) XLM parsers.

For several fields we adopt advances and techniques previously [exploited in `pubmed.py`](https://huggingface.co/datasets/ncbi/pubmed/blob/main/pubmed.py). 
