# pubmed_articles_iter

An [iterator](https://github.com/nicolay-r/pubmed_articles_iter/blob/1dc021dbef965ad858b53b1a31eeb5237970d804/core/pubmed_parser.py#L6-L20) of parsed articles over [PubMed Open-Access (OA) subset](https://pmc.ncbi.nlm.nih.gov/tools/ftp/) `XML` data content.

As a one use-case this iterator utilized for converting `XML` data content into `JSONL`. 

# Motivation

Mostly driven by limitations of the existing approaches.

⚠️ **Limitations:**
1. [`ncbi/pubmed` on Huggingface](https://huggingface.co/datasets/ncbi/pubmed) -- The existing **dropped the support for 2025**
    * The [`pubmed.py`](https://huggingface.co/datasets/ncbi/pubmed/blob/main/pubmed.py) is based on `datasets` data fetcher. 
    * This implementation requires to **construct train split** to skim through the whole data before start using it.
2. [`pubmeb_parser` on GitHub](https://github.com/titipata/pubmed_parser) -- is not compatible for processing extracted `xml` for paper skimming
    * [`pp.parse_pubmed_references`](https://github.com/titipata/pubmed_parser?tab=readme-ov-file#parse-pubmed-oa-citation-references) returns `None` for unzipped `xml`.

# Install

```
pip install git+https://github.com/nicolay-r/pubmed_articles_iter@master
```

# Usage

1. downloading `pubmed` resources:
```python
from pubmed_articles_iter.downloader import download_files

download_files(
    urls=[f"https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/pubmed25n{i:04d}.xml.gz" for i in range(1, 1275)],
    output_dir='./pubmed_data',
    max_files=None
)
```

2. `XML` to `JSONL` conversion for `articles`:
```python
from pubmed_articles_iter.pubmed_parser import pubmed_papers_it
from pubmed_articles_iter.utils import iter_dir_filepaths
from pubmed_articles_iter.utils_filter import iter_articles
from pubmed_articles_iter.utils_jsonl import write_jsonl

write_jsonl(
    file_path=f"pubmed.jsonl",
    records_it=iter_articles(
        filepaths=iter_dir_filepaths(root_dir='./pubmed_data'),
        filter_func=None,
        desc="Converting PubMed XML to JSONL",
        fp_handler=pubmed_papers_it,
    )
)
```

# AI Disclaimer

The AI has been applied in implementation for: 
1. `xml.gz` content downloader
2.  XLM parsers.

For several fields we adopt advances and techniques previously [exploited in `pubmed.py`](https://huggingface.co/datasets/ncbi/pubmed/blob/main/pubmed.py). 
